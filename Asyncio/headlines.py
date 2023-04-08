import requests

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=9bb2a8ecd18543db82f1cd2b19d3e2df"

res = requests.get(url)
print(res.text)
