from app.rag.loader import load_folder
from app.rag.splitter import split_text

docs = load_folder("knowledge_base")

for doc in docs:
    print("=" * 60)
    print(doc["source"])

    chunks = split_text(doc["text"])

    print(f"Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i+1}")
        print(chunk[:200])