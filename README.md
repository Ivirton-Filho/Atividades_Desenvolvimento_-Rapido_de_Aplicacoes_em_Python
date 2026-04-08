# Atividades — Desenvolvimento Rápido de Aplicações em Python

Repositório com as atividades práticas da disciplina **Desenvolvimento Rápido de Aplicações em Python**.

---

## 👥 Colaboradores

| Nome | Matrícula |
|------|-----------|
| Beatriz Cavalcante Cursino de Araújo | 202503394041 |
| Yasmin Andrade Senhorinho Torres | 202503508771 |
| Ivirton Hilario da Silva Filho | 202502407114 |

---

## 📁 Estrutura das Atividades

### Atividade 01 — API Calculadora com Flask

Desenvolvimento de uma API REST simples de calculadora utilizando **Python** e **Flask**.

**Funcionalidades:**
- Realiza as quatro operações matemáticas básicas: soma, subtração, multiplicação e divisão.
- Recebe os dados via requisição POST em formato JSON e retorna o resultado no mesmo formato.
- Inclui tratamento de erro para divisão por zero.
- Possui um cliente (`client.py`) que se comunica com a API via terminal.

**Arquivos:**
- `app/app.py` — Servidor Flask com o endpoint `/` (POST).
- `app/back.py` — Lógica de cálculo das operações.
- `client.py` — Interface de linha de comando para consumir a API.

**Como executar:**
```bash
# Instalar dependências
pip install flask requests

# Iniciar o servidor
python app/app.py

# Em outro terminal, executar o cliente
python client.py
```

**Exemplo de requisição:**
```json
{
  "numero_a": 20,
  "numero_b": 10,
  "operacao": "soma"
}
```

**Exemplo de resposta:**
```json
{
  "resultado": 30
}
```

---

### Atividade 02 — Análise de Dados de Vendas com Pandas

Análise exploratória de dados de vendas de uma livraria utilizando **Pandas**, **NumPy** e **Matplotlib**.

**Arquivos:**
- `main.py` — Cria o dataset de vendas, gera gráfico de tendência de faturamento mensal e identifica vendas de alto valor (acima de R$ 200,00) por categoria.
- `nulos.py` — Demonstra o tratamento de valores nulos: insere 5 linhas nulas no dataset e realiza a limpeza com `dropna()`.
- `ticket_medio.py` — Calcula o ticket médio por vendedor e identifica o melhor vendedor.
- `vendas_livraria.csv` — Dataset gerado com 50 registros de vendas de livros (2024).

**Principais análises:**
- Evolução do faturamento mês a mês.
- Gráfico de linha com a tendência de vendas.
- Identificação e tratamento de valores nulos.
- Cálculo do ticket médio por vendedor.
- Análise de vendas de alto valor por categoria.

**Como executar:**
```bash
# Instalar dependências
pip install pandas matplotlib numpy

# Gerar dataset e executar análises
python main.py

# Tratar valores nulos
python nulos.py

# Calcular ticket médio
python ticket_medio.py
```

---

### Atividade 03 — Análise de Dados com Desafios Avançados

Continuação da análise de dados de vendas com foco em desafios específicos de manipulação e visualização utilizando **Pandas**, **Matplotlib** e **NumPy**.

**Arquivo:**
- `main.py` — Recria o dataset de vendas e resolve desafios como evolução de faturamento mensal, gráfico de tendência e filtragem de vendas acima de R$ 200,00 com análise por categoria.

**Como executar:**
```bash
# Instalar dependências
pip install pandas matplotlib numpy

python main.py
```

---

### Atividade 4 — Dashboard Interativo com Streamlit

Desenvolvimento de um **dashboard interativo** de análise de funcionários utilizando **Streamlit**, **Pandas** e **NumPy**.

**Funcionalidades:**
- Exibição de KPIs: salário médio, total de funcionários e salário máximo.
- Filtros interativos na sidebar: cidade, faixa salarial e categoria salarial.
- Tabela de dados filtrados com opção de download em CSV.
- Gráficos de barras: média salarial por cidade e distribuição por categoria salarial.
- Tabela dinâmica (pivot table) com salário médio por cidade e categoria.
- Upload de arquivo CSV personalizado pelo usuário.

**Arquivo:**
- `app.py` — Aplicação Streamlit completa com geração de dados, filtros e visualizações.

**Como executar:**
```bash
# Instalar dependências
pip install streamlit pandas numpy

# Iniciar o dashboard
streamlit run app.py
```

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Streamlit](https://streamlit.io/)
