from app.rag.loader import load_folder
from app.rag.splitter import split_text
from app.rag.embedder import embed_texts

docs = load_folder("knowledge_base")

all_chunks = []

for doc in docs:
    chunks = split_text(doc["text"])
    all_chunks.extend(chunks)

print(f"Chunks: {len(all_chunks)}")

embeddings = embed_texts(all_chunks)

print(f"Embedding shape: {embeddings.shape}")

print("First 10 values of first embedding:")
print(embeddings[0][:10])