PROMPTS = {
    "hello": """Hello, how are you my friend {input_text}?"""
}

def get_prompt(task: str, input_text: str) -> str:
    if task not in PROMPTS:
        raise ValueError(f"Invalid task: {task}")
    return PROMPTS[task].format(input_text=input_text)