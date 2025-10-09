import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from typing import List

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ----------------- JOB LISTINGS -----------------

def extract_job_texts(job_json) -> List[str]:
    text_list = []
    for job in job_json.get("data", []):
        parts = []

        if job.get("job_title"):
            parts.append(job["job_title"])
        if job.get("job_description"):
            parts.append(job["job_description"])

        highlights = job.get("job_highlights", {})
        for values in highlights.values():
            if isinstance(values, list):
                parts.extend(values)

        if job.get("employer_name"):
            parts.append(f"Company: {job['employer_name']}")
        if job.get("job_city") or job.get("job_state"):
            parts.append(f"Location: {job.get('job_city', '')}, {job.get('job_state', '')}")

        full_text = "\n".join(filter(None, parts)).strip()
        if full_text:
            text_list.append(full_text)

    return text_list

def embed_joblistings(job_file: str):
    with open(job_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    job_embeddings = []
    for job in data.get("data", []):
        # Combine fields into one string for embedding
        text_to_embed = f"{job.get('job_title', '')} {job.get('job_description', '')}"
        response = client.embeddings.create(
            input=text_to_embed,
            model="text-embedding-3-small"
        )
        vector = response.data[0].embedding

        job_embeddings.append({
            "job_id": job.get("job_id"),
            "vector": vector,
            "metadata": {
                "job_title": job.get("job_title", "Unknown"),
                "employer_name": job.get("employer_name", "Unknown"),
                "job_city": job.get("job_city", ""),
                "job_state": job.get("job_state", "")
            }
        })

    return job_embeddings

# ----------------- RESUME -----------------

def extract_resume_text(resume_json) -> str:
    parts = []

    basics = resume_json.get("basics", {})
    if basics.get("name"):
        parts.append(basics["name"])
    if basics.get("label"):
        parts.append(basics["label"])
    if basics.get("summary"):
        parts.append(basics["summary"])

    for job in resume_json.get("work", []):
        parts.extend([
            job.get("position", ""),
            job.get("name", ""),
            job.get("summary", "")
        ])
        parts.extend(job.get("highlights", []))

    for edu in resume_json.get("education", []):
        parts.extend([
            edu.get("institution", ""),
            edu.get("studyType", ""),
            edu.get("area", "")
        ])

    for skill in resume_json.get("skills", []):
        parts.append(skill.get("name", ""))
        parts.extend(skill.get("keywords", []))

    for interest in resume_json.get("interests", []):
        parts.append(interest.get("name", ""))
        parts.extend(interest.get("keywords", []))

    return "\n".join(filter(None, parts)).strip()

def embed_resume(file_path: str, model="text-embedding-3-small"):
    """Read resume JSON, embed as a single vector, save output JSON."""
    with open(file_path, "r", encoding="utf-8") as f:
        resume_json = json.load(f)

    resume_text = extract_resume_text(resume_json)
    if not resume_text:
        raise ValueError("No text found in resume to embed.")

    response = client.embeddings.create(
        input=resume_text,
        model=model
    )

    embedding = response.data[0].embedding

    out_path = "./project1/data/resumeEmbedding.json"
    with open(out_path, "w", encoding="utf-8") as out_f:
        json.dump({"vector": embedding}, out_f, ensure_ascii=False, indent=2)

    print(f"Resume loaded and Embedded!")
    return embedding
