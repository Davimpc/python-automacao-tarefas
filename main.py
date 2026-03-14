import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(x=530, y=593)
time.sleep(1)

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(5)

# fazer login
pyautogui.click(x=547, y=371)
pyautogui.write("exemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("Senha*Exemplo00")
pyautogui.click(x=792, y=539)
time.sleep(5)

tabela = pd.read_csv("produtos.csv")

print(tabela)

# cadastrar produtos
for linha in tabela.index:
    pyautogui.click(x=561, y=261)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
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
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)