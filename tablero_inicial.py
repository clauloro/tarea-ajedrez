tablero_inicial = '♜\t♞\t♝\t♛\t♚\t♝\t♞\t♜\n♟\t♟\t♟\t♟\t♟\t♟\t♟\t♟\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\n♙\t♙\t♙\t♙\t♙\t♙\t♙\t♙\n♖\t♘\t♗\t♕\t♔\t♗\t♘\t♖'
VACIO="-"
TORRE="TORRE"
CABALLO="CABALLO"
ALFIL="ALFIL"
REY="REY"
REINA="REINA"
tablero=[[VACIO for i in range(8)]for j in range(8)]
tablero.append(tablero)
tablero [0][0]= TORRE
tablero [0][7]= TORRE
tablero [7][0]= TORRE
tablero [7][7]= TORRE
tablero [0][1]= CABALLO
tablero [0][6]= CABALLO
tablero [7][1]= CABALLO
tablero [7][6]= CABALLO
tablero [0][2]= ALFIL
tablero [0][5]= ALFIL
tablero [7][2]= ALFIL
tablero [7][5]= ALFIL
tablero [0][3]= REY
tablero [7][3]= REY
tablero [0][4]= REINA
tablero [7][4]= REINA
print(tablero)

    
