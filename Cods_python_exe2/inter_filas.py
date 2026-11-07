from collections import deque

# Função que intercala duas filas ordenadas
# em uma única fila também ordenada
def intercalar_filas(fila1, fila2):

    # Cria uma fila vazia para armazenar o resultado
    fila_resultado = deque()

    # Enquanto as duas filas tiverem elementos
    while len(fila1) > 0 and len(fila2) > 0:

        # Compara os primeiros elementos de cada fila
        if fila1[0] <= fila2[0]:

            # Remove o menor elemento da fila1
            # e adiciona na fila resultado
            fila_resultado.append(fila1.popleft())

        else:

            # Remove o menor elemento da fila2
            # e adiciona na fila resultado
            fila_resultado.append(fila2.popleft())

    # Caso ainda sobrem elementos na fila1,
    # adiciona todos ao resultado
    while len(fila1) > 0:
        fila_resultado.append(fila1.popleft())

    # Caso ainda sobrem elementos na fila2,
    # adiciona todos ao resultado
    while len(fila2) > 0:
        fila_resultado.append(fila2.popleft())

    # Retorna a fila intercalada
    return fila_resultado


# Filas de exemplo
fila1 = deque([1, 2, 4])
fila2 = deque([3, 5, 9])

# Chama a função para intercalar as filas
resultado = intercalar_filas(fila1, fila2)

# Exibe as filas originais e a fila resultante
print("Fila 1:", [1, 2, 4])
print("Fila 2:", [3, 5, 9])
print("Fila Resultante:", list(resultado))

# Saída esperada:
# Fila 1: [1, 2, 4]
# Fila 2: [3, 5, 9]
# Fila Resultante: [1, 2, 3, 4, 5, 9]