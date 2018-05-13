m = input('How much do you need to give money? : ')

def money(m):
    if m <= 0:
        return 'you are a debtor'
    elif m - int(m) != 0:
        M = m - int(m)
        return 'no such money — ' + str(M)
    else:
        a = m / 50
        b = m % 50 / 10
        c = m % 50 % 10 / 5
        d = m % 50 % 10 % 5
        return 'Number of coins: '+ '50kopecks—' + str(a) + ', 10kopecks—' + str(b) + ', 5kopecks—' + str(c)\
               + ', 1kopecks—' + str(d)

print(money(m))