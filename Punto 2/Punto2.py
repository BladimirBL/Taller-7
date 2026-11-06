buscar_mayor = [
    [1, 2, 83],
    [500, 34, 58],
    [458, 385, 8]
]

promedio = 0
menor = []
mayor = []
for vector in buscar_mayor:
    for numero in vector:
        promedio += numero / 9


for vector in buscar_mayor:
    for numero in vector:
        if numero <= promedio:
            menor.append(numero)
        else:
            mayor.append(numero)
        
        

print(promedio)
print(menor)
print(mayor)
