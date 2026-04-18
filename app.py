import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Candidate Fit Analyzer")
st.write("Evaluate Candidate based on skills not just CVs")

job = st.text_area("Paste Job description here")
candidate = st.text_area("Paste candidate profile")

if st.button("Analyze Fit"):
    prompt = f"""
    You are an AI hiring assistant focused on skills-based hiring.

    Compare the job description and candidate profile.

    Provide:
    1. Fit Score (0-100)
    2. Key matching skills
    3. Missing skills
    4. Strengths
    5. Risks
    6. Final recommendation (Hire / Consider / Reject)

    Structure the output clearly.

    Job:
    {job}

    Candidate:
    {candidate}
    """

    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}]
    )

    st.write(response.choices[0].message.content)
