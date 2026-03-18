'''
🏋️ Ejercicio 1 — Nivel medio | Análisis de ventas por región
Una cadena de supermercados tiene 4 regiones y registra ventas de 6 categorías durante un trimestre:

regiones = ["Norte", "Sur", "Oriente", "Occidente"]

categorias = ["Lácteos", "Carnes", "Frutas", "Bebidas", "Limpieza", "Panadería"]

ventas_trimestre = [
    [4500, 8200, 3100, 6700, 2900, 5100],  # Norte
    [3800, 7500, 4200, 5900, 3400, 4800],  # Sur
    [5200, 9100, 2800, 7200, 3100, 5600],  # Oriente
    [4100, 6800, 3900, 6100, 2700, 4300],  # Occidente
]

meta_trimestral = 5000  # por categoría por región
presupuesto_region = 30000  # presupuesto total por región

Calcula:

Total vendido por región y si superó el presupuesto asignado
Total vendido por categoría en todo el trimestre
Categoría estrella por región — la que más vendió en cada región
Porcentaje de cumplimiento de meta por categoría por región — cuántas categorías cumplieron la meta en cada región (ejemplo: "Norte cumplió 4/6 categorías")
Región más equilibrada — la que tiene menor diferencia entre su categoría más alta y más baja

'''

# Total vendido por región y si superó el presupuesto asignado

regiones = ["Norte", "Sur", "Oriente", "Occidente"]

categorias = ["Lácteos", "Carnes", "Frutas", "Bebidas", "Limpieza", "Panadería"]

ventas_trimestre = [
    [4500, 8200, 3100, 6700, 2900, 5100],  # Norte
    [3800, 7500, 4200, 5900, 3400, 4800],  # Sur
    [5200, 9100, 2800, 7200, 3100, 5600],  # Oriente
    [4100, 6800, 3900, 6100, 2700, 4300],  # Occidente
]

meta_trimestral = 5000  # por categoría por región
presupuesto_region = 30000  # presupuesto total por región

categorias_numero = 6
total_vendido =[]

for i in ventas_trimestre:
    x = sum(i)
    total_vendido.append(x)

print('\t------ Total vendido por región y si supero el presupuesto asignado ------')
for i, y in zip(regiones, total_vendido):
    print(f'\t\tregion: {i}: ${y}')
    if y > presupuesto_region:
        print(f'\t\t\tRegion {i} supero el presupuesto asignado por ${y-presupuesto_region}')
    else:
        print(f'\t\t\tRegion {i} no supero el presupuesto asignado, le faltato ${presupuesto_region-y} para llegar a la meta')


# 2 Total vendido por categoría en todo el trimestre

print('\t------ Total vendido por categoría en todo el trimestre ------')
for i in range(categorias_numero):
    suma = 0
    for y in range(len(ventas_trimestre)):
        suma = suma + ventas_trimestre[y][i]
    print(f'\t\tLa categoria {categorias[i]} vendio: {suma} en el trimestre')


# 3 Categoría estrella por región — la que más vendió en cada región

print('\t------ Categoría estrella por región — la que más vendió en cada región ------=')
for x in range(len(ventas_trimestre)):
    maxi = max(ventas_trimestre[x])
    print(f'\t\tEn la region {regiones[x]}: la categoria que mas vendio fue: {categorias[ventas_trimestre[x].index(maxi)]}: ${maxi}')


# 4 porcentaje de cumplimiento de meta por categoría por región — cuántas categorías cumplieron la meta en cada región 
# (ejemplo: "Norte cumplió 4/6 categorías")
print('\t------ porcentaje de cumplimiento de meta por categoría por región ------')

for x in range(len(ventas_trimestre)):
    suma = 0
    for i in range(categorias_numero):
        if ventas_trimestre[x][i] >= 5000:
            suma = suma +1
    print(f'\t\t{regiones[x]}: cumplio {suma}/6 categorias')

# Región más equilibrada — la que tiene menor diferencia entre su categoría más alta y más baja

print('\t------ Región más equilibrada — la que tiene menor diferencia entre su categoría más alta y más baja ------')
lista = []
for i in ventas_trimestre:
    x = max(i)-min(i)
    lista.append(x)

x = min(lista)

print(f'\t\tLa región más equilibrada es {regiones[lista.index(x)]} con {x} de diferencia entre su categoría más alta y más baja')


'''
    categorias = ["Lácteos", "Carnes", "Frutas", "Bebidas", "Limpieza", "Panadería"]

ventas_trimestre = [
    [4500, 8200, 3100, 6700, 2900, 5100],  # Norte
    [3800, 7500, 4200, 5900, 3400, 4800],  # Sur
    [5200, 9100, 2800, 7200, 3100, 5600],  # Oriente
    [4100, 6800, 3900, 6100, 2700, 4300],  # Occidente
]

regiones = ["Norte", "Sur", "Oriente", "Occidente"]
meta_trimestral = 5000  # por categoría por región
presupuesto_region = 30000  # presupuesto total por región
'''