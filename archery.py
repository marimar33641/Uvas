#Misma estructura del backtracking visto en clase
from sys import stdin
import sys
import queue

sys.setrecursionlimit(1000000)
solution = queue.Queue()
minLen = float('inf')

def solve(scores, value, sols):
    global solution, minLen
    if len(sols) < minLen and value == 0:
        minLen = len(sols)
        solution.put(list(sols))
        if (solution.qsize()) > 1:
            solution.get()
    else:
        if (value >= 0 and len(sols) < minLen):
            for i in range(0, len(scores)):
                solve(scores, value - scores[i], sols + [scores[i]])
     
def main():
    global solution, minLen
    t = int(stdin.readline().strip())
    numberCases = 1
    for _ in range(t):
        n, s = map(int, stdin.readline().strip().split())
        scores = list(map(int, stdin.readline().strip().split()))
        scores.sort(reverse=True)
        solve( scores, s, [])
        if solution.qsize() == 0:
            print(f'Case {numberCases}: impossible')
        else:
            res = solution.get()
            print(f'Case {numberCases}: [{(len(res))}]', *res)
        solution = queue.Queue()
        minLen = float('inf')
        numberCases += 1

main()