
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
# Preencher e-mail
pyautogui.click(x=693, y=513)
pyautogui.write("irisrbarbosa.contato@gmail.com")

# Preencher campo senha
pyautogui.press("tab")
pyautogui.write("senhadementirinha")

# Botão logar
pyautogui.press("tab")
pyautogui.press("enter")


# 3 Importar a base de produtos pra cadastrar

# 4 Cadastrar um produto

    # 5 Repetir o processo de cadastro até o fim