 
# O modulo time aqui foi utilizado para esperar o carregamento das paginas atraves do firefox
import time

# o modulo webdriver e necessario para definir qual navegador sera utilizado para fazer a automacao
from selenium import webdriver

# o modulo Select sera utilizado para interagir com a caixa de selecao onde sera definido o ano em que quero buscar os dados
from selenium.webdriver.support.ui import Select

# esse modulo sera utilizado para 
from bs4 import BeautifulSoup

# a linha abaixo define qual e o navegador que queremos utilizar, lembrando que eu instalei somente o driver para conexao com o firefox, mas existem tambem para Chrome e InternetExplorer
driver = webdriver.Firefox()

# abaixo foi definido qual e o site que quero acessar
driver.get("http://leideacesso.etransparencia.com.br/itaquaquecetuba.prefeitura.sp/Portal/desktop.html?410")

# o Sleep abaixo e para aguardar o carregamento da pagina
time.sleep(15)

# Aqui estou buscando o elemento que possui na classe o valor valo01, que e respectivo ao valor da receita onde quero clicar para ir na proxima pagina
receita = driver.find_element_by_class_name("val01")

# aqui e feito um clique no elemento que foi encontrado acima
receita.click()

# aguardando o carregamento da pagina
time.sleep(10)

# agora quero as receitas desde 2013 ate 2017
anos = ["2013","2014","2015","2016","2017"]

for a in anos:
    # aqui e utilizado o modulo Select do selenium para interagir com o ComboBox
    select = Select(driver.find_element_by_name("exe"))

    # aqui e alterado o valor do ComboBox
    select.select_by_value(a)
    # agora e buscado o elemento cujo o ID e igual a imgFiltrar
    filtrar = driver.find_element_by_id('imgFiltrar')
    # retornado o elemento da busca e clicado no botao
    filtrar.click()
    # aguardando o carregamento da tabela
    time.sleep(3)

    # armazenando a div que possui a tabela dentro da variavel dados
    dados = driver.find_element_by_id("bd10")

    # aqui e pegado o codigo HTML que esta dentro da div bd01 no codigo que foi mostrado acima
    html = dados.get_attribute("innerHTML")

    # com o codigo HTML dentro da variavel, vamos usar o BeautifulSoup para fazer o parser desse HTML
    soup = BeautifulSoup(html, "html.parser")
    
    # dentro da variavel soup temos o codigo html retornado pelo Selenium ja convertido para o BS
    # vou utilizar o metodo select_one para buscar o elemento table dentro desse codigo
    table = soup.select_one("table")

    # no conteudo dessa tabela temos varias virgulas e espacos, como vou converter esses dados pra csv, vou definir o delimitador com o caracter |
    # na linha abaixo estou buscando todos os elementos tr, que possui a classe Grid_title e os elementos filhos cujo a tag e td
    # e feito um list comprehesion para pegar somente os elementos e eles estao sendo separados pelo caracter |

    headers = [header.text+"|" for header in table.select("tr.Grid_title td")]
   
    # abaixo estou buscando os elementos tr que possuem a classe Grid_line no css
    # e um novo list comprehension para criar uma lista somente com o s elementos que eu quero
    line = []
    data = [d for d in table.select("tr.Grid_line")]
    for d in data:
        linha = ""
        for t in d.select("td"):
            linha += t.text+"|"
        line.append(linha)

    # aqui e a mesma coisa que acima porem com a classe Grid_line_even
    line_even = []
    data = [ d for d in table.select("tr.Grid_line_even")]
    for d in data:
        linha = ""
        for t in d.select("td"):
            linha += t.text+"|"
        line_even.append(linha)

    # agora que os dados ja foram parseados, vou fazer a escrita do arquivo CSV
    with open("%s.csv"%a,"w") as f:
        s = "".join(headers)
        f.write(s+"\n")

        for l in line:
            f.write(l+"\n")

        for l in line_even:
            f.write(l+"\n")

# fim 
time.sleep(10)
driver.close()
