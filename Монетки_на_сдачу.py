# coding=utf-8
m = input('Сколько нужно дать сдачи? : ')

def money(m):
    a = m / 50
    b = m % 50 / 10
    c = m % 50 % 10 / 5
    d = m % 50 % 10 % 5
    return 'Кол-во монет: '+ '50коп.—' + str(a) + ', 10коп.—' + str(b) + ', 5коп.—' + str(c)  + ', 1коп.—' + str(d)

print(money(m))

