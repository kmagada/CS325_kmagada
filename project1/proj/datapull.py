import json
import ssl
import http.client
import os
from dotenv import load_dotenv
load_dotenv()


def create_ssl_context():
    try:
        import certifi
        cafile = certifi.where()
        return ssl.create_default_context(cafile=cafile)
    except Exception:
        return ssl.create_default_context()

# because OPENAI wants a list of strings
def clean_job_data(raw_json):
    cleaned_jobs = []

    jobs = raw_json.get("data", [])
    for job in jobs:
        cleaned_jobs.append({
            "job_id": job.get("job_id"),
            "employer_name": job.get("employer_name"),
            "job_title": job.get("job_title"),
            "job_description": job.get("job_description"),
            "job_highlights": job.get("job_highlights", {}),
            "job_posted_at": job.get("job_posted_at_datetime_utc"),
            "job_city": job.get("job_city"),
            "job_state": job.get("job_state"),
            "job_country": job.get("job_country"),
            "job_url": job.get("job_apply_link"),
        })

    return {"data": cleaned_jobs}


def main():
    print("Running datapull.py...")
    ctx = create_ssl_context()
    try:
        conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com", context=ctx)
        headers = {
            'x-rapidapi-key': (os.getenv("RAPI_API_KEY")),
            'x-rapidapi-host': "jsearch.p.rapidapi.com"
        }
        conn.request(
            "GET",
            "/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all",
            headers=headers
        )

        # connecting and reading then cleaning data
        raw_data = conn.getresponse().read()
        decoded = json.loads(raw_data.decode("utf-8"))
        cleaned = clean_job_data(decoded)

        # file path for JSON
        file_path = "./project1/data/jobData.json"

        # always overwrite file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(cleaned, f, ensure_ascii=False, indent=4)

        conn.close()
        print("Data pulled successfully.")

    except Exception as e:
        print("In Datapull Error:", e)

if __name__ == '__main__':
    main()
