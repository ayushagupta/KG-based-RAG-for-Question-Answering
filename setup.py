from config.config import config
import os
from vectorDB.create_vectordb import create_vector_db, create_vector_db_no_batching
import time


if not os.path.exists("logs"):
    os.makedirs("logs")
    

try:
    if os.path.exists(config.VECTOR_DB_PATH):
        print("VectorDB already exists.")
    else:
        start_time = time.time()
        create_vector_db()
        batched_time = time.time() - start_time
        print(f"Time taken to create VectorDB: {batched_time:.2f} seconds")

except:
    print("VectorDB creation could not be completed.")