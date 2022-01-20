import streamlit as st
from newsapi import NewsApiClient
#この先ニュース取得
api = NewsApiClient(api_key="b4db0f52d6fe498e8153750a1ba090f9")
api = NewsApiClient(api_key="APIキー")

print(api.get_everything(q='大阪'))