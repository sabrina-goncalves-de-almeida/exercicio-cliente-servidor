# - Adicione a tag <nome> do utilizador em cada mensagem enviada
# OK - Uma opção para sair do programa
# - Após enviar a mensagem automaticamente limpar a tela e exibir toda a conversa novamente

import requests
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()

SERVIDOR_URL = 'http://127.0.0.1:5555'

def enviar_mensagem():
    msg = input("Digite sua mensagem: ")
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
    text.stylize("bold white on #054f77")
    return text

if __name__ == '__main__':
    console.rule("[bold white]CHAT PYTHON")
    print("\n")
    while True:
        console.print("1. Enviar mensagem", style="bold white on #054f77", justify="center")
        console.print("2. Receber mensagens", style="bold white on #054f77", justify="center")
        console.print("3. Sair", style="bold white on #054f77", justify="center")
        print("\n\n")
        escolha = Prompt.ask(estiliza_texto("Escolha uma opção"))
        
        if escolha == '1':
            enviar_mensagem()
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