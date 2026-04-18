# AI Candidate Fit Analyzer

An AI-powered tool that evaluates job candidates based on **skills rather than CV signals like titles or years of experience**.

This project is designed to support modern **skills-based hiring**, helping recruiters quickly understand whether a candidate is actually a good fit for a role.

---

## What This Project Does

The AI Candidate Fit Analyzer compares:

- A **job description**
- A **candidate profile (CV / LinkedIn text)**

…and generates a structured hiring assessment including:

- Fit score (0–100)
- Matching skills
- Missing skills
- Strengths and risks
- Final hiring recommendation

---

## Why This Matters

Traditional hiring systems rely heavily on:
- Job titles
- Years of experience
- Keyword matching

This tool shifts the focus to:
> **What a candidate can actually do**

It demonstrates how AI can improve hiring decisions by:
- Reducing manual screening effort
- Improving consistency in evaluation
- Supporting skills-based hiring frameworks

---

## Key Features

### AI-Powered Evaluation
Automatically analyzes job + candidate fit using LLM reasoning.

### Structured Output
Returns a clear, structured breakdown:
- Fit Score (0–100)
- Skills match analysis
- Gaps and risks
- Recommendation (Hire / Consider / Reject)

### Skills-Based Thinking
Focuses on real capabilities instead of CV metadata.

### LLM Integration
Built using OpenAI API for reasoning and structured evaluation.

---

## 🛠️ Tech Stack

- Python  
- Streamlit (UI layer)  
- OpenAI API (LLM engine)  

---

## Installation

Clone the repository:

```bash id="k3v9pl"
git clone https://github.com/yourusername/ai-candidate-fit.git
cd ai-candidate-fit
pip install -r requirements.txt
Create a .streamlit/secrets.toml file:
OPENAI_API_KEY = "your-api-key-here"
Then Run:
streamlit run app.py
