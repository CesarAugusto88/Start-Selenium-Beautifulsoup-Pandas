from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
from tabulate import tabulate

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.novasaopaulo.com.br/imovel/locacao-casa-americanopolis-sao-paulo/JA18809")

html = driver.page_source.encode("utf-8")

soup = bs(html, "lxml")

results = []

# url = 'https://www.novasaopaulo.com.br/imovel/locacao-casa-americanopolis-sao-paulo/JA18809'

#ff = webdriver.Firefox()
#ff.get(url)
#html = ff.page_source

#bs_obj = bs(html, 'html.parser')

#print(bs_obj.find_all('div'))
divs = soup.find_all('div', {'class': 'icoImovelImovel'})
#div_txt = divs[0].text
#print(div_txt)
qts_quartos = divs[0].find_all('div')[0]
quartos = qts_quartos.text.split()

for qt in quartos:
    print(qt)

table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print(tabulate(df[0]))

#df = pd.read_html(str(soup.find_all('table')[0]))

#df = pd.read_html(divs)
#print( tabulate(df[0], headers='keys', tablefmt='psql'))
