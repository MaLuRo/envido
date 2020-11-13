
import random

class Mazo_de_Truco:

    def __init__(self):
        """metodo constructor que genera el mazo de truco"""
        self.palos = ("Oro", "Basto", "Espada", "Copa")
        self.numeros = (1,2,3,4,5,6,7,10,11,12)
        self.baraja = []
        for palo in self.palos:
            for num in self.numeros:
                carta = (palo, num)
                self.baraja.append(carta)

    def barajar(self):
        """metodo para barajar la copia del mazo"""
        self.baraja_truco = self.baraja[:]
        random.shuffle(self.baraja_truco)
        

    def repartir(self):
        """metodo para repartir 3 cartas a cada jugador"""
        self.cartas =[]
        for i in range(3):
            self.cartas.append(self.baraja_truco.pop(0))
        return self.cartas
        




                        
class Jugador:
    
    def __init__(self):
        self.jugadorH = jugadorH
        
        
    def mostrar(self):
        """solo para verificar que repartir() llego a clase Jugador"""
        return self.jugadorH
        
        
        
        
        

    def contar_envido(self):
        """metodo para contar el envido"""
        self.dic_palos = {"Oro":[], "Basto":[], "Copa":[], "Espada":[]}
        suma = 0
        for palo,valor in self.jugadorH:
                for palo_dic in self.dic_palos:
                        if palo == palo_dic:
                                if valor >= 10:
                                        self.dic_palos[palo_dic].append(0)
                                else:
                                        self.dic_palos[palo_dic].append(valor)
                                        
        for palo,valor in self.dic_palos.items():
                if len(valor) >= 2:
                        suma += 20
                        for i in valor:
                            suma += i
                            self.envido = palo,suma
                elif len(valor) == 1:
                        for i in valor:
                            if i > suma:
                                suma = i
                                self.envido = palo,suma
        


                    
        return self.envido

 
        
        
    

    
"""        
    def jugar():
      pass  

class Tablero_de_puntos():
    def __init__(self):

    def calcular_ganador(self):
        
    def exhibir_tablero(self):

    def declarar_ganador(self):
"""

#Programa Principal
print("Juguemos al Envido")
mazo = Mazo_de_Truco()
mazo.barajar()
jugadorH = mazo.repartir()
jugadorIA = mazo.repartir()
jugador1 = Jugador()
print(jugador1.mostrar())
print(jugador1.contar_envido())





""""
While ( puntos_jugador_1 < 15 or puntos_AI 
calcular_ganador()
exhibir_cartas_AI()
exhibir_tablero()
declarar_ganador()
"""
