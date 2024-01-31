from sys import stdin 

def main():
    queue = [[] for i in range( 2 )]
    c = int(stdin.readline())
    for i in range( 0, c ):
        n, t, m = list(map(int, stdin.readline().split())) #m lineas, t tiempo, n carros
        for j in range( 0, m ):
            vals = stdin.readline().split()
            #print("vals: ", vals)
            if vals[1] == "left":
                queue[0].append( ( j, int(vals[0]) ) )
            else:
                queue[1].append( (j, int(vals[0])) )
        tiempo = 0
        side = 0
        pos1 = [ 0 for j in range(m) ]
        #print("queue: ", queue[0])
        while( len(queue[0]) > 0 or len( queue[1] ) > 0 ):
            if( len( queue[0] ) == 0 ):
                val = queue[1][0][1]
            elif( len( queue[1] ) == 0 ):
                val = queue[0][0][1]
            else:
                #print(queue[0], queue[1])
                val = min( queue[0][0][1], queue[1][0][1] )
            
            tiempo = max( tiempo, val )
            while( len(queue[side]) > 0 and tiempo >= queue[side][0][1] ):
                a = queue[side].pop(0)
                pos1[a[0]] = tiempo+t
            tiempo = tiempo + t
            if( side == 0 ):
                side = 1
            else:
                side = 0
        for j in range(len(pos1)):
            print(pos1[j]) 
main()