#1.	Elaborar un algoritmo que genere un arreglo de N elementos y encuentre el valor y la posición del mayor elemento.


buscar_mayor = [
    [1, 2, 83],
    [500, 34, 58],
    [458, 385, 8]
]

conteo = 0
for vector in buscar_mayor:
    for numero in vector:
        if numero > conteo:
            conteo = numero

print("El mayor elemento es:", conteo)