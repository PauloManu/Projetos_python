import pyautogui
import time
import  pandas
from selenium import webdriver


opcoes = webdriver.ChromeOptions()
opcoes.add_argument('--headless=new')

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome", options=opcoes)
pyautogui.press("enter")

time.sleep(3)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=606, y=494)
pyautogui.write("paulomanuh@gmail.com")

pyautogui.press("tab")
pyautogui.write("suasenhaaqui")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:

    pyautogui.click(x=606, y=345)

    codigo = tabela.loc[linha, "codigo"]

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        


    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)