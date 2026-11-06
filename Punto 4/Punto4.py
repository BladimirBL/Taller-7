ventas = [
    [100, 200, 150, 300],   
    [400, 500, 600, 700],   
    [250, 350, 450, 550]    
]

# Totales por vendedor
totales_vendedores = [sum(vendedor) for vendedor in ventas]

# Totales por año (sumando columna por columna)
totales_anios = [sum(fila[j] for fila in ventas) for j in range(len(ventas[0]))]

# Gran total
gran_total = sum(totales_vendedores)

# Mostrar resultados
print("Total por vendedor:")
for idx, total in enumerate(totales_vendedores, start=1):
    print(f"Vendedor {idx}: {total}")

print("\nTotal por año:")
for idx, total in enumerate(totales_anios, start=1):
    print(f"Año {idx}: {total}")

print("\nGran total de la empresa:", )