import tablero_inicial
import chess 
import os
import time as t
import subprocess as s
board= chess.Board()
print(board)

def ClearScreen():  

    movimiento_inicial = 0

    Empezar = input ("Empezar |S| si, |N| no: ")
    if Empezar == "s":
        f = open("tablero_inicial","w")
        juego="juego"
        if juego():
            input('Introduce la fila de la pieza a mover: ')
            fila_origen = int()
            input('Introduce la columna de la pieza a mover: ')
            columna_origen = int()
            input('Introduce la fila de destino: ')
            fila_destino = int()
            input('Introduce la columna de destino: ')
            columna_destino = int()
        
            board[fila_destino-1][columna_destino-1] = board[fila_origen-1][columna_origen-1]
            board[fila_origen-1][columna_origen-1] = '-'
            
            movimiento += 1
           
            f = open("tablero_inicial", 'w')
            
            f.write('Movimiento' + str(movimiento) + '\n')
    
            for fila in board:
                f.write('\t'.join(fila) + '\n')
            f.close()
        
        else:
                print("adios")
                t.sleep(1)
                while True:
                    try:
                        jugada = input("Jugada: ")
                        if jugada == "exit":
                            t.sleep(0,30)
                            f.close()
                        print(board)    # imprime el tablero actual en pantalla
                        #detector de jaque mate
                        if board.is_checkmate():
                            print("---------\nJAQUE MATE \n --------")
                            t.sleep(1)
                            pregunta = input ("Quieres repetir la partida? |S| si,|N| no:")
                            if pregunta == "s":
                                board = chess.Board()
                    
                            elif pregunta == "n":
                                print("vale hasta la proxima")
                                t.sleep(1)
                                f.close()
                            else:
                                print("opcion no valida")
                        #si se escribe se reinicia el juego
                        if jugada == "restart":
                            board = chess.Board()
                            print(board) 
                    except:
                        print("\nJugada invalida\n")
                        print("\n{}".format(board))
    
       

        
        
        