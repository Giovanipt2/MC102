def acha_robo(comodo: list[list[str]]) -> tuple:
    '''Acha a posição do robô no cômodo
    
    Parâmetro:
    comodo -- matriz (lista de listas)

    Retorno
    posicao_atual -- tupla de números inteiros
    '''
    global posicao_atual

    for i in range(len(comodo)):
        for j in range(len(comodo[i])):
            if comodo[i][j] == 'r':
                posicao_atual = (i, j)
                return posicao_atual


def caminho_normal(comodo: list[list[str]]) -> str:
    '''Decide o caminho padrão do robô
    
    Se a linha for par, vai da esquerda para a direira
    Se a linha for ímpar, vai da direira para a esquerda

    Parâmetro:
    comodo -- matriz (lista de listas)

    Retorno:
    direcao_normal -- string
    '''
    (i, j) = posicao_normal

    if i % 2 == 0:
        if j + 1 < len(comodo[i]):
            direcao_normal = 'direita'
            return direcao_normal
            
        else:
            direcao_normal = 'baixo'
            return direcao_normal

    else:   
        if j - 1 >= 0:
            direcao_normal = 'esquerda'
            return direcao_normal
        
        else:
            direcao_normal = 'baixo'
            return direcao_normal


def move_robo(comodo: list[list[str]], n_linhas: int, tamanho_linha: int) -> None:
    '''Move o robô dentro do cômodo de acordo com a direçao normal

    Parâmetros:
    comodo -- matriz (lista de listas)
    n_linhas -- número inteiro
    tamanho_linha -- número inteiro

    Retorno
    None
    '''
    global posicao_normal
    global posicao_atual

    direcao_normal = caminho_normal(comodo)
    (i, j) = posicao_normal

    if direcao_normal == 'direita':
        comodo[i][j + 1] = 'r'
        comodo[i][j] = '.'
        posicao_normal = (i, j + 1)
        posicao_atual = posicao_normal
            
    elif direcao_normal == 'baixo':
        comodo[i + 1][j] = 'r'
        comodo[i][j] = '.'
        posicao_normal = (i + 1, j)
        posicao_atual = posicao_normal

    else:
        comodo[i][j - 1] = 'r'
        comodo[i][j] = '.'
        posicao_normal = (i, j - 1)
        posicao_atual = posicao_normal
        
    imprime(comodo, n_linhas, tamanho_linha)
        

def escaneia_ambeiente(comodo: list[list[str]], tamanho_linha: int) -> str:
    '''A partir da posição do robô, procura por sujeira no comôdo
    
    Parâmetros:
    comodo -- matriz (lista de listas)
    tamanho_linha -- número inteiro

    Retorno
    direcao_limpeza -- string
    '''
    global posicao_atual
    
    posicao_atual = acha_robo(comodo)
    (l, k) = posicao_atual
    
    direcao_limpeza = None

    if k - 1 < tamanho_linha:
        if k != 0:
            if comodo[l][k - 1] == 'o':
                direcao_limpeza = 'esquerda'

    if l - 1 < len(comodo):
        if l != 0:
            if comodo[l - 1][k] == 'o':
                direcao_limpeza = 'cima'       
        
    if k + 1 < tamanho_linha:
        if comodo[l][k + 1] == 'o':
            direcao_limpeza = 'direita'
        
    if l + 1 < len(comodo):
        if comodo[l + 1][k] == 'o':
            direcao_limpeza = 'baixo'

    if direcao_limpeza == None:
       posicao_atual = posicao_normal

    return direcao_limpeza


def limpar(comodo: list[list[str]], direcao_limpeza: str, n_linhas: int, tamanho_linha: int) -> None:
    '''Vai até a posição onde há sujeira e a limpa
    
    Ordem de prioridade da movimentação do robô:
    1) Esquerda
    2) Cima
    3) Direita
    4) Baixo

    Parâmetros:
    comodo -- matriz (lista de listas)
    direcao_limpeza -- string
    n_linhas -- número inteiro
    tamanho_linha -- número inteiro

    Retorno:
    None
    '''
    global posicao_normal
    global posicao_atual

    (i, j) = posicao_normal
    (l, k) = posicao_atual

    if direcao_limpeza == 'esquerda':
        comodo[l][k - 1] = 'r'
        comodo[l][k] = '.'
        posicao_atual = (l, k - 1)
        k -= 1

    elif direcao_limpeza == 'cima':
        comodo[l - 1][k] = 'r'
        comodo[l][k] = '.'
        posicao_atual = (l - 1, k)
        l -= 1

    elif direcao_limpeza == 'direita':
        comodo[l][k + 1] = 'r'
        comodo[l][k] = '.'
        posicao_atual = (l, k + 1)
        k += 1

    elif direcao_limpeza == 'baixo':
        comodo[l + 1][k] = 'r'
        comodo[l][k] = '.'
        posicao_atual = (l + 1, k)
        l += 1

    if direcao_limpeza == caminho_normal(comodo):
        if l - 1 == i and k == j:
            posicao_normal = posicao_atual
        
        elif l == i and k == j - 1:
            posicao_normal = posicao_atual

        elif l == i and k == j + 1:
            posicao_normal = posicao_atual

    imprime(comodo, n_linhas, tamanho_linha)


def retorna_posicao(comodo: list[list[str]], n_linhas: int, tamanho_linha: int) -> None:
    '''Faz com que o robô volte à posição em que ele deveria estar normalmente
    
    Parâmetros:
    comodo -- matriz (lista de listas)
    n_linhas -- número inteiro
    tamanho_linha -- número inteiro

    Retorno:
    None
    '''
    global posicao_normal
    global posicao_atual

    (i, j) = posicao_normal
    (l, k) = posicao_atual

    direcao_limpeza = escaneia_ambeiente(comodo, tamanho_linha)
    
    if direcao_limpeza == None:
        while k != j:
            if k < j:
                comodo[l][k + 1] = 'r'
                comodo[l][k] = '.'
                k += 1
                
            else:
                comodo[l][k - 1] = 'r'
                comodo[l][k] = '.'
                k -= 1

            imprime(comodo, n_linhas, tamanho_linha)

        while l != i:
            if l < i:
                comodo[l + 1][k] = 'r'
                comodo[l][k] = '.'
                l += 1

            else:
                comodo[l - 1][k] = 'r'
                comodo[l][k] = '.'
                l -= 1

            imprime(comodo, n_linhas, tamanho_linha)

    else:
        limpar(comodo, direcao_limpeza, n_linhas, tamanho_linha)


def finalizar_limpeza(comodo: list[list[str]], n_linhas: int, tamanho_linha: int) -> None:
    '''Quando o robô termina toda a limpeza, desliga o robô
    
    Parâmetros:
    comodo -- matriz (lista de listas)
    n_linhas -- número inteiro
    tamanho_linha -- número inteiro

    Retorno:
    None
    '''
    global posicao_normal

    (i, j) = posicao_normal
    
    if n_linhas % 2 != 0:
        if posicao_normal == (len(comodo) - 1, tamanho_linha - 1):
            exit()

    else:
        if posicao_normal == (len(comodo) - 1, 0):
            while posicao_normal != (len(comodo) - 1, tamanho_linha - 1):
                comodo[i][j + 1] = 'r'
                comodo[i][j] = '.'
                posicao_normal = (i, j + 1)
                j += 1
                imprime(comodo, n_linhas, tamanho_linha)
            exit()


def imprime(comodo: list[list[str]], n_linhas: int, tamanho_linha: int,ultima_linha: bool = False) -> None:
    '''Imprime a saída da forma correta, linha por linha
    
    Parâmetro:
    comodo -- matriz (lista de listas)
    n_linhas -- número inteiro
    tamanho_linha -- número inteiro
    ultima_linha -- booleana

    Retorno:
    None
    '''
    for linha in comodo:
        print(' '.join(linha))

    if n_linhas % 2 != 0:
        if posicao_normal == (len(comodo) - 1, tamanho_linha - 1):
            ultima_linha = True

    else:
        if posicao_normal == (len(comodo) - 1, tamanho_linha - 1) and posicao_atual != posicao_normal:
            ultima_linha = True

    if not ultima_linha: 
        print()


def main() -> None:
    global posicao_normal

    posicao_normal = (0, 0)                     #posição incial do robô no cômodo

    n_linhas: int = int(input())                #número de linhas da matriz que representa o cômodo

    comodo: list[list[str]] = []                #matriz que representa o cômodo em questão
    
    for _ in range(n_linhas):
        parte_comodo = input().split()
        comodo.append(parte_comodo)

    tamanho_linha: int = len(parte_comodo)      #quantas colunas há na matriz 

    while True:
        direcao_limpeza = escaneia_ambeiente(comodo, tamanho_linha)
        if direcao_limpeza == None:
            move_robo(comodo, n_linhas, tamanho_linha)

        else:
            limpar(comodo, direcao_limpeza, n_linhas, tamanho_linha)
        
        retorna_posicao(comodo, n_linhas, tamanho_linha)
        finalizar_limpeza(comodo, n_linhas, tamanho_linha)
    

if __name__ == "__main__":
    main()