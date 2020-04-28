import requests
import csv
from bs4 import BeautifulSoup


url = 'https://asloterias.com.br/resultados-da-lotofacil-2020?ordenacao=sorteio'
html = requests.get(url)
bs = BeautifulSoup(html.text, "lxml")


if __name__ == "__main__":
    result = bs.find_all('span', class_='dezenas dezenas_lfacil')
    sorteios = []
    counter = 0
    sorteio = ''
    with open('resultado.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for item in result:
            sorteio = f'{sorteio},{item.text}'
            counter+=1
            if counter > 14:
                writer.writerow(sorteio.split(',')[1:])
                sorteio = ''
                counter = 0

    pass