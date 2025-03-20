import pickle
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config.config import config
from tqdm import tqdm

data_path = config.VECTOR_DB_DISEASE_ENTITY_PATH
vector_db_name = config.VECTOR_DB_PATH
chunk_size = config.VECTOR_DB_CHUNK_SIZE
chunk_overlap = config.VECTOR_DB_CHUNK_OVERLAP
batch_size = config.VECTOR_DB_BATCH_SIZE
sentence_embedding_model = config.VECTOR_DB_SENTENCE_EMBEDDING_MODEL

def load_data():
    with open(data_path, "rb") as f:
        data = pickle.load(f)
    metadata_list = list(map(lambda x:{"source": x + " from SPOKE knowledge graph"}, data))
    return data, metadata_list


def create_vector_db_no_batching():
    data, metadata_list = load_data()
    print(f"Loaded {len(data)} data points")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.create_documents(data, metadatas=metadata_list)

    print("Initializing Chroma VectorDB with HuggingFaceEmbeddings...")
    vector_store = Chroma(embedding_function=HuggingFaceEmbeddings(model_name=sentence_embedding_model), persist_directory=vector_db_name)
    
    for doc in tqdm(docs, desc="Adding documents to VectorDB", unit="doc"):
        vector_store.add_documents(documents=[doc])

    print("VectorDB created successfully!")


def create_vector_db():
    data, metadata_list = load_data()
    print(f"Loaded {len(data)} data points")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.create_documents(data, metadatas=metadata_list)
    batches = [docs[i:i + batch_size] for i in range(0, len(docs), batch_size)]

    print("Initializing Chroma VectorDB with HuggingFaceEmbeddings...")
    vector_store = Chroma(embedding_function=HuggingFaceEmbeddings(model_name=sentence_embedding_model), persist_directory=vector_db_name)
    
    for batch in tqdm(batches, desc="Adding documents to VectorDB", unit="batch"):
        vector_store.add_documents(documents=batch)

    print("VectorDB created successfully!")


