import requests
import json


def conectar_api():
    print("Olá, bem vindo a calculadora!")

    try:
        while True:
            operacao_validas = ['soma', 'subtração', 'divisão', 'multiplicação']
            entrada_operacao = input("Qual operação você vai querer realizar? (exemplo: soma, subtração, divisão e multiplicação)")
            operacao = entrada_operacao.lower()

            if not operacao in operacao_validas:
                print('Digite com acentuação ou com alguma entrada correta!')
                continue
            break

        numero_a = float(input("Digite o primeiro número: "))
        numero_b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite um valor valido")

    dados_para_enviar = {
            "numero_a": numero_a,
            "numero_b": numero_b,
            "operacao": operacao
        }

    url_api = "http://127.0.0.1:5000/"

    try:
        resposta = requests.post(url_api, json=dados_para_enviar)
        resultado_json = resposta.json()
        json_formatado = json.dumps(resultado_json, indent=4, ensure_ascii=False)
        print(json_formatado)

    except requests.exceptions.ConnectionError:
        print("Não foi possivel se conectar com a API")

if __name__ == '__main__':
    conectar_api()