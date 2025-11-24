# mini_compiler.py
# Compilador MUITO simples de expressões com + e -

# -------------------------
# ETAPA 1: TOKENIZAÇÃO
# -------------------------
# Recebe uma string "1 + 2 - 3" e vira ["1", "+", "2", "-", "3"]
def tokenize(source: str):
    return source.strip().split()


# -------------------------
# ETAPA 2: PARSE (ANÁLISE SINTÁTICA)
# -------------------------
# Garante que está no formato:
#   numero (op numero)*
# Ex: 1 + 2 - 3 + 4
# e cria uma "AST" bem simples (lista com números e operadores)
def parse(tokens):
    if not tokens:
        raise ValueError("Expressão vazia")

    ast = []
    expect_number = True  # se True, esperamos número; se False, esperamos operador

    for t in tokens:
        if expect_number:
            # tentar converter pra inteiro
            try:
                n = int(t)
            except ValueError:
                raise ValueError(f"Esperado número, mas encontrei: {t}")
            ast.append(n)
            expect_number = False
        else:
            # aqui esperamos + ou -
            if t not in ['+', '-']:
                raise ValueError(f"Esperado operador + ou -, mas encontrei: {t}")
            ast.append(t)
            expect_number = True

    if expect_number:
        # Se terminou esperando número, quer dizer que acabou em operador
        # Ex: "1 + 2 -"
        raise ValueError("Expressão termina com operador")

    return ast


# -------------------------
# ETAPA 3: COMPILAÇÃO (GERAR BYTECODE)
# -------------------------
# A partir da AST [num, op, num, op, num,...]
# gera instruções de "bytecode" para uma máquina de pilha:
#   PUSH n
#   ADD
#   SUB
def compile_to_bytecode(ast):
    instructions = []

    # primeiro número
    instructions.append(("PUSH", ast[0]))

    i = 1
    while i < len(ast):
        op = ast[i]
        num = ast[i + 1]

        # empilha o próximo número
        instructions.append(("PUSH", num))

        # gera instrução de operação
        if op == '+':
            instructions.append(("ADD", None))
        else:
            instructions.append(("SUB", None))

        i += 2

    return instructions


# -------------------------
# ETAPA 4: EXECUÇÃO (MÁQUINA VIRTUAL)
# -------------------------
# Executa o bytecode numa pilha e devolve o resultado final
def run_bytecode(instructions):
    stack = []

    for inst, arg in instructions:
        if inst == "PUSH":
            stack.append(arg)
        elif inst == "ADD":
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
        elif inst == "SUB":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        else:
            raise ValueError("Instrução desconhecida: " + inst)

    if len(stack) != 1:
        raise ValueError("Erro: pilha terminou com tamanho diferente de 1.")

    return stack[0]


# -------------------------
# ETAPA 5: PROGRAMA PRINCIPAL
# -------------------------
def main():
    print("=== Mini compilador de expressões (+ e -) ===")
    print("Digite números e operadores separados por espaço.")
    print("Exemplo: 1 + 2 - 3 + 4\n")

    expr = input("Expressão: ")

    try:
        # 1) transformar em tokens
        tokens = tokenize(expr)

        # 2) analisar sintaxe e montar AST
        ast = parse(tokens)

        # 3) compilar pra bytecode
        bytecode = compile_to_bytecode(ast)

        print("\nBytecode gerado:")
        for inst, arg in bytecode:
            if arg is not None:
                print(f"  {inst} {arg}")
            else:
                print(f"  {inst}")

        # 4) rodar o bytecode na máquina virtual
        result = run_bytecode(bytecode)
        print("\nResultado da execução:", result)
    except Exception as e:
        print("\nERRO:", e)


if __name__ == "__main__":
    main()
