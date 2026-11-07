# Função recursiva que conta quantos números pares existem na pilha
def contaPar(pilha):

    # Condição de parada: se a pilha estiver vazia,
    # não há mais elementos para verificar
    if pilha == []:
        return 0

    # Remove o elemento que está no topo da pilha
    elemento = pilha.pop()

    # Verifica se o elemento removido é par
    if elemento % 2 == 0:

        # Se for par, soma 1 e continua a contagem
        # nos elementos restantes da pilha
        return 1 + contaPar(pilha)

    else:

        # Se for ímpar, não soma nada e continua
        # verificando o restante da pilha
        return contaPar(pilha)


# Teste com pilha vazia
print("Lista vazia:")
print(contaPar([]))

# Teste com pilha contendo apenas números ímpares
print("\nLista somente com ímpares:")
print(contaPar([1, 3, 5, 7]))

# Teste com pilha contendo apenas números pares
print("\nLista somente com pares:")
print(contaPar([2, 4, 6, 8]))

# Teste com pilha contendo números pares e ímpares
print("\nLista mista:")
print(contaPar([1, 2, 3, 4, 5, 6]))