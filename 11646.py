from sys import stdin
import math
"""
Maria Del Mar Villaquiran Davila 
28 de Agosto 2021
3 : 2
5 : 4
"""
eps = 1e-12
def main():
    line = stdin.readline()
    cases = 1
    while line != "":
        a, b = [float(a) for a in line.strip().split(":")] #Leer a y b
        low, high = 0, 1000
        line = stdin.readline()
        while( high - low > eps ): #Se hace una cota que es la eps, por lo que cuando high-low > eps pues se va a seguir ejecutando
            mid = ( low + high ) / 2 #Se hace lo del punto medio (mid)
            w = ( b / a ) * mid 
            r =  math.sqrt(( mid / 2 ) * ( mid / 2 ) + ( w / 2 ) * ( w / 2 ) )
            theta = math.acos( mid / ( 2 * r ) )
            arc = 2 * r * theta
            if( 2 * ( arc + mid ) > 400 ): high = mid #Si el arco*2 + mid*2 el punto medio que se va cambiando por el (high+low)  es mayor al perimetro (400) significa que el high va a ser igual al mid (por biseccion)
            else: low = mid #de lo contrario, pues low va a ser igual a mid
        print("Case %d: %.10f %.10f" % ( cases, mid, w ) )
        cases += 1
main()