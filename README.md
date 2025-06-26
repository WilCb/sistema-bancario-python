# 💰 Sistema Bancário com Python

Este é um mini-projeto de um **Sistema Bancário em Python**, desenvolvido com o objetivo de praticar os fundamentos da linguagem, como estruturas condicionais, laços de repetição, manipulação de dados, modularização e validação de entradas.

> Desafio proposto pela [DIO](https://www.dio.me/)

---

## 📌 Descrição

O sistema permite que o usuário:

- Deposite valores na conta.
- Realize saques com limite diário.
- Visualize o extrato com histórico de transações.

Todas as operações são feitas via terminal/console, com interface simples e intuitiva.

---

## 🎯 Funcionalidades

- ✅ Depósito com validação de valor (não aceita 0 ou negativos).
- ✅ Saque limitado a **3 por dia**, com valor máximo de **R$ 500 por saque**.
- ✅ Histórico de operações com data e hora de cada movimentação.
- ✅ Visualização do extrato completo.
- ✅ Mensagens informativas e de erro amigáveis ao usuário.
- ✅ Limpeza automática do terminal entre as ações (para melhor leitura).

---

## 🛠 Tecnologias utilizadas

- Python 3.13+
- Biblioteca padrão (`datetime`, `os`)

---

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/WilCb/sistema-bancario-python.git
   ```

2. Acesse a pasta do projeto:
    ```bash
    cd sistema-bancario-python
    ```

3. Execute o script:
    ```bash
    python sistema_bancario.py
    ```

## 📈 Próximos passos (em desenvolvimento)

- Refatorar o código para programação orientada a objetos (POO).

- Criar suporte para múltiplos usuários.

- Salvar/extrair extrato em .txt ou .csv.

- Criar uma interface gráfica com Tkinter ou versão Web com Flask.

## 👨‍💻 Autor
Desenvolvido por Williams Araujo