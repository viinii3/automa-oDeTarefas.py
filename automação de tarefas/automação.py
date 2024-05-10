# AUTOMATIZAÇÃO DE TAREFAS

import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
 
time.sleep(1.5)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter") 

pyautogui.click(x=1209, y=517)
pyautogui.write("raphaclemente05@gmail.com")
pyautogui.press("tab")

pyautogui.write("blablabla")
pyautogui.press("tab")
pyautogui.press("enter")

tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=600, y=360)
    pyautogui.write(codigo)
    pyautogui.press("tab")
   
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
   
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
   
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
   
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
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
