import random


numeros = [1,2,3]
numeros_ganadores = []
for i in range(3):
    numeros_ganadores.append(random.randint(1,101))
        
    if numeros[i] == numeros_ganadores[i]:
        print('si')
    print('no')