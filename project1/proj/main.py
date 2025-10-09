import os
import datapull
import embedding
import ranking

def main():
    JOB_FILE = os.path.join('project1', 'data', 'jobData.json')
    RESUME_FILE = os.path.join('project1', 'data', 'resume.json')

    try:
        #pulls data with the API and saves to a JSON file
        datapull.main()

        #embeds the resume and job listings
        job_embeddings = embedding.embed_joblistings(JOB_FILE)
        resume_embeddings = embedding.embed_resume(RESUME_FILE)
        
        # Top N Selection
        job_vecs = load_job_embeddings()
        resume_vec = load_resume_embedding()
        ranked = rank_top_jobs(resume_vec, job_vecs, top_n=10)

        # print ranked jobs
        print_ranked_jobs(ranked)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()