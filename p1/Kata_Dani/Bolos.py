import random
import TestBolos

class Bolos:
   
    # Constructor 
    def __init__(self):
        self.rondas = 0
        self.puntos = 0

    def jugar_partida(self):
        for ronda in range(self.rondas):
            # Tirada 1
            bolos = random.randint(0, 10)
            self.puntos += bolos
            # Tirada 2
            bolos = random.randint(0, 10)
            self.puntos += bolos
        return self.puntos

    


    


    


    

        



    



    

