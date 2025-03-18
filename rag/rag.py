from rag.utils import *
from rag.spoke import get_context_from_spoke_api
from config.config import config

class RAG:
    def __init__(self, openai_client):
        self.vector_store = get_vector_store(config.VECTOR_DB_PATH, config.VECTOR_DB_SENTENCE_EMBEDDING_MODEL)
        self.embedding_function = get_embedding_function(model_name=config.EMBEDDING_MODEL_FOR_CONTEXT_RETRIEVAL)
        self.openai_client = openai_client

    def retrieve(self, question):
        disease_entities = extract_disease_entities(question, self.openai_client)
        nodes_found = []

        if disease_entities:
            for disease in disease_entities:
                node_search_result = self.vector_store.similarity_search_with_score(disease, k=1)
                nodes_found.append(node_search_result[0][0].page_content)

            question_embedding = get_text_embedding(question, self.embedding_function)
            
            for node in nodes_found:
                get_context_from_spoke_api(node)    

        else:
            pass