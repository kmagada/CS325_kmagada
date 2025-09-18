import json
import ssl
import http.client


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
        conn.request("GET", "/search?query=developer%20jobs%20in%20chicago&page=1&num_pages=1&country=us&date_posted=all", headers=headers)
        res = conn.getresponse()
        data = res.read()
        with open("project1/data/data.json", "w", encoding="utf-8") as f:
            json.dump(json.loads(data.decode("utf-8")), f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error:", e)
    finally:
        try:
            conn.close()
        except Exception:
            pass


if __name__ == '__main__':
    main()