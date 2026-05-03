import time
from src.load_data import load_documents
from src.chunking import split_documents
from src.embeddings import get_embedding_model
from src.retriever import build_vector_store, get_retriever
from src.utils import extract_standards

documents = load_documents("data/dataset.pdf")
chunks = split_documents(documents)
embeddings = get_embedding_model()
vector_db = build_vector_store(chunks, embeddings)
retriever = get_retriever(vector_db)


def rag_pipeline(query):
    start = time.time()

    query = query + " BIS standard IS number cement concrete"

    docs = retriever.invoke(query)
    texts = [doc.page_content for doc in docs]

    print("QUERY:", query)
    for doc in docs:
        print(doc.page_content[:300])

    standards = extract_standards(texts)

    latency = time.time() - start

    return standards, latency
