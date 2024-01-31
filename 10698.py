"""
6 10
tA
tB
tC
td
tE
tF
tA 1 - 1 tB
tC 0 - 0 td
tE 0 - 0 tA
tC 0 - 0 tB
td 0 - 0 tE
tA 0 - 0 tC
tB 0 - 0 tE
td 0 - 0 tA
tE 0 - 0 tC
tB 0 - 0 td
2 2
Botafogo
Flamengo
Botafogo 3 - 2 Flamengo
Flamengo 2 - 3 Botafogo
5 10
tA
tB
tC
tD
tE
tA 0 - 0 tB
tC 0 - 0 tD
tE 0 - 0 tA
tC 0 - 0 tB
tD 0 - 0 tE
tA 0 - 0 tC
tB 0 - 0 tE
tD 0 - 0 tA
tE 0 - 0 tC
tB 0 - 0 tD
3 2
Quinze-Novembro
Flamengo
Santo-Andre
Quinze-Novembro 6 - 0 Flamengo
Flamengo 0 - 2 Santo-Andre
0 0

"""

"""
Maria Del Mar Villaquiran Davila
9 de agosto 2021
"""

from sys import stdin

def main():
    nE, nP = list(map(int, stdin.readline().split()))
    while ( nE != 0 or nP != 0):
        lista1 = []
        for i in range( nE ):
            """
            Posicion 0 --> Nombre del equipo
            Posicion 1 --> Cantidad de puntos
            Posicion 2 --> Cantidad de juegos que jugó
            Posicion 3 --> Cantidad de goles a favor
            Posicion 4 --> Cantidad de goles en contra
            Posicion 5 --> Diferencia de goles(Posicion 3 - Posicion 4)
            """
            nEquipo = [ stdin.readline().strip() , 0, 0, 0, 0, 0]
            lista1.append(nEquipo)
        for i in range( nP ):
            resultado = stdin.readline().strip().split()
            #print(resultado)
            for j in lista1:
                if( j[ 0 ] == resultado[ 0 ] ): # Nombre de la lista donde esta todo == nombre de la lista del resultado(El primer nombre)
                    if( int(resultado[ 1 ]) == int(resultado[ 3 ]) ): #Comparar los goles (En este caso si son iguales)
                        j[ 1 ] += 1#Si es asi, se le suma 1 punto
                    elif( int(resultado[ 1 ]) > int(resultado[ 3 ]) ):#Comparar los goles (En este caso el primer equipo tiene mas goles que el segundo equipo)
                        j[ 1 ] += 3 #Si es asi, se le suma 3 puntos 
                    j[ 2 ] += 1 #Partidos jugados
                    j[ 3 ] += int( resultado[ 1 ] ) #Se le suma la cantidad de goles que hizo (resultado[1])
                    j[ 4 ] += int( resultado[ 3 ] ) #Se le suma la cantidad de goles en contra (resultado[3])
                    j[ 5 ] = int( j[ 3 ] - j[ 4 ] ) #Diferencia de goles 

                elif(  j[ 0 ] == resultado[ 4 ] ): #[[0, 'tA', 0, 0, 0, 0, 0, 0] == ['tA', '1', '-', '1', 'tB']# Nombre de la lista donde esta todo == nombre de la lista del resultado(El segundo nombre)
                    if( int(resultado[ 3 ]) > int(resultado[ 1 ]) ):#Comparar los goles (En este caso el primer equipo tiene mas goles que el segundo equipo)
                        j[ 1 ] += 3#Si es asi, se le suma 3 puntos 
                    elif( int(resultado[ 3 ]) == int(resultado[ 1 ]) ):#Comparar los goles (En este caso si son iguales)
                        j[ 1 ] += 1 #Si es asi, se le suma 1 punto
                    j[ 2 ] += 1 #Partidos jugados
                    j[ 3 ] += int( resultado[ 3 ] ) #Se le suma la cantidad de goles que hizo (resultado[3])
                    j[ 4 ] += int( resultado[ 1 ] ) #Se le suma la cantidad de goles en contra (resultado[1])
                    j[ 5 ] = int( j[ 3 ] - j[ 4 ] )#Diferencia de goles 
        #print(lista1) 
        lista1.sort( key = lambda x: ( -x[ 1 ], -x[ 5 ], -x[ 3 ], x[ 0 ].lower() ) ) #Ordenamiento con la funcion sort
        l = 0
        for i in range( nE ):
            if( i == 0 or lista1[ i ][ 1 ] != lista1[ i - 1 ][ 1 ] or lista1[ i ][ 3 ] != lista1[ i - 1 ][ 3 ] or lista1[ i ][ 5 ] != lista1[ i - 1 ][ 5 ] ): #Se verifica que la cantidad de puntos, los goles a favor y la diferencia de goles no sea igual al anterior (esto para poder imprimir con el formato que nos pide)
                l+=1
                print( "%2d. "% l, end='' )
            else: #Si son iguales se imprime todos los datos con un formato diferente
                l += 1
                print("    ", end = '' )
            print( "%15s%4d%4d%4d%4d%4d " % ( lista1[ i ][ 0 ], lista1[ i ][ 1 ], lista1[ i ][ 2 ], lista1[ i ][ 3 ], lista1[ i ][ 4 ], lista1[ i ][ 5 ] ), end = '' )
            if( lista1[ i ][ 2 ] == 0 ):#Numero de juegos jugados    3(No tiene juegos)
                print( "%6s" % "N/A" ) #Si no tiene partidos jugados se coloca N/A
            else:
                a = lista1[ i ][ 1 ] / (3.0* lista1[ i ][ 2 ]) * 100 #Porcentaje 
                print( "%6.2f" % a)
        cont = 1
        nE, nP = list(map(int, stdin.readline().split()))
        if nE == 0: #Corregir el salto de linea de mas
            cont = 0
        if( cont != 0 ):
            print()   
main()