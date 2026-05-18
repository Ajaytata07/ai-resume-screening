from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load pretrained embedding model (lightweight + fast)
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    """
    Convert text → vector embedding
    """
    return model.encode([text])[0]


def compute_similarity(resume_text, job_description):
    """
    Compute similarity score between resume and job description
    """

    # Step 1: Convert text to embeddings
    resume_vector = get_embedding(resume_text)
    job_vector = get_embedding(job_description)

    # Step 2: Reshape for cosine similarity
    resume_vector = np.array(resume_vector).reshape(1, -1)
    job_vector = np.array(job_vector).reshape(1, -1)

    # Step 3: Compute similarity
    score = cosine_similarity(resume_vector, job_vector)[0][0]

    # Step 4: Convert to percentage
    return round(float(score * 100), 2)
