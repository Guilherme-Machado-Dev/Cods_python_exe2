from collections import deque

# Função que inverte a ordem dos elementos de uma fila
# utilizando uma pilha auxiliar
def inverter_fila(fila):

    # Cria uma pilha vazia
    pilha = []

    # Remove todos os elementos da fila
    # e os coloca na pilha
    while len(fila) > 0:
        pilha.append(fila.popleft())

    # Remove os elementos da pilha
    # e os adiciona novamente na fila
    # Como a pilha segue o padrão LIFO
    # (Último a entrar, Primeiro a sair),
    # os elementos retornam em ordem inversa
    while len(pilha) > 0:
        fila.append(pilha.pop())

    # Retorna a fila já invertida
    return fila


# Cria uma fila de exemplo
fila = deque([1, 2, 3, 4, 5])

# Exibe a fila original
print("Fila original:", list(fila))

# Chama a função para inverter a fila
inverter_fila(fila)

# Exibe a fila após a inversão
print("Fila invertida:", list(fila))

# Saída esperada:
# Fila original: [1, 2, 3, 4, 5]
# Fila invertida: [5, 4, 3, 2, 1]