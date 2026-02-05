import requests
from bs4 import BeautifulSoup

def ultimas_noticias():
    url = "https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
    site = requests.get(url)
    noticias = BeautifulSoup(site.text, 'html.parser')
    noticias_texto = []
    for item in noticias.findAll('item')[:4]:
        titulo = item.title.text
        noticias_texto.append(titulo)
    return " ".join(noticias_texto)


