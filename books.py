from sys import stdin

def calculateSum(p, mid):
    divisiones = 0
    sumaActual = 0
    for x in range(len(p)):
        sumaActual += p[x]
        if sumaActual > mid:
            divisiones += 1
            sumaActual = p[x]
    return divisiones

def solve(p, k):
    low = 0
    high = sum(p)
    while low < high:
        mid = (low + high) // 2
        divisiones = calculateSum(p, mid)
        divisiones += 1
        if divisiones <= k:
            high = mid
        else:
            low = mid + 1
    return low

def distributeScribers(p, k):
    maxBooks = solve(p, k)
    sum = 0
    i = 0
    scribersLeft = k
    first = True
    while i < len(p):
        sum += p[i]
        if sum >= maxBooks and scribersLeft > 1 and not first:
            print("/ ", end = '')
            scribersLeft -= 1
            sum = p[i]
        if i == len(p) - 1:
            print(p[i])
            first = False
        else:
            print(p[i], end = ' ')
            first = False
        i += 1

def main():
    c = int(stdin.readline())
    for _ in range(c):
        vals = stdin.readline().split() 
        m = int(vals[0])
        k = int(vals[1])
        P = list(map(int, stdin.readline().split()))
        distributeScribers(P, k)
main()