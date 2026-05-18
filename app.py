import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.embeddings import compute_similarity
from utils.gpt_utils import generate_interview_questions

# Page config
st.set_page_config(page_title="AI Resume Screening Assistant", layout="centered")

# Title
st.title(" AI Resume Screening & Interview Assistant")

st.write("Upload a resume and compare it with a job description using AI.")

# Job Description Input
job_description = st.text_area(" Paste Job Description", height=200)

# File Upload
uploaded_file = st.file_uploader(" Upload Resume (PDF)", type=["pdf"])

# Button Trigger
if st.button("Analyze Resume"):

    if uploaded_file is None or job_description.strip() == "":
        st.error("Please upload a resume and enter job description")
    else:

        # Step 1: Extract text
        resume_text = extract_text_from_pdf(uploaded_file)

        # Step 2: Compute similarity score
        score = compute_similarity(resume_text, job_description)

        # Step 3: Display Score
        st.subheader(" Match Score")
        st.metric(label="AI Compatibility Score", value=f"{score} %")

        # Score interpretation
        if score >= 80:
            st.success("Excellent Match ")
        elif score >= 60:
            st.warning("Moderate Match ")
        else:
            st.error("Low Match ")

        # Step 4: Interview Questions
        st.subheader(" AI Generated Interview Questions")

        with st.spinner("Generating questions using AI..."):
            questions = generate_interview_questions(resume_text, job_description)

        st.write(questions)
