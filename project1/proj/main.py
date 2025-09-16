import http.client

conn = http.client.HTTPSConnection("li-data-scraper.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "a7d9c93d88mshd416eddf6bc76e8p1f29efjsn9578710bfc4c",
    'x-rapidapi-host': "li-data-scraper.p.rapidapi.com"
}

conn.request("GET", "/get-profile-data-by-url?url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fadamselipsky%2F", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))