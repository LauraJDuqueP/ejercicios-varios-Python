'''
🔴 EJERCICIOS PORTAFOLIO — Data Science

🏆 Ejercicio 7 — Análisis completo de encuesta

# Resultados de encuesta de satisfacción — empresa de tecnología
respuestas = [
    {"id": 1,  "area": "Desarrollo",  "cargo": "Junior",  "satisfaccion": 7,  "recomendaria": True,  "años": 1, "salario": 3200000},
    {"id": 2,  "area": "Datos",       "cargo": "Senior",  "satisfaccion": 9,  "recomendaria": True,  "años": 5, "salario": 7800000},
    {"id": 3,  "area": "Diseño",      "cargo": "Junior",  "satisfaccion": 5,  "recomendaria": False, "años": 2, "salario": 2900000},
    {"id": 4,  "area": "Desarrollo",  "cargo": "Senior",  "satisfaccion": 8,  "recomendaria": True,  "años": 6, "salario": 8200000},
    {"id": 5,  "area": "Datos",       "cargo": "Junior",  "satisfaccion": 6,  "recomendaria": False, "años": 1, "salario": 3500000},
    {"id": 6,  "area": "Diseño",      "cargo": "Senior",  "satisfaccion": 4,  "recomendaria": False, "años": 4, "salario": 6100000},
    {"id": 7,  "area": "Desarrollo",  "cargo": "Junior",  "satisfaccion": 8,  "recomendaria": True,  "años": 2, "salario": 3800000},
    {"id": 8,  "area": "Datos",       "cargo": "Senior",  "satisfaccion": 10, "recomendaria": True,  "años": 7, "salario": 9500000},
    {"id": 9,  "area": "Diseño",      "cargo": "Junior",  "satisfaccion": 6,  "recomendaria": True,  "años": 1, "salario": 2800000},
    {"id": 10, "area": "Desarrollo",  "cargo": "Senior",  "satisfaccion": 7,  "recomendaria": True,  "años": 3, "salario": 7200000},
]

# Analiza:
# 1. Promedio de satisfacción por área
# 2. Promedio de salario por cargo (Junior vs Senior)
# 3. NPS (Net Promoter Score):
#    NPS = (cantidad que recomendaría / total) * 100
# 4. Correlación simple satisfacción vs años de experiencia:
#    para cada empleado calcula satisfaccion * años
#    promedia esos productos — ¿los más experimentados están más satisfechos?
# 5. Segmentación de empleados:
#    "embajador"    satisfaccion >= 8 y recomendaria True
#    "neutro"       satisfaccion entre 6 y 7
#    "en riesgo"    satisfaccion <= 5 o recomendaria False
# 6. Área con mayor riesgo de rotación — la que tiene más empleados "en riesgo"
# 7. Reporte ejecutivo final — un diccionario con todos los hallazgos
#    que puedas presentar como entregable a una empresa

'''