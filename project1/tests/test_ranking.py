from ranking import rank_top_jobs

def test_rank_top_jobs_basic():
    resume_vec = [1,0]
    job_embeddings = [
        {"vector": [1,0], "metadata": {"job_title": "A"}},
        {"vector": [0,1], "metadata": {"job_title": "B"}},
    ]

    result = rank_top_jobs(resume_vec, job_embeddings, top_n=1)

    assert len(result) == 1
    job, score = result[0]
    assert job["job_title"] == "A"
    assert score > 0.9
