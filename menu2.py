from funcoes_busca import *
from menu3 import *


def menu_busca(list):
    while True:
        escolha = input('\nOpções de Busca\n1 - Busca Linear\n2 - Busca Binaria\n3 - Voltar\nComo deseja fazer a busca?: ')
        if escolha == '1':
            valor = int(input('Qual valor deseja procurar?: '))
            print(linesrch(list, valor))
            opt = input('Deseja procurar outro valor na lista?: ')
            if opt == 'sim':
                True
            else:
                False
        elif escolha == '2':
            valor = int(input('Qual valor deseja procurar?: '))
            print(binarysrch(list, valor))
            opt = input('Deseja procurar outro valor na lista?: ')
            if opt == 'sim':
                True
            else:
                False        
        else:
            return
