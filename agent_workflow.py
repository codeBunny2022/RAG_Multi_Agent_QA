# agent_workflow.py - AI Agentic Workflow for handling queries

import os
import openai
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_openai import OpenAI

# Ensure OpenAI API key is set in the environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("Please set your OpenAI API key in the environment variable OPENAI_API_KEY.")

# Load the FAISS vector store with embeddings (allow safe deserialization)
VECTOR_STORE_PATH = 'models/faiss_index'
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vector_store = FAISS.load_local(VECTOR_STORE_PATH, embeddings=embeddings, allow_dangerous_deserialization=True)

# Initialize the LLM
llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Define the tools (for calculation and dictionary lookups)
tools = [
    Tool(
        name="Calculator",
        func=lambda query: eval(query),  # Simple calculator
        description="Useful for solving math problems."
    ),
    Tool(
        name="Dictionary",
        func=lambda query: f"Definition of {query}: Placeholder definition.",
        description="Useful for defining words."
    ),
]

# Initialize the agent
agent = initialize_agent(
    tools,
    llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def handle_query(query):
    """Process the user query and return an answer."""
    
    # Check if the query contains a "calculate" or "define" keyword
    if "calculate" in query.lower():
        response = agent.run(query)
    elif "define" in query.lower():
        response = agent.run(query)
    else:
        # Default flow using the vector store
        retrieved_chunks = vector_store.similarity_search(query, k=3)
        context = "\n".join([chunk.page_content for chunk in retrieved_chunks])
        
        prompt = f"Answer the following question based on the context provided:\n{context}\nQuestion: {query}\nAnswer:"
        response = llm(prompt)  
        
    return response