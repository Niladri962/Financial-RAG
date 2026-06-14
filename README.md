# 📈 Financial Research Copilot using GraphRAG

A GraphRAG-powered Financial Research Assistant that combines **semantic search** and **knowledge graph reasoning** to answer complex financial questions from annual reports and SEC filings.

Built with **LangChain, Qdrant, Neo4j, all-MiniLM-L6-v2, Ollama, and Streamlit**, the system provides explainable, citation-backed answers using a hybrid retrieval architecture.

---

## 🚀 Features

* Hybrid Retrieval (Vector + Graph Search)
* GraphRAG Architecture
* Semantic Search with all-MiniLM-L6-v2
* Knowledge Graph Reasoning using Neo4j
* Local LLM Inference with Llama 3
* Streamlit Chat Interface
* Explainable AI with Source Attribution
* OCR Support for Scanned Documents
* Table Extraction from Financial Statements
* Extensible Agentic AI Architecture

---

# System Architecture

```text
PDF Reports
       │
       ▼
Document Loader + OCR
(PyPDFLoader + Tesseract)
       │
       ▼
Chunking
(LangChain Recursive Text Splitter)
       │
       ▼
Embedding Generation
(all-MiniLM-L6-v2)
       │
       ▼
Qdrant Vector Database
(Semantic Search)
       │
       ▼
Neo4j Knowledge Graph
(Entities & Relationships)
       │
       ▼
Hybrid Retriever
(Vector + Graph Fusion)
       │
       ▼
Llama 3 via Ollama
       │
       ▼
Streamlit Frontend
```

---

# Tech Stack

| Category         | Technology       |
| ---------------- | ---------------- |
| Language         | Python           |
| Frontend         | Streamlit        |
| Framework        | LangChain        |
| Vector Database  | Qdrant           |
| Graph Database   | Neo4j            |
| Embedding Model  | all-MiniLM-L6-v2 |
| LLM              | Llama 3          |
| Inference Engine | Ollama           |
| OCR              | Tesseract OCR    |
| PDF Processing   | PyPDFLoader      |
| Containerization | Docker           |

---

# Folder Structure

```text
Financial-RAG
│
├── app.py
├── requirements.txt
├── .env
│
├── data
│     └── reports
│
├── ingestion
│     ├── pdf_loader.py
│     ├── chunking.py
│     ├── ocr.py
│     └── parser.py
│
├── embeddings
│     └── embedding_model.py
│
├── vector_db
│     └── qdrant_setup.py
│
├── graph_db
│     └── neo4j_setup.py
│
├── retrieval
│     ├── vector_retriever.py
│     ├── graph_retriever.py
│     └── hybrid_retriever.py
│
├── llm
│     └── llm_model.py
│
├── chains
│     └── rag_chain.py
│
├── prompts
│     └── finance_prompt.py
│
├── frontend
│     └── streamlit_app.py
│
└── utils
```

---

# Workflow

### Document Ingestion

1. Load financial PDFs
2. Apply OCR (for scanned documents)
3. Extract text and tables
4. Split documents into chunks

### Embedding Generation

* all-MiniLM-L6-v2
* 384-dimensional embeddings

### Storage

#### Qdrant

Stores:

* Text embeddings
* Metadata
* Chunk references

#### Neo4j

Stores:

* Company entities
* Revenue
* Risks
* Executives
* Products
* Relationships

### Hybrid Retrieval

* Semantic similarity search from Qdrant
* Graph traversal from Neo4j
* Context fusion
* Prompt construction

### Answer Generation

* Llama 3 (Ollama)
* Citation-backed responses

---

# Example Questions

* What was Apple's revenue?
* Compare Microsoft and Nvidia operating margins.
* What risks are mentioned in Tesla's annual report?
* Which products contribute to Apple's revenue?
* Who are Microsoft's competitors?

---

# Explainability

The system provides:

* Source tracing
* Retrieved chunks
* Graph facts
* Citation-backed answers

---

# Scalability

Future improvements include:

* Persistent Qdrant server
* Neo4j clustering
* Docker deployment
* Redis caching
* GPU acceleration
* Streaming responses

---

# Future Enhancements

### Agentic AI

* LangGraph
* CrewAI
* AutoGen

### Specialized Agents

* Document Agent
* Financial Analyst Agent
* Comparison Agent
* Chart Agent
* News Agent
* Supervisor Agent

### Additional Features

* Memory Systems
* MCP Integration
* Real-time Financial APIs
* Interactive Dashboards
* Multi-document Support

---

# Applications

* Investment Research
* Enterprise Search
* Risk Analysis
* Financial Analytics
* Compliance Systems
* Knowledge Management

---

# Installation

```bash
git clone https://github.com/YOUR_USERNAME/Financial-RAG.git

cd Financial-RAG

pip install -r requirements.txt
```

---

# Run Streamlit Application

```bash
streamlit run frontend/streamlit_app.py
```

---

# Resume Highlight

> Built a GraphRAG-based Financial Research Copilot using LangChain, Qdrant, Neo4j, all-MiniLM-L6-v2, and Llama 3, enabling hybrid retrieval over financial reports with explainable citation-backed answers.

---

# Future Roadmap

* Multi-Agent Financial Copilot
* Real-Time Market Data
* MCP Support
* LangGraph Integration
* Financial KPI Dashboards
* Production Deployment with Docker

---

# License

MIT License

---

## ⭐ If you found this project useful, consider giving it a star.
