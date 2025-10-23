import random

class Rifa:
        
    def __init__(self, numeros):
        
        self.numeros = numeros

    def sortear(self):
        
        numero_ganador = random.randint(1,101)
        for i in (self.numeros):
            if i == numero_ganador:
                return [True, numero_ganador]
        return [False, numero_ganador]
        
        