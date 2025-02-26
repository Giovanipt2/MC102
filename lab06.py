def soma_vetores(v1: list[int], v2: list[int]) -> list[int]:
    '''Soma elemento a elemento de dois vetores.

    Quando um vetor for menor que o outro, acrescenta-se zeros no menor.

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    if len(v1) > len(v2):
        for _ in range(len(v2), len(v1)):
            v2.append(0)
    elif len(v1) < len(v2):
        for _ in range(len(v1), len(v2)):
            v1.append(0)

    vetor_corrente = []

    for i in range(len(v1)):
        soma_termos = v1[i] + v2[i]
        vetor_corrente.append(soma_termos)

    return vetor_corrente


def subtrai_vetores(v1: list[int], v2: list[int]) -> list[int]:
    '''Subtração elemento a elemento de dois vetores.

    Quando um vetor for menor que o outro, acrescenta-se zeros no menor.

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    if len(v1) > len(v2):
        for _ in range(len(v2), len(v1)):
            v2.append(0)
    elif len(v1) < len(v2):
        for _ in range(len(v1), len(v2)):
            v1.append(0)

    vetor_corrente = []

    for i in range(len(v1)):
        subtracao_termos = v1[i] - v2[i]
        vetor_corrente.append(subtracao_termos)

    return vetor_corrente


def multiplica_vetores(v1: list[int], v2: list[int]) -> list[int]:
    '''Multiplicação elemento a elemento de dois vetores.

    Caso os vetores tenham tamanhos diferentes, acrescenta-se uns no menor.

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    if len(v1) > len(v2):
        for _ in range(len(v2), len(v1)):
            v2.append(1)
    elif len(v1) < len(v2):
        for _ in range(len(v1), len(v2)):
            v1.append(1)

    vetor_corrente = []

    for i in range(len(v1)):
        multiplicacao_termos = v1[i] * v2[i]
        vetor_corrente.append(multiplicacao_termos)

    return vetor_corrente


def divide_vetores(v1:  list[int], v2: list[int]) -> list[int]:
    '''Divisão inteira elemento a elemento de dois vetores.

    Deve-se adicionar zeros no primeiro vetor, se ele for menor
    Deve-se adicionar uns no segundo vetor, se ele for menos

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    if len(v1) > len(v2):
        for _ in range(len(v2), len(v1)):
            v2.append(1)
    elif len(v1) < len(v2):
        for _ in range(len(v1), len(v2)):
            v1.append(0)

    vetor_corrente = []

    for i in range(len(v1)):
        divisao_termos = v1[i] // v2[i]
        vetor_corrente.append(divisao_termos)

    return vetor_corrente


def multiplicacao_escalar(v1: list[int], escalar: int) -> list[int]:
    '''Multiplica cada elemento por um escalar.

    Parâmetros:
    v1 -- lista de inteiros
    escalar -- número inteiro

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    vetor_corrente = []

    for i in range(len(v1)):
        termos_multiplicados = v1[i] * escalar
        vetor_corrente.append(termos_multiplicados)

    return vetor_corrente


def n_duplicacao(v1: list[int], n: int) -> list[int]:
    '''Duplica o vetor n vezes, com n >=0.

    Se n = 0, retorna uma lista vazia([])

    Parâmetros:
    v1 -- lista de inteiros
    n -- número inteiro

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    vetor_corrente = []

    if n > 0:
        for _ in range(n):
            vetor_corrente.extend(v1)
        return vetor_corrente

    else:
        return vetor_corrente


def soma_elementos(v1: list[int]) -> int:
    '''Soma todos os elementos do vetor

    Parâmetros:
    v1 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    resultado = 0

    for i in v1:
        resultado += i

    return resultado


def produto_interno(v1: list[int], v2: list[int]) -> int:
    '''Multiplica elemento a elemento e depois soma o resultado

    Adiciona-se uns no final do vetor menor, caso exista

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    if len(v1) > len(v2):
        for _ in range(len(v2), len(v1)):
            v2.append(1)
    elif len(v1) < len(v2):
        for _ in range(len(v1), len(v2)):
            v1.append(1)

    auxiliar = []
    resultado = 0

    for i in range(len(v1)):
        auxiliar.append(v1[i] * v2[i])

    for g in auxiliar:
        resultado += g

    return resultado


def multiplica_todos(v1: list[int], v2: list[int]) -> list[int]:
    '''Multiplica cada elemento de um vetor pelo outro e soma o resultado

    Parâmetros:
    v1 -- lista de inteiros
    v2 -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    vetor_corrente = []

    for i in range(len(v1)):
        resultado_i = 0
        for h in range(len(v2)):
            resultado_i += v1[i] * v2[h]
        vetor_corrente.append(resultado_i)

    return vetor_corrente


def correlacao_cruzada(v1: list[int], mascara: list[int]) -> list[int]:
    '''A máscara é um vetor que percorre o outro calculando o produto interno

    A máscara tem sempre um tamanho menor ou ingual ao vetor de entrada

    Parâmetros:
    v1 -- lista de inteiros
    máscara -- lista de inteiros

    Retorno:
    vetor_corrente -- lista de inteiros
    '''

    vetor_corrente = []
    pre_vetor = []
    auxiliar = []
    contador1 = 0
    contador2 = len(mascara)
    resultado = 0

    while contador1 <= (len(v1) - len(mascara)) + 1:
        auxiliar = v1[contador1:contador2]

        if len(auxiliar) == len(mascara):
            for g in range(len(mascara)):
                pre_vetor.append(auxiliar[g] * mascara[g])
            contador1 += 1
            contador2 += 1

            for g in pre_vetor:
                resultado += g
            vetor_corrente.append(resultado)

            pre_vetor = []
            resultado = 0

        else:
            break

    return vetor_corrente


def main() -> None:

    vetor_corrente = list(map(int, input().split(',')))
    comandos = input()

    while True:
        if comandos == "soma_vetores":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = soma_vetores(vetor_corrente, v2)

        elif comandos == "subtrai_vetores":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = subtrai_vetores(vetor_corrente, v2)

        elif comandos == "multiplica_vetores":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = multiplica_vetores(vetor_corrente, v2)

        elif comandos == "divide_vetores":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = divide_vetores(vetor_corrente, v2)

        elif comandos == "multiplicacao_escalar":
            escalar = int(input())
            vetor_corrente = multiplicacao_escalar(vetor_corrente, escalar)

        elif comandos == "n_duplicacao":
            n = int(input())
            vetor_corrente = n_duplicacao(vetor_corrente, n)

        elif comandos == "soma_elementos":
            vetor_corrente = [soma_elementos(vetor_corrente)]

        elif comandos == "produto_interno":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = [produto_interno(vetor_corrente, v2)]

        elif comandos == "multiplica_todos":
            v2 = list(map(int, input().split(',')))
            vetor_corrente = multiplica_todos(vetor_corrente, v2)

        elif comandos == "correlacao_cruzada":
            mascara = list(map(int, input().split(',')))
            vetor_corrente = correlacao_cruzada(vetor_corrente, mascara)

        elif comandos == "fim":
            break

        print(vetor_corrente)

        comandos = input()


if __name__ == "__main__":
    main()
