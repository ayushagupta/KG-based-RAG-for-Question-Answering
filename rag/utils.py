from llm.openai_client import OpenAIClient
from prompts.system_prompts import get_system_prompt
from prompts.user_prompts import get_user_prompt
from utils.schema_loader import load_task_schema
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def extract_disease_entities(text: str, client: OpenAIClient):
    system_prompt = get_system_prompt(task="disease_entity_extraction")
    user_prompt = get_user_prompt(task="disease_entity_extraction", input_text=text)
    text_data = load_task_schema(task="disease_entity_extraction")
    if not text_data:
        return None
    response = client.generate_json_response(instructions=system_prompt, input_text=user_prompt, text_data=text_data)
    return response["diseases"]


def get_embedding_function(model_name):
    return HuggingFaceEmbeddings(model_name=model_name)


def get_vector_store(vector_db_path, sentence_embedding_model):
    embedding_function = get_embedding_function(model_name=sentence_embedding_model)
    return Chroma(embedding_function=embedding_function, persist_directory=vector_db_path)


def get_text_embedding(text, embedding_function):
    return embedding_function.embed_query(text)


def calculate_similarities(question_embedding, node_context_embeddings):
    similarities = [
        cosine_similarity(np.array(question_embedding).reshape(1, -1), np.array(node_context_embedding).reshape(1, -1))
        for node_context_embedding in node_context_embeddings
    ]
    return [s[0][0] for s in similarities]


def filter_high_similarity_indices(similarities, percentile_threshold, min_threshold, max_count):
    sorted_indices = np.argsort(similarities)[::-1]
    percentile_threshold_value = np.percentile(similarities, percentile_threshold)
    
    high_similarity_indices = [
        i for i in sorted_indices
        if similarities[i] > percentile_threshold_value and similarities[i] > min_threshold
    ]

    if len(high_similarity_indices) > max_count:
        high_similarity_indices = high_similarity_indices[:max_count]

    return high_similarity_indices


def extract_relevant_context(node_context, question_embedding, embedding_function, percentile_threshold=90, min_threshold=0.5, max_count=3):
    node_context_list = node_context.split(". ")
    node_context_embeddings = embedding_function.embed_documents(node_context_list)

    similarities = calculate_similarities(question_embedding, node_context_embeddings)
    high_similarity_indices = filter_high_similarity_indices(similarities, percentile_threshold, min_threshold, max_count)

    high_similarity_context = [node_context_list[i] for i in high_similarity_indices]
    return ". ".join(high_similarity_context) + ". "