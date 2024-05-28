import unittest
import Partida 

class TestPartidaBolos(unittest.TestCase):

        def testCrearPartidaBolos(self):
               self.partida = Partida() 
        
        def testPartidaNula(self):
                partida = Partida()
                self.bolosPorTirada(0, 20)
                #assert self.partida.score() == 0
                self.assertEqual(self.partida.score(), 0)
        
        def testPartidaTodoUnos(self):
                partida = Partida()
                self.bolosPorTirada(1, 20)
                #assert self.partida.score() == 20
                self.assertEqual(self.partida.score(), 20)

        def testUnSpare(self):
                self.partida.tirada(5)
                self.partida.tirada(5)
                self.partida.tirada(3)
                self.bolosPorTirada(0, 17)
                #assert self.partida.score() == 16
                self.assertEqual(self.partida.score(), 16)
        
        def testUnStrike(self):
                self.partida.tirada(10)
                self.partida.tirada(4)
                self.partida.tirada(3)
                self.bolosPorTirada(0, 16)
                #assert self.partida.score() == 24
                self.assertEqual(self.partida.score(), 24)

        def testPartidaPerfecta(self):
                self.bolosPorTiradas(10, 12)
                #assert self.partida.score() == 300
                self.assertEqual(self.partida.score(), 300)

        def  testTodoSpare(self):
                self.bolosPorTirada(5, 21)
                #assert self.partida.score() == 150
                self.assertEqual(self.partida.score(), 150)
        
if __name__ == '__main__':
        unittest.main()
        





  