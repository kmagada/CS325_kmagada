import json
import numpy as np
from typing import List, Dict, Tuple

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    a = np.array(vec_a)
    b = np.array(vec_b)
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot / (norm_a * norm_b))

def load_resume_embedding(path: str = "./project1/data/resumeEmbedding.json") -> List[float]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["vector"]

def load_job_embeddings(path: str = "./project1/data/jobEmbeddings.json") -> List[Dict]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def rank_top_jobs(
    resume_vector: List[float],
    job_embeddings: List[Dict],
    job_data_path: str = "./project1/data/jobData.json",
    top_n: int = 10
) -> List[Tuple[Dict, float]]:
    """Return top N job postings ranked by similarity to the resume."""
    # Load original job data to get titles, company, location, etc.
    with open(job_data_path, "r", encoding="utf-8") as f:
        job_data = json.load(f)["data"]

    scored_jobs = []
    for emb_entry in job_embeddings:
        job_id = emb_entry["job_id"]
        vector = emb_entry["vector"]
        score = cosine_similarity(resume_vector, vector)

        # match the embedding back to the original job info
        job_info = next((job for job in job_data if job.get("job_id") == job_id), None)
        if job_info:
            scored_jobs.append((job_info, score))

    # Sort descending by similarity score
    scored_jobs.sort(key=lambda x: x[1], reverse=True)

    return scored_jobs[:top_n]

def print_ranked_jobs(ranked_jobs: List[Tuple[Dict, float]]):
    """Nicely print the top N ranked jobs."""
    print("\n=== 🏆 Top Job Matches ===")
    for idx, (job, score) in enumerate(ranked_jobs, 1):
        title = job.get("job_title", "N/A")
        company = job.get("employer_name", "N/A")
        city = job.get("job_city", "")
        state = job.get("job_state", "")
        print(f"{idx}. {title} at {company} ({city}, {state}) — Similarity: {score:.4f}")
