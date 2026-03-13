from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

with open("rag_data/medical_data.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def retrieve_context(question: str) -> str:
    q_vec = vectorizer.transform([question])
    similarities = cosine_similarity(q_vec, doc_vectors)
    best_idx = np.argmax(similarities)
    return documents[best_idx].strip()