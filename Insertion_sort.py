List = [2, 1, 4, 3]

for i in range(1, len(List)):
        x = List[i]
        j = i - 1
        while j >= 0 and List[j] > x:
            List[j + 1] = List[j]
            j -= 1
        List[j + 1] = x

print(List)