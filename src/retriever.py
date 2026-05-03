from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, embeddings):
    return FAISS.from_documents(chunks, embeddings)

def get_retriever(vector_db):
    return vector_db.as_retriever(search_kwargs={"k": 15})
