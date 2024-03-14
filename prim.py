from numpy import zeros
def matriz_a_diccionario(matriz):
    #regresa un diccionario con las aristas como clave y el peso como valor
    diccionario = {}
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != 0:
                diccionario[(i+1,j+1)] = matriz[i][j]#estructura de los elementos en el diccionario(i,j):v
    return diccionario

def prim(matriz):
	X=[1]#conjunto de vertices
	Ck={}#conjunto de aristas posibles en cada iteracion
	A=[]#conjunto de aristas del arbol minimo
	for k in range(1,len(matriz)):#iteramos n-1 veces
		for i,j in matriz_a_diccionario(matriz).items():#agregar los que solo tengan un extremo en X, i es la arista y j es su peso
			if (i[0] in X) and (i[1] not in X):
				Ck[i]=j
			if (i[1] in  X) and (i[0] not in X):
				Ck[i]=j
		a=min(Ck.items(), key=lambda x: x[1])#arista con el valor mas pequeño a=((i,j),v)
		Ck={}
		A.append(a[0])
		if a[0][0] in X:#ingresar el vertice nuevo
			X.append(a[0][1])
		else:
			X.append(a[0][0])
	arbol_minimo=zeros((len(matriz),len(matriz)))#matriz de ceros con dimensiones de la original
	for i,j in A:
		arbol_minimo[i-1][j-1]=matriz_a_diccionario(matriz)[(i,j)] #ingresamos los pesos de las aristas del arbol de peso minimo
	return arbol_minimo

def peso(matriz):
	suma=0
	for i in matriz:
		suma+=sum(i)
	return suma
	
matriz = [[0,20,0,35,30,0,0,0,0],
              [0,0,7,0,18,9,0,0,0],
              [0,0,0,0,0,20,0,0,0],
              [0,0,0,0,15,0,25,0,0],
              [0,0,0,0,0,11,12,15,25],
              [0,0,0,0,0,0,0,0,4],
              [0,0,0,0,0,0,0,22,0],
              [0,0,0,0,0,0,0,0,20],
              [0,0,0,0,0,0,0,0,0]]

print(prim(matriz))
print(f'El peso del arbol minimo es {peso(prim(matriz))}')
