from sentence_transformers import SentenceTransformer

# Load once when the application starts
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: list[str]):
    """
    Convert a list of text chunks into embeddings.
    """
    return model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
    )