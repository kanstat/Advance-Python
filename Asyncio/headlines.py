from constants_ import NEWS_API
import requests
import json
# newsapi = NewsApiClient(NEWS_API)   
def get_topheadlines():
    top_headlines_list = []
    headlines_url =f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API}"
    res = requests.get(headlines_url)
    resp = json.loads(res.text)
    for itm in resp["articles"]:
        titles = itm["title"]
        top_headlines_list.append(titles)
    return top_headlines_list

