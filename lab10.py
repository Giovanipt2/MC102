def calcula_recuperacao(vida_aloy: int) -> int:
    '''Calcula quantos pontos de vida Aloy pode recuperar
    
    Parâmetro:
    vida_aloy -- número inteiro

    Retorno:
    vida_recuperada -- número inteiro
    '''
    vida_recuperada: int = vida_aloy // 2

    return vida_recuperada


def flechas(quais_flechas: list) -> dict:
    '''Cria um dicionário com as flechas e suas respectivas quantidades
    
    Parâmetro:
    quais_flechas -- lista de strings

    Retorno:
    flechas -- dicionário
        chave -- tipo da flecha
        valor -- quantidade de flechas do tipo
    '''
    flechas: dict = {} 
    tipo_flechas: list = []
    quantidade_flechas: list = []

    for i in range(len(quais_flechas)):
        if i % 2 == 0:
            tipo_flechas.append(quais_flechas[i])

        else:
            quantidade_flechas.append(quais_flechas[i])

    lista_flechas = zip(tipo_flechas, quantidade_flechas)

    for flecha, quantidade in lista_flechas:
        flechas[flecha] = int(quantidade)

    return flechas


def calcula_flechas(flechas_aloy: dict) -> int:
    '''Calcula a quantidade de flechas totais que Aloy possui
    
    Parâmetro:
    flechas_aloy -- dicionário
        chave -- tipo da flecha
        valor -- quantidade de flechas do tipo

    Retorno:
    quantidade_flechas -- número inteiro
    '''
    quantidade_flechas: int = 0

    for quantidade in flechas_aloy.values():
        quantidade_flechas += quantidade

    return quantidade_flechas


def cria_partes(atributos_maquina: list) -> dict:
    '''Cria um dicionário com os partes e seus respectivos atributos
    
    Parâmetro:
    atributos_montros -- lista de números inteiros

    Retorno:
    partes_maquina -- dicionário
        chave -- parte
        valor -- lista com a fraqueza, o dano máximo e a posição dessa parte no monstro (tupla)
    '''
    partes_maquina: dict = {}
    atributos_partes: list = []

    for _ in range(int(atributos_maquina[2])):
        atributos_parte = input().split(', ')           #informações sobre as partes que compõem cada monstro
        atributos_partes.append(atributos_parte)

    for i in range(len(atributos_partes)):
        partes_maquina[atributos_partes[i][0]] = [atributos_partes[i][1], int(atributos_partes[i][2]), (int(atributos_partes[i][3]), int(atributos_partes[i][4]))]

    return partes_maquina


def cria_maquinas_partes(partes_maquinas: list, atributos_maquinas: list) -> dict:
    '''Cria um dicionário com as maquinas e suas respectivas partes
    
    Parâmetro:
    partes_maquinas -- lista de dicionários
    atributos_maquinas -- lista de números inteiros

    Retorno:
    maquinas_e_partes -- dicionário
        chave -- máquina
        valor -- informações das partes que compõem a máquina
    '''
    maquinas_e_partes: dict = {}

    for i in range(len(atributos_maquinas)):
        for j in range(len(atributos_maquinas[i])):
            atributos_maquinas[i][j] = int(atributos_maquinas[i][j])

    for i in range(len(partes_maquinas)):
        maquinas_e_partes[str(i)] = partes_maquinas[i]

    return maquinas_e_partes


def cria_maquinas_atributos(atributos_maquinas: list) -> dict:
    '''Cria um dicionário com as máquinas e seus respectivos atributos
    
    Parâmetro:
    atributos_maquinas -- matriz (lista de listas)

    Retorno:
    maquinas_e_atributos -- dicionário
        chave -- máquina
        valor -- atributos da máquina
    '''
    maquinas_e_atributos: dict = {}

    for i in range(len(atributos_maquinas)):
        maquinas_e_atributos[str(i)] = atributos_maquinas[i]

    return maquinas_e_atributos


def calcula_dano(maquinas_e_partes: dict, ataque: list) -> int:
    '''Calcula o dano causado pelo ataque de Aloy com base nas regras do jogo
    
    Parâmetro:
    maquinas_e_partes -- dicionário
        chave -- máquina
        valor -- informações das partes que compõem a máquina
    ataque -- lista de strings

    Retorno:
    dano_causado -- número inteiro
    '''
    inimigo = ataque[0]
    parte_atacada = ataque[1]
    flecha_utilizada = ataque[2]
    fx, fy = int(ataque[3]), int(ataque[4])                         #posição acertada pela flecha
    fraqueza = maquinas_e_partes[inimigo][parte_atacada][0]
    dano_maximo = maquinas_e_partes[inimigo][parte_atacada][1]
    cx, cy = maquinas_e_partes[inimigo][parte_atacada][2]           #posição do crítico na máquina                   

    distancia_manhattan = abs((cx - fx) + (cy - fy))

    if flecha_utilizada == fraqueza or fraqueza == 'todas':
        dano_causado = dano_maximo - distancia_manhattan

    else:
        dano_causado = (dano_maximo - distancia_manhattan) // 2

    if dano_causado <= 0:
        dano_causado = 0
    
    return dano_causado


def calcula_criticos(maquinas_e_partes: dict, ataque: list, n_maquinas: int) -> dict:
    '''Verifica e armazena se a máquina atacada recebeu um crítico
    
    Parâmetros:
    maquinas_e_partes -- dicionário
        chave -- máquina
        valor -- informações das partes que compõem a máquina
    ataque -- lista de strings
    criticos -- dicionário
        chave -- máquina
        valor -- pontos críticos acertados

    Retorno:
    criticos -- dicionário
        chave -- máquina
        valor -- pontos críticos acertados
    '''
    criticos: list = [{str(i):[]} for i in range(n_maquinas)]

    inimigo = ataque[0]
    parte_atacada = ataque[1]
    fx, fy = int(ataque[3]), int(ataque[4])                     #posição acertada pela flecha
    cx, cy = maquinas_e_partes[inimigo][parte_atacada][2]       #posição do crítico na máquina

    distancia_manhattan = abs((cx - fx) + (cy - fy))

    if distancia_manhattan == 0:
        criticos[int(inimigo)][inimigo].append((fx, fy)) 

    return criticos


def flechas_gastas(flechas_utilizadas: list, flechas_aloy: dict) -> dict:
    '''Calcula as flechas que sobraram para Aloy após o combate
    
    Parâmetros:
    flechas_utilizadas -- lista de strings
    flechas_aloy -- dicionário
        chave -- tipo da flecha
        valor -- quantidade de flechas do tipo
    '''
    for flecha in flechas_aloy:
        flechas_aloy[flecha] -= flechas_utilizadas.count(flecha)

    return flechas_aloy


def dano_maquina(maquinas_e_atributos: dict, ataque: list, dano_causado: int) -> dict:
    '''Aplica o dano na máquina e verifica se ela foi derrotada
    
    Parâmetros:
    maquinas_e_atributos -- dicionário
        chave -- máquina
        valor -- atributos da máquina
    ataque -- lista de strings
    dano_causado -- número inteiro

    Retorno:
    maquinas_e_atributos -- dicionário
        chave -- máquina
        valor -- atributos da máquina
    '''
    inimigo = ataque[0]
    vida_maquina = maquinas_e_atributos[inimigo][0]

    vida_maquina -= dano_causado

    if vida_maquina <= 0:
        vida_maquina = 0

    maquinas_e_atributos[inimigo][0] = vida_maquina

    return maquinas_e_atributos


def maquina_morta(maquinas_e_atributos: dict, ataque: list, maquinas_mortas: list) -> list:
    '''Verifica se a máquina estṕa viva ou não
    
    Parâmetro:
    maquinas_e_atributos -- dicionário
        chave -- máquina
        valor -- atributos da máquina
    ataque -- lista de strings

    Retorno:
    maquinas_mortas -- lista de strings
    '''
    inimigo = ataque[0]
    vida_maquina = maquinas_e_atributos[inimigo][0]

    if vida_maquina <= 0:
        maquinas_mortas.append(inimigo)

    return maquinas_mortas


def dano_aloy(vida_aloy: int, maquinas_e_atributos: dict, ataque: list) -> int:
    '''Calcula o dano sofrido por Aloy após três ataques
    
    Parâmetros:
    vida_aloy -- número inteiro
    maquinas_e_atributos -- dicionário
        chave -- máquina
        valor -- atributos da máquina
    ataque -- lista de strings

    Retorno:
    vida_aloy -- número inteiro
    '''
    inimigo = ataque[0]
    dano_da_maquina = maquinas_e_atributos[inimigo][1]

    vida_aloy -= dano_da_maquina

    return vida_aloy


def recupera_vida(vida_aloy: int, vida_recuperada: int, vida_max_aloy: int) -> int:
    '''Faz com que Aloy recupere a vida após o combate
    
    Parâmetros:
    vida_aloy -- número inteiro
    vida_recuperada -- número inteiro
    vida_max_aloy -- número inteiro
    
    Retorno
    vida_aloy -- número inteiro
    '''
    vida_aloy += vida_recuperada

    if vida_aloy >= vida_max_aloy:
        vida_aloy = vida_max_aloy
    
    return vida_aloy


def recupera_flechas(flechas_aloy: dict, flechas_aloy_originais: dict) -> dict:
    '''Recupera as flechas da Aloy após o combate
    
    Parâmetros:
    flechas_aloy -- dicionário
        chave -- tipo da flecha
        valor -- quantidade de flechas do tipo
    flechas_aloy_originais -- dicionário
        chave -- tipo da flecha
        valor -- quantidade de flechas do tipo
    '''
    flechas_aloy = flechas_aloy_originais

    return flechas_aloy


def fim_de_combate(vida_aloy: int, flechas_aloy: dict, maquinas_vivas_da_vez: list, maquinas_mortas: list) -> bool:
    '''Verifica se o combate acabou
    
    Parâmetros:
    vida_aloy -- número inteiro
    quantidade_flechas -- número inteiro
    maquinas_vivas_da_vez -- lista de strings
    maquinas_mortas -- lista de strings

    Retorno:
    fim_combate -- booleano
    '''
    quantidade_flechas = calcula_flechas(flechas_aloy)
    
    if vida_aloy == 0 or quantidade_flechas == 0 or maquinas_vivas_da_vez == maquinas_mortas:
        fim_combate = True

    return fim_combate


def fim_de_jogo(fim_combate: bool, maquinas_vivas: list) -> bool:
    '''Verifica se o jogo acabou
    
    Parâmetros:
    fim_combate -- booleano
    maquinas_vivas -- lista de strings

    Retorno:
    fim_jogo -- booleano
    '''
    if fim_combate and maquinas_vivas == []:
        fim_jogo = True

    return fim_jogo


def imprime() -> None:
    '''Imprime a saída da forma correta'''


def main() -> None:
    vida_max_aloy = int(input())                                            #pontos de vida máximo da Aloy    
    vida_aloy = vida_max_aloy

    vida_recuperada = calcula_recuperacao(vida_max_aloy)

    quais_flechas = input().split()                                         #quais os tipos de flecha que Aloy possui e suas respectivas quantidades
    
    flechas_aloy_originais = flechas(quais_flechas)
    flechas_aloy = flechas(quais_flechas)

    n_maquinas = int(input())                                               #quantidade de máquinas que Aloy enfrentará
    
    maquinas_vivas: list = [str(i) for i in range(n_maquinas)]              #maquinas vivas ao todo
    
    contador_combates: int = 0

    while True:
        maquinas_da_vez = int(input())                                      #quantos máquinas Aloy enfrentrá no combate específico (por vez)

        maquinas_vivas_da_vez: list = [str(i) for i in range(maquinas_da_vez)]      #maquinas vivas no começo do combate

        atributos_maquinas: list = []                                       #informações sobre os atributos de cada máquina
        partes_maquinas: list = []                                          #informações sobre os atributos de cada parte da máquina

        for _ in range(maquinas_da_vez):
            atributos_maquina = input().split()
            atributos_maquinas.append(atributos_maquina)
            partes_maquina = cria_partes(atributos_maquina)
            partes_maquinas.append(partes_maquina) 

        maquinas_e_partes = cria_maquinas_partes(partes_maquinas, atributos_maquinas)
        maquinas_e_atributos = cria_maquinas_atributos(atributos_maquinas)
        
        flechas_utilizadas: list = []                                       #quais flechas Aloy usou em seus ataques
        contador_ataques: int = 0                                           #conta quantos ataques foram dados para saber se Aloy recebe dano ou não
        
        maquinas_mortas:list = []
        
        print(f'Combate {contador_combates}, vida = {vida_aloy}')

        while True:
            ataque = input().split(', ')
            contador_ataques += 1
            flechas_utilizadas.append(ataque[2])

            dano_causado = calcula_dano(maquinas_e_partes, ataque)
            criticos = calcula_criticos(maquinas_e_partes, ataque, n_maquinas)
            flechas_aloy = flechas_gastas(flechas_utilizadas, flechas_aloy)
            maquinas_e_atributos = dano_maquina(maquinas_e_atributos, ataque, dano_causado)
            
            if contador_ataques % 3 == 0:
                dano_aloy(vida_aloy, maquinas_e_atributos, ataque)

            maquinas_mortas = maquina_morta(maquinas_e_atributos, ataque)

            maquinas_vivas = [maquina for maquina in maquinas_vivas if maquina not in maquinas_mortas]
            fim_combate = fim_de_combate(vida_aloy, flechas_aloy, maquinas_vivas_da_vez, maquinas_mortas)
            quantidade_flechas = calcula_flechas(flechas_aloy)

            if fim_combate:
                contador_combates += 1
                if vida_aloy == 0 and maquinas_mortas != []:
                    for maquina in maquinas_mortas:
                        print(f'Máquina {maquina} derrotada')
                    print(f'Vida após o combate = {vida_aloy}')
                    print('Aloy foi derrotada em combate e não retornará a tribo.')

                elif quantidade_flechas == 0:
                    print
                
                break
        
        vida_aloy = recupera_vida(vida_aloy, vida_recuperada, vida_max_aloy)
        flechas_aloy = recupera_flechas(flechas_aloy, flechas_aloy_originais)

        fim_jogo = fim_de_jogo(fim_combate, maquinas_vivas)

        if fim_jogo:
            break


if __name__ == '__main__':
    main()