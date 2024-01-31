#C - Growing Trees

from sys import stdin
#PROGRAMACION DINAMICA CON MEMORIZACION
#Complejidad temporal es lineal O(n)
#Complejidad espacial es lineal O(n) Ya que se necesita n posiciones en la memoria

def fib_memo(n, mem):
    ans = None
    if n in mem: ans = mem[n] 
    else:
        if n<=1: ans = n
        else: ans = fib_memo(n-2, mem) + fib_memo(n-1, mem)
        mem[n] = ans 
    return ans

def main():
    n = int(stdin.readline())
    while n != 0:
        print(fib_memo( n, {} ))
        n = int(stdin.readline())

main()