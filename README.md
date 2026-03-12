API de calculadora simples que realiza operações de soma, subtração, multiplicação e divisão. 
A calculadora realiza operações entre dois números digitados pelo usuário e recebendo resultado em formato JSON.
A aplicação foi desenvolvida usando Python e framework Flask para criar o servidor da API.

Como executar o projeto:
  Primeiro é necessario instalar as dependências necessárias (pip install flash requests).
  Depois, executar o servidor da API (python app.py)
  E então, o servidor será iniciado no endereço http://127.0.0.1:5000. 

Parâmetros:
  numero_a (float) - Primeiro número da operação.
  numero_b (float) - Segundo número da operação.
  operacao (string) - Tipo de operação matemática realizada. 

Endpoints da API:
  SOMA:
    Realiza a soma entre dois números.
    Exemplo:
      {
  "numero_a": 20,
  "numero_b": 10,
  "operacao": "soma"
}
    Resposta:
      {
  "resultado": 30
}

  SUBTRAÇÃO:
    Realiza a subtração entre dois números.
    Exemplo:
      {
  "numero_a": 20,
  "numero_b": 10,
  "operacao": "subtração"
}
    Resposta:
      {
  "resultado": 10
}

  MULTIPLICAÇÃO:
    Realiza a multiplicação entre dois números.
    Exemplo:
      {
  "numero_a": 20,
  "numero_b": 10,
  "operacao": "multiplicação"
}
    Resposta:
      {
  "resultado": 200
}

  DIVISÃO:
    Realiza a divisão entre dois números.
    Exemplo:
      {
  "numero_a": 20,
  "numero_b": 10,
  "operacao": "divisão"
}
    Resposta:
      {
  "resultado": 2
}
  Caso o segundo número seja 0, a API retornará um erro.
  Exemplo:
    {
  "numero_a": 20,
  "numero_b": 0,
  "operacao": "divisão",
  "resultado": "Erro: Divisão por zero não é permitida."
}
