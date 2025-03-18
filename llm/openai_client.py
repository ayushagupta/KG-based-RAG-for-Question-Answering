from openai import OpenAI
from llm.config import config
import logging
import json

logging.basicConfig(
    filename="llm_responses.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=config.OPENAI_API_KEY)

    def generate_response(self, instructions, input_text):
        try:
            response = self.client.responses.create(
                model = config.MODEL_NAME,
                instructions = instructions,
                input = input_text
            )

            self.log_response(instructions, input_text, response)

            return response.output_text
        
        except Exception as e:
            logging.error(f"OpenAI API call failed: {e}")
            return "Error generating response."
        
    
    def log_response(self, instructions, input_text, response):
        log_data = {
            "model": config.MODEL_NAME,
            "instructions": instructions,
            "input_text": input_text,
            "response": response.output_text
        }
        logging.info(json.dumps(log_data, indent=4))
    

