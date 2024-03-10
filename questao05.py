cadeiaString = str(input('Digite o texto para inverter: '))
print(cadeiaString)

stringReversa = ''
for n in range(len(cadeiaString)):
    stringReversa += cadeiaString[(len(cadeiaString) - 1) - n]
    print(cadeiaString[(len(cadeiaString) - 1) - n])
    
print(stringReversa)