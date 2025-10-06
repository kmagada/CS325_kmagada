import json
import ssl
import http.client
import os


def create_ssl_context():
    try:
        import certifi
        cafile = certifi.where()
        return ssl.create_default_context(cafile=cafile)
    except Exception:
        return ssl.create_default_context()


def main():
    print("Running datapull.py...")
    ctx = create_ssl_context()
    try:
        conn = http.client.HTTPSConnection("jsearch.p.rapidapi.com", context=ctx)
        headers = {
            'x-rapidapi-key': "a7d9c93d88mshd416eddf6bc76e8p1f29efjsn9578710bfc4c",
            'x-rapidapi-host': "jsearch.p.rapidapi.com"
        }
        conn.request(
            "GET",
            "/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all",
            headers=headers
        )

        # connecting and reading data
        raw_data = conn.getresponse().read()
        decoded = json.loads(raw_data.decode("utf-8"))

        # file path for JSON
        file_path = "./project1/data/tempData.json"


        # always overwrite file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(decoded, f, ensure_ascii=False, indent=4)

        # Keep a copy in memory for embedding i think might delete tempData.json so idk or return the data instead
        data = decoded
        conn.close()
        print("Data pulled successfully.")

    except Exception as e:
        print("In Datapull Error:", e)

if __name__ == '__main__':
    main()
