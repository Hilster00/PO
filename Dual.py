def converter_para_dual(coeficientes_objetivo, matriz_restricoes, vetor_recursos):
    num_variaveis = len(coeficientes_objetivo)
    num_restricoes = len(matriz_restricoes)

    # Inicializa a matriz de coeficientes do dual com zeros
    matriz_dual = [[0 for _ in range(num_restricoes)] for _ in range(num_variaveis)]

    # Inicializa o vetor de recursos do dual com zeros
    vetor_recursos_dual = [0] * num_restricoes

    # Inicializa o vetor de coeficientes da função objetivo do dual com zeros
    coeficientes_objetivo_dual = [0] * num_restricoes

    # Preenche a matriz de coeficientes do dual
    for i in range(num_variaveis):
        for j in range(num_restricoes):
            matriz_dual[i][j] = matriz_restricoes[j][i]

    # Preenche o vetor de recursos do dual
    for i in range(num_restricoes):
        vetor_recursos_dual[i] = coeficientes_objetivo[i]

    # Preenche o vetor de coeficientes da função objetivo do dual
    for i in range(num_restricoes):
        coeficientes_objetivo_dual[i] = vetor_recursos[i]

    return matriz_dual, vetor_recursos_dual, coeficientes_objetivo_dual

# Exemplo de uso
coeficientes_objetivo = [3, 4]
matriz_restricoes = [[1, 2], [3, 2]]
vetor_recursos = [5, 6]

matriz_dual, vetor_recursos_dual, coeficientes_objetivo_dual = converter_para_dual(coeficientes_objetivo, matriz_restricoes, vetor_recursos)

print("Matriz de coeficientes do dual:", matriz_dual)
print("Vetor de recursos do dual:", vetor_recursos_dual)
print("Coeficientes da função objetivo do dual:", coeficientes_objetivo_dual)
