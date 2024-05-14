import time

def linesrch(list, value):
    inicio = time.time()
    for i in range(len(list)):
        if list[i] == value:
            fim = time.time()
            cronometro = fim - inicio
            return f'O valor {value} foi encontrado na posição {i} da lista em {cronometro:.2f} segundos'
    return f'O valor {value} não foi encontrado na lista'

def binarysrch(list, value):
    inicio = time.time()
    left = 0
    right = len(list) - 1
    
    while left<right:
        mid = (left+right)//2
        
        if list[mid]==value:
            fim = time.time()
            cronometro = fim - inicio
            return f'O valor {value} foi encontrado na posição {mid} em {cronometro:.2f} segundos'
        
        elif list[mid]<value:
            left = mid + 1
            
        else:
            right = mid - 1        
    
    return f'O valor {value} não foi encontrado na lista'