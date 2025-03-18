from llm.openai_client import OpenAIClient
from rag.utils import *
from config.config import config

# client = OpenAIClient()
# text = "I have diabetes and arthiritis from birth."
# diseases = extract_disease_entities(text=text, client=client)
# print(diseases)

vector_db_path = config.VECTOR_DB_PATH
sentence_embedding_model = config.VECTOR_DB_SENTENCE_EMBEDDING_MODEL

vector_store = get_vector_store(vector_db_path, sentence_embedding_model)
node_search_result = vector_store.similarity_search_with_score("diabetes", k=1)
print(node_search_result)