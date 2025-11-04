import os
import datapull         # using Rapi Api to pull job data
import embedding        # embedding job and resume data using OpenAI
import ranking          # ranking job listings 

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
        ranked = ranking.rank_top_jobs(resume_embeddings, job_embeddings, top_n=5)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()