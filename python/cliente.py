# - Adicione a tag <nome> do utilizador em cada mensagem enviada
# - Uma opção para sair do programa
# - Após enviar a mensagem automaticamente limpar a tela e exibir toda a conversa novamente

import requests

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

if __name__ == '__main__':
    while True:
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            enviar_mensagem()
        elif escolha == '2':
            receber_mensagens()
        else:
            print("Opção inválida.")