# OpsMind — AI-Powered Internal Engineering Knowledge Assistant

OpsMind is an AI-powered internal engineering knowledge assistant designed to help engineering teams quickly investigate operational issues using company knowledge, incident records, service documentation, architecture documents, runbooks, and policies.

The project combines **OKF-based knowledge organization, semantic search, FAISS vector retrieval, RAG, Groq LLM, Streamlit, and MCP tools** into one practical engineering support system.

---

## Project Overview

In a typical engineering environment, operational knowledge is distributed across incident reports, service documentation, architecture documents, runbooks, and company policies.

Finding the correct information manually can take time.

OpsMind provides a centralized AI-based interface where engineers can ask questions such as:

* Why are orders failing?
* What should I do when the Payment API returns a 500 error?
* How do I troubleshoot an authentication failure?
* What services does the Order Service depend on?
* Which incidents are related to order failures?
* What information is available about a particular service?

OpsMind retrieves relevant internal knowledge and uses an LLM to generate an answer based only on the retrieved context.

---

## Key Features

* Internal engineering knowledge base
* OKF-style structured knowledge organization
* Document chunking and knowledge-base generation
* Semantic search using sentence embeddings
* FAISS vector similarity search
* RAG-based question answering
* Groq LLM integration
* Source-aware answers
* Relevance filtering for unknown questions
* Streamlit web interface
* MCP server with reusable engineering tools
* Incident and service dependency search

---

## Architecture

```text
                    Engineering Knowledge
                            |
                            v
                +-------------------------+
                |      Knowledge Docs     |
                |-------------------------|
                | Services                |
                | Incidents               |
                | Runbooks                |
                | Architecture            |
                | Policies                |
                +------------+------------+
                             |
                             v
                     build_okf.py
                             |
                             v
                  Knowledge Base
                  129 Knowledge Chunks
                             |
                             v
                  Sentence Transformers
                   all-MiniLM-L6-v2
                             |
                             v
                    384-D Embeddings
                             |
                             v
                         FAISS
                             |
                             v
                 Semantic Retrieval
                             |
                             v
                       Groq LLM
                             |
                             v
                  Answer + Sources
                             |
                             v
                      Streamlit UI


                    MCP Integration
                            |
            +---------------+----------------+
            |               |                |
            v               v                v
   search_knowledge  search_incidents  service_dependencies
```

---

## RAG Workflow

OpsMind follows a Retrieval-Augmented Generation workflow.

```text
User Question
      |
      v
Question Embedding
      |
      v
FAISS Semantic Search
      |
      v
Relevant Knowledge Chunks
      |
      v
Context Construction
      |
      v
Groq LLM
      |
      v
Grounded Answer
      |
      v
Sources
```

The LLM receives retrieved company knowledge as context and is instructed to answer using that context rather than inventing information.

---

## Knowledge Base

The project contains engineering knowledge organized into different categories.

### Services

Examples:

* Authentication Service
* Order Service
* Inventory Service
* Payment API
* Notification Service
* Search Service

### Incidents

Examples:

* Order Service HTTP 500 errors
* Authentication failures
* Payment timeout
* Inventory synchronization issues
* Deployment failures
* Database timeout incidents

### Runbooks

Examples:

* Authentication failure troubleshooting
* Database timeout troubleshooting
* Inventory synchronization failure
* Order API 500 troubleshooting
* Payment API 500 troubleshooting
* Service degradation handling

### Architecture

Examples:

* Database architecture
* Service dependencies
* System architecture

### Policies

Examples:

* Deployment policy
* Escalation policy
* Incident severity policy

---

## OKF Knowledge Processing

The project uses `build_okf.py` to process the engineering documentation.

The pipeline is:

```text
Markdown Documents
       |
       v
Document Processing
       |
       v
Section Chunking
       |
       v
Metadata Extraction
       |
       v
knowledge_base.json
```

The current knowledge base contains:

```text
129 knowledge chunks
```

---

## Embeddings

OpsMind uses:

```text
all-MiniLM-L6-v2
```

to convert text into numerical vector representations.

The embedding dimension is:

```text
384
```

This allows the system to compare the meaning of a user's question with the meaning of stored engineering knowledge.

---

## FAISS Vector Search

OpsMind uses **FAISS** for vector similarity search.

The generated vector index is:

```text
knowledge.index
```

The system searches the vector database to find knowledge chunks that are semantically related to the user's question.

Example:

```text
Question:
Why are orders failing?

        ↓

Semantic Search

        ↓

Relevant knowledge:
- Order Service
- Order Service incidents
- Inventory Service
- Deployment incidents
```

---

## RAG Answer Generation

After retrieving relevant knowledge, OpsMind builds a context containing the retrieved documents.

The context is sent to the Groq LLM with instructions such as:

```text
Answer the user's question using only the provided context.

If the answer is not available in the context,
say that the information is not available
in the OpsMind knowledge base.

Do not invent facts.
```

This helps keep answers grounded in the internal knowledge base.

---

## Groq LLM

OpsMind uses Groq for LLM-based answer generation.

The project currently uses:

```text
openai/gpt-oss-20b
```

The API key is stored in the `.env` file and is not included directly in the source code.

Example:

```text
GROQ_API_KEY=your_api_key
```

---

## MCP Integration

OpsMind also provides an MCP server that exposes engineering knowledge as reusable tools.

The MCP server provides three tools:

### 1. Search Knowledge

```text
search_knowledge(query)
```

Searches the OpsMind knowledge base for relevant engineering information.

### 2. Search Incidents

```text
search_incidents(query)
```

Searches incident records for operational problems and previous incidents.

### 3. Get Service Dependencies

```text
get_service_dependencies(service)
```

Returns dependency information for a specific service.

Example:

```text
Order Service
     |
     +---- Payment API
     |
     +---- Inventory Service
```

These tools allow an MCP-compatible client or agent to interact with the OpsMind engineering knowledge system.

---

## Streamlit Interface

OpsMind provides a simple Streamlit interface.

The user enters a question:

```text
Why are orders failing?
```

OpsMind then:

```text
Question
   ↓
Semant
```
