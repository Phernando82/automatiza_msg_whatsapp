# https://wa.me/
import webbrowser
import pyautogui
from time import sleep

telefones = []

with open('telefones.txt', 'r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])

for telefone in telefones:
    webbrowser.open(f'https://wa.me/{telefone}')
    sleep(10)
    pyautogui.typewrite('Olá!')
    sleep(5)
    pyautogui.press('enter')
    sleep(30)
