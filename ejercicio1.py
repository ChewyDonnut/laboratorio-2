import random 
matriz1=[]
matriz2=[]
#b=random.randint(2,5)
#a=random.randint(2,5)
a=1
b=2
for i in range(a):
    aux=[]
    aux2=[]
    fila=int(input("ingrese  fila 1\n"))
    cola=int(input("ingrese  fila 2\n"))
    aux.append(fila)
    aux2.append(cola)
    for j in range(b):
        fil=int(input("ingrese columna de  1\n"))
        col=int(input("ingrese columna de  2\n"))
        aux.append(fil)
        aux2.append(col)
        
        matriz1.append(aux)
        matriz2.append(aux2)
matriz3=[]
for i in range(a):
    aux3=[]
    suma=0
    for j in range(b):
        suma+=0
        suma=(matriz1[i][j]-matriz2[i][j])
        aux3.append(suma)
    matriz3.append(aux3)    
print(matriz1)    
print("\n")
print(matriz2)
print("\n")
print(matriz3)