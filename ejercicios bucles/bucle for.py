## 🏋️ DESAFÍO 1 — Bucle for 

'''


Tienes los datos de ventas de una tienda durante una semana, organizados por día y por vendedor:

vendedores = ["Ana", "Carlos", "María", "Luis", "Sofía"]

ventas = [
[320, 150, 480, 210, 390], # Lunes
[280, 420, 190, 510, 300], # Martes
[450, 380, 220, 175, 490], # Miércoles
[190, 260, 410, 330, 150], # Jueves
[500, 310, 270, 440, 360], # Viernes
]

meta_semanal = 1500 # Cada vendedor debe superar esto

Tu misión es escribir un programa que calcule con bucles for:

El total vendido por cada vendedor durante la semana
Si cada vendedor cumplió o no la meta semanal
El vendedor estrella (el que más vendió en total)
El total general de ventas de toda la tienda en la semana

Pista: Vas a necesitar un for dentro de otro for — a eso se le llama bucle anidado 🤯


'''

# total vendido por cada vendedor durante la semana
resultado = []

for i in range(4):
    suma = 0
    for venta in ventas:
        suma += venta[i]
    resultado.append(suma)

nuevo = list(zip(vendedores, resultado))

for nombre, ventas in zip(vendedores, resultado):
    print(f'\t{nombre} vendio {ventas} en la semana')

# si quiero usar zip 

resultado = [sum(x) for x in zip(*ventas)]
print(resultado)

# saber si los vendedores cumplieron la meta : meta_semanal = 1500 # Cada vendedor debe superar esto


print('\tlos vendedores y sus ventas fueron:')
for nombre, ventas in zip(vendedores, resultado):
    if ventas > 1500:
        print(f'\t\t{nombre} vendio {ventas} en la semana: Supero la meta semanal')
    elif ventas <= 1500: 
        print(f'\t\t{nombre} vendio {ventas} en la semana: NO Supero la meta semanal')
 
 # El vendedor estrella (el que más vendió en total)

print(f'\tEl vendedor estrella es:\n\t\t{vendedores[resultado.index(max(resultado))]} con {max(resultado)}')   
    
# El total general de ventas de toda la tienda en la semana
print(f'El total de ventas semanal de la tienda es {sum(resultado)}')
