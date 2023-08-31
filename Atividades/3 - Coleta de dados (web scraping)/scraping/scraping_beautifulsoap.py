import csv
import requests
from bs4 import BeautifulSoup

# URL da página que queremos fazer scraping
url = "https://olhardigital.com.br"

# Conexão: Enviar uma solicitação GET para a URL
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida (status 200)
if response.status_code == 200:
    # Parse a página com o BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Encontre os elementos HTML que contêm os títulos de notícias
    headlines = soup.find_all( 'h3', class_="cardV2-title" )

    edit = soup.find_all(  'div',  class_="cardV2-editoria")

    #cria arquivo csv
    file = open('export_data.csv', 'w', newline='') 
    writer = csv.writer(file)
    headers = ['Materias', 'Editorias']
    writer.writerow(headers)

    # Loop pelos elementos e imprimir os títulos
    for headline in headlines:
        print(headline.text)
        #cada noticia
        noticia = [headline.text]
        edit = [headline.text]


        #salvar noticia no arquivo
        file = open('export_data.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        writer.writerow([noticia, edit])
        file.close()

else:
    print("Falha ao acessar a página:", response.status_code)
