from selenium import webdriver


class Duck:
    def __init__(self, drive):
        self.drive = drive
        self.url = 'http://ddg.gg'
        self.search_bar = 'search_form_input_homepage'  # id ddg
        self.btn_search = 'search_button_homepage'  # id ddg
        self.btn_lucky = 'btnI'  # name google


    def navigate(self):
        self.drive.get(self.url)


    def search(self, word='None'):
        self.drive.find_element_by_id(
                self.search_bar).send_keys(word)
        self.drive.find_element_by_id(
                self.btn_search).click()


class Google:
    def __init__(self, drive):
        self.drive = drive
        self.url = 'http://google.com.br'
        self.search_bar = 'q'  # name
        self.btn_search = 'btnK'  # name
        self.btn_lucky = 'btnI'  # name 


    def navigate(self):
        self.drive.get(self.url)
        

    def search(self, word='None'):
        self.drive.find_element_by_name(
                self.search_bar).send_keys(word)
        self.drive.find_element_by_name(
                self.btn_search).click()


    def lucky(self, word='None'):
        self.drive.find_element_by_name(
                self.search_bar).send_keys(word)
        self.drive.find_element_by_name(
                self.btn_lucky).click()


ff = webdriver.Firefox()
d = Duck(ff)
# g = Google(ff) # Erro name bnt
d.navigate()
d.search('CesarAugusto88.github.io')
# g.lucky('CesarAugusto88.github.io')
