#Aceite Primor Titulos
from bs4 import BeautifulSoup
import requests

url = 'https://www.plazavea.com.pe/abarrotes?filter=specificationFilter_7337:con+Tarjeta+Oh!'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
title = soup.find_all('figcaption', class_="is-hidden")
print(title)