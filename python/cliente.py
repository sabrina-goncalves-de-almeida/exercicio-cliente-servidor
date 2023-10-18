# - Adicione a tag <nome> do utilizador em cada mensagem enviada
# OK - Uma opção para sair do programa
# OK - Após enviar a mensagem automaticamente limpar a tela e exibir toda a conversa novamente

import requests
import os
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()

SERVIDOR_URL = 'http://127.0.0.1:5555'

estilo_texto = "bold white on #054f77"

def enviar_mensagem():
    msg = Prompt.ask(estiliza_texto("Digite sua mensagem"))
    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'mensagem': msg})
    print(resposta.json()['status'])

def receber_mensagens():
    resposta = requests.get(f'{SERVIDOR_URL}/receber')
    mensagens = resposta.json()['mensagens']
    print("Mensagens recebidas:")
    for msg in mensagens:
        print(f"- {msg}")

def estiliza_texto(texto):
    text = Text(texto)
    text.stylize(estilo_texto)
    return text

if __name__ == '__main__':
    console.rule("[bold white]CHAT PYTHON")
    while True:
        console.print("1. Enviar mensagem", style=estilo_texto, justify="center")
        console.print("2. Receber mensagens", style=estilo_texto, justify="center")
        console.print("3. Sair", style=estilo_texto, justify="center")
        print("\n\n")
        escolha = Prompt.ask(estiliza_texto("Escolha uma opção"))
        
        if escolha == '1':
            enviar_mensagem()
            os.system('clear')
            receber_mensagens()
        elif escolha == '2':
            receber_mensagens()
        elif escolha == '3':
            print("\n")
            console.rule("[bold white]Até mais, tenha um ótimo dia.")
            print("\n")
            break
        else:
            print("\n")
            console.print("Opção inválida.", style="bold #ff0000", justify="center")
            print("\n")