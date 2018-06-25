Founding_Fathers = {'Kenneth Eugene Iverson': 'APL',
                    'Walter Bright': 'C++',
                    'John George Kemeny': 'BASIC',
                    'Larry Wall': 'Perl',
                    'Dennis MacAlistair Ritchie': 'B, C, BCPL',
                    'Don Syme': 'F#',
                    'Alfred Vaino Aho': 'AWK',
                    'Seymour Papert ': 'Logo',
                    'Randall Hyde': 'HLA',
                    'John McCarthy': 'Lisp',
                    'James Lyon': 'INTERCAL',
                    'Guido van Rossum': 'Python',
                    'Richard Hickey': 'Clojure',
                    'Barbara Liskov': 'CLU',
                    'Konrad Zuse': 'Plankalkul'}

Word = input('write name or language inside two apostrophes ')


#formation of the list of found people
def s(Founding_Fathers, Word):
    List = []
    for k,v in Founding_Fathers.items():
        if k.find(Word) != -1:
            L = [k,':',v]
            List.append(L)
        elif v.find(Word) != -1:
            L = [k,':',v]
            List.append(L)
        return('no found')
    n = 1                              # <- sort the list by name
    while n < len(List):
        for i in range(len(List) - n):
            if List[i] > List[i + 1]:
                List[i], List[i + 1] = List[i + 1], List[i]
        n += 1
    List1 = []                         # <- output of information from a new line
    for j in range(len(List)):
        elem = ' '.join(List[j])
        List1.append(elem)
    for l in range(len(List1)):
        print(List1[l])

print(s(Founding_Fathers, Word))
