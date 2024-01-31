from sys import stdin
from heapq import heappush, heappop
import math

#Codigo basico de la estructura general para resolver el problema
#Algoritmo de prim tomado de Carlos Ramirez de la clase. Complementado se toma codigo de Prim de arboles y grafos.
#Luego se calcula en la funcion dist la distancia entre dos puntos.
c, p = [0 for i in range(55)], [0 for i in range(55)]

def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def prim( grafo, s, n ):
    queue = []
    visited = [False for i in range(n)]
    for i in range(n):
        c[i] = float("inf")
        p[i] = -1
    total = 0
    c[s] = 0
    heappush(queue, (0,s))
    while len(queue) > 0:
        peso, u = heappop(queue)
        visited[u] = True
        if peso == c[u]:
            total+= peso
            for (v, pesoAux) in grafo[u]:
                if not visited[v] and pesoAux < c[v]:
                    p[v] = u
                    c[v] = pesoAux
                    heappush(queue, (c[v], v))

def main():
    t = int(stdin.readline())
    G = []
    for _ in range(t):
        numberRofT = int(stdin.readline())
        x, y = list(map((int, stdin.readline().split())))
        while x != -1:
            for i in range(x):
                for j in range(y):
                    x1, y1 = x[i], y[j]
                    x2, y2 = x[j], y[j]
                    dis = dist( x1, y1, x2, y2 )
                    G[i].append( ( j, dis ) )
                    G[j].append( ( i, dis ) )
            prim( G, 0, numberRofT )
            x, y = list(map((int, stdin.readline().split())))
   
main()