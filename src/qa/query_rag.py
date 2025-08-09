from sentence_transformers import SentenceTransformer


def query(chunks, index, query, top_k=5):
    # Load the pre-trained model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Encode the text chunks to generate embeddings
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding[0], top_k)

    similar_content = "\n\n".join([chunks[index] for index in indices])

    return similar_content


