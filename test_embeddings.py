from utils.embeddings import compute_similarity

resume = """
Python developer with experience in machine learning, SQL, and data analysis.
Built dashboards and worked on predictive models.
"""

job = """
We are looking for a Data Scientist with Python, machine learning, and SQL experience.
Knowledge of data visualization is required.
"""

score = compute_similarity(resume, job)

print("Match Score:", score)
