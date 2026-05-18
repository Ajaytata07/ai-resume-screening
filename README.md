# AI Resume Screening & Interview Assistant

This project is an AI-powered web application that helps compare resumes with job descriptions using Natural Language Processing (NLP) and Machine Learning techniques.

The application allows users to upload a resume in PDF format and paste a job description. It then analyzes how well the resume matches the job role and generates interview questions using AI.

The main goal of this project was to learn how modern AI systems use embeddings, semantic similarity, and Large Language Models (LLMs) in real-world applications like recruitment platforms and ATS systems.

---

## Features

- Upload resume PDFs
- Extract text from resumes
- Compare resumes with job descriptions
- Generate AI-based match score
- Create interview questions automatically
- Simple and interactive Streamlit interface

---

## Technologies Used

- Python
- Streamlit
- OpenAI API
- Sentence Transformers
- Scikit-learn
- PyPDF2
- NumPy
- Pandas

---

## How the Project Works

### Step 1: Resume Upload
The user uploads a resume in PDF format.

### Step 2: Text Extraction
The application extracts text from the PDF using PyPDF2.

### Step 3: Embedding Generation
The resume text and job description are converted into vector embeddings using the `all-MiniLM-L6-v2` sentence transformer model.

### Step 4: Similarity Matching
Cosine similarity is used to compare the embeddings and generate a match score.

### Step 5: AI Interview Questions
The application sends the resume and job description to OpenAI GPT models to generate interview questions.

---

## Project Structure

```bash
ai-resume-screening/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── parser.py
│   ├── embeddings.py
│   └── gpt_utils.py
│
├── resumes/
└── data/
