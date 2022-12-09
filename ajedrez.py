import ajedrez 
import os
import time as t
import subprocess as s
def partida_ajedrez(nombre_fichero):
    tablero =[]
    tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
    print(tablero)
    for i in tablero_inicial.split('\n'):
        tablero.append(i.split('\t'))
    f = open(nombre_fichero, 'w')
    for i in tablero:
        f.write('\t'.join(i) + '\n')
    f.close()

    def tablero():
        Empezar = input ("Empezar |S| si, |N| no: ")
        if Empezar == "s":
            bool = True
        else:
            print("adios")
            t.sleep(1)
    while True:
        try:
            movimientos_legales = tablero.movimientos_legales
            jugada = input("jugada: ")

            movimiento =+1
            if movimiento ==2:
                f.write("Movimiento" + str(movimiento) + '\n')
                movimiento = 0
            if jugada == "movimientos_legales":
                print("\nEstas son las jugadas legales que puedes realizar en este momento: \n {}".format(movimientos_legales))
            if jugada == "delvolver":  # devueve la jugada al escribir delvolver
                tablero.pop()
            if jugada == "salir":
                t.sleep(0,30)
                f.close()
                Bool = False
            print(tablero) # imprime el tablero actual en pantalla
        except:
            print("\n Jugada invalida\n")
            print("\n{}".format(tablero))
    
    
partida_ajedrez('partida1.txt')  
            

