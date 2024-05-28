import unittest
import random
from KataBolos import KataBolos

class TestKataBolos(unittest.TestCase):
    # Creo el escenario
    def setUp(self):
        self.partida = KataBolos()
        # Que no hay partidas incompletas
        self.partida_completa()

    def partida_completa(self, bolos=0):
        # Simular una partida de 10 rondas
        for _ in range(20):
            self.partida.tirada(bolos)

    def test_tirada_normal(self):
        self.partida = KataBolos()  # Reiniciar el juego para este test específico
        self.partida.tirada(5)
        self.assertEqual(self.partida.puntuacion(), 5)
        # Completar el juego para reflejar 10 rondas completas
        for _ in range(19):
            self.partida.tirada(0)
    
    def test_pleno_en_dos(self):
        self.partida = KataBolos()  # Reiniciar el juego para este test específico
        self.partida.tirada(7)
        self.partida.tirada(3)
        self.partida.tirada(5)
        # Rellenar con tiros de cero para completar el juego, teniendo en cuenta los ya realizados.
        for _ in range(17):
            self.partida.tirada(0)
        self.assertEqual(self.partida.puntuacion(), 20)

    def test_pleno_y_bonus(self):
        self.partida = KataBolos()  # Reiniciar el juego para este test específico
        self.partida.tirada(10)  # Strike
        self.partida.tirada(3)
        self.partida.tirada(4)
        for _ in range(16):
            self.partida.tirada(0)
        self.assertEqual(self.partida.puntuacion(), 24)

    def test_juego_perfecto(self):
        self.partida = KataBolos()  # Reiniciar el juego para este test específico
        for _ in range(12):  # En un juego perfecto, se lanzan 12 strikes
            self.partida.tirada(10)
        self.assertEqual(self.partida.puntuacion(), 300)
    
    def test_no_entero2(self):
        self.partida = KataBolos()
        with self.assertRaises(TypeError):
            self.partida.tirada("texto")
        self.assertEqual(self.partida.puntuacion(), 0)
    
    def test_no_entero3(self):
        self.partida = KataBolos()
        with self.assertRaises(TypeError):
            self.partida.tirada(3.14)
        self.assertEqual(self.partida.puntuacion(), 0)

    def test_ronda_abierta(self):
        self.partida = KataBolos()
        # Simular una ronda abierta donde el jugador no tira todos los bolos
        self.partida.tirada(5)
        self.partida.tirada(3)
        self.assertEqual(self.partida.puntuacion(), 8)

    def test_spare_ultima_ronda(self):
        self.partida = KataBolos()
        # Simular una última ronda con un spare
        for _ in range(18):
            self.partida.tirada(0)
        self.partida.tirada(5)
        self.partida.tirada(5)
        self.partida.tirada(5)  # Se permite lanzamiento adicional
        self.assertEqual(self.partida.puntuacion(), 15)

    def test_mas_de_10_bolos(self):
        self.partida = KataBolos()
        with self.assertRaises(ValueError):
            self.partida.tirada(11)  # Intentar tirar más de 10 bolos en una ronda
        self.assertEqual(self.partida.puntuacion(), 0)

    def test_jugador_sin_brazos(self):
        self.partida = KataBolos()
        # Simular una ronda donde el jugador no tira ningún bolo
        for _ in range(2):
            self.partida.tirada(0)
        self.assertEqual(self.partida.puntuacion(), 0)

    def test_ultima_ronda_perfecta(self):
        self.partida = KataBolos()
        # Simular 9 rondas completas con lanzamientos de 0
        for _ in range(18):
            self.partida.tirada(0)
        # En la última ronda, la suerte de su vida
        self.partida.tirada(10)  # Strike en el primer lanzamiento de la última ronda
        self.partida.tirada(10)  # Strike en el segundo lanzamiento de la última ronda
        self.partida.tirada(10)  # Strike en el tercer lanzamiento de la última ronda
        self.assertEqual(self.partida.puntuacion(), 30)

    def test_juego_incompleto(self):
        self.partida = KataBolos()
        # Simular una partida incompleta de 7 rondas
        for _ in range(7):
            bolos_1 = random.randint(0, 10)
            bolos_2 = random.randint(0, 10 - bolos_1)
            self.partida.tirada(bolos_1)
            self.partida.tirada(bolos_2)
        self.assertEqual(self.partida.puntuacion(), self.partida.puntuacion())

    def test_partida_vacia(self):
        self.partida = KataBolos()
        self.assertEqual(self.partida.puntuacion(), 0)

    def test_lanzamientos_excedidos(self):
        self.partida = KataBolos()
        # Intentar realizar más lanzamientos de lo normal lanza un error
        with self.assertRaises(ValueError):
            for _ in range(26):
                self.partida.tirada(0)

    def test_bolos_negativos(self):
        self.partida = KataBolos()
        # Intentar realizar una tirada con un número negativo de bolos
        with self.assertRaises(ValueError):
            self.partida.tirada(-5)
        self.assertEqual(self.partida.puntuacion(), 0)







