# Importante: 
# Reglas del juego:
# - Una partida de bolos consiste en 10 turnos.
# - Cada turno (excepto el último) tiene 2 tiradas para derribar bolos.
# - Si se derriban todos los bolos en la primera tirada (strike), se anota 10 puntos más la suma de los dos siguientes lanzamientos.
# - Si se derriban todos los bolos en dos tiradas (spare), se anota 10 puntos más la suma de los bolos derribados en el siguiente lanzamiento.
# - Si no se derriban todos los bolos en dos tiradas, se anota la suma de los bolos derribados en ambas.
# - En el último turno, se tienen 3 tiradas en total, independientemente de si se consigue un strike o un spare en las dos primeras.

# Test 1: Todos los bolos derribados en un turno normal.
# Test 2: Un strike seguido de dos lanzamientos específicos.
# Test 3: Un spare seguido de un lanzamiento específico.
# Test 4: Una partida perfecta con todos los strikes.
# Test 5: Una partida sin strikes ni spares.
# Test 6: Manejar el último frame con diferentes escenarios.
# Test 7: Validar el número de lanzamientos y frames.
# Test 8: Manejar entradas no válidas (por ejemplo, más de 10 pinos derribados).
# Test 9: Probar diferentes casos de borde (por ejemplo, strikes y spares consecutivos).

import unittest
from Bolos import Bolos

class TestBolos(unittest.TestCase):
        
        # Vamos a diseñar los tests desde lo más general a lo más concreto 
        # Configuración de una partida de bolos (10 rondas) - caráceter general 
        def rondas_partida(self):
                partida = Bolos()
                self.assertEqual(partida.rondas, 10)




         
         
           
          
            
    
        




