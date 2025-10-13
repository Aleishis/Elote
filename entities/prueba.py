

condicion = True

frase = input("Ingresa un palindromo: ").replace(" ", "")


for i in range(len(frase)):
            
    if frase[i] != frase[len(frase) - i - 1]:
        condicion = False
    
if condicion:
    print("Si es palindromo")
else:
    print("No es un palindromo")
