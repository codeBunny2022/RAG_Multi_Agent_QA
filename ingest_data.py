# ingest_data.py - Document Ingestion and Vector Store Creation

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Correct import from langchain
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS  # Correct import from langchain_community
from langchain_openai.embeddings import OpenAIEmbeddings

# Configuration
DATA_DIR = 'data'
MODEL_DIR = 'models'
VECTOR_STORE_PATH = f'{MODEL_DIR}/faiss_index'

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# Load Documents from data folder
documents = []

for filename in os.listdir(DATA_DIR):
    file_path = os.path.join(DATA_DIR, filename)
    if filename.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            documents.append(Document(page_content=content))

if not documents:
    print("❌ No text documents found in the 'data' folder. Please add some .txt files.")
    exit()

print(f"✅ Loaded {len(documents)} documents from the 'data' folder.")

# Document Chunking
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
chunks = [chunk for doc in documents for chunk in text_splitter.split_text(doc.page_content)]

print(f"✅ Document chunked into {len(chunks)} pieces.")

# Embedding and Vector Store
# Ensure OpenAI API key is set in the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("Please set your OpenAI API key in the environment variable OPENAI_API_KEY.")

print("✅ OpenAI API key found. Proceeding with embedding creation.")

embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)

# Check embeddings object
print(f"✅ Embeddings object created: {embeddings}")

# Create the FAISS vector store
print("✅ Creating FAISS vector store...")
vector_store = FAISS.from_texts(chunks, embeddings)

# Check vector store object
print(f"✅ Vector store created: {vector_store}")

# Save Vector Store
print(f"✅ Saving vector store at {VECTOR_STORE_PATH}...")
vector_store.save_local(VECTOR_STORE_PATH)

print(f"✅ Vector store created and saved at {VECTOR_STORE_PATH}")
