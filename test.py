from config.config import config
from llm.openai_client import OpenAIClient
from rag.utils import *
from rag.rag import RAG
from prompts.system_prompts import get_system_prompt
from utils.schema_loader import load_task_schema

openai_client = OpenAIClient()

question = "Are there any drugs used for weight management in patients with Bardet-Biedl Syndrome?"

rag = RAG(openai_client, config.CONTEXT_VOLUME, config.QUESTION_VS_CONTEXT_SIMILARITY_PERCENTILE_THRESHOLD, config.QUESTION_VS_CONTEXT_MINIMUM_SIMILARITY)
context = rag.retrieve(question)

enriched_prompt = "Context: "+ context + "\n" + "Question: "+ question
system_prompt = get_system_prompt(task="mcq_question")
text_data = load_task_schema(task="mcq_question")
output = openai_client.generate_json_response(instructions=system_prompt, input_text=enriched_prompt, text_data=text_data)

print(output)