from config.config import config
import os
from vectorDB.create_vectordb import create_vector_db

try:
    if os.path.exists(config.VECTOR_DB_PATH):
        print("VectorDB already exists.")
    else:
        create_vector_db()

except:
    print("VectorDB creation could not be completed.")