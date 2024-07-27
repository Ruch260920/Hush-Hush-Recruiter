import requests
import time
import threading
import pandas as pd
import time
from dotenv import load_dotenv
import os


urls = []
start = time.strftime('%X') 
for i in range(1,1001):
    urls.append(f"https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&pagesize=100&page={i}")

payload = payloadheaders = {
    'KEY': key,
    'api-key': api_key,
    'Content-Type': content_type,
    'Cookie': cookie
}
    
def data_fetch(urls):
    df_append = pd.DataFrame()
    i = 1
    for url in urls:
        time.sleep(1)
        rawResults = requests.request("GET", url, headers=headers, data=payload)
        results = rawResults.json()
        owners = [item['owner'] for item in results['items']]
        view_count = [item['view_count'] for item in results['items']]
        score = [item['score'] for item in results['items']]
        df_stackwebscrape = pd.DataFrame(owners)
        df_append = pd.concat([df_append, df_stackwebscrape], ignore_index=True)
        i+=1
    return df_append
        
df = data_fetch(urls)
df.to_csv('profile_links.csv',index=False)
