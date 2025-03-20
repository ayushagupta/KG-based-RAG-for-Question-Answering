# Knowledge Graph-Based RAG for Question Answering  

This project leverages a **knowledge graph** to extract relevant context and provide answers to **domain-specific multiple-choice questions (MCQs)**.

## 🚀 Setup  

### 1️⃣ Install Dependencies  
Ensure all required packages are installed by running:  
```bash
pip install -r requirements.txt
```

### 2️⃣ Create the Vector Database
The system requires a vector database to store embeddings generated from a medical knowledge base containing diseases and their associated genes. You can set it up with:
```bash
python setup.py
```
This command also creates a logs folder to store execution logs.

### 3️⃣ Configure Environment Variables
Create a `.env` file in the project's root directory and add your **OpenAI API** key:
```
OPENAI_API_KEY="your-api-key-here"
```

## 🛠 Features
* **Knowledge Graph Integration**: Extracts relevant information from a structured graph.
* **Vector Database**: Stores embeddings of medical entities for efficient retrieval.
* **Question Answering**: Uses retrieved context to enhance response generation.