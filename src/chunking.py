from langchain_core.documents import Document
import re

def split_documents(documents):
    full_text = "\n".join([doc.page_content for doc in documents])

    sections = re.split(r'(SUMMARY OF\s+IS\s*\d+\s*:\s*\d+)', full_text)

    chunks = []

    for i in range(1, len(sections), 2):
        title = sections[i]
        content = sections[i+1] if i+1 < len(sections) else ""

        chunk_text = title + content

        chunks.append(Document(page_content=chunk_text))

    return chunks
