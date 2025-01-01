import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_community.vectorstores import Pinecone as PineconeVectorStore

from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Return the extracted data
extracted_data = load_pdf_file(data='data/')

# Return text chunks
text_chunks = text_split(extracted_data)

# Create vector embeddings
embeddings = download_hugging_face_embeddings()

# Create Pinecone Index
pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "health-bot"

pc.create_index(
    name=index_name,
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

# Embed each chunk and upsert the embeddings into Pinecone Index
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)
