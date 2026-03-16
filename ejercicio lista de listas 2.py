'''
tiendas = ["Bogotá", "Medellín", "Cali", "Barranquilla"]

productos = ["Arroz", "Aceite", "Azúcar", "Leche", "Café"]

inventario = [
    [120, 45,  80,  200, 35],    # fila 0 → Bogotá
    [85,  90,  60,  150, 20],    # fila 1 → Medellín
    [200, 30,  95,  180, 50],    # fila 2 → Cali
    [60,  75,  40,  220, 15],    # fila 3 → Barranquilla
]

stock_minimo = 50
```

Recuerda lo que debes calcular:

1. El **total de cada producto** sumando todas las tiendas
2. La **tienda con más inventario total**
3. Casos donde el stock está **por debajo del mínimo** → `"⚠️ ALERTA: [tienda] tiene solo [X] unidades de [producto]"`
4. El **producto más escaso** en total
5. El **inventario promedio** de cada tienda

---

## Pistas antes de empezar:
```
Total por producto  →  suma por COLUMNA  (como el promedio de estudiantes)
Total por tienda    →  suma por FILA     (más fácil)
'''

tiendas = ["Bogotá", "Medellín", "Cali", "Barranquilla"]

productos = ["Arroz", "Aceite", "Azúcar", "Leche", "Café"]

inventario = [
    [120, 45,  80,  200, 35],    # fila 0 → Bogotá
    [85,  90,  60,  150, 20],    # fila 1 → Medellín
    [200, 30,  95,  180, 50],    # fila 2 → Cali
    [60,  75,  40,  220, 15],    # fila 3 → Barranquilla
]

stock_minimo = 50

#1. El **total de cada producto** sumando todas las tiendas
Numeros_productos_Vender = 5
print('\t---- **total de cada producto** sumando todas las tiendas ----')

for i in range(Numeros_productos_Vender):
    suma = 0
    for j in range(len(inventario)):
        suma = suma + inventario[j][i]
    print(f'\t\tproducto: {productos[i]} - total en tiendas: {suma}')

# 2. La **tienda con más inventario total**

print(f'\t-----La tienda con mas inventario total es: ----')
total_enTienda = []
for i in inventario:
    total= sum(i)
    total_enTienda.append(total)
print(f'\t\t{tiendas[total_enTienda.index(max(total_enTienda))]} con : {max(total_enTienda)} en inventario')

# 3. Casos donde el stock está **por debajo del mínimo** → `"⚠️ ALERTA: [tienda] tiene solo [X] unidades de [producto]"`

print('\t----- stock debajo del minimo ----')
for i in range(len(tiendas)):
    for j in range(Numeros_productos_Vender):
        if inventario[i][j] < stock_minimo:
            print(f'\t\t⚠️ ALERTA: {tiendas[i]} tiene solo {inventario[i][j]} unidades de {productos[j]}')
    
# 4. El **producto más escaso** en total

print('\t---- El producto mas escaso teniendo en cuenta todas las tiendas: ----')
total_producto = []

for i in range(Numeros_productos_Vender):
    suma = 0
    for j in range(len(inventario)):
        suma = suma + inventario[j][i]
    total_producto.append(suma)
print(f'\t\tEl producto mas escaso es el {productos[total_producto.index(min(total_producto))]} con {min(total_producto)} productos en stock')

# 5. El **inventario promedio** de cada tienda

print('\t---- Inventario promedio de cada tienda ----')

for i in range(len(inventario)):
    total = sum(inventario[i])
    promedio = total/len(inventario[i])
    print(f'\t\t{tiendas[i]}: {promedio} unidades de productos')

