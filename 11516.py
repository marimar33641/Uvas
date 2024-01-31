"""
Maria Del Mar Villaquiran Davila
4 de Septiembre 2021
"""
from sys import stdin
def main():
    cases = int(stdin.readline())
    while cases:
        vals = []
        n, m = map(int, stdin.readline().split()) #Se recibe n,m
        for i in range(m):
            vals.append( int(stdin.readline()) )
        vals.sort() #Para que los elementos queden organizado
        low, high = vals[ 0 ], vals[ m - 1 ] #low = a la primera posicion del lista, y high = la ultima posicion de la lista 
        while( low  + 1 < high ):        
            c = 1
            mid = ( high + low ) / 2 #Encuentro el punto medio  
            rango = vals[ 0 ] + mid #Y el rango va a ser el primer elemento y el punto medio
            for i in range( m ):
               if( vals[ i ] > rango ): #Se recorre las posiciones del arreglo y se verifica Si cada elemento del arreglo es mayor al rango calculado
                    rango =  vals[ i ] + mid #De ser asi, el rango pasará a hacer el valor del elemento mas el mid
                    c += 1    #Y cuando lo encontro, pues necesitamos un contador que vaya sumando la cantidad de veces en la que se encuentra, para poder saber si bajar el high o subir el low.
            if( c > n ): #Si las veces en las que se cumplio que el elemento + mid es mayor al rango, es igual a "n" (La cantidad estipulada de puntos de acceso). Si es mayor, pues el low pasará a ser el mid (Se sube el low).
                low = mid
            else:
                high = mid #De lo contrario si no encontro o es menor e igual a "n" (La cantidad estipulada de puntos de acceso), pues el high va a ser mid (se baja el high).
        if( n >= m ):
            print( "%.1f" % ( int( high ) // 2 ) ) #Si la cantidad de accesos es mayor a el numero de casas, pues se hace division entera para que de 0.0
        else:
            print( "%.1f" % ( int( high ) / 2 ) ) #De lo contrario pues se coge el high como entero y se divide / 2, para que no de valores ".x" diferentes. 
        cases -= 1

main()