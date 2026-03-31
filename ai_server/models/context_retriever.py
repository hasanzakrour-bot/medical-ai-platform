from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# تحميل بيانات نصية طبية - سنستخدم قسم ملاحظات الأطباء من MIMIC-III كمثال
def load_medical_documents(max_docs=200):
    dataset = load_dataset("mimiciii_notes", split="train[:{}]".format(max_docs))
    # في الغالب العمود المطلوب هو TEXT أو TEXT أو NOTE
    docs = [entry['TEXT'] for entry in dataset if entry.get('TEXT')]
    return docs

documents = load_medical_documents()

vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def retrieve_context(question: str) -> str:
    q_vec = vectorizer.transform([question])
    similarities = cosine_similarity(q_vec, doc_vectors)
    best_idx = np.argmax(similarities)
    return documents[best_idx]