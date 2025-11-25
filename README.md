# Mini Compilador em Python

Este é um mini compilador **bem simples**, feito para a faculdade, que lê expressões com números inteiros e os operadores `+` e `-`, gera um “bytecode” e executa em uma máquina virtual de pilha.

## Como executar

1. Certifique-se de ter o Python instalado.
2. No terminal/PowerShell, vá até a pasta do projeto:

```bash
cd "C:\Users\MACEDO SA\Documents\mini-compiler"
python mini_compiler.py

Quando o programa pedir, digite uma expressão, por exemplo:


Copiar código
1 + 2 - 3 + 4
O que o compilador faz
Tokenização: separa a expressão em partes (números e operadores).

Análise sintática: verifica se a expressão está correta (ex.: número → operador → número).

Geração de bytecode: cria instruções como PUSH, ADD, SUB.

Execução: roda o bytecode em uma máquina de pilha e mostra o resultado.

Exemplo de saída
Entrada:

text
Copiar código
1 + 2 - 3 + 4
Saída:

text
Copiar código
Bytecode gerado:
  PUSH 1
  PUSH 2
  ADD
  PUSH 3
  SUB
  PUSH 4
  ADD

Resultado da execução: 4
