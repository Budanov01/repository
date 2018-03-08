# coding=utf-8
List = list(input('введите список '))

for i in range(len(List)):
        x = List[i]
        j = i - 1
        while j >= 0 and List[j] > x:
            List[j + 1] = List[j]
            j -= 1
        List[j + 1] = x

print(List)