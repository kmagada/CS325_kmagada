import os
import datapull
import embedding


def main():
    JOB_FILE = os.path.join('project1', 'data', 'jobData.json')
    RESUME_FILE = os.path.join('project1', 'data', 'resumeData.json')

    try:
        #pulls data with the API and saves to a JSON file
        datapull.main()

        #embeds the resume and job listings
        job_embeddings = embedding.main(JOB_FILE)
        #resume_embeddings = embedding.main(RESUME_FILE)
        
        # add Top N Selection here for top 10 jobs for the resume maybe use the OpenAI embedding to show recommendations
        # here
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()