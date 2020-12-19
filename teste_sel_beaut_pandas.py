from selenium import webdriver
import pandas as pd
import time
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://coinmunity.co/")

html = driver.page_source.encode("utf-8")

soup = BeautifulSoup(html, "lxml")

results = []

for row in soup.find_all("tr")[2:]:
    data = row.find_all("td")
    name = data[1].find("a").text
    value = data[2].find("p").text
    # get the rest of the data you need about each coin here,
    # then add it to the dictionary that you append to results
    results.append({"name": name, "value": value})

df = pd.DataFrame(results)

df.head()
