from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd

class Page:
    def __init__(self, driver):
        self.driver = driver


ff = webdriver.Firefox()
ff.get('http://ddg.gg')
# error: print(ff.page_source())
html = ff.page_source
