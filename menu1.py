import random
from funcoes_busca import *
from menu3 import menu_org
from menu2 import menu_busca

def menu1():
    while True:
        gen = input('\nTeste de Desempenho\nMenu Inicial\n1 - Gerar lista\n2 - Inserir lista\n3 - Sair\nOque deseja fazer?: ')
        if gen == '1':
            tam = int(input('Quantos numeros deseja gerar?: '))
            data = random.sample(range(-100000000000000,100000000000000), tam)
            print(f'{data}\nEsses serão seus {tam} números.')
            opt = input('\n1 - Procurar na lista\n2 - Organizar lista\n3 - Sair\nOque deseja fazer?: ')   
            if opt == '1':
                menu_busca(data)
            elif opt == '2':
                menu_org(data)
            else:
                pass
        
        elif gen == '2':
            data = []
            dado = input('Digite os valores que deseja inserir: ').split(', ')
            
            for i in dado:
                int(i)
                
                if i in data:
                    gen = input(f'{i} Esse numero já está na lista, deseja inserir mesmo assim?: ')
                    
                    if gen == 'sim':
                        data.append(i)
                    
                    else:
                        pass
                
                else:
                    data.append(i)
            print(f'{data}\nEsses serão seus {len(data)} números.')
            opt = input('\n1 - Procurar na lista\n2 - Organizar lista\n3 - Sair\nOque deseja fazer?: ')    
            if opt == '1':
                    menu_busca(data)
            elif opt == '2':
                    menu_org(data)
            else:
                pass
            
        else:
            print('Você escolheu sair.')
            False

menu1()