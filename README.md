Project: Document Q&A Assistant (RAG)

Upload your own documents (PDFs, notes, articles), ask questions in plain language, get answers grounded in those documents with citations back to the source.

Why this one: RAG — Retrieval-Augmented Generation — is the single most common pattern in real AI product work right now. Building one end to end means you can actually discuss chunking strategy, embeddings, and retrieval quality in an interview, which is exactly what gets asked.

Stages

Stage 1 — Talk to a model at all

Get an API key (Anthropic, OpenAI, or run a local model with Ollama if you'd rather not pay)
Simple terminal chat loop: user types, model replies, conversation history is maintained in a list
Teaches: lists, dicts, while loops, API requests, environment variables for secrets (never hardcode a key and push it to GitHub — use a .env file and a .gitignore)

Stage 2 — Read the documents

Extract text from PDFs and .txt files
Split text into overlapping chunks of a few hundred words
Teaches: file handling, string manipulation, pathlib

Stage 3 — Retrieval

Convert chunks to embeddings, store them in a vector database (Chroma is the easiest to start with)
On each question, retrieve the most relevant chunks and pass them to the model as context
Teaches: the core concept, plus working with third-party libraries

Stage 4 — Make it a real app

Refactor into classes: DocumentLoader, VectorStore, ChatEngine
Handle failures gracefully — API timeouts, unreadable PDFs, empty results
Add a Streamlit UI (roughly 50 lines gets you a usable web interface)

Stage 5 — The differentiators

Show source citations with each answer, so users can verify
An eval script: a set of test questions with expected answers, scored automatically. Almost no junior portfolio has this, and it signals you understand that AI output needs measuring.
README explaining your chunking and retrieval choices and their tradeoffs
Lighter alternatives if that feels big
Resume analyzer — upload a resume and job description, get a match score and gap analysis
Meeting notes summarizer — transcript in, action items and decisions out as structured JSON
Smart expense categorizer — the tracker from before, but an LLM auto-categorizes each entry
