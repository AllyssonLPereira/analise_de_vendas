# 📊 Análise de vendas

Um pequeno programa em Python para calcular estatísticas de vendas diárias durante a semana. Ele solicita ao usuário os valores das vendas de segunda a domingo e exibe:

- Total das vendas
- Média das vendas
- Menor venda (dia e valor)
- Maior venda (dia e valor)

Tudo isso com uma saída colorida no terminal para melhor visualização.

---

## 🧾 Funcionalidades

- Entrada de valores de vendas por dia da semana.
- Cálculo automático de:
  - Total de vendas
  - Média das vendas
  - Menor e maior venda com dia correspondente
- Mensagens de erro claras e coloridas.
- Interface simples no terminal com cores ANSI para facilitar a leitura.

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/AllyssonLPereira/analise_de_vendas.git
cd calculate-sales
```

### 2. Execute o programa

```bash
python main.py
```

### 2. Informe os valores de venda

```bash
Qual o valor de venda dos seguintes dias:

Monday: R$
Tuesday: R$
...
Sunday: R$
```

---

## 🧪 Exemplo de saída

```bash
Vendas por dia: {'Monday': 100.0, 'Tuesday': 200.0, ..., 'Sunday': 300.0}
Total das vendas: R$ 1400.00
Média das vendas: R$ 200.00
Menor venda: R$ 100.00 - Monday
Maior venda: R$ 300.00 - Sunday
```

---

## 🛠️ Estrutura do código

- bcolors: Classe utilitária com códigos ANSI para colorir a saída no terminal.
- CalculateSales: Classe principal que:
    - Recebe os dados de entrada.
    - Calcula os valores agregados.
    - Apresenta os resultados com formatação.
- get_infos(): Método de classe que coleta os dados via input().
- total, media, min, max: Propriedades que retornam os valores calculados.

---

## ⚠️ Requisitos

- Python 3.6 ou superior

---

## 📌 Observações

- Se você deixar de preencher algum dia ou digitar valores inválidos, o programa exibirá mensagens de erro apropriadas.
- A entrada deve ser numérica (ponto flutuante).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
