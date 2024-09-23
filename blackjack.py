import random

def crear_baraja():
    palos = ['Corazones', 'Diamanates', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    baraja = [(valor, palo) for palo in palos for valor in valores]
    random.shuffle(baraja)
    return baraja

#Funcion para calcular el valor de una mano de cartas
def valor_mano(mano):
    total = 0
    ases = 0
    
    for carta in mano:
        valor = carta[0]
        if valor in ['J', 'Q', 'K']:
            total += 10
        elif valor == 'A':
            total += 11
            ases += 1
        else:
            total += int(valor)
            
    # Ajustar el valor del As si el total supera 21
    while total > 21 and ases:
        total -= 10
        ases -= 1
        
    return total

#Funcion para mostrar las cartas de una mano
def mostrar_mano(mano, jugador = True):
    #Muestra la mano del jugador o de la computadora
    if jugador:
        print("Tu mano: ", mano)
    else: 
        print("Mano de la computadora: ", mano)

#Turno del jugador
def turno_jugador(baraja, mano_jugador):
    #Pide cartas hasta que decida plantarse o se pase de 21
    #False = se pasa, True = si sigue en el juego
    while True:
        mostrar_mano(mano_jugador)
        valor = valor_mano(mano_jugador)
        print(f"Tu puntaje: {valor}")
        
        if valor > 21:
            print("Te pasaste de 21! Pierdes.")
            return False
        
        decision = input("¿Deseas pedir otra carta? (s/n): ").lower()
        if decision == 's':
            mano_jugador.append(baraja.pop())
        else:
            break
        
    return True

#Turno de la computadora
def turno_computadora(baraja, mano_computadora):
    while valor_mano(mano_computadora) < 17:
        mano_computadora.append(baraja.pop())
        
    mostrar_mano(mano_computadora, jugador=False)
    print(f"Puntaje de la computadora: {valor_mano(mano_computadora)}")
    
#Determinar el ganador
def determinar_ganador(mano_jugador, mano_computadora):
    #Compara las manos del jugador y la computadora y dermina el ganador
    valor_jugador = valor_mano(mano_jugador)
    valor_computadora = valor_mano(mano_computadora)
    
    if valor_computadora > 21:
        print("La computadora se paso de 21. ¡Ganas!")
    elif valor_jugador > valor_computadora:
        print("¡Ganaste! 😀")
    elif valor_jugador < valor_computadora:
        print(" Perdiste 😢")
    else:
        print("Empate 🏳️")
        
# Función para jugar una ronda de Blackjack
def ronda_blackjack():
    baraja = crear_baraja()
    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_computadora = [baraja.pop(), baraja.pop()]

    print("\nBienvenido al Blackjack\n")

    # Turno del jugador
    if turno_jugador(baraja, mano_jugador):
        # Si el jugador no se pasa, turno de la computadora
        turno_computadora(baraja, mano_computadora)
        # Determinamos el ganador
        determinar_ganador(mano_jugador, mano_computadora)
    


#Funcion principal para jugar
def jugar_blackjack():
    while True:
        ronda_blackjack()
        decision = input("\n¿Deseas volver a jugar? (s/n): ").lower()
        if decision != 's':
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        
#Ejecutar el juego
if __name__ == "__main__":
    jugar_blackjack()