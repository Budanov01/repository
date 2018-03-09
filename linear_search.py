# coding=utf-8
List = list(input('введите сисок '))
x = input('введите искомый ключ ')

def search(List, x):
    for i in range(len(List)):
        if List[i] == x:
            return 'element under number' + str(i)
    return 'no search'

print(search(List, x))