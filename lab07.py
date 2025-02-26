VOGAIS = ['a', 'e', 'i', 'o', 'u']
CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']
NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def acha_indice_1(marcador1: str, caracteres: list[str]) -> int:
    '''Encontra a primeira posição em que o marcador1 aparece na mensagem

    Parâmetros:
    marcador1 -- carcter ou tipo de carcater (string)
    caracteres -- lista de strings

    Retorno:
    indice1 -- número inteiro
    '''
    if marcador1 == 'vogal':
        for g in caracteres:
            if g.lower() in VOGAIS:
                return caracteres.index(g)

    elif marcador1 == 'consoante':
        for g in caracteres:
            if g.lower() in CONSOANTES:
                return caracteres.index(g)

    elif marcador1 == 'numero':
        for g in caracteres:
            if g in NUMEROS:
                return caracteres.index(g)

    else:
        return caracteres.index(marcador1)


def acha_indice_2(marcador2: str, indice1: int, caracteres: list[str]) -> int:
    '''Encontra a primeira posição em que o marcador2 aparece na mensagem

    A contagem do índice para o marcador 2 só começa após o índice do marcador1

    Parâmetros:
    marcador2 -- carcter ou tipo de carcater (string)
    indice1 -- número inteiro
    caracteres -- lista de strings

    Retorno:
    indice2 -- número inteiro
    '''
    if marcador2 == 'vogal':
        for g in caracteres[indice1:]:
            if g.lower() in VOGAIS:
                return caracteres.index(g)

    elif marcador2 == 'consoante':
        for g in caracteres[indice1:]:
            if g.lower() in CONSOANTES:
                return caracteres.index(g)

    elif marcador2 == 'numero':
        for g in caracteres[indice1:]:
            if g in NUMEROS:
                return caracteres.index(g)

    else:
        return caracteres[indice1:].index(marcador2) + indice1


def calcula_chave(operacao: str, indice1: int, indice2: int) -> int:
    '''Calcula a chave com base nos índices encontrados e na operação

    Parâmetros:
    operacao -- '+', '-', ou '*'
    indice1 -- número inteiro
    indice2 -- número inteiro

    Retorno:
    chave -- número inteiro
    '''
    if operacao == '+':
        return indice1 + indice2

    elif operacao == '-':
        return indice1 - indice2

    elif operacao == '*':
        return indice1 * indice2


def descriptografia(caracteres: list[str], chave: int) -> list[str]:
    '''Corrige possíveis problemas com o ord dos caracteres

    Caso eles não estejam entre 32 e 126 da tabela ASCII

    Parâmetros:
    caracteres -- lista de strings
    chave -- número inteiro

    Retorno:
    caracteres_descriptografados -- lista de inteiros
    '''
    caracteres_descriptografados: list[int] = []

    for g in caracteres:
        novo_ord = ord(g) + chave
        while novo_ord > 126:
            novo_ord -= 95

        while novo_ord < 32:
            novo_ord += 95

        caracteres_descriptografados.append(chr(novo_ord))

    return caracteres_descriptografados


def mensagem_descriptografada(caracteres_descriptografados: list[str], linhas: list[str]) -> list[str]:
    '''Devolve os caracteres descriptografados em suas respectivas linhas

    Parâmetros:
    caracteres_descriptografados -- lista de strings
    linhas -- lista de strings

    Retorno:
    linhas_descriptografadas -- lista de strings
    '''
    linhas_descriptografadas: list[str] = []
    comeco = 0

    for g in range(len(linhas)):
        fim = comeco + len(linhas[g])
        nova_linha = ''.join(caracteres_descriptografados[comeco:fim])
        comeco = fim
        
        linhas_descriptografadas.append(nova_linha)

    return linhas_descriptografadas


def main() -> None:
    linhas: list[str] = []
    caracteres: list[str] = []

    operacao = input()
    marcador1 = input()
    marcador2 = input()
    linhas_analisadas = int(input())

    for _ in range(linhas_analisadas):
        mensagem = input()
        linhas.append(mensagem)

    for linha in linhas:
        for caracter in linha:
            caracteres.append(caracter)

    indice1 = acha_indice_1(marcador1, caracteres)
    indice2 = acha_indice_2(marcador2, indice1, caracteres)
    chave = calcula_chave(operacao, indice1, indice2)
    caracteres_descriptografados = descriptografia(caracteres, chave)
    linhas_descriptografadas = mensagem_descriptografada(caracteres_descriptografados, linhas)

    print(chave)

    for g in linhas_descriptografadas:
        print(g)


if __name__ == '__main__':
    main()
