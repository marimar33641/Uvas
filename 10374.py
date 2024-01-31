from sys import stdin
from operator import itemgetter
"""
Maria Del Mar Villaquiran Davila
7 de agosto 2021 - 4 de Septiembre
"""

def main():
    cases = int(stdin.readline())
    lista3 = []
    while cases != 0:
        lista = []
        listaCandidatos = {}
        lista2 = []
        if stdin.readline() != "": #Espacio en la segunda linea
            candidatos = int(stdin.readline()) #Cantidad de candidados
            for i in range( candidatos ): 
                nombreCandidato = stdin.readline().strip()
                nombrePartido = stdin.readline().strip()
                lista2.append( nombreCandidato )
                listaCandidatos[ nombreCandidato ] = [ 0, nombrePartido ]
            votos = int( stdin.readline() )
            for i in range( votos ):
                nombresEscogidos = stdin.readline().strip()
                lista.append( nombresEscogidos )
            for i in lista:#['John Smith\n', 'Marilyn Manson\n', 'Marilyn Manson\n', 'Jane Doe\n', 'John Smith\n', 'Marilyn Manson\n']
                for j in lista2:
                    if i == j:
                        listaCandidatos[i][0] += 1 #contador de veces que se encuentra
        listaCandidatos_ = sorted( listaCandidatos.items(), key = itemgetter(1), reverse=True )  
        if(listaCandidatos_[0][1][0] != listaCandidatos_[1][1][0] ): #Verifico que los votos no sean iguales
            a = listaCandidatos_[0][1][1]
            lista3.append(a)     
        else:
            a = "tie"
            lista3.append(a)
        cases -=1
    l = 0
    while l < ( len(lista3) - 1 ): #Corregir el salto de linea de mas
        print( str( lista3[l] ) + "\n" )
        l += 1
    print( lista3[l] )
    lista3 = []
main()