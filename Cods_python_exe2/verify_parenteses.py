# Função que verifica se os parênteses de uma expressão
# estão balanceados (abrem e fecham corretamente)
def verifica_parenteses(expressao):

    # Cria uma pilha vazia para armazenar os parênteses de abertura
    pilha = []

    # Percorre cada caractere da expressão
    for caractere in expressao:

        # Se encontrar um parêntese de abertura,
        # adiciona-o na pilha
        if caractere == "(":
            pilha.append(caractere)

        # Se encontrar um parêntese de fechamento
        elif caractere == ")":

            # Se a pilha estiver vazia,
            # significa que não existe um "(" correspondente
            if len(pilha) == 0:
                return False

            # Remove um "(" da pilha,
            # indicando que foi encontrado seu par correspondente
            pilha.pop()

    # Ao final, a pilha deve estar vazia.
    # Caso contrário, existem parênteses sem fechamento.
    return len(pilha) == 0


# Lista de expressões para teste
expressoes = [
    "(())",
    "(()())",
    "()()",
    ")(",
    "(()(",
    "))(("
]

print("=== VERIFICAÇÃO DE PARÊNTESES ===\n")

# Verifica cada expressão da lista
for exp in expressoes:

    # Se a função retornar True,
    # a expressão está correta
    if verifica_parenteses(exp):
        print(exp, "- Correta")

    # Caso contrário, está incorreta
    else:
        print(exp, "- Incorreta")