import random
#Clase llamada metodo80, porque dicho metodo tiene una probabilidad de ganar de mas del 80%
class Metodo80:

    #Constructor de la clase metodo80
    def __init__(self, ganadores):
        self.ganadores = ganadores

    #Metodo que verifica si el numero ganador esta entre los numeros apostados
    def encuentraGanador(self, ganador):
        l = self.ganadores
        gano = False
        for x in l:
            if ganador == x:
                gano = True
                break
        return gano

#Metodo main del programa
if __name__ == '__main__':
    dineroInicial = 1000 #Dinero con el que inicias a jugar
    dinero = 1000 #Dinero que se apostara en el juego
    apuesta = 5 #Apuesta minima que requiere el metodo 
    numJuegos = 5 #El numero de veces que se jugara al juego
    numJuegosAux = 0 #Numero de veces que se jugo a la ruleta antes de que ya no se pueda apostar
    l = [1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] #lista de numeros a los que se apostaran
    estrategia = Metodo80(l)
    puedeJugar = True #variable que nos indica si alguien puede seguir jugando

    #Ciclo while que siula jugar al juego de la ruleta un numero determinado de veces
    while numJuegos != 0:
        if dinero >= (apuesta * 5):
            ganador = random.randrange(36)
            gano = estrategia.encuentraGanador(ganador)
            if gano:
                dinero = dinero + apuesta
            else:
                dinero = dinero - (apuesta*5)

            numJuegos = numJuegos - 1
        else:
            numJuegos = numJuegos - 1
            puedeJugar = False
            numJuegosAux = numJuegos
            break

    if puedeJugar:
        if dineroInicial < dinero:
            dineroFinal = dinero - dineroInicial
            mensajeFinal1 = 'Ganaste ' +str(dineroFinal)+ ' pesos'
            print(mensajeFinal1)
        else:
            dineroFinal = dineroInicial - dinero 
            mensajeFinal2 = 'Perdiste ' + str(dineroFinal)+ ' pesos'
            print(mensajeFinal2)
    else: 
        mensaje = 'jugaste ' + str(numJuegosAux) + ' juegos y te quedan ' + str(dinero) + ' pesos'
        print(mensaje)
