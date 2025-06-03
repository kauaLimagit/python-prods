import random

#matriz do game
line1 = []
line2 = []
line3 = []
line4 = []
listas = [line1,line2,line3,line4]

#casas onde averão uma bomba
selected_number = []

#mecanismo de loop, caso exploda o loop de perguntas acaba
explodiu = 0

# pontuação do player
pontos = 0

#tamanho horizontal do campo minado
valores = 7
ind_number = '⬜'

#sistema em loop que adiciona as casas na matriz, que é separada em varias listas
while len(line1) != valores:
    for i in listas:
        i.append(ind_number)
        
for place in range(0, len(line1)):
    if place == random.randint(1,valores):
        selected_number.append(place)

for place in range(0, len(line2)):
    if place == random.randint(1,valores):
        selected_number.append(place)
        
for place in range(0, len(line3)):
    if place == random.randint(1,valores):
        selected_number.append(place)
        
for place in range(0, len(line4)):
    if place == random.randint(1,valores):
        selected_number.append(place)
        
#mostrar jogo(debug mode)
print(selected_number)
print(line1)
print(line2)
print(line3)
print(line4)

##mostrar jogo
print(*line1)
print(*line2)
print(*line3)
print(*line4)
print('-------------------------------')
        
#loop caso exploda ou não
while explodiu == 0:
    
    #coordenada vertical selecionada (lista expecifica selecionada)
    local_selecionado = int(input('digite o numero da linha >'))

    #aderir a lista escolhida
    lista_selecionada = None

    match local_selecionado:
        case 1: 
            lista_selecionada = line1
        case 2:
            lista_selecionada = line2
        case 3:
            lista_selecionada = line3
        case 4:
            lista_selecionada = line4
            
    #coordenada horizontal selecionada (local expecifico na lista selecionada)
    local_selecionado2 = int(input('digite o numero da coluna >'))

    #loop que compara cada coluna da lista selecionada com as casas que possuem bomba
    for i in lista_selecionada:
        
        #verificação se é uma bomba, caso sim, o jogo acaba
        if local_selecionado2 == selected_number[local_selecionado-1]:
            
            #mudar icone para bomba
            lista_selecionada[local_selecionado2-1] = '💣'
            
            #mostrar tabela atual
            match local_selecionado:
                case 1:
                    print(*lista_selecionada)
                    print(*line2)
                    print(*line3)
                    print(*line4)
                case 2:
                    print(*line1)
                    print(*lista_selecionada)
                    print(*line3)
                    print(*line4)
                case 3:
                    print(*line1)
                    print(*line2)
                    print(*lista_selecionada)
                    print(*line4)
                case 4:
                    print(*line1)
                    print(*line2)
                    print(*line3)
                    print(*lista_selecionada)
            print('----------------------')
            
            #aviso de fim de jogo
            print('----------bomba----------')
            print('-------------------------')
            print(f'Voce fez {pontos} pontos!!')
            
            #mostrar para o codigo que ele caiu em uma bomba
            explodiu = 1
            
            
            break
        else:# caso não seja
            print('não é bomba')
            
            #aumentar numero de pontos caso não haja bomba
            pontos +=1
            
            #excluir casa selecionada que não é bomba
            lista_selecionada[local_selecionado2-1] = '🟦' 
            
            #mostrar tabela atual
            print('----------------------')
            match local_selecionado:
                case 1:
                    print(*lista_selecionada)
                    print(*line2)
                    print(*line3)
                    print(*line4)
                case 2:
                    print(*line1)
                    print(*lista_selecionada)
                    print(*line3)
                    print(*line4)
                case 3:
                    print(*line1)
                    print(*line2)
                    print(*lista_selecionada)
                    print(*line4)
                case 4:
                    print(*line1)
                    print(*line2)
                    print(*line3)
                    print(*lista_selecionada)
            print('----------------------')
            break
            
print('!!!!!!!!!! fim de jogo !!!!!!!!!!!')
