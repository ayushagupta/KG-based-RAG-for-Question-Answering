import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5")
    TEMPERATURE = float(os.getenv("TEMPERATURE", 0))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))

    VECTOR_DB_DISEASE_ENTITY_PATH = os.getenv(
        "VECTOR_DB_DISEASE_ENTITY_PATH", "data/disease_with_relation_to_genes.pickle"
    )
    VECTOR_DB_PATH = os.getenv(
        "VECTOR_DB_PATH", "data/vectorDB/disease_nodes_db"
    )
    VECTOR_DB_CHUNK_SIZE = int(os.getenv("VECTOR_DB_CHUNK_SIZE", 650))
    VECTOR_DB_CHUNK_OVERLAP = int(os.getenv("VECTOR_DB_CHUNK_OVERLAP", 200))
    VECTOR_DB_BATCH_SIZE = int(os.getenv("VECTOR_DB_BATCH_SIZE", 200))
    VECTOR_DB_SENTENCE_EMBEDDING_MODEL = os.getenv(
        "VECTOR_DB_SENTENCE_EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
    )

    EMBEDDING_MODEL_FOR_NODE_RETRIEVAL = os.getenv(
        "EMBEDDING_MODEL_FOR_NODE_RETRIEVAL", "sentence-transformers/all-MiniLM-L6-v2"
    )
    EMBEDDING_MODEL_FOR_CONTEXT_RETRIEVAL = os.getenv(
        "EMBEDDING_MODEL_FOR_CONTEXT_RETRIEVAL", "pritamdeka/S-PubMedBert-MS-MARCO"
    )

config = Config()
