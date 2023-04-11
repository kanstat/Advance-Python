from dotenv import load_dotenv
import os 

load_dotenv()

TGAPI = os.getenv("TGAPI")
TGURL = f"https://api.telegram.org/bot{TGAPI}"

NEWSAPI = os.getenv("NEWSAPI")
NEWSURL = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWSAPI}"