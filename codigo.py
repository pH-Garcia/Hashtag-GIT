

# passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2: Fazer login: 
# passo 3: Importar a base de dados
# passo 4: Cadastrar 1 produto
# passo 5: Repetir todos os produtos

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time


pyautogui.PAUSE = 0.5

# passo 1: Abrir o chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#
# digitgar o site

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1.5)

#passo 2: Fazer login
#selecionar o campo email

pyautogui.click(x=-854, y=406)
#escrever o campo email e senha
pyautogui.write("phgarcia@live.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.click(x=-711, y=568)
time.sleep(3)

# passo 3: Importar a base de dados

import pandas   

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# passo 4: Cadastrar 1 produto manualmente

for linha in tabela.index:  # para cada linha da tabela

    pyautogui.click(x=-889, y=287)

 
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para o próximo campo

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])   #string = texto  -> str()
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# passo 5: Repetir para todos os produtos




