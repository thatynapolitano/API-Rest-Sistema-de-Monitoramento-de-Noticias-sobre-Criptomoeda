import requests
import pandas as pd

#inp == dados inputados pelo usuario para o POST;
inp = {'author': 'Test1', 'title': 'Test', 'description': 'more Test',
       'url': 'www.Test.com.br', 'urlToImage': 'htpps://Test', 
       'publishedAt': '2024-04-07 T19:00:00Z'}

url = 'http://127.0.0.1:5001/dados'

requests.post(url, json = inp)


