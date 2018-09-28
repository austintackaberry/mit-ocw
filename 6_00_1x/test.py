school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0
cons = ""

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        # print(char)
        print('feg')
    else:
        cons += char
        print(numCons)
        numCons -= 1

print(cons)
print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
