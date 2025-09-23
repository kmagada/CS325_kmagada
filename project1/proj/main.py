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
        res = conn.getresponse()
        raw_data = res.read()
        decoded = json.loads(raw_data.decode("utf-8"))

        # Ensure directory exists
        file_path = "./project1/data/tempData.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # always overwrite it with latest data
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(decoded, f, ensure_ascii=False, indent=4)

        # Keep a copy in memory for embedding i think might delete tempData.json
        data = decoded
        print("Data saved successfully.")

    except Exception as e:
        print("Error:", e)
    finally:
        try:
            conn.close()
        except Exception:
            pass


if __name__ == '__main__':
    main()
