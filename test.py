from llm.openai_client import OpenAIClient
from rag.utils import *
from config.config import config
from rag.rag import RAG

openai_client = OpenAIClient()
text = "I have diabetes and arthiritis from birth."
rag = RAG(openai_client)
rag.retrieve(text)