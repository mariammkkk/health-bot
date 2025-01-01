from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone
from langchain_community.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os

from pinecone import Pinecone, ServerlessSpec

app = Flask(__name__)
CORS(app)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# Download embeddings
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Ensure the index exists or create it
index_name = "health-bot"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=1536,  # Update this to match your embedding dimension
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_API_ENV
        )
    )

# Load the index
from langchain_pinecone import Pinecone as PineconeVectorStore

# Use PineconeVectorStore to interact with the index
docsearch = PineconeVectorStore(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV,
    index_name=index_name,
    embedding=embeddings
)

# Define prompt template
PROMPT = PromptTemplate(template='prompt.py', input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

# Load LLM
llm = CTransformers(
    model = "model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type = "llama",
    config = {'max_new_tokens': 512, 'temperature': 0.8}
)

# Define the QA chain
qa = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever = docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents = True,
    chain_type_kwargs = chain_type_kwargs
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form.get["msg"]
    if not msg:
        return "Invalid input.", 400
    result = qa({"query": msg})
    return str(result["result"])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    