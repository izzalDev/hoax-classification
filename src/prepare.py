import pandas as pd
from data.news_dao import NewsDAO
from tqdm import tqdm
import time

news_count = NewsDAO.get_news_total_count()
limit = 100
offset = 0
news_list = []

with tqdm(total=news_count, desc="Fetching News") as pbar:
    for i in range(0, news_count, limit):
        news_list += NewsDAO.get_news_list(limit, offset=i)
        pbar.update(limit)
    
df = pd.DataFrame.from_records([news.to_dict() for news in news_list])
df.to_csv('data/antihoax.csv', index=False)


