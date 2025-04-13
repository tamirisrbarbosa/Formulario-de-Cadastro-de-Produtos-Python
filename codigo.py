
import pyautogui
import time

pyautogui.PAUSE = 0.5

# 1 Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrir o navegador padrão (no meu caso, o meu Windows e o brave)  
pyautogui.press("win")     

pyautogui.write("brave")
pyautogui.press("enter")

# Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 3 segundos
time.sleep(3)


# 2 Fazer login
# Preencher

pyautogui.click(x=693, y=513)
pyautogui.write("irisrbarbosa.contato@gmail.com")

# Preencher campo senha
pyautogui.press("tab")
pyautogui.write("senhadementirinha")

# Botão logar
pyautogui.press("tab")
pyautogui.press("enter")

# Espera de 3 segundos
time.sleep(3)

# 3 Importar a base de produtos pra cadastrar
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# 4 Cadastrar um produto

for linha in tabela.index: # cadastrando cada linha da tabela
    pyautogui.click(x=737, y=361)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab") # passar para próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab") # passar para próximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab") # passar para próximo campo
    categoria = str(tabela.loc[linha, "categoria"])  # str() para transformar em String = texto
    pyautogui.write(categoria)

    pyautogui.press("tab") # passar para próximo campo
    preco_unitario =str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # passar para próximo campo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab") # passar para próximo campo
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":          
        pyautogui.write(obs)

    pyautogui.press("tab") # passando para o botão enviar
    pyautogui.press("enter")

    pyautogui.scroll(100000) # subir para o início da página

# 5 Repetir o processo de cadastro até o fim