class KataBolos:
    def __init__(self):
        self.lanzamientos = [] 

    def tirada(self, bolos):
        if not isinstance(bolos, int):
            raise TypeError("Solo se permiten números enteros en las tiradas de mi bolera")
        if bolos < 0 or bolos > 10:
            raise ValueError("El número de bolos debe estar entre 0 y 10")
        if len(self.lanzamientos) > 20:
            raise ValueError("Se ha excedido el número máximo de lanzamientos en la partida")
        self.lanzamientos.append(bolos)



    def puntuacion(self):
        result = 0
        lanzamientoIndex = 0
        for frame in range(10):
            if self.is_strike(lanzamientoIndex):
                result += 10 + self.strike_bonus(lanzamientoIndex)
                lanzamientoIndex += 1
            elif self.is_spare(lanzamientoIndex):
                result += 10 + self.spare_bonus(lanzamientoIndex)
                lanzamientoIndex += 2
            else:
                result += self.sum_of_balls_in_frame(lanzamientoIndex)
                lanzamientoIndex += 2
        return result

    def is_strike(self, lanzamientoIndex):
        return lanzamientoIndex < len(self.lanzamientos) and self.lanzamientos[lanzamientoIndex] == 10

    def is_spare(self, lanzamientoIndex):
        return lanzamientoIndex + 1 < len(self.lanzamientos) and self.lanzamientos[lanzamientoIndex] + self.lanzamientos[lanzamientoIndex + 1] == 10

    def strike_bonus(self, lanzamientoIndex):
        bonus = 0
        if lanzamientoIndex + 1 < len(self.lanzamientos):
            bonus += self.lanzamientos[lanzamientoIndex + 1]
        if lanzamientoIndex + 2 < len(self.lanzamientos):
            bonus += self.lanzamientos[lanzamientoIndex + 2]
        return bonus

    def spare_bonus(self, lanzamientoIndex):
        return self.lanzamientos[lanzamientoIndex + 2] if lanzamientoIndex + 2 < len(self.lanzamientos) else 0

    def sum_of_balls_in_frame(self, lanzamientoIndex):
        if lanzamientoIndex >= len(self.lanzamientos):
            return 0
        return self.lanzamientos[lanzamientoIndex] + (self.lanzamientos[lanzamientoIndex + 1] if lanzamientoIndex + 1 < len(self.lanzamientos) else 0)
