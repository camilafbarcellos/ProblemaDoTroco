import time
import random


def troco_programacao_dinamica(moedas, valor):
    '''
    Calcula o mínimo de moedas necessárias para dar o troco utilizando programação dinâmica

    Args:
        moedas (list): Lista das moedas disponíveis
        valor (int): Valor do troco desejado em centavos

    Returns:
        tuple: Tupla contendo o mínimo de moedas necessárias e a lista das moedas utilizadas
               Retorna (-1, []) se não for possível obter o troco
    '''
    
    # Lista de tamanho 'valor+1' para armazenar a quantidade mínima de moedas necessárias para
    # cada valor de 0 a 'valor' e inicializa em infinito 'float('inf')'
    min_moedas = [float('inf')] * (valor+1)
    
    # Definir o troco de 0 como 0, pois ele não tem troco
    min_moedas[0] = 0
    
    # Lista para armazenar as moedas utilizadas para cada valor de 0 a 'valor'
    moedas_utilizadas = [[] for _ in range(valor + 1)]
    
    # Loop para calcular a quantidade mínima de moedas para cada valor de 1 a 'valor'
    for i in range(1, valor+1):
        # Loop para percorrer as moedas disponíveis
        for moeda in moedas:
            # Verifica se a moeda atual é menor ou igual ao valor atual (pode ser utilizada)
            # e se a moeda atual pode diminuir a atual menor quantidade de moedas (compara se a
            # quantidade mínima com a moeda é menor do que a quantidade mínima atual)
            if moeda <= i and min_moedas[i - moeda] + 1 < min_moedas[i]:
                    # Atualiza a quantidade mínima de moedas para o valor atual
                    min_moedas[i] = min(min_moedas[i], min_moedas[i-moeda] + 1)
                    # Armazena as moedas utilizadas para o valor atual
                    moedas_utilizadas[i] = moedas_utilizadas[i - moeda] + [moeda]
    
    # Verificar se é possível dar o troco exato com as moedas disponíveis
    if min_moedas[valor] == valor + 1:
        return -1, []
    
    # Retorna a quantidade mínima de moedas e a lista de moedas utilizadas
    return min_moedas[valor], moedas_utilizadas[valor]


def troco_algoritmo_guloso(moedas, valor):
    '''
    Calcula o mínimo de moedas necessárias para dar o troco utilizando algoritmo guloso

    Args:
        moedas (list): Lista das moedas disponíveis
        valor (float): Valor do troco desejado em centavos

    Returns:
        tuple: Tupla contendo o mínimo de moedas necessárias e a lista das moedas utilizadas
               Retorna (-1, []) se não for possível obter o troco
    '''

    # Inicializar a contagem de moedas mínimas
    min_moedas = 0

    # Criar lista para armazenar as moedas utilizadas
    moedas_utilizadas = []

    # Loop para iterar sobre as moedas disponível
    for moeda in moedas:
        # Verificar se a moeda atual pode ser utilizada para o troco
        if valor >= moeda:
            # Calcular a quantidade máxima de moedas daquele valor que pode ser utilizada
            quant_moedas = valor // moeda
            # Atualizar a contagem de moedas
            min_moedas += quant_moedas
            # Adiciona a moeda atual multiplicada pela quantidade de vezes
            # que ela é utilizada à lista de moedas utilizadas
            moedas_utilizadas.extend([moeda] * quant_moedas)
            # Atualizar o valor do troco restante
            valor -= quant_moedas * moeda

    # Verificar se é possível dar o troco exato com as moedas disponíveis
    if valor == 0:
        return min_moedas, moedas_utilizadas

    return -1, []


def main():
    '''
    Função principal que solicita o valor do troco e exibe o resultado
    '''

    print(
        '\n-- Seminário de ACA - Análise de Complexidade de Algoritmos --' +
        '\n Resolução do Problema do Troco (Coin Change Problem)' +
        '\n Abordagem com Programação Dinâmica e Algoritmo Guloso' +
        '\n-- Camila Barcellos, 2023/1 --\n'
    )

    # Cenário normal
    moedas = [1, 2, 5, 10, 20, 50, 100, 200] # sistema canônico com a moeda 1
    valor = int(input('Digite o valor do troco desejado: R$'))
    
    # Cenário que penaliza o Algoritmo Guloso (ex.: valor 343)
    # moedas = [2, 5, 10, 20, 50, 100, 200] # sistema não-canônico sem a moeda 1
    # valor = int(input('Digite o valor do troco desejado: R$'))
    
    # Cenário para testar velocidade de execução
    # moedas = [2, 5, 10, 50] 
    # valor = random.randint(10000, 500000)
    
    # Exibe a lista de moedas disponíveis
    print('Moedas disponíveis:', moedas)

    # Calcula o resultado com Programação Dinâmica
    print('Abordagem com Programação Dinâmica')
    resultado, moedas_utilizadas = troco_programacao_dinamica(moedas, valor)
    if resultado == -1:
        print(
            f' Não é possível obter o troco de R${valor} com as moedas disponíveis!')
    else:
        # Captura o tempo de início da execução
        inicio = time.time()

        # Exibe resultado
        print(f' Mínimo de moedas necessárias para obter o troco de R${valor}: {resultado}')
        print(' Moedas utilizadas:', moedas_utilizadas)

        # Captura o tempo de fim da execução e exibe o tempo total
        fim = time.time()
        print(f' Tempo de execução: {fim - inicio}s')

    # Calcula o resultado com Algoritmo Guloso
    print('\nAbordagem com Algoritmo Guloso')
    # Ordenar as moedas em ordem decrescente (garante usar as maiores moedas primeiro)
    moedas.reverse()
    resultado, moedas_utilizadas = troco_algoritmo_guloso(moedas, valor)
    if resultado == -1:
        print(f' Não é possível obter o troco de R${valor} com as moedas disponíveis!')
    else:
        # Captura o tempo de início da execução
        inicio = time.time()

        # Exibe resultado
        print(
            f' Mínimo de moedas necessárias para obter o troco de R${valor}: {resultado}')
        print(' Moedas utilizadas:', moedas_utilizadas)

        # Captura o tempo de fim da execução e exibe o tempo total
        fim = time.time()
        print(f' Tempo de execução: {fim - inicio}s')


if __name__ == '__main__':
    main()
