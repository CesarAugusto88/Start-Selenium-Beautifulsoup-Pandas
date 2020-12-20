from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.novasaopaulo.com.br/imovel/locacao-casa-americanopolis-sao-paulo/JA18809")

html = driver.page_source.encode("utf-8")

soup = BeautifulSoup(html, "lxml")

div_quarto = soup.find_all('div', {'class': 'icoImovelImovel'})
# div_txt = divs[0].text
# print(div_txt)
qts_quartos = div_quarto[0].find_all('div')[0]
quartos = qts_quartos.text.split()
# print(type(quartos))
quartos = dict(zip(quartos[::2], [quartos[1::2]]))

div_img = soup.find_all('div', {'class': 'slick-slide slick-current slick-active'})
# print(div_img[0].find('img'))
link = div_img[0].find('img').get('src')
# print(link)
# print(type(link))
link_img = {'IMAGEM': [link]}
# print(link_img)

# fundindo dicionarios
quartos.update(link_img)

df = pd.DataFrame(data=quartos)
print(df)
