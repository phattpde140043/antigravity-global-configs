---
name: vector-search
description: "Expert in Vector Databases and Similarity Search. Focuses on semantic retrieval, RAG optimization, and high-scale nearest neighbor search patterns."
---

# Vector Search & Semantic Retrieval

Expertise in building scalable similarity search systems for AI applications.

## 🏗️ Retrieval Patterns
- **Semantic Search**: Use dense vector embeddings (OpenAI, HuggingFace) to find meaning-based matches.
- **Hybrid Search**: Combine vector search with keyword-based filters (BM25) to improve precision.
- **RAG Optimization**: Retrieve the most relevant chunks for LLM augmentation using cosine similarity or dot product.
- **Nearest Neighbor (k-NN)**: Efficiently find the $k$ most similar items in high-dimensional space.

## 🚀 Scaling & Performance
- **Indexing**: Choose appropriate index types (HNSW, Flat, IVF-PQ) based on the scale and latency requirements.
- **Filtering**: Use metadata filtering to narrow down search space before or during vector search.
- **Embedding Management**: Handle embedding versioning and re-indexing when models change.

## 🛡️ Best Practices
- **Normalization**: Ensure vectors are normalized if using Cosine Similarity.
- **Chunking Strategy**: Optimize text chunk sizes for the specific retrieval goal (sentences vs paragraphs).
- **Evaluation**: Use metrics like Precision@K, Recall@K, and MRR to measure retrieval quality.

## 📋 Verification Checklist
- [ ] Is the vector similarity metric (Cosine vs Dot Product) correct for the model?
- [ ] Is Hybrid search considered for better keyword precision?
- [ ] Is the indexing strategy (e.g., HNSW) appropriate for the data scale?
- [ ] Are metadata filters applied to optimize search latency?
- [ ] Is there an evaluation metric in place for retrieval quality?
