from llm.openai_client import OpenAIClient
from rag.utils import *

client = OpenAIClient()
text = "I have diabetes and arthiritis from birth."
diseases = extract_disease_entities(text=text, client=client)
print(diseases)