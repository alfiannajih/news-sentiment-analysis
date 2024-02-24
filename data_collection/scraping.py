from dotenv import load_dotenv
import requests
import os
import json
from tqdm import tqdm

load_dotenv()

api_key = os.getenv("SECRET_KEY")

def get_news(q, api_key):
    url = "https://newsapi.org/v2/everything"
    
    raw_data = requests.get(url, params={"q": q, "apiKey": api_key}).json()
    cleaned_data = []
    for article in tqdm(raw_data["articles"]):
        cleaned_data.append({
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "date": article["publishedAt"]
        })
    
    with open('output.txt', 'w') as outfile:
        for entry in cleaned_data:
            json.dump(entry, outfile)
            outfile.write('\n')

get_news("bitcoin", api_key)