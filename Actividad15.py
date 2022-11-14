import random


print("Ingrese cuantos numeros aleatorios desea obtener")
n=int(input())
aleatorios = [random.randint(0,1000) for _ in range(n)]
print(aleatorios)
