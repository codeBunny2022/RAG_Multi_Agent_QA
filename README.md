# RAG-Powered Q&A Assistant

## 📌 Project Overview

The RAG-Powered Q&A Assistant is an intelligent, real-time question-answering application that uses Retrieval-Augmented Generation (RAG) architecture. The application leverages a LangChain-powered knowledge base, where user questions are answered using context retrieved from the ingested document collection.

## ⚙️ Architecture

* **Streamlit Frontend**: Provides a clean, interactive UI for users to input questions and view answers.
* **Agent Workflow (agent_workflow.py)**: Handles the main logic of answering user queries by:
  * Loading pre-computed document embeddings using FAISS vector store.
  * Using LangChain with OpenAI to generate intelligent, contextually accurate answers.
  * Maintaining query history for user convenience.
* **Data Ingestion (ingest_data.py)**: Manages document ingestion and vectorization using FAISS.
* **Knowledge Base (data/)**: A directory for storing all source documents used in the knowledge base.
* **Vector Store (models/faiss_index)**: Contains the FAISS index file for fast document vector lookup.

## 🚀 Key Design Choices


1. **RAG Architecture**: Combines document retrieval (via FAISS) with OpenAI's LLM for high-quality answers.
2. **Elegant UI/UX with Streamlit**: An intuitive interface with smooth animations and query history.
3. **Scalability**: Easily extendable to accommodate more documents and different LLMs.
4. **Security**: The vector store is locally managed, avoiding unnecessary API calls for document retrieval.

## ✅ How to Run

### 1. Installation

* Clone the repository:

  ```bash
  git clone https://github.com/yourusername/RAG_Powered_QA.git
  cd RAG_Powered_QA
  ```
* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```
* Set your OpenAI API key as an environment variable:

  ```bash
  export OPENAI_API_KEY=your_openai_api_key
  ```

### 2. Data Ingestion

* Add your documents to the `data/` folder.
* Run the data ingestion script to build the vector store:

  ```bash
  python ingest_data.py
  ```

### 3. Start the Application

* Launch the Streamlit app:

  ```bash
  streamlit run app.py
  ```
* Access the app at `http://localhost:8501`.

### 4. Usage

* Ask any question in the input box.
* The answer will be generated using the context from your knowledge base.
* Query history is displayed below for easy reference.

## 🛠️ Customization

* To add new documents, simply place them in the `data/` folder and re-run `ingest_data.py`.
* Modify the LLM settings in `agent_workflow.py` to switch to another model.

## 📄 License

This project is licensed under the MIT License.

## 🌐 Contact

For any questions, feel free to reach out at chiragcrypt@gmail.com : )