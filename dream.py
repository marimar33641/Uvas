from sys import stdin

def fun(n, A):
    ans = 0
    for i in n:
        ans += abs(A - i)
    return ans

def binarySearchMin(n, low, hi):
    if low == hi:
        #print("A")
        return low
    else:
        mid = low + ((hi - low) >> 1)
        val = fun(n, n[mid])
        next = fun(n, n[mid - 1]) 
        if next < val:
            #print("B")
            return binarySearchMin(n, low, mid)
        else:
            #print("C")
            next = fun(n, n[mid + 1])
            if next < val:
                return binarySearchMin(n, mid, hi)
            else:
                if mid != low+1:   
                    if fun(n, n[mid - 1]) >= val:
                        #print(fun(n, n[mid-1]), fun(n, n[mid]), fun(n, n[mid+1]), n[mid])
                        #print(fun(n, 16386))
                        return mid
                        
                    else:
                        return binarySearchMin(n, low, mid)

def binarySearchMax(n, val, low, hi):
    if low >= hi:
        return low
    else:
        mid = low + ((hi - low) >> 1)
        next = fun(n, n[mid])
        if next > val:
            return binarySearchMax(n, val, low, mid)
        else:
            if mid < len(n):
                if fun(n, n[mid + 1]) >= val:
                    return mid
                else:
                    return binarySearchMax(n, val, mid, hi)
            return binarySearchMax(n, val, mid, hi)

def solve(n):
    minV = binarySearchMin(n, 0, len(n) - 1)
    maxV = binarySearchMax(n, fun(n, n[minV]), minV, len(n) - 1)
    #print("---", maxV, minV, maxV-minV+1)
    print(n[minV], maxV - minV + 1, n[maxV] - n[minV] + 1)

def main():
    line = stdin.readline()
    while line != "":
        n = []
        for i in range(int(line)):
            vals = int(stdin.readline())
            n.append(vals)
        n.sort()
        solve(n)
        line = stdin.readline()
        #print(fun(n, 16013))
        #print(fun(n, 16326))
        

main()

"""
25
1
3
4
6
7
9
10
11
13
15
17
18
20
23
25
28
29
32
35
38
41
42
46
48
50

"""