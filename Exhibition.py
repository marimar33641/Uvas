from sys import stdin

def main():
    numeroCasosPrueba = int( stdin.readline() )
    for i in range( numeroCasosPrueba ):
        numeroAmigos = int( stdin.readline() )
        listEstampas = []
        repetidos = {}
        cont = 0
        for _ in range( numeroAmigos ):
            estampas = list( map( int, stdin.readline().split( " " ) ) )[ 1: ]
            repetidosXColumna = []
            for j in estampas:
                if j in repetidos and not j in repetidosXColumna:
                    repetidos[j] += 1
                else:
                    repetidos[j] = 1
                    repetidosXColumna.append( j )
            estampas = list(set(estampas))
            listEstampas.append( estampas )
        for j in repetidos.values():
            if str(j) == str(1):
                cont+=1
        estampasAmigo = 0
        cantidadTotal = 0
        print( f"Case { i + 1 }:", end = '' )
        for j in range( 0, numeroAmigos ):
            for k in range( len( listEstampas[ j ] ) ):
                if repetidos[ listEstampas[j][k]] == 1:
                    estampasAmigo+=1
            ganancia = ( ( estampasAmigo / cont ) * 100 ) - cantidadTotal
            cantidadTotal += ganancia
            print( " %.6lf" % ganancia +"%" ,end = '' )
        print() 
main()