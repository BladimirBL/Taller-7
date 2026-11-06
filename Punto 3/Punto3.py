respuestas_correctas = [1,2,3,4,5]*12  

# Lista de estudiantes (ejemplo)
estudiantes = [
    {"credencial":"A001","matematicas":[1,2,3,4,5]*6,"verbales":[1,2,3,4,5]*6},
    {"credencial":"A002","matematicas":[1]*30,"verbales":[2]*30},
    {"credencial":"A003","matematicas":[5]*30,"verbales":[5]*30}
]

resultados = []
for e in estudiantes:
    pm = sum(e["matematicas"][i]==respuestas_correctas[i] for i in range(30))
    pv = sum(e["verbales"][i]==respuestas_correctas[30+i] for i in range(30))
    resultados.append((e["credencial"], pm, pv, pm+pv))

n = len(estudiantes)
prom_mat = sum(r[1] for r in resultados)/n
prom_ver = sum(r[2] for r in resultados)/n
prom_total = sum(r[3] for r in resultados)/n

print("Resultados:")
for c, pm, pv, pt in resultados:
    print(f"{c}: Mat={pm}, Ver={pv}, Total={pt}")

print("\nPromedios:", prom_mat, prom_ver, prom_total)

print("\n>= Promedio total:")
for c, pm, pv, pt in resultados:
    if pt >= prom_total:
        print(c, pt)

mayor = max(resultados, key=lambda x: x[3])
print("\nMayor puntaje:", mayor[0], mayor[3])

