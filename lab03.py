j = int(input())                                        #número de jogadores

numeros_magicos = input().split()                       #números tirados pelos jogadores
numeros_magicos = list(map(int, numeros_magicos))                

intervalos = input().split()
intervalos = list(map(int, intervalos))

pontos = []
for i in range ((j+1) // 2):
    pontuacao_1 = (intervalos[2*i + 1] - intervalos[2*i]) * numeros_magicos[i]
    pontos.append(pontuacao_1)

for i in range ((j+1) // 2, j):
    pontuacao_2 = (intervalos[2*i + 1] - intervalos[2*i]) + numeros_magicos[i]
    pontos.append(pontuacao_2)

i_maximo = 0

for i in range (j):
    if pontos[i] > pontos[i_maximo]:
        i_maximo = i

k = 0       
for i in range (j):
    if pontos[i] == pontos[i_maximo]:
        k += 1
    
if k == 1:   
    print("O jogador número", i_maximo + 1, "vai receber o melhor bolo da cidade pois venceu com", pontos[i_maximo], "ponto(s)!")
else:
    print("Rodada de cerveja para todos os jogadores!")