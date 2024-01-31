from sys import stdin
from heapq import heappush, heappop

def main():
    line = stdin.readline().split()
    while line != []:
        colaPrioridad = []
        instrumentos = list(map(int,stdin.readline().split()))
        cont = 0
        for i in instrumentos:
            tripleta = ( i*-1, i, cont )
            heappush( colaPrioridad, tripleta )
        res = (int(line[0])) - (int(line[1]))
        for i in range( res ):
            if res > 0:
                val = heappop( colaPrioridad ) #Tripleta 0 (-8,8,0)
                if( (( val[1]) % (2+val[2])) == 0 ):
                    new = (( val[1]) // (2+val[2] ))
                else:
                    new = int((val[1] // ( 2+val[2] )) + 1 )
                cont = val[2] + 1
                newTripleta = ( new*-1, val[1], cont )
                heappush( colaPrioridad, newTripleta )
        a = heappop( colaPrioridad )
        print( a[0]*-1)
        line = stdin.readline().split()
main()