
from menu2 import *
from funcoes_org import *


def menu_org(list):
    dataord = []
    for i in list:
        dataord.append(i)

    escolha = input(
        '\nOpções de organização\n1 - Selection Sort\n2 - Insertion Sort\n3 - Bubble Sort\n4 - Voltar ao menu inicial\nComo deseja organizar a lista?: ')

    if escolha == '1':
        ordenado = selectionSort(dataord)
        opt = input('Deseja buscar algum valor na lista?: ')
        if opt == 'sim':
            menu_busca(ordenado)
        else:
            escolha = 4

    elif escolha == '2':
        ordenado = insertionSort(dataord)
        opt = input('Deseja buscar algum valor na lista?: ')
        if opt == 'sim':
            menu_busca(ordenado)
        else:
            escolha = 4

    elif escolha == '3':
        ordenado = bubbleSort(dataord)
        opt = input('Deseja buscar algum valor na lista?: ')
        if opt == 'sim':
            menu_busca(ordenado)
        else:
            escolha = 4
    else:
        return 

