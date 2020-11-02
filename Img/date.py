#Imagen de Aceite Primor 
from bs4 import BeautifulSoup
import requests

url = 'https://www.plazavea.com.pe/abarrotes?filter=specificationFilter_7337:con+Tarjeta+Oh!'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
img = soup.find_all('figure', class_="Showcase__photo")

print(img)