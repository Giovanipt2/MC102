d = int(input())                                                    #número de dias analisados

for i in range (d):
    m = int(input())                                                #número de pares de animais que brigam
    lista_animais_brigam = []
    for j in range (m):
        animais_brigam = input().split()
        lista_animais_brigam.append(animais_brigam)
    procedimentos = input().split()                                 #procedimentos disponíveis e suas quantidades
    for j in range (1, len(procedimentos), 2):
        quantidade = int(procedimentos[j])
        procedimentos[j] = quantidade
    z = int(input())                                                #número de animais que foram ao Pet Shop
    lista_animal_procedimento = []
    for j in range (z):         
        animal_procedimento = input().split()
        lista_animal_procedimento.append(animal_procedimento)

    brigas = 0
   
    for g in range (len(lista_animal_procedimento)):
        for h in range (len(lista_animais_brigam)):
            if lista_animais_brigam[h][0] == lista_animal_procedimento[g][0]:
                for l in range (len(lista_animal_procedimento)):
                    if lista_animais_brigam [h][1] == lista_animal_procedimento[l][0]:
                        brigas += 1

    todos_procedimentos = []
    animais_atendidos = []
    animais_nao_atendidos = []
    procedimentos_indisponiveis = []

    for j in range (1, len(procedimentos), 2):
        quantidade = int(procedimentos[j])
        procedimentos[j] = quantidade
    for g in range (len(procedimentos)):
        if type(procedimentos[g]) == int:
            for c in range (procedimentos[g]):
                todos_procedimentos.append(procedimentos[g-1])
    
    for g in lista_animal_procedimento:
        if g[1] in todos_procedimentos:
            todos_procedimentos.remove(g[1])
            animais_atendidos.append(g[0])
        elif g[1] in procedimentos:
            animais_nao_atendidos.append(g[0])
        else:
            procedimentos_indisponiveis.append(g[0])

        
    
    print("Dia:", i + 1)
    print("Brigas:", brigas)
    if len(animais_atendidos) > 0:
        for t in range (len(animais_atendidos)):
            if t == 0:
                print("Animais atendidos:", animais_atendidos[t], end="")
            else:
                print(",", animais_atendidos[t], end="")
        print("")
    if len(animais_nao_atendidos) > 0:
        for t in range (len(animais_nao_atendidos)):
            if t == 0:
                print("Animais não atendidos:", animais_nao_atendidos[t], end="")
            else:
                print(",", animais_nao_atendidos[t], end="")
        print("")
    if len(procedimentos_indisponiveis) > 0:
        for t in range (len(procedimentos_indisponiveis)):
            print("Animal", procedimentos_indisponiveis[t], "solicitou procedimento não disponível.")
    print("")
