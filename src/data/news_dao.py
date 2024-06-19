import requests
from data.news_model import NewsModel
from dotenv import load_dotenv
import os
load_dotenv

class NewsDAO(NewsModel):
    API_URL = os.getenv("API_ENDPOINT")  # Replace with your actual API URL
    API_KEY = os.getenv("API_KEY")
    verbose = True

    @staticmethod
    def api_call(endpoint, data={}):
        """
        Melakukan panggilan API dengan endpoint dan data yang diberikan.
        Mengembalikan respons dalam bentuk JSON.
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        data['key'] = NewsDAO.API_KEY
        response = requests.post(f"{NewsDAO.API_URL}{endpoint}", headers=headers, data=data)
        response.raise_for_status()
        return response.json()

    @classmethod
    def get_news_list(cls, limit=10, offset=0, verbose=True):
        """
        Mendapatkan daftar berita dengan batasan jumlah dan offset tertentu.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        cls.verbose = verbose
        response = cls.api_call('/antihoax/', {'limit': limit, 'offset': offset})
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list

    @classmethod
    def get_news_item(cls, news_id):
        """
        Mendapatkan detail berita berdasarkan ID.
        Mengembalikan objek NewsModel.
        """
        response = cls.api_call('/antihoax/', {'id': news_id})
        return NewsModel.from_json(response)

    @classmethod
    def get_news_total_count(cls):
        """
        Mendapatkan total jumlah berita.
        Mengembalikan jumlah total berita.
        """
        return cls.api_call('/antihoax/get_total')

    @classmethod
    def search_news(cls, method, value, limit=10, total=0):
        """
        Mencari berita berdasarkan metode dan nilai tertentu.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call('/antihoax/search', {'method': method, 'value': value, 'limit': limit, 'total': total})
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list

    @classmethod
    def search_news_by_date(cls, start, end):
        """
        Mencari berita berdasarkan rentang tanggal.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call('/antihoax/search_date', {'start': start, 'end': end})
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list


    @classmethod
    def get_random_news(cls):
        """
        Mendapatkan berita acak.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call('/antihoax/random')
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list

    @classmethod
    def get_latest_news(cls):
        """
        Mendapatkan berita terbaru.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call('/antihoax/latest')
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list

    @classmethod
    def get_popular_news(cls):
        """
        Mendapatkan berita populer.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call('/antihoax/get_popular_article')
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list

    @classmethod
    def get_news_by_author(cls, author_id):
        """
        Mendapatkan berita berdasarkan ID penulis.
        Mengembalikan daftar berita dalam bentuk objek NewsModel.
        """
        response = cls.api_call(f'/antihoax/author/{author_id}')
        news_list = [NewsModel.from_json(news_item) for news_item in response]  # Using Halo spinner
        return news_list
