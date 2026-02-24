import streamlit as st
import tempfile

from src.parser.resume_parser import extract_resume_text
from src.nlp.preprocess import preprocess_to_string
from src.nlp.skill_extractor import extract_skills
from src.matching.job_matcher import compute_similarity, get_match_label
from src.scoring.ats_scorer import calculate_skill_match, calculate_final_ats_score

st.set_page_config(page_title="AI Resume Screener", page_icon="📄", layout="centered")

st.title("🤖 AI Resume Screening System")
st.markdown("Upload a resume and compare it with a job description.")

# Upload resume
uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("📝 Paste Job Description", height=200)

if st.button("🚀 Analyze Resume"):

    if uploaded_file is None or not job_description.strip():
        st.warning("Please upload a resume and paste job description.")
    else:
        with st.spinner("Analyzing..."):

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                resume_path = tmp.name

            # Resume processing
            raw_text = extract_resume_text(resume_path)
            clean_resume = preprocess_to_string(raw_text)

            # Job processing
            clean_job = preprocess_to_string(job_description)

            # Skills
            resume_skills = extract_skills(clean_resume)

            # Scores
            similarity_score = compute_similarity(clean_resume, clean_job)
            skill_match_score, matched_skills, missing_skills = calculate_skill_match(resume_skills, clean_job)
            final_score = calculate_final_ats_score(similarity_score, skill_match_score)
            match_label = get_match_label(final_score)

        st.success("Analysis Complete ✅")

        # Results
        st.subheader("🏆 ATS Results")
        st.metric("Final ATS Score", f"{final_score}%")
        st.write(f"**Match Level:** {match_label}")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                for skill in matched_skills:
                    st.write("✔", skill)
            else:
                st.write("No matched skills found.")

        with col2:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                for skill in missing_skills:
                    st.write("✘", skill)
            else:
                st.write("No missing skills 🎉")