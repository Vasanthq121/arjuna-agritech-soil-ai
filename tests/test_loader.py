from pathlib import Path
from app.rag.loader import load_folder

print("Current working directory:", Path.cwd())

kb = Path("knowledge_base")
print("Knowledge base exists:", kb.exists())

if kb.exists():
    print("\nFiles found:")
    for f in kb.rglob("*"):
        print(f)

docs = load_folder("knowledge_base")

print(f"\nLoaded {len(docs)} documents")

for d in docs:
    print("=" * 60)
    print(d["source"])
    print(d["text"][:300])