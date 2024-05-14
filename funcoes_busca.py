def linesrch(list, value):
    for i in range(len(list)):
        if list[i] == value:
            return f'O valor {value} foi encontrado na posição {i} da lista'
    return f'O valor {value} não foi encontrado na lista'

def binarysrch(list, value):
    left = 0
    right = len(list) - 1
    
    while left<right:
        mid = (left+right)//2
        
        if list[mid]==value:
            return f'O valor {value} foi encontrado na posição {mid}'
        
        elif list[mid]<value:
            left = mid + 1
            
        else:
            right = mid - 1        
    
    return f'O valor {value} não foi encontrado na lista'