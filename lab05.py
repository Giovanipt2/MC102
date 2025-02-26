def reverter(i, j):
    '''Reverte a subsequência de i até j do genoma atual'''
    global genoma_atual
    trecho = genoma_atual[i:j + 1]
    trecho_revertido = trecho[::-1]
    genoma_atual = genoma_atual[:i] + trecho_revertido + genoma_atual[j + 1:]
    return genoma_atual

def transpor(i, j, k):
    '''Troca a posição da subsequência iniciada em i e terminada em j com a subsequência iniciada em j + 1 até k'''
    global genoma_atual
    trecho_1 = genoma_atual[i:j + 1]
    trecho_2 = genoma_atual[j + 1:k + 1]
    genoma_atual = genoma_atual[:i] + trecho_2 + trecho_1 + genoma_atual[k + 1:]
    return genoma_atual


def combinar(novo_genoma_1, i):                    
    '''Insere o novo genoma informado na i-ésima posição do genoma atual'''
    global genoma_atual
    trecho_1 = genoma_atual[:i]
    trecho_2 = genoma_atual[i:]
    genoma_atual = trecho_1 + novo_genoma_1 + trecho_2
    return genoma_atual

def concatenar(novo_genoma_2):
    '''Adiciona ao final do genoma atual um novo genoma informado'''
    global genoma_atual
    genoma_atual = genoma_atual + novo_genoma_2
    return genoma_atual
    
def remover(i, j):
    '''Remove a subsequência [i, j] do genoma atual'''
    global genoma_atual
    trecho_removido = genoma_atual[i:j + 1]
    genoma_atual = genoma_atual[:i] + genoma_atual[j+1:]
    return genoma_atual

def transpor_e_reverter(i, j, k):
    '''Transpõe o genoma considerando i, j e k e, depois, reverte-o considerando os indíces i e k'''
    global genoma_atual
    transpor(i, j, k)
    reverter(i, k)

def buscar(genoma_de_busca):
    '''Mostra o número de vezes que o genoma em questão aparece no genoma atual'''
    contador = genoma_atual.count(genoma_de_busca)
    print(contador) 

def buscar_bidirecional(genoma_de_busca):
    '''Exibe quantas vezes um genoma de interesse aparece no genoma atual, ou em sua forma original, ou em sua forma invertida'''
    contador_1 = genoma_atual.count(genoma_de_busca)
    contador_2 = genoma_atual.count(genoma_de_busca[::-1])
    contador_final = contador_1 + contador_2
    print(contador_final)

def mostrar():
    '''Mostra qual é o genoma atual para o usuário'''
    global genoma_atual
    print(genoma_atual)

def ajeita_tamanho_1(comando):
    '''Se um dos índices exceder o tamanho da palavra, o maior índice válido será considerado'''
    novo_comando = []
    for i in range(len(comando)):
        if i > 0:
            comando[i] = int(comando[i])
    
    if len(novo_comando) > len(genoma_atual):
        novo_comando = novo_comando[:len(genoma_atual)]

def ajeita_tamanho_2(comando):
    '''Se um dos índices exceder o tamanho da palavra, o maior índice válido será considerado'''
    novo_comando = []
    for i in range(len(comando)):
        if i > 1:
            comando[i] = int(comando[i])
    
    if len(novo_comando) > len(genoma_atual):
        novo_comando = novo_comando[:len(genoma_atual)]   

genoma_atual = input()
entradas = input().split()


while True:
    if entradas[0] == "reverter":
        ajeita_tamanho_1(entradas)
        reverter(entradas[1], entradas[2])
        
    elif entradas[0] == "transpor":
        ajeita_tamanho_1(entradas)
        transpor(entradas[1], entradas[2], entradas[3])

    elif entradas[0] == "combinar":
        ajeita_tamanho_2(entradas)
        combinar(entradas[1], entradas[2])

    elif entradas[0] == "concatenar":
        concatenar(entradas[1])

    elif entradas[0] == "remover":
        ajeita_tamanho_1(entradas)
        remover(entradas[1], entradas[2])

    elif entradas[0] == "transpor_e_reverter":
        ajeita_tamanho_1(entradas)
        transpor_e_reverter(entradas[1], entradas[2], entradas[3])

    elif entradas[0] == "buscar":
        buscar(entradas[1])

    elif entradas[0] == "buscar_bidirecional":
        buscar_bidirecional(entradas[1])

    elif entradas[0] == "mostrar":
        mostrar()

    elif entradas[0] == "sair":
        break
    
    entradas = input().split()