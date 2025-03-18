USER_PROMPTS = {
    "disease_entity_extraction": 
    """You are an expert disease entity extractor from a sentence and report it as JSON in the following format:
    diseases: <List of extracted entities>
    Please report only Diseases. Do not report any other entities like Genes, Proteins, Enzymes etc.
    Input: {input_text}"""
}

def get_user_prompt(task: str, input_text: str) -> str:
    if task not in USER_PROMPTS:
        raise ValueError(f"Invalid task: {task}")
    
    return USER_PROMPTS[task].format(input_text=input_text)