from sys import stdin 
def main():
    queue = []
    c = int(stdin.readline())
    for _ in range(c):
        n, t, m = list(map(int, stdin.readline().split())) #m lineas, t tiempo, n carros 
        for j in range(0, m):
            vals = int(stdin.readline())
            queue.append(vals)
        totalTime = int(queue[-1])
        minimumTrips = 0
       #Input: 3 10 136
       #Output: 2193 46
        if( m % n == 0 ):
            minimumTrips = m/n
        else:
            minimumTrips = (m // n) + 1
        print( totalTime + t, int(minimumTrips) )
main()