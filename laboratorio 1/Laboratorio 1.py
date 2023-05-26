import random
fila=int(input("ingrese cantidad de filas"))
columnas=int(input("ingrese cantidad de columnas"))
m1=[];m2=[];m3=2
for i in range(columnas):#este ciclo debeira ingresar las componentes que formaran la matriz
    for j in range(fila):
        m1.append(random.randint(0,5))
print(m1)