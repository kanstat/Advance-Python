import json
import requests
from const import NEWSURL



global titles_lst 
titles_lst = []

def get_news():
    titles_lst = []
    news_url = f"{NEWSURL}"
    resp = requests.get(news_url)
    resp = json.loads(resp.text)
    for itm in resp["articles"]:
        titles = itm["title"]  
        titles_lst.append(titles)
    return titles_lst