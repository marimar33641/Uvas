"""
Problem name: As Long as I Learn, I Live
Maria Del Mar Villaquiran Davila
22 de septiembre 2021
15 de octubre del 2021- Parcial 2 practico
"""
from sys import stdin
MAX = 50
visitado = [0 for i in range(MAX)]
adj = [[] for i in range(MAX)] #El grafo creado con tamaño n

#Ya en este si sirve
def main():
    T, x, cases = int(stdin.readline()), 0, 0
    while T != 0:
        stdin.readline()
        vals = []
        n, m = list(map(int, stdin.readline().split())) #Leo el numero de nodos y el numero de aristas
        vals = list(map(int, stdin.readline().split())) #Los valores de cada uno de los nodos
        adj = [[] for i in range(n)] #El grafo creado con tamaño n
        sumaT, nodo = 0, 0 
        for i in range(m):
            u, v = list(map(int, stdin.readline().split()))
            adj[u].append( v ) #Agrego en la matriz adj la posicion u donde haya conexion v, por ejemplo 5 4 (u = 5, v = 4), se agrega en la posicion 5 el elemento 4 y asi con todos
        while( adj[ nodo ] ):
            sumaT += vals[ nodo ] #Le voy sumando lo que esta en la lista donde se les da el valor del nodo
            a = 0
            for i in range(len(adj[nodo])): #Recorro cada posicion de la matriz, es decir [1,2] luego [5]... Y asi
                if( vals[ adj[nodo][i] ] > a ): #Si el valor de la matriz en vals, es decir (8,9,2,7,5(la lista vals)) es mayor a "a" (esto se hace para saber que nodo tenga mayor aprendizaje)
                    w = adj[nodo][i]
                    a =  vals[ w ]
            nodo = w #Ya con la clase de hoy, supongo que es el orden topologico del grafo(ya viendolo en especifico) y con esto pues es el nodo donde se va por el camino con nodos con mayor experiencia.
        cases += 1
        print("Case %d: %d %d" % ( cases, sumaT + a, nodo ))
        T -= 1
main()