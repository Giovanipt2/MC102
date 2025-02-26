def calcula_media(categorias: dict) -> dict:
    '''Calcula a média aritmética das notas recebidas pelos filmes
    
    Parâmetro:
    categorias -- dicionário de dicionário
        chaves_1 -- categorias
        valores_1/chaves_2 -- filmes
        valores_2 -- lista de notas
 
    Retorno:
    analise_avaliacoes -- dicionáio de dicionário
        chaves_1 -- categorias
        valores_1/chaves_2 -- filmes
        valores_2 -- lista com a média e o número de notas recebidas
    '''
    analise_avaliacoes: dict = categorias
 
    for categoria in categorias:
        for filme in categorias[categoria]:
            media = sum(categorias[categoria][filme]) / len(categorias[categoria][filme])
            novo_valor = [media, len(categorias[categoria][filme])]
            analise_avaliacoes[categoria][filme] = novo_valor
    
    return analise_avaliacoes
 
 
def acha_vencedores_simples(analise_avaliacoes: dict) -> dict:
    '''Encontra o filme vencedor de cada categoria simples
    
    Parâmetro:
    analise_avaliacoes -- dicionário de dicionários
        chave_1 -- categorias
        valor_1/chave_2 -- filmes
        valor_2 -- lista com a média e o número de notas recebidas
 
    Retorno:
    vencedores_simpĺes -- dicionário
        chave -- categoria
        valor -- filme vencedor da categoria
    '''
    vencedores_simples: dict = {'filme que causou mais bocejos':None, 'filme que foi mais pausado':None, 'filme que mais revirou olhos':None, 'filme que não gerou discussão nas redes sociais':None, 'enredo mais sem noção':None}
 
    for categoria in analise_avaliacoes:
        media_max: int = 0
        avaliacoes_max: int = 0
        filme_ganhador: str = ""
 
        for filme in analise_avaliacoes[categoria]:
            if analise_avaliacoes[categoria][filme][0] > media_max:
                media_max = analise_avaliacoes[categoria][filme][0]
                avaliacoes_max = analise_avaliacoes[categoria][filme][1]
                filme_ganhador = filme
            
            elif analise_avaliacoes[categoria][filme][0] == media_max:
                if analise_avaliacoes[categoria][filme][1] > avaliacoes_max:
                    media_max = analise_avaliacoes[categoria][filme][0]
                    avaliacoes_max = analise_avaliacoes[categoria][filme][1]
                    filme_ganhador = filme
        
        vencedores_simples[categoria] = filme_ganhador
 
    return vencedores_simples
 
 
def calcula_pontos_total(analise_avaliacoes: dict, filmes: list[str]) -> dict:
    '''Calcula a soma das médias de cada filme que foi avaiado
    
    Função que será usada no critério de desempate para determinar o vencedor do prêmio: "pior filme do ano"
 
    Parâmetro:
    analise_avaliacoes -- dicionário de dicionários
        chaves_1 -- categorias
        valores_1/chaves_2 -- filmes
        valores_2 -- lista com a média e o número de notas recebidas
 
    Retorno:
    pontos_filmes -- dicionário
        chaves -- filmes
        valores -- soma de suas respectivas médias
    '''
    pontos_filmes: dict = {filme: [] for filme in filmes}
 
    for categoria in analise_avaliacoes:
        for filme in analise_avaliacoes[categoria]:
            pontos_filmes[filme].append(analise_avaliacoes[categoria][filme][0])
 
    for filme in pontos_filmes:
        pontos_filmes[filme] = sum(pontos_filmes[filme])
 
    return pontos_filmes
 
 
def acha_pior_filme_ano(vencedores_simples: dict, filmes: list[str], pontos_filmes: dict) -> str:
    '''Encontra o filme vencedor do prêmio: "Pior filme do ano"
    
    Parâmetros:
    vencedores_simples -- dicionário
        chaves -- categoria
        valores -- filme vencedor da categoria
    filmes -- lista de strings
    pontos_filmes -- dicionário
        chaves -- filmes
        valores -- soma das médias das notas de cada filme
    
    Retorno:
    pior_filme_ano -- string
    '''
    quantidade_premios: dict = {filme: 0 for filme in filmes}
 
    for categoria in vencedores_simples:
        if vencedores_simples[categoria] in quantidade_premios:
            quantidade_premios[vencedores_simples[categoria]] += 1
 
    premios_max: int = 0
    pontos_max: int = 0
    pior_filme_ano: str = ""
 
    for filme in quantidade_premios:
        if quantidade_premios[filme] > premios_max:
            premios_max = quantidade_premios[filme]
            pontos_max = pontos_filmes[filme]
            pior_filme_ano = filme
 
        elif quantidade_premios[filme] == premios_max:
            if pontos_filmes[filme] > pontos_max:
                premios_max = quantidade_premios[filme]
                pontos_max = pontos_filmes[filme]
                pior_filme_ano = filme
 
    return pior_filme_ano
 
 
def acha_nao_merecia_estar_aqui(filmes: list[str], filmes_avaliados: set) -> str:
    ''' Encontra, se existir, o filme vencedor do prêmio: "Não merecia estar aqui
    
    Parâmetros:
    filmes -- lista de strings
    filmes_avaliados -- conjunto
 
    Retorno:
    filme_nao_deveria -- list[str]
    '''
    filme_nao_merecia: list[str] = []
    
    for filme in filmes:
        if filme not in filmes_avaliados:
            filme_nao_merecia.append(filme)
 
    return filme_nao_merecia
 
 
def main() -> None:
 
    numero_filmes: int = int(input())      
 
    filmes: list[str] = []
    filmes_avaliados: set = set()
    categorias: dict = {'filme que causou mais bocejos':{}, 'filme que foi mais pausado':{}, 'filme que mais revirou olhos':{}, 'filme que não gerou discussão nas redes sociais':{}, 'enredo mais sem noção':{}}
 
    for _ in range(numero_filmes):
        nome_filme = input()
        filmes.append(nome_filme)
 
    numero_avaliacoes: int = int(input())
 
    for _ in range(numero_avaliacoes):                          
        avaliacao = input().split(', ')
        if avaliacao[2] not in categorias[avaliacao[1]]:
            categorias[avaliacao[1]][avaliacao[2]] = []
        categorias[avaliacao[1]][avaliacao[2]].append(int(avaliacao[3]))
 
        filmes_avaliados.add(avaliacao[2])
 
    analise_avaliacoes = calcula_media(categorias)
    vencedores_simples = acha_vencedores_simples(analise_avaliacoes)
    pontos_filmes = calcula_pontos_total(analise_avaliacoes, filmes)
    pior_filme_ano = acha_pior_filme_ano(vencedores_simples, filmes, pontos_filmes)
    filme_nao_deveria = acha_nao_merecia_estar_aqui(filmes, filmes_avaliados)
 
    lista_vencedores_simples: str = []
    
    for categoria in vencedores_simples:
        lista_vencedores_simples.append(vencedores_simples[categoria])
 
    print("#### abacaxi de ouro ####")
    print()
    print("categorias simples")
    print("categoria: filme que causou mais bocejos")
    print("- " + lista_vencedores_simples[0])
    print("categoria: filme que foi mais pausado")
    print("- " + lista_vencedores_simples[1])
    print("categoria: filme que mais revirou olhos")
    print("- " + lista_vencedores_simples[2])
    print("categoria: filme que não gerou discussão nas redes sociais")
    print("- " + lista_vencedores_simples[3])
    print("categoria: enredo mais sem noção")
    print("- " + lista_vencedores_simples[4])
    print()
    print("categorias especiais")
    print("prêmio pior filme do ano")
    print("- " + pior_filme_ano)
    print("prêmio não merecia estar aqui")
    
    if filme_nao_deveria == []:
        print("- sem ganhadores")
 
    else:
        nao_mereciam: str = ", ".join(filme_nao_deveria)
        print("- " + nao_mereciam)
 
 
if __name__ == '__main__':
    main()
