import PySimpleGUI as sg
from time import sleep
#Tema
sg.theme('reddit')

#Layout

telaLogin = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(password_char='*', key='senha')],
    [sg.Button('Enviar')],
    #Criando uma tela de "log" onde fala o que foi feito no prjeto
    #       Tamanho=  X, Y
    [sg.Output(size=(43,10))],
]
#Criar a janela

janela = sg.Window('Login',layout=telaLogin)

#Ler os eventos

while True:
    event,values = janela.read()
    #1°Evento, Fechar a janela
    if event == sg.WIN_CLOSED:
        break
    #2°Evento, Clicou em enviar
    elif event == 'Enviar':
        usuarioDigitado = values['usuario']
        senhaDigitado = values['senha']
        print("Passo um feito")
        sleep(10)
        print('Passo 2 feito')

