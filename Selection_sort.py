List = [300, 800, 22]

n = 0
while n < len(List) - 1:
    m = n
    i = n + 1
    while i < len(List):
        if List[i] < List[m]:
            m = i
        i += 1
    t = List[n]
    List[n] = List[m]
    List[m] = t
    n += 1

print(List)