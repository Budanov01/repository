sentence = input('what to encrypt: ')
key = input('cipher key: ')

#This program will work correctly only if you write in Caps Look
#character dictionary for encryption
list = []
cipher = []
cipher1 = []
m = len(sentence)//len(key)
n = len(sentence)%len(key)
list.append(key*m)
list.append(key[0:n])

#line encryption
List = ''.join(list)
for i,j in enumerate(sentence):
    c = (ord(j)+ord(List[i]))%26
    C = chr(c + 65)
    cipher.append(C)
    Cipher = ''.join(cipher)
print(Cipher)
