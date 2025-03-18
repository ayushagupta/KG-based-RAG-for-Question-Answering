SYSTEM_PROMPTS  = {
    "default":
    """You are a helpful AI assisstant.""",

    "disease_entity_extraction": 
    """You are an expert disease entity extractor from a sentence and report it as JSON in the following format:
    diseases: <List of extracted entities>
    Please report only Diseases. Do not report any other entities like Genes, Proteins, Enzymes etc."""
}

def get_system_prompt(task: str) -> str:
    return SYSTEM_PROMPTS.get(task, SYSTEM_PROMPTS["default"])