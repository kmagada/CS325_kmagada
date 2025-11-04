import json
import numpy as np
from typing import List, Dict, Tuple

def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    a = np.array(vec_a)
    b = np.array(vec_b)
    dot = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(dot / (norm_a * norm_b))

def rank_top_jobs(
    resume_vector: List[float],
    job_embeddings: List[Dict],
    top_n: int = 10
) -> List[Tuple[Dict, float]]:
    """
    Rank top N jobs by similarity to the resume vector.
    job_embeddings is expected to be a list of dicts like:
    [
        { "job_id": "123", "vector": [...], "metadata": {...job info...} },
        ...
    ]
    """
    scored_jobs = []

    for emb_entry in job_embeddings:
        vector = emb_entry["vector"]
        score = cosine_similarity(resume_vector, vector)

        # attach metadata (e.g. title, company, location)
        job_info = emb_entry.get("metadata", {})
        scored_jobs.append((job_info, score))

    scored_jobs.sort(key=lambda x: x[1], reverse=True)
    top_jobs = scored_jobs[:top_n]

    print_ranked_jobs(top_jobs)
    return top_jobs

def print_ranked_jobs(ranked_jobs: List[Tuple[Dict, float]]):
    print("\n=== Top Job Matches ===")
    for idx, (job, score) in enumerate(ranked_jobs, 1):
        title = job.get("job_title", "no title!")
        company = job.get("employer_name", "no company name!")
        city = job.get("job_city", "")
        state = job.get("job_state", "")
        print(f"{idx}. {title} at {company}\n ({city}, {state})\t Similarity: {score:.2%}\n")
