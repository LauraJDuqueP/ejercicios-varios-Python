'''
🔴 EJERCICIOS PORTAFOLIO — Data Science

🏆 Ejercicio 6 — Simulador de inventario con movimientos

# Sistema de inventario que registra entradas y salidas de productos
inventario_inicial = {
    "laptop_dell":     {"nombre": "Laptop Dell",     "stock": 15, "precio_unitario": 2500000, "categoria": "tecnologia"},
    "mouse_logitech":  {"nombre": "Mouse Logitech",  "stock": 42, "precio_unitario": 85000,   "categoria": "tecnologia"},
    "silla_ergonomica":{"nombre": "Silla Ergonómica","stock": 8,  "precio_unitario": 850000,  "categoria": "mobiliario"},
    "monitor_lg":      {"nombre": "Monitor LG",      "stock": 20, "precio_unitario": 980000,  "categoria": "tecnologia"},
    "escritorio":      {"nombre": "Escritorio",      "stock": 5,  "precio_unitario": 650000,  "categoria": "mobiliario"},
}

movimientos = [
    {"tipo": "salida",  "producto": "laptop_dell",      "cantidad": 3,  "fecha": "2024-01-05"},
    {"tipo": "entrada", "producto": "mouse_logitech",   "cantidad": 20, "fecha": "2024-01-07"},
    {"tipo": "salida",  "producto": "silla_ergonomica", "cantidad": 6,  "fecha": "2024-01-08"},
    {"tipo": "salida",  "producto": "monitor_lg",       "cantidad": 15, "fecha": "2024-01-10"},
    {"tipo": "entrada", "producto": "laptop_dell",      "cantidad": 10, "fecha": "2024-01-12"},
    {"tipo": "salida",  "producto": "escritorio",       "cantidad": 5,  "fecha": "2024-01-15"},
    {"tipo": "salida",  "producto": "mouse_logitech",   "cantidad": 8,  "fecha": "2024-01-18"},
    {"tipo": "entrada", "producto": "silla_ergonomica", "cantidad": 15, "fecha": "2024-01-20"},
    {"tipo": "salida",  "producto": "laptop_dell",      "cantidad": 7,  "fecha": "2024-01-22"},
    {"tipo": "salida",  "producto": "monitor_lg",       "cantidad": 4,  "fecha": "2024-01-25"},
]

# Construye:
# 1. Procesa cada movimiento y actualiza el stock en inventario_inicial
#    — si una salida supera el stock disponible no la proceses
#    — imprime una alerta: "ALERTA: stock insuficiente para X"
# 2. Inventario final con stock actualizado
# 3. Productos con stock crítico — menos de 5 unidades
# 4. Valor total del inventario final — stock * precio_unitario por producto
# 5. Total de entradas vs salidas por producto
# 6. Producto con mayor movimiento total (entradas + salidas)
# 7. Reporte por categoría:
#    - cuántos productos tiene cada categoría
#    - valor total de cada categoría
#    - producto más valioso por categoría

'''
