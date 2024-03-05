# Passo a passo do projeto
# Passo 01: entrar no site da empresa:
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
time.sleep(0.3)
pyautogui.write(link)
pyautogui.press('enter')

# passo 02: fazer login

time.sleep(2)

pyautogui.click(x=1263, y=393)
pyautogui.write('gsant@gmail.com')
pyautogui.press('tab')
pyautogui.write('morango123')
pyautogui.press('tab')
pyautogui.press('enter')

# passo 03: importar a base de dados
# pip install pandas

import pandas
tabela = pandas.read_csv('produtos.csv')


# passo 04: cadastrar 1 produto

# time.sleep(2)
# pyautogui.click(x=1196, y=285)

# pyautogui.write("codigo do produto")
# pyautogui.press('tab')
# pyautogui.write("marca")
# pyautogui.press('tab')
# pyautogui.write("tipo")
# pyautogui.press('tab')
# pyautogui.write("categoria")
# pyautogui.press('tab')
# pyautogui.write("preço")
# pyautogui.press('tab')
# pyautogui.write("custo")
# pyautogui.press('tab')
# pyautogui.write("obs")
# pyautogui.press('tab')
# pyautogui.press('enter')


# passo 05: repedir o processo do cadastro até acabar
time.sleep(2)
for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = str(tabela.loc[linha, 'categoria'])
    preco = str(tabela.loc[linha, 'preco_unitario'])
    custo = str(tabela.loc[linha, 'custo'])
    obs = tabela.loc[linha, 'obs']
    
    pyautogui.click(x=1196, y=285)
    pyautogui.write(codigo)
    pyautogui.press('tab')
    pyautogui.write(marca)
    pyautogui.press('tab')
    pyautogui.write(tipo)
    pyautogui.press('tab')
    pyautogui.write(categoria)
    pyautogui.press('tab')
    pyautogui.write(preco)
    pyautogui.press('tab')
    pyautogui.write(custo)
    pyautogui.press('tab')
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)
    
