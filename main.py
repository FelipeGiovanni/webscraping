from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.reclameaqui.com.br/empresa/magazine-luiza-loja-online/')
sleep(15)

def ClosePopup():
    print('localizando PopUp')
    try:
        close_popup = driver.find_element_by_id('stickbar-touchpoint-btn-close')
        close_popup.click()
        print('PopUp Fechado')
        sleep(1)

    except:
        print('PopUp Não encontrado')
        pass

def AceptCookies():
    print('Aceitando Cookies')
    try:
        acept_cookie = driver.find_element_by_id('onetrust-accept-btn-handler')
        acept_cookie.click()
        print('Cookies Aceitos')
        SelecionaUltimo()
    except:
        pass

def SelecionaUltimo():
    try:
        print("Filtrandos os ultimos")
        filter_last = driver.find_elements_by_tag_name('button')
        filter_last[15].text
        filter_last[15].click()
        sleep(4)
        ClosePopup()
        sleep(1)
        print("Elementos filtrados. Selecionando o ultimo")
        select_last = driver.find_elements_by_tag_name('h4')
        select_last[0].click()
        sleep(2)
        ColetaDeDados()
    except:
        print("Erro ao Filtrar elementos. Tentando novamente em 2 segundos...")
        sleep(2)
        SelecionaUltimo()

def ColetaDeDados():
    try:
        print("Selecionando o ultimo. Coletando os dados")
        get_title = driver.find_element_by_tag_name('h1')
        title = get_title.text

        get_status = driver.find_elements_by_tag_name('img')
        status = get_status[8].get_attribute("title")

        get_message = driver.find_elements_by_tag_name('p')
        message = get_message[12].text

        print('Dados Coletados')

        print(title)
        print(status)
        print(message)

    except:
        print('*** ERRO NA COLETA DE DADOS. TENTANDO NOVAMENTE ***')
        ColetaDeDados()

AceptCookies()

