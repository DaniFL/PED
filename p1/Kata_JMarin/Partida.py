class Partida:
    def __init__(self):
        self.tiradas = []


    def tirada(self, bolos):
        self.tiradas.append(bolos)
    
    def score(self):
        result = 0
        tiradasIniciales = 0
        for i in range(20):
            if self.esStrike(tiradasIniciales):
                result += self.strikeScore(tiradasIniciales)
                tiradasIniciales += 1
            elif self.esSpare(tiradasIniciales):
                result += self.spareScore(tiradasIniciales) 
                tiradasIniciales += 2
            else:
                result += self.frameScore(tiradasIniciales)
                tiradasIniciales += 2   
        return result
    
    def esStrike(self, tiradasIniciales):
        return self.tiradas[tiradasIniciales] == 10    
    
    def esSpare(self, tiradasIniciales):
        return self.tiradas[tiradasIniciales] + self.tiradas[tiradasIniciales + 1] == 10
    
    def strikeScore(self, tiradasIniciales):
        return 10 + self.tiradas[tiradasIniciales + 1] + self.tiradas[tiradasIniciales + 2]

    def spareScore(self, tiradasIniciales):
        return 10 + self.tiradas[tiradasIniciales + 2]
    
    def frameScore(self, tiradasIniciales):
        return self.tiradas[tiradasIniciales] + self.tiradas[tiradasIniciales + 1]

    def bolosPorTirada(self, bolos, tiradas):
        for i in range(tiradas):
                self.partida.tirada(bolos)
        
    



     





