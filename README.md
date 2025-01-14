# Medical Chatbot

This project is an **AI-powered medical chatbot** designed to provide users with accurate, context-aware, and natural language responses to medical-related questions. By leveraging advanced AI technologies such as LangChain, OpenAI, Pinecone, and Hugging Face, the chatbot ensures a seamless and user-friendly experience for users seeking medical information.

---

## Features
- **Semantic Search**: Converts medical textbooks into vector embeddings, enabling advanced semantic search for precise information retrieval.
- **AI-Driven Responses**: Utilizes Large Language Models (LLMs) to generate conversational, human-like answers to user queries.
- **Scalable Database Integration**: Employs Pinecone to store and retrieve medical data efficiently using vectorized search.
- **Hugging Face Models**: Uses pre-trained models from Hugging Face for additional natural language processing tasks.
- **Context-Aware Answers**: Delivers relevant responses that consider the context of user queries for enhanced accuracy.

---

## How It Works

### 1. Data Preparation
- **Text Processing**: Medical textbooks and related resources are tokenized and processed into vector embeddings using LangChain and Hugging Face.
- **Vector Database**: The embeddings are stored in Pinecone for fast and scalable similarity search.

### 2. Query Handling
- **User Input**: Users submit questions through a conversational interface.
- **Semantic Search**: The chatbot searches the vector database for closely related medical information.
- **Natural Language Generation**: OpenAI's LLM, augmented with Hugging Face models, generates a human-like response based on the retrieved information.

### 3. Response Delivery
- **Conversational Output**: The chatbot returns accurate, contextually relevant answers in a natural language format.

---

## Tech Stack
- **Programming Language**: Python
- **Core Libraries and Frameworks**:
  - [LangChain](https://github.com/hwchase17/langchain): For managing and querying vector embeddings.
  - [OpenAI](https://openai.com/): Provides the primary LLM for generating responses.
  - [Pinecone](https://www.pinecone.io/): Handles vector-based storage and semantic search.
  - [Hugging Face Transformers](https://huggingface.co/): Used for pre-trained models to enhance natural language processing capabilities.
- **Data Sources**: Medical textbooks and datasets converted into embeddings for query processing.

---

## How to run:
### STEPS:

Clone the repository

```bash
Project repo: https://github.com/mariammkkk/health-bot.git
```

```bash
conda create -n bot python=3.10 -y
```

```bash
conda activate bot
```

Install Requirements
```bash
pip install -r requirements.txt
```
