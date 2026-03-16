'''
Escribe un programa que calcule:

El promedio de cada estudiante en todas las materias
El promedio de cada materia entre todos los estudiantes
El estudiante con mejor promedio general
La materia más difícil (la que tiene el promedio más bajo)
Cuántos estudiantes reprobaron al menos una materia (nota < 6.0... sí, Carlos 👀)

estudiantes = ["Laura", "Carlos", "María", "Luis"]
'''

estudiantes = ["Laura", "Carlos", "María", "Luis"]

notas = [
    [8.5, 6.2, 9.1, 7.0],   # fila 0 → Matemáticas
    [7.3, 5.8, 8.0, 6.5],   # fila 1 → Ciencias
    [9.5, 9.0, 8.7, 7.8],   # fila 2 → Historia
    [6.0, 7.5, 9.2, 8.3],   # fila 3 → Inglés
]

materias = ["Matemáticas", "Ciencias", "Historia", "Inglés"]
cantidad_notas = 4

#promedio de cada nota 
promedios_sinCalculo = []
promedio_Por_materias = []

## aqui sacamos la suma de cada materia es decir el punto 2. 
# promedio de cada materia entre todos los estudiantes
for materia in notas:
    suma = 0
    for nota in materia:
        suma = suma + nota
    promedios_sinCalculo.append(suma)

# aqui calculamos el promedio dividiendo por la cantidad de notas la suma de las notas por materia

for nota in promedios_sinCalculo:
    calculo = round(nota/cantidad_notas, 2)
    promedio_Por_materias.append(calculo)

# imprimiendo el promedio de cada materia

print(f'\t ---- El promedio general de cada materia es: ----')
for promedio, materia in list(zip(promedio_Por_materias, materias)):
    print(f'\t\tPara {materia}: El ponderizado es {promedio}')


## El promedio de cada estudiante en todas las materias. 
# punto 1. El promedio de cada estudiante en todas las materias


promedio_estudiante_sinCalcular = []
promedio_estudiante = []
cantidad_materias = 4

for i in range(len(estudiantes)):
    suma = 0
    for nota in notas: 
        suma = nota[i] + suma
    promedio_estudiante_sinCalcular.append(suma)

for numero in promedio_estudiante_sinCalcular:
    n = round(numero/cantidad_materias,2)    
    promedio_estudiante.append(n)

print(f"\t----El promedio de cada estudiante es:  ----")
for promedio, estudiante in zip(promedio_estudiante, estudiantes):
    print(f"\t\t{estudiante} tiene de promedio general: {promedio}")

# El estudiante con mejor promedio general
print(f'\t----El estudiante con mejor promedio es: ----\n\t\t{estudiantes [promedio_estudiante.index(max(promedio_estudiante))]} con : {max(promedio_estudiante)}')

#La materia más difícil (la que tiene el promedio más bajo)
print(f'\t----La materia mas dificiles: ----\n\t\t{materias[promedio_Por_materias.index(min(promedio_Por_materias))]} con: {min(promedio_Por_materias)}')

#Cuántos estudiantes reprobaron al menos una materia (nota < 6.0... sí, Carlos 👀)
print(f'\t----Estudiantes que reprobaron por lo menos una nota---- ')
for i in range(len(estudiantes)):
    mala_nota = []
    materia_reprobada= []
    for j in range(len(notas)):
        if notas[j][i] < 6.0:
            mala_nota.append(notas[j][i])
            materia_reprobada.append(materias[j])
    if mala_nota:
        
        for materia, nota in zip(materia_reprobada, mala_nota):
            print(f'\t\t{estudiantes[i]} reprobó {materia} con {nota}')
    else:
        print(f'\t\t{estudiantes[i]} no perdió ninguna nota')
               