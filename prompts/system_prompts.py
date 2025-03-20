SYSTEM_PROMPTS  = {
    "default":
    """You are a helpful AI assisstant.""",

    "disease_entity_extraction": 
    """You are an expert disease entity extractor from a sentence and report it as JSON in the following format:
    diseases: <List of extracted entities>
    Please report only Diseases. Do not report any other entities like Genes, Proteins, Enzymes etc.""",

    "mcq_question":
    """You are an expert biomedical researcher. For answering the Question at the end, you need to first read the Context provided.
    Based on that Context, provide your answer in the following JSON format for the Question asked.
    "answer": <correct answer>
    """
}

def get_system_prompt(task: str) -> str:
    return SYSTEM_PROMPTS.get(task, SYSTEM_PROMPTS["default"])