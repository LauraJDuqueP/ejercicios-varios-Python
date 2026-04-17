'''
🔴 EJERCICIOS PORTAFOLIO — Data Science

🏆 Ejercicio 4 — Pipeline de limpieza de datos

# Eres Data Scientist y recibes datos crudos con problemas típicos del mundo real
datos_crudos = [
    {"id": 1, "nombre": "  María García ", "edad": 28,   "salario": "2500000", "ciudad": "bogotá",   "activo": "si"},
    {"id": 2, "nombre": "CARLOS LÓPEZ",    "edad": None, "salario": "3200000", "ciudad": "Medellín", "activo": "no"},
    {"id": 3, "nombre": "ana martinez",    "edad": 35,   "salario": None,      "ciudad": "CALI",     "activo": "si"},
    {"id": 4, "nombre": "Pedro Ruiz  ",    "edad": 200,  "salario": "1800000", "ciudad": "bogotá",   "activo": "si"},
    {"id": 5, "nombre": "  LUCIA VERA",    "edad": 29,   "salario": "4100000", "ciudad": "medellín", "activo": "no"},
    {"id": 6, "nombre": "Jorge Castro",    "edad": 41,   "salario": "2900000", "ciudad": "Cali",     "activo": "si"},
    {"id": 7, "nombre": "  ",              "edad": 33,   "salario": "3500000", "ciudad": "Bogotá",   "activo": "si"},
]

# Tu pipeline debe:
# 1. Limpiar nombres — strip() de espacios, capitalizar correctamente
# 2. Eliminar registros con nombre vacío o solo espacios
# 3. Convertir salario a entero — si es None asignar el promedio de los demás salarios
# 4. Validar edades — si es None o mayor a 100 reemplazar por la edad promedio
# 5. Estandarizar ciudades — primera letra mayúscula, resto minúscula
# 6. Convertir activo — "si" → True, "no" → False
# 7. Agregar campo "nivel_salario":
#    - "bajo" si salario < 2500000
#    - "medio" si entre 2500000 y 3500000
#    - "alto" si > 3500000
# 8. Reporte final:
#    - Cuántos registros entraron vs cuántos salieron limpios
#    - Promedio de edad del dataset limpio
#    - Cuántos activos vs inactivos
#    - Distribución de nivel_salario — cuántos en cada nivel

'''
