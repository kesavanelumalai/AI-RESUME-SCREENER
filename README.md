AI RESUME SCREENER
📌 Overview

The AI Resume Screener automates resume filtering by comparing candidate resumes with a job description and generating a relevance score. It helps recruiters quickly identify the most suitable candidates without manual screening.

🎯 Problem Statement

Manual resume screening is:

Time-consuming

Inconsistent

Error-prone

This project solves the problem by using AI to automatically evaluate and rank resumes based on their relevance to a given job description.

🚀 Features

📄 Upload resume (PDF)

🧠 Automatic text extraction

🔍 Resume vs Job Description matching

📊 Similarity scoring

🏆 Candidate ranking

⚡ FastAPI backend

🌐 Simple web interface

🛠️ Tech Stack

Languages & Frameworks

Python

FastAPI

HTML / CSS

Libraries

pdfplumber (PDF parsing)

scikit-learn

TF-IDF Vectorizer

Cosine Similarity

NLP preprocessing tools

⚙️ How It Works

Resume Upload
User uploads a resume in PDF format.

Text Extraction
Resume text is extracted using pdfplumber.

Text Preprocessing

Lowercasing

Stopword removal

Tokenization

Job Description Input
User provides the job description manually.

Feature Extraction
TF-IDF converts text into numerical vectors.

Similarity Matching
Cosine similarity compares resume and job description.

Scoring
Generates a relevance score (0–100).

📊 Example Output
Resume Score: 84%

Top Skills Detected:
✔ Python
✔ Machine Learning
✔ NLP
✔ Deep Learning

Recommendation: Highly Suitable Candidate
🧠 Project Architecture
Resume Upload → Text Extraction → NLP Processing → TF-IDF Vectorization → Cosine Similarity → Score Output
📁 Folder Structure
AI_resume_screener/
│
├── app.py
├── requirements.txt
├── src/
│   ├── parser/
│   ├── matcher/
│   └── utils/
│
├── templates/
├── static/
└── README.md
🧪 Challenges

Handling different resume formats

Cleaning noisy PDF text

Improving matching accuracy

🔮 Future Improvements

BERT-based semantic matching

Multi-language resume support

ATS integration

Resume feedback system

Candidate ranking dashboard

🏁 Conclusion

This project demonstrates how AI and NLP can automate real-world recruitment workflows. It reduces manual effort, improves screening accuracy, and provides a scalable solution for modern hiring systems.
