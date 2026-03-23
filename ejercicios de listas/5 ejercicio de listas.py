'''
🔥 Ejercicio 3 — Nivel difícil | Sistema de calificación académica

estudiantes = ["Ana", "Bruno", "Carmen", "Diego", "Elena", "Fernando"]

asignaturas = ["Cálculo", "Estadística", "Programación", "Base_Datos", "ML"]

# Peso de cada asignatura en la nota final
pesos = [0.25, 0.20, 0.20, 0.15, 0.20]

notas = [
    [8.5, 9.2, 9.8, 8.1, 9.5],   # Ana
    [5.2, 6.8, 7.1, 6.5, 5.9],   # Bruno
    [9.1, 8.7, 9.2, 9.5, 9.8],   # Carmen
    [6.8, 7.2, 8.5, 7.9, 7.1],   # Diego
    [4.5, 5.1, 6.2, 5.8, 4.9],   # Elena
    [7.8, 8.1, 8.9, 7.5, 8.3],   # Fernando
]

escala = {
    "Sobresaliente": 9.0,
    "Notable":       7.5,
    "Aprobado":      6.0,
    "Reprobado":     0.0
}

Calcula:

Nota final ponderada de cada estudiante — cada asignatura tiene un peso diferente. Fórmula: nota_final = suma(nota * peso) para cada asignatura
Clasificación de cada estudiante según la escala
Asignatura con mejor y peor rendimiento del grupo
Ranking completo de estudiantes de mayor a menor nota final — sin usar sort(), impleméntalo tú con bucles
Estudiantes en riesgo académico — los que tienen más de 2 asignaturas por debajo de 6.0

Calcula:

Nota final ponderada → suma(nota * peso) por cada asignatura
Clasificación de cada estudiante según la escala
Asignatura con mejor y peor rendimiento del grupo
Ranking de mayor a menor nota — sin usar sort()
Estudiantes en riesgo — más de 2 asignaturas bajo 6.0

'''

estudiantes = ["Ana", "Bruno", "Carmen", "Diego", "Elena", "Fernando"]

asignaturas = ["Cálculo", "Estadística", "Programación", "Base_Datos", "ML"]

# Peso de cada asignatura en la nota final
pesos = [0.25, 0.20, 0.20, 0.15, 0.20]

notas = [
    [8.5, 9.2, 9.8, 8.1, 9.5],   # Ana
    [5.2, 6.8, 7.1, 6.5, 5.9],   # Bruno
    [9.1, 8.7, 9.2, 9.5, 9.8],   # Carmen
    [6.8, 7.2, 8.5, 7.9, 7.1],   # Diego
    [4.5, 5.1, 6.2, 5.8, 4.9],   # Elena
    [7.8, 8.1, 8.9, 7.5, 8.3],   # Fernando
]

escala = {
    "Sobresaliente": 9.0,
    "Notable":       7.5,
    "Aprobado":      6.0,
    "Reprobado":     0.0
}

# 1 Nota final ponderada → suma(nota * peso) por cada asignatura
# Nota final ponderada de cada estudiante — cada asignatura tiene un peso diferente. Fórmula: nota_final = suma(nota * peso) para cada asignatura
# nota_final = suma(nota * peso) para cada asignatura

print('\n\t\t------ 1. Nota final ponderada de cada estudiante ------\n')
ponderado_notas = []

for x in range(len(estudiantes)): # x estudiantes en notas
    
    nota_final = 0
    for y in range(len(asignaturas)): # y asignaturas en cada i de las notas
         nota_final = round(nota_final + (notas[x][y] * pesos[y]), 2)

    ponderado_notas.append(nota_final)

print('\n\t\t\tEstudiante     Ponderado')

for estudiante, nota in zip(estudiantes, ponderado_notas):
    print(f'\t\t\t{estudiante}            {nota}')


# 2 Clasificación de cada estudiante según la escala


print('\n\t\t------ 2. Clasificación de cada estudiante según la escala ------\n')
print('\t\t\tEstudiante     Clasificacion')
for x in range(len(estudiantes)):
    for clasificacion, datos in escala.items():
        if ponderado_notas[x] >= datos:
            print(f'\t\t\t{estudiantes[x]}            {clasificacion} con {ponderado_notas[x]} ')
            break
       
# 3 Asignatura con mejor y peor rendimiento del grupo


print('\n\t\t------ 3. Asignatura con mejor y peor rendimiento del grupo ------\n')
rendimiento_notas = []
for x in range(len(asignaturas)): # x son las aignaturas
    suma = 0
    for y in range(len(estudiantes)): # y son los estudiantes en notas osea la cantidad de elementos dentro de notas
        suma = suma + notas[y][x]

    rendimiento_notas.append(round(suma/(len(estudiantes)),2))

print(f'\t\t\tLa asignatura con mejor rendimiento fue: {asignaturas[rendimiento_notas.index(max(rendimiento_notas))]} con {max(rendimiento_notas)}')
print(f'\t\t\tLa asignatura con peor rendimiento fue: {asignaturas[rendimiento_notas.index(min(rendimiento_notas))]} con {min(rendimiento_notas)}')

# 4 Ranking completo de estudiantes de mayor a menor nota final — sin usar sort(), impleméntalo tú con bucles

print('\n\t\t------ 4. Ranking completo de estudiantes de mayor a menor nota final ------\n')
nuevo_ranking = []
# estudiantes = ["Ana", "Bruno", "Carmen", "Diego", "Elena", "Fernando"]
# print(ponderado_notas)  [9.03, 6.23, 9.23, 7.45, 5.23, 8.13]
estudiantes_copia = estudiantes[:]
ponderado_notas_copia = ponderado_notas[:]
for x in range(len(estudiantes_copia)): # x recorre por cada estudiante
    posicion = 1
    for y in range(len(ponderado_notas_copia)): # y recorre las notas
        if ponderado_notas_copia[x] > ponderado_notas_copia[y]:
            posicion +=1 
    nuevo_ranking.append(posicion)

ranking = []

while len(ponderado_notas_copia) > 0:
        n = max(ponderado_notas_copia)
        z = ponderado_notas_copia.index(n)
        y = [ponderado_notas_copia[z], estudiantes_copia[z]]
        ranking.append(y)
        del ponderado_notas_copia[z]
        del estudiantes_copia[z]
       

print(ranking)

for posicion, dato in enumerate(ranking, 1):
    print(f'\t\t\t{posicion}° {dato[1]} : {dato[0]}')

# puedes usar enumerate() o un for como este
#for x in ranking:
#   print(f'\t\t\t{x[1]} : {x[0]}')


# 5 Estudiantes en riesgo académico — los que tienen más de 2 asignaturas por debajo de 6.0
print('\n\t\t------ 5. Estudiantes en riesgo académico — los que tienen más de 2 asignaturas por debajo de 6.0 ------\n')


for x in range(len(estudiantes)): # x recorre la lista de notas por estudiante
    riesgo = 0
    for y in range(len(asignaturas)): # y recorre la sublista por asignatura
        if notas[x][y] < 6.0:
            riesgo += 1
        
    if riesgo >2:
        print(f'\t\t\tEstudiante {estudiantes[x]} perdio {riesgo} notas y por tanto esta en riesgo')
    
