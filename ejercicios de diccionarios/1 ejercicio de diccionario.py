'''
1. 📝 Ejercicio 1 — Ficha de estudiante

# Crea un diccionario que represente un estudiante con estas claves:
# nombre, edad, carrera, promedio, materias (lista de al menos 4)

# Luego:
# 1. Imprime solo el nombre y la carrera
# 2. Agrega una clave "activo" con valor True
# 3. Actualiza el promedio a 4.2
# 4. Recorre todas las claves e imprime: "La clave X tiene el valor Y"
# 5. Verifica si la clave "beca" existe — si no existe imprime "Sin beca registrada"

'''

estudiante = { 'nombre':'Laura', 'edad':33, 'carrera':'Ingeniera Industrial', 'promedio': 4.0, 'materias': ['Cálculo', 'Estadística', 'Programación', 'Física'] }
print('\t\t---- Lista de estudiante ----')
print(f'\t\t\nNombre: {estudiante['nombre']}, Carrera: {estudiante['carrera']}')

estudiante['activo'] = True
estudiante['Promedio'] = 4.2

for clave, valor in estudiante.items():
    print(f'\t\t\nLa clave {clave} tiene el valor {valor}')

if 'beca' in estudiante:
    print(f'\t\t\nLa clave existe y su valor es: {estudiante['beca']}')
    
else:
    print('\t\t\nSin beca registrada')
