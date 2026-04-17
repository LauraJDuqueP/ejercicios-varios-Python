'''
CUANDO HAGA EL PORTAFOLIO COLOCAR LA SOLUCION DE ABAJO

📝 Ejercicio 2 — Contador de palabras

texto = "el gato come pescado y el perro come carne y el gato duerme"

# Con ese texto:
# 1. Cuenta cuántas veces aparece cada palabra
# 2. Guarda el resultado en un diccionario así: {"el": 3, "gato": 2, ...}
# 3. Imprime la palabra que más se repite
# 4. Imprime las palabras que aparecen más de una vez


'''

texto = "el gato come pescado y el perro come carne y el gato duerme"
palabras = texto.split()
grupo_palabras = {}

for i in range(len(palabras)):
    contador = 0
    for palabra in palabras:
        if palabras[i] == palabra:
            contador += 1 
    grupo_palabras[palabras[i]] = contador
    
#print(palabras)
#print(len(palabras))
print(grupo_palabras)

# 3. Imprime la palabra que más se repite

print(f'\n\t\tla palabra que más se repite es: {max(grupo_palabras, key=grupo_palabras.get)} y aparece {max(grupo_palabras.values())} veces')

# 4. Imprime las palabras que aparecen más de una vez

print('\n\t\tlas palabras que aparecen más de una vez son: ')
for clave, valor in grupo_palabras.items():
    if valor > 1:
        print(f'\t\t\t {clave}: {valor} {'vez' if valor == 1 else 'veces' }')


# mejorando el codigo para 1. Cuenta cuántas veces aparece cada palabra


'''
for palabra in palabras:                    # recorre solo una vez
    if palabra in grupo_palabras:           # ya existe la clave? se pregunta porque si la palabra ya esta en el diccionario entonces ....
        grupo_palabras[palabra] += 1        # si ya existe, suma uno
    else:
        grupo_palabras[palabra] = 1         # si no existe, se crea una clave y le asigna el valor de 1

'''