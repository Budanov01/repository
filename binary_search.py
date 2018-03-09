# coding=utf-8
A = list(input('введите список '))
key = input('введите искомый ключ ')

def binary_search(A, key):
    left = -1
    right = len(A) 
    while right > left + 1:
        middle = (left + right) // 2 
        if A[middle] >= key: 
            right = middle 
        else: 
            left = middle 
    return 'искомый ключ под номером ' + str(right)

print(binary_search(A, key))