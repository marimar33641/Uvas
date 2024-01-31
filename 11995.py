"""
Maria Del Mar Villaquiran Davila
2 de Septiembre
"""
from sys import stdin
def main():
    line = stdin.readline()
    while line != "":
        x, cont1, cont2, cont3 = 0, 0, 0, 0  #La x es para verificar en el caso que no se le inserte ningun elemento y los cont, son banderas en caso de que no se este cumpliendo ya sea una stack, queue o priority queue.
        lista1, lista3 = [], []#La lista1 es la stack y la lista3 seria la priority queue, el cual la hice manual
        lista2 = [] #La lista2 seria la queue
        cases = int (line)
        for i in range(cases):
            datos = list(map(int, stdin.readline().split()))
            intoTheBag, fromTheBag = datos[0], datos[1] #Recibo los datos
            if( intoTheBag == 1 ): #Si inserta un elemento
                #Se las voy agregar a la stack, a la queue y a la prioritu queue
                lista1.append(fromTheBag) 
                lista2.append(fromTheBag) 
                lista3.append(fromTheBag)
            elif( intoTheBag == 2 ): #Si va a sacar un elemento
                lista3.sort( reverse = True ) #Esto lo que hace la priority queue, por ejemplo [1,2,3,4,5] en esto me daria [5,4,3,2,1] por lo que los estaria ordenando por prioridad de cantidad
                if( len(lista1) == 0 ): #Eso se hace cuando no se le ingresa un elemento a la lista, con tan solo verificar 1, se cumple
                    x = 1 #Por lo que la bandera seria = 1
                else:
                    if( lista1[len(lista1)-1] != fromTheBag ): cont1 = 1 #Si el ultimo en la posicion de la stack es diferente al elemento que se desea sacar, pues se sabe que no seria una Stack, ya que es ultimo en entrar, primero en salir(LIFO)

                    if( lista3[ 0 ] != fromTheBag ): cont3 = 1  #Si en la priority queue, el primer elemento es diferente al elemento que se desea sacar, pues se sabe que no seria una priority queue, ya que saldria el primero en entrar, es el primero en salir(FIFO)
                    
                    if( lista2[ 0 ] != fromTheBag  ): cont2 = 1 #Si en la queue, el primer elemento es diferente al elemento que se desea sacar, pues se sabe que no seria una queue
                    lista1.pop() #Elimino el elemento en la Stack para seguir al otro
                    lista2.pop(0) #Elimino el elemento en la posicion 0 de la queue 
                    lista3.sort() #Le hago sort para volverla a ordenar y poder eliminar el elemento que primero entro 
                    lista3.pop()  #Y elimino               
        #Si se cumplen las tres, significa que no es ninguna de las tres
        if( ( cont1 + cont2 + cont3) == 3 or x == 1): print( "impossible" ) #Si las tres banderas dan 3 o la bandera "x" == 1 (es decir, no se le inserto ningun elemento) , significa que no se cumplió ninguna, por lo que si o si debe imprimir "impossible".
        elif( ( cont1 + cont2 + cont3 ) < 2 ): print( "not sure" ) #Si la bandera de una se coloca, significa que no se puede estar seguro de que estructura es
        elif( cont3 == 0 ): print( "priority queue" ) #Si la bandera cont3 == 0, signfica que si se cumplio la condicion que la lista[0] == fromTheBag
        elif( cont2 == 0 ): print( "queue" ) #Si la bandera cont2 == 0, signfica que si se cumplio la condicion que la lista[0] == fromTheBag
        elif( cont1 == 0 ): print( "stack" )  #Si la bandera cont1 == 0, signfica que si se cumplio la condicion que la lista[len(lista1)-1] == fromTheBag.
        line = stdin.readline()         
main()