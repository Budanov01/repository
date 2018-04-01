# coding=utf-8
h = input('height: ')


def pyramida(h):
    if h < 1:
        print('Высота не может быть маленькой')
    elif h > 23:
        print('Это слишком большая высота')
    elif h - int(h) != 0:
        print('Высота должна целым числом')
    else:
        a = [[' '] * (h + 1) for i in range(h)]
        for i in range(h):
            for j in range(h + 1):
                if i <= j:
                    a[i][j] = '#'
                elif i > j:
                    a[i][j] = ' '
        for row in a.__reversed__():
            print(' '.join([str(elem) for elem in row]))


print(pyramida(h))