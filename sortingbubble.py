List = ['a', 'f', 'b', 'a', 'v']
n = 1
while n < len(List):
    for i in range(len(List) - n):
        if List[i] > List[i + 1]:
            List[i], List[i + 1] = List[i + 1], List[i]
    n += 1
print(List)