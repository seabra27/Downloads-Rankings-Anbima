import os
from datetime import date
from time import sleep
import customtkinter as ctk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

ctk.set_appearance_mode("system")

sites = ['https://www.anbima.com.br/pt_br/informar/ranking/mercado-de-capitais/mercado-de-capitais.htm',
         'https://www.anbima.com.br/pt_br/informar/ranking/fundos-de-investimento/fundos-de-investimento.htm']

def mover_arquivo():
    downloads = os.path.expanduser("~") + "\\Downloads"
    pasta_mover_fundos_investimento = rf'{downloads}\Fundos de Investimento'
    pasta_mover_mercado_capitais = rf'{downloads}\Mercado de Capitais'

    os.makedirs(pasta_mover_fundos_investimento, exist_ok=True)
    os.makedirs(pasta_mover_mercado_capitais, exist_ok=True)

    return pasta_mover_fundos_investimento, pasta_mover_mercado_capitais

def options_edge(diretorio_download):
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--inprivate')
    options.add_argument('--window-size=1920,1080')
    options.add_experimental_option("prefs", {
        "download.default_directory": diretorio_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })

    return options

retorno = mover_arquivo()
pasta_mover_fundos_investimento = retorno[0]
pasta_mover_mercado_capitais = retorno[1]

print(options_edge)

# Definição da função fundos_investimento
def fundos_investimento(pasta):
    options = options_edge(pasta)

    try:
        navegador = webdriver.Edge(options=options)
    except WebDriverException:
        return 'Instale ou atualize seu navegador Edge.'

    navegador.get(sites[1])  # Certifique-se de que o índice está correto

    try:
        cookies = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/p[2]/a')))
        navegador.execute_script("arguments[0].click();", cookies)
    except TimeoutException:
        pass

    elements_to_click = [
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[1]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[2]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[3]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[4]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[5]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[6]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p')
    ]

    for main_xpath, file_xpath in elements_to_click:
        try:
            main_element = WebDriverWait(navegador, 5).until(EC.visibility_of_element_located((By.XPATH, main_xpath)))
            navegador.execute_script("arguments[0].click();", main_element)
            sleep(2)  # Espera para garantir que a página carregue
            file_element = WebDriverWait(navegador, 5).until(EC.visibility_of_element_located((By.XPATH, file_xpath)))
            navegador.execute_script("arguments[0].click();", file_element)
            sleep(2)  # Espera para garantir que o download comece
            navegador.back()  # Volta para a página inicial
            sleep(2)  # Espera para garantir que a página inicial carregue
        except TimeoutException:
            print(f"Elemento não encontrado: {main_xpath}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    sleep(3)
    print('Arquivos de Fundos de Investimento baixados!')
    navegador.quit()

def mercado_capitais(pasta):
    options = options_edge(pasta)

    try:
        navegador = webdriver.Edge(options=options)
    except WebDriverException:
        return 'Instale ou atualize seu navegador Edge.'

    navegador.get(sites[0])

    try:
        cookies = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/p[2]/a')))
        navegador.execute_script("arguments[0].click();", cookies)
    except TimeoutException:
        pass

    elements_to_click = [
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[2]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[3]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[1]/a/p'),
        ('/html/body/div[3]/div/main/main/div/div/div/div/div[4]/div/a[1]/h4', '/html/body/div[3]/div/main/div[2]/form/div/div/ul/li[2]/a/p')
    ]

    for main_xpath, *file_xpaths in elements_to_click:
        try:
            main_element = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, main_xpath)))
            navegador.execute_script("arguments[0].click();", main_element)
            for file_xpath in file_xpaths:
                file_element = WebDriverWait(navegador, 10).until(EC.visibility_of_element_located((By.XPATH, file_xpath)))
                navegador.execute_script("arguments[0].click();", file_element)
                sleep(1)
            navegador.back()  # Volta para a página inicial
            sleep(2)  # Espera para garantir que a página inicial carregue
        except TimeoutException:
            print(f"Elemento não encontrado: {main_xpath}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    sleep(3)
    print('Arquivos de Mercado de Capitais baixados!')
    navegador.quit()

# Chamada da função para mover os arquivos

print("Os arquivos estão sendo baixados...")

pasta_mover_fundos_investimento, pasta_mover_mercado_capitais = mover_arquivo()

fundos_investimento(pasta_mover_fundos_investimento)
mercado_capitais(pasta_mover_mercado_capitais)

print(f"Arquivos de Fundos de Investimento e Mercado de Capitais foram baixados com sucesso!")