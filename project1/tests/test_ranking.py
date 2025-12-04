from proj.ranking import rank_top_jobs

def test_rank_top_jobs_basic():
    # Fake job vectors (the actual similarity math doesn't matter for this test)
    job_embeddings = [
        {"job_id": 1, "vector": [0.9, 0.0, 0.0]},
        {"job_id": 2, "vector": [0.7, 0.0, 0.0]},
        {"job_id": 3, "vector": [0.8, 0.0, 0.0]},
    ]

    resume_vector = [1.0, 0.0, 0.0]

    result = rank_top_jobs(resume_vector, job_embeddings, top_n=2)

    assert len(result) == 2
