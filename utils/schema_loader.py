import json
import logging

logging.basicConfig(
    filename="logs/schema_loader.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_task_schema(task: str):
    try:
        with open("schemas/task_schemas.json", "r") as file:
            task_schemas = json.load(file)
        
        if task in task_schemas:
            return task_schemas[task]
        else:
            logging.error(f"Schema for task '{task}' not found.")
            return None
        
    except FileNotFoundError:
        logging.error("Schema file 'task_schemas.json' not found.")
        return None
    
    except json.JSONDecodeError:
        logging.error("Error decoding the JSON schema file.")
        return None
    
    except Exception as e:
        logging.error(f"Unexpected error while loading task schema: {e}")
        return None
