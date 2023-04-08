from dotenv import load_dotenv
import os 


load_dotenv()

TG_API = os.getenv("TG_API")

BASE_URL = f"https://api.telegram.org/bot{TG_API}"

