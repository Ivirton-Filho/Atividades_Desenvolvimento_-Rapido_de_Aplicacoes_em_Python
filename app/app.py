from flask import Flask, request, jsonify
from back import calculo

app = Flask("__name__")

@app.route('/', methods=['POST'])
def api_calculadora():
    dados = request.get_json()

    numero_a = dados.get('numero_a')
    numero_b = dados.get('numero_b')
    operacao = dados.get('operacao')

    resultado = calculo(numero_a, numero_b, operacao)

    resposta = {
        "numero_a": numero_a,
        "numero_b": numero_b,
        "operacao": operacao,
        "resultado": resultado
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run()

