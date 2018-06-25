alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = input('write the word inside two apostrophes ')
key = input('write the key of cipher ' )
new_word = []

def cipher_of_Caesar(word, key, new_word, alphabet):
    for i in range(len(word)):
        for j in range(len(alphabet)):
            if word[i] == alphabet[j]:
                new_word.append(alphabet[j+key])
    WORD = ''.join(new_word)
    return(WORD)

print(cipher_of_Caesar(word, key, new_word, alphabet))
