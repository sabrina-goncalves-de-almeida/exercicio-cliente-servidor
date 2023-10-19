# - Exiba na tela cada mensagem recebida
# - Adicione um número único (id) para cada mensagem
# - Tenha como parâmetro um valor de mensagem para retornar apenas as mensagens deste id em diante

from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = []

@app.route('/enviar/<nome>', methods=['POST'])
def enviar(nome):
    msg = request.json.get('mensagem')
    if msg:
        mensagens.append([nome,msg])
        return jsonify({'status': 'Mensagem enviada'}), 200
    return jsonify({'status': 'Erro ao enviar mensagem'}), 400

@app.route('/receber/<nome>', methods=['GET'])
def receber(nome):
    return jsonify({'mensagens': mensagens})

if __name__ == '__main__':
    app.run(debug=True, port=5555)