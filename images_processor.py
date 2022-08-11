import requests
from bs4 import BeautifulSoup
import urllib.request
import os

PATH_BASE = os.getcwd()
PATH_SOURCE = os.path.join(PATH_BASE, "base_images")

if not os.path.exists(PATH_SOURCE):
    os.makedirs(PATH_SOURCE, exist_ok=True)

PATH_PROSSED = os.path.join(PATH_BASE, "processed_images")

if not os.path.exists(PATH_PROSSED):
    os.makedirs(PATH_PROSSED, exist_ok=True)


URL = "https://github.com/ZonaFabo/Taller-de-Programacion/blob/main/Documentos/ParcialesImperativo.md"

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
images = soup.find_all('img', attrs={'alt': 'image'})

links = [
    image['src']
    for image in images
]

for index, image in enumerate(links):
    urllib.request.urlretrieve(
    image, f'{PATH_SOURCE}\\{index}.png'
    )
    