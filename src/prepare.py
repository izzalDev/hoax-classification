import requests
import os
from dotenv import load_dotenv
from tqdm.auto import tqdm

load_dotenv
base_url = os.getenv("API_ENDPOINT")
api_key = os.getenv("API_KEY")

class News:
    def __init__(self, id: int, authors: str, status: str, classification: str, title: str, content: str, fact: str, references: str, source_issue: str, source_link: str, picture1: str, picture2: str, tanggal: str, tags: str, conclusion: str):
        self.id = id
        self.authors = authors
        self.status = status
        self.classification = classification
        self.title = title
        self.content = content
        self.fact = fact
        self.references = references
        self.source_issue = source_issue
        self.source_link = source_link
        self.picture1 = picture1
        self.picture2 = picture2
        self.tanggal = tanggal
        self.tags = tags
        self.conclusion = conclusion
        
    def __init__(self):
        pass

    def __get_by_id(self, id):
        response = requests.post(os.path.join(base_url, "antihoax/"), data={
            'key': api_key,
            'id': id,
        })
        return response.json()
    
    def __get_total(self):
        response = requests.post(os.path.join(base_url, "antihoax/get_total"), data={
            'key': api_key,
        })
        return response.json()
    
    def search(key, method, value, limit=None, total=None):
        response = requests.post(os.path.join(base_url, "antihoax/search"), data={
            'key': api_key,
            'method': method,
            'value': value,
            'limit': limit,
            'total': total,
        })
        return response.json()

    def search_date(self, start, end):
        response = requests.post(os.path.join(base_url, "antihoax/search_date"), data={
            'key': api_key,
            'start': start,
            'end' : end,
        })
        return response.json()

    def get_random(self):
        response = requests.post(os.path.join(base_url, "antihoax/get_random"), data={
            'key': api_key,
        })
        return response.json()

    def get_latest(self):
        response = requests.post(os.path.join(base_url, "antihoax/latest"), data={
            'key': api_key,
        })
        return response.json()

    def get_popular(self):
        response = requests.post(os.path.join(base_url, "antihoax/get_popular_article"), data={
            'key': api_key,
        })
        return response.json()

    def __len__(self):
        return self.__get_total()

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop, step = key.indices(len(self))
            return [self.__get_by_id(i) for i in tqdm(range(start, stop, step))]
        elif isinstance(key, int):
            return self.__get_by_id(key)
        elif isinstance(key, tuple):
            return [self.__get_by_id(i) for i in tqdm(key)]
        else:
            raise TypeError(f'Invalid argument type: {type(key)}')

list_news = News()[:9]
print(list_news[4])

