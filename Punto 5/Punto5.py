# Datos iniciales de equipos 
equipos = {
    "E01": {"jugados":0,"ganados":0,"empatados":0,"goles_favor":0,"goles_contra":0,"puntos":0},
    "E02": {"jugados":0,"ganados":0,"empatados":0,"goles_favor":0,"goles_contra":0,"puntos":0},
    "E03": {"jugados":0,"ganados":0,"empatados":0,"goles_favor":0,"goles_contra":0,"puntos":0}
}

# Lista de partidos 
partidos = [
    {"local":"E01","goles_local":2,"visitante":"E02","goles_visitante":1},
    {"local":"E03","goles_local":0,"visitante":"E01","goles_visitante":0},
    {"local":"E02","goles_local":3,"visitante":"E03","goles_visitante":2}
]

# Procesar partidos
for p in partidos:
    local = p["local"]
    visitante = p["visitante"]
    gl = p["goles_local"]
    gv = p["goles_visitante"]

    # Actualizar partidos jugados
    equipos[local]["jugados"] += 1
    equipos[visitante]["jugados"] += 1

    # Actualizar goles
    equipos[local]["goles_favor"] += gl
    equipos[local]["goles_contra"] += gv
    equipos[visitante]["goles_favor"] += gv
    equipos[visitante]["goles_contra"] += gl

    # Resultado
    if gl > gv:  # gana local
        equipos[local]["ganados"] += 1
        equipos[local]["puntos"] += 3
    elif gv > gl:  # gana visitante
        equipos[visitante]["ganados"] += 1
        equipos[visitante]["puntos"] += 3
    else:  # empate
        equipos[local]["empatados"] += 1
        equipos[visitante]["empatados"] += 1
        equipos[local]["puntos"] += 1
        equipos[visitante]["puntos"] += 1

# Convertir diccionario en lista para ordenar manualmente
tabla = list(equipos.items())

# Ordenar manualmente por puntos (bubble sort)
for i in range(len(tabla)):
    for j in range(len(tabla)-1):
        if tabla[j][1]["puntos"] < tabla[j+1][1]["puntos"]:
            tabla[j], tabla[j+1] = tabla[j+1], tabla[j]

# Mostrar tabla
print("Tabla de clasificación:")
print("Equipo  PJ  PG  PE  GF  GC  Pts")
for codigo, datos in tabla:
    print(f"{codigo}   {datos['jugados']}   {datos['ganados']}   {datos['empatados']}   "
          f"{datos['goles_favor']}   {datos['goles_contra']}   {datos['puntos']}")
