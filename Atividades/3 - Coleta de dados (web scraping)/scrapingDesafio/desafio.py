import csv
import requests
from bs4 import BeautifulSoup

# URL da página que queremos fazer scraping
url = "https://g1.globo.com"

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos de notícias
    post = soup.find_all("div", class_="feed-post bstn-item-shape type-materia")

    #cria arquivo csv
    file = open('export_desafio.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    headers = ['Assunto ', 'Chamada ', 'Data/Time ']
    writer.writerow(headers)


    # Loop pelos elementos e imprimir os títulos
    for post in post:
        assunto = post.find("div", class_="feed-post-body").text.strip()
        chamada = post.find("div", class_="_evt").text.strip()    
        time = post.find("div",class_="feed-post-metadata").text.strip()

        row = [assunto, chamada, time]
        writer.writerow(row)

    file.close()
    print("Dados exportados para export_desafio,csv")
else:
    print("Falha ao acessar a página:", response.status_code)
