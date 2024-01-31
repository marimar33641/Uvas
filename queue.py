from sys import stdin 

def main():
    t = int(stdin.readline())
    Cases = 1
    while t != 0:
        valsT = {}
        queue = []
        pos1 = []
        maxi = []
        for i in range(0, t ):
            vals = stdin.readline().split()#3 101 102 103
            n = int(vals[0]) #3
            maxi.append(n)
            pos1 = [ [] for j in range(0, 1000) ]
            for j in range( len(vals[1:]) ):
                valsT[vals[1:][j]] = i # {'101': 0, '102': 0, '103': 0, '201': 1, '202': 1, '203': 1}
        vals2 = stdin.readline().split()
        print(f"Scenario #{Cases}")
        while vals2[0] != "STOP":
            if vals2[0] == "ENQUEUE":
                if str(vals2[1]) in valsT.keys():
                    if valsT[str(vals2[1])] not in queue:
                        queue.append(valsT[str(vals2[1])])
                    pos1[valsT[str(vals2[1])]].append(str(vals2[1]))
            else:
                if( len(queue) > 0 ):
                    print(pos1[queue[0]].pop(0))
                    if len( pos1[queue[0]] ) == 0:
                        queue.pop(0)
            vals2 = stdin.readline().split()
        print()
        valsT = {}
        t = int(stdin.readline())
        Cases+=1
main()