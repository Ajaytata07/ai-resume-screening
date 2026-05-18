import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_interview_questions(resume_text, job_description):
    """
    Generate AI interview questions based on resume + job description
    """

    prompt = f"""
    You are an expert technical recruiter.

    Based on the resume and job description below, generate 8–10 interview questions.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Focus on technical + behavioral questions.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content