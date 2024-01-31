from sys import stdin
import math
eps = 1e-12

"""
Maria Del Mar Villaquiran Davila 
27 de Agosto 2021

1
-1 2
2
-8 6 9
0

"""
def main():
    T = int(stdin.readline())
    while T != 0:
        low = -0.99 #El low es -0.99 por el enunciado
        high = 10000 #Y el valor maximo, o sea high que puede tomar es 10000
        CF = list(map(int, stdin.readline().split()))
        while( high - low > eps ): #Se hace una cota que es la eps, por lo que cuando high-low > eps pues se va a seguir ejecutando
            mid = (low+high) / 2#Se hace lo del punto medio (mid)
            NPV = 0
            for i in range( T + 1 ):
                NPV += CF[ i ] / pow( 1 + mid, i ) #Se calcula la formula que nos dice el enunciado
            if( NPV > 0 ): low = mid #Si la formula es mayor a 0, el low pasará a ser el mid, ya que es mayor a 0 NPV
            else: high = mid #De lo contrario high va a ser mid
        print( "%.2f" % mid )
        T = int(stdin.readline())

main()