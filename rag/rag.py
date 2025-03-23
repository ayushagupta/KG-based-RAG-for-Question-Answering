from rag.utils import *
from rag.spoke import get_context_from_spoke_api
from config.config import config


class RAG:
    def __init__(self, openai_client, context_volume, context_similarity_percentile_threshold, context_similarity_min_threshold):
        self.vector_store = get_vector_store(vector_db_path=config.VECTOR_DB_PATH, sentence_embedding_model=config.VECTOR_DB_SENTENCE_EMBEDDING_MODEL)
        self.embedding_function = get_embedding_function(model_name=config.EMBEDDING_MODEL_FOR_CONTEXT_RETRIEVAL)
        self.openai_client = openai_client
        self.context_volume = context_volume
        self.context_similarity_percentile_threshold = context_similarity_percentile_threshold
        self.context_similarity_min_threshold = context_similarity_min_threshold

    def retrieve(self, question):
        disease_entities = extract_disease_entities(question, self.openai_client)
        question_embedding = get_text_embedding(question, self.embedding_function)
        nodes_found = []
        node_context_extracted = ""
        max_number_of_high_similarity_context_per_node = 0

        if disease_entities:
            max_number_of_high_similarity_context_per_node = int(self.context_volume/len(disease_entities))
            for disease in disease_entities:
                node_search_result = self.vector_store.similarity_search_with_score(disease, k=1)
                nodes_found.append(node_search_result[0][0].page_content)
        else:
            k = 5
            nodes_found = self.vector_store.similarity_search_with_score(question, k=k)
            max_number_of_high_similarity_context_per_node = int(self.context_volume/k)

        for node in nodes_found:
            node_context, context_table = get_context_from_spoke_api(node)

            relevant_context = extract_relevant_context(
                node_context=node_context,
                question_embedding=question_embedding,
                embedding_function=self.embedding_function,
                percentile_threshold=self.context_similarity_percentile_threshold,
                min_threshold=self.context_similarity_min_threshold,
                max_count=max_number_of_high_similarity_context_per_node
            )

            node_context_extracted += relevant_context

        return node_context_extracted
