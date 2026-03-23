'''
🔥 Ejercicio 4 — Nivel difícil | Análisis financiero

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

departamentos = ["Ventas", "Marketing", "Tecnología", "RRHH", "Operaciones"]

# Ingresos mensuales por departamento
ingresos = [
    [85, 92, 78, 95, 88, 102, 98, 105, 91, 87, 115, 125],   # Ventas
    [45, 48, 42, 51, 49, 55,  52, 58,  47, 44, 62,  68 ],   # Marketing
    [62, 65, 70, 68, 72, 75,  71, 78,  69, 67, 80,  85 ],   # Tecnología
    [28, 29, 27, 31, 30, 32,  29, 33,  28, 27, 35,  38 ],   # RRHH
    [95, 98, 88, 102,96, 108, 104,112, 99, 93, 118, 130],   # Operaciones
]

# Presupuesto mensual por departamento
presupuesto = [90, 50, 65, 30, 100]  # uno por departamento

Calcula:

Variación mensual de cada departamento — diferencia entre cada mes y el anterior. ¿En qué mes tuvo su mayor crecimiento cada departamento?
Meses deficitarios por departamento — meses donde el ingreso estuvo por debajo del presupuesto. Imprime cuántos meses estuvo por debajo y el promedio de déficit
Trimestres — agrupa los meses en 4 trimestres y calcula el total por departamento por trimestre
Departamento más consistente — el que tiene menor desviación entre sus meses. Fórmula desviación: sqrt(suma((x - promedio)²) / n) — impleméntala sin importar librerías
Proyección anual — usando el promedio de crecimiento mensual de cada departamento, proyecta cuánto generaría el mes 13
'''

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

departamentos = ["Ventas", "Marketing", "Tecnología", "RRHH", "Operaciones"]

# Ingresos mensuales por departamento
ingresos = [
    [85, 92, 78, 95, 88, 102, 98, 105, 91, 87, 115, 125],   # Ventas
    [45, 48, 42, 51, 49, 55,  52, 58,  47, 44, 62,  68 ],   # Marketing
    [62, 65, 70, 68, 72, 75,  71, 78,  69, 67, 80,  85 ],   # Tecnología
    [28, 29, 27, 31, 30, 32,  29, 33,  28, 27, 35,  38 ],   # RRHH
    [95, 98, 88, 102,96, 108, 104,112, 99, 93, 118, 130],   # Operaciones
]

# Presupuesto mensual por departamento
presupuesto = [90, 50, 65, 30, 100]  # uno por departamento

# 1. Variación mensual de cada departamento — diferencia entre cada mes y el anterior. ¿En qué mes tuvo su mayor crecimiento cada departamento?
print('\n\t\t------ 1. Variación mensual de cada departamento ------\n')
print('\t\t\tEnero no tiene variacion por ser el primer mes y no tenemos informacion de diciembre del ano anterior')

variaciones_totales = {}

for x in range(len(departamentos)): # x pasa por los departamentos en ingresos
    print(f'\n\t\t\t---{departamentos[x]}: ')
    variaciones_mes = {}
    for y in range(1,len(meses)): # y pasa por los meses en ingresos
        n = ingresos[x][y]-ingresos[x][y-1]
        variaciones_mes[f'{meses[y]}'] = n
        print(f'\t\t\t{meses[y]}: {n}')
    variaciones_totales[departamentos[x]] = variaciones_mes      


# print(variaciones_totales)

print('\n\t\t------ 1.1 ¿En qué mes tuvo su mayor crecimiento cada departamento? ------\n')
for depto in variaciones_totales:
    mejor_mes = max(variaciones_totales[depto], key=variaciones_totales[depto].get)
    variacion = variaciones_totales[depto][mejor_mes]
    print(f'\t\t\t{depto}: mejor mes: {mejor_mes}: con {variacion}')

# 2 Meses deficitarios por departamento — meses donde el ingreso estuvo 
# por debajo del presupuesto. Imprime cuántos meses estuvo por debajo y el promedio de déficit


promedios_deficit = []
print('\n\t\t------ 2 Meses deficitarios por departamento ------\n')
for x in range(len(presupuesto)): # x recorre ingresos por departamento desde presupuesto
    print(f'\n\t\t\t----Departamento: -- {departamentos[x]} --')
    suma = 0
    lista = []
    for y in  range(len(meses)): # y recorre cada mes de ingresos para compararlo con presupuesto
        if ingresos[x][y] < presupuesto[x]: 
            n = presupuesto[x] - ingresos[x][y] 
            suma += 1
            lista.append(n)
            print(f'\t\t\t mes {meses[y]}: deficit: {n}') 
    if len(lista) > 0:
        promedios_deficit.append(round(sum(lista)/(len(lista)),2))
    else:
         promedios_deficit.append(0)
    
    print(f'\n\t\t\t{departamentos[x]} - meses en deficit: {suma}') 

print('\n\t\t------ 2.1 Promedio de déficit del departamento al año ------\n')
for x, y in zip(departamentos, promedios_deficit): # vamos a unir el departamento con el promedio de cada uno por posicion
    print(f'\t\t\t{x}: {y}')

#print(promedios_deficit) 

# 3 Trimestres — agrupa los meses en 4 trimestres y calcula el total por departamento por trimestre

print('\n\t\t------ 3 Trimestres — agrupa los meses en 4 trimestres y calcula el total por departamento por trimestre ------\n')
ingresos_2 = ingresos.copy()
numero = 3

for i in range(len(departamentos)): # i recorre los departamentos en ingresos 
    print(f'\n\t\t\t----Departamento: -- {departamentos[i]} --')
    lista= []
    y = 0
    z = 3    
    #for j in range(len(meses)): # j recorre cada departamento de ingresos osea recorre los 12
    for x in range(round(len(meses)/numero)): # x me da la cantidad de meses que son los que voy a agrupar en 4 grupos dado por el 12/3
        n = ingresos_2[i][y:z]
       # print(f'{y}: {z}')
        print(f'\t\tEn el {x+1} trimestre')
        suma = sum(n)
        print(f'\t\tingresos: {suma}')
        y += 3 # y me va a dar la posicion inicial debe ser de 3 en 3
        z += 3 # z me va a dar la posicion final debe empezar en 4 porque con [y:z] z no se devuelve
        lista.append(n)
        # print(n)
    
   # print(lista)
    

# 4 Departamento más consistente — el que tiene menor desviación entre sus meses. 
# Fórmula desviación: sqrt(suma((x - promedio)²) / n) — impleméntala sin importar librerías

print('\n\t\t------ 4 Departamento más consistente — el que tiene menor desviación entre sus meses ------\n')
'''
1. Calcula el promedio de los 12 meses
2. A cada mes, réstale ese promedio → (x - promedio)
3. Eleva ese resultado al cuadrado → (x - promedio)²
4. Suma todos esos cuadrados
5. Divide entre n (cantidad de meses = 12)
6. Sácale la raíz cuadrada

sqrt( suma((x - promedio)²) / n )
'''

desviación_totales = []
for x in range(len(departamentos)): # x va a recorrer los departamentos en ingresos
    suma = sum(ingresos[x])
    #print(suma)
    promedio = suma/(len(ingresos[x]))
    #print(promedio)
    lista = []
    for y in range(len(meses)): # y va a recorrer x por la cantidad de posiciones en x que estan en ingresos
        n = round(ingresos[x][y] - promedio, 2)
        lista.append(round((n * n), 2))
    suma_cuadrados = sum(lista)
    #print(suma_cuadrados)
    divi = suma_cuadrados/len(meses)
    #print(divi)
    desviación = round(divi ** 0.5, 2)
    desviación_totales.append(desviación)
    # print(desviación)

n = min(desviación_totales)
print(f'\t\tEl departamento que tiene menor desviación entre sus meses, el mas consistente es:\n'
f'\t\t{departamentos[desviación_totales.index(n)]}: con {n} de desviacion')


# 5 Proyección anual — usando el promedio de crecimiento mensual de cada departamento, proyecta cuánto generaría el mes 13

print('\n\t\t------ 5 Proyección anual: proyecta cuánto generaría el mes 13 ------\n')

# print(variaciones_totales)

for x in range(len(departamentos)):
    
    n = []
    for valor in variaciones_totales[departamentos[x]].values():
        n.append(valor)
    prom_crecimiento = round(sum(n)/(len(n)), 2)
    # print(n)
    # print(prom_crecimiento)
    print(f'\t\t\tDepartamento --{departamentos[x]}-- tuvo un crecimiento promedio mensual de: {prom_crecimiento}')
    print(f'\t\t\tProyeccion de ingresos para el mes 13: {ingresos[x][-1] + prom_crecimiento}')
