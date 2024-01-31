"""
Maria Del Mar Villaquiran Davila
7 de agosto 2021
"""

from sys import stdin
from heapq import heappush, heappop
def main():
    cases = int(stdin.readline())
    while cases != 0:
        cola = []
        vals = list(map(int, stdin.readline().split()))
        n, m = vals[ 0 ], vals[ 1 ]
        for i in range(n):
            datos = stdin.readline().split()
            nombre = datos[ 0 ]
            min = int(datos[ 1 ])
            heappush( cola, [min, i, nombre, min] ) #Guardo los datos en la cola de prioridad, de tal forma que el primer elemento sea los minutos, luego la prioridad, el nombre y por ultimo otra de minutos, para asi poder guardar esos minutos e irlos sumando
        for i in range(m):
            aux = heappop( cola ) #aux va a ser el primero en la cola para borrarlo y seguir con el otro
            print( aux[0], aux[ 2 ] ) #Imprime los minutos y el nombre
            aux[ 0 ] += aux[ 3 ] #A los minutos que si cambian (posicion 0 en la cola) se le va a sumar los minutos que hay en la posicion (3) 
            heappush( cola, aux )#Luego se hace un push a la cola del aux, por el cambio que se hizo en min
        cases -= 1
main()