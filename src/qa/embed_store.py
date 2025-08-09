from sentence_transformers import SentenceTransformer
import faiss


# going from plain text chunking as there is no structure to transcript
def chunk_text(text, chunk_size=256, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks


def embed_text(text_chunks):
    # Load the pre-trained model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Encode the text chunks to generate embeddings
    embeddings = model.encode(text_chunks)

    print(f"Shape of embeddings: {embeddings.shape}")
    index = faiss.IndexFlatL2(embeddings.shape[-1])
    index.add(embeddings)

    return index
