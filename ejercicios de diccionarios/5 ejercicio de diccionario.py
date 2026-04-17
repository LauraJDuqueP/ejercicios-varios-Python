'''
🔴 EJERCICIOS PORTAFOLIO — Data Science

🏆 Ejercicio 5 — Análisis de estudiantes y deserción

# Base de datos de un programa académico — detecta patrones de deserción
estudiantes = [
    {"id": "E001", "nombre": "Laura",   "semestre": 3, "notas": [3.2, 4.1, 2.8, 3.9, 2.5], "pagos_al_dia": True,  "asistencia": 78},
    {"id": "E002", "nombre": "Carlos",  "semestre": 2, "notas": [2.1, 1.8, 2.4, 2.0, 1.9], "pagos_al_dia": False, "asistencia": 52},
    {"id": "E003", "nombre": "María",   "semestre": 5, "notas": [4.5, 4.2, 4.8, 4.1, 4.6], "pagos_al_dia": True,  "asistencia": 95},
    {"id": "E004", "nombre": "Pedro",   "semestre": 1, "notas": [2.8, 3.1, 2.5, 2.9, 2.7], "pagos_al_dia": False, "asistencia": 61},
    {"id": "E005", "nombre": "Ana",     "semestre": 4, "notas": [3.8, 3.5, 4.0, 3.7, 3.9], "pagos_al_dia": True,  "asistencia": 88},
    {"id": "E006", "nombre": "Jorge",   "semestre": 2, "notas": [1.5, 2.0, 1.8, 1.6, 2.1], "pagos_al_dia": False, "asistencia": 45},
    {"id": "E007", "nombre": "Lucía",   "semestre": 6, "notas": [4.0, 3.8, 4.2, 3.9, 4.1], "pagos_al_dia": True,  "asistencia": 91},
    {"id": "E008", "nombre": "Andrés",  "semestre": 3, "notas": [2.5, 2.8, 2.3, 2.6, 2.4], "pagos_al_dia": True,  "asistencia": 70},
]

# Analiza:
# 1. Promedio de notas por estudiante — agrégalo como campo "promedio" a cada registro
# 2. Clasificación por rendimiento:
#    "excelente" promedio >= 4.0
#    "bueno"     promedio >= 3.5
#    "regular"   promedio >= 3.0
#    "en riesgo" promedio < 3.0
# 3. Score de deserción por estudiante (0 a 100, donde 100 = máximo riesgo):
#    - promedio < 3.0      → suma 40 puntos
#    - asistencia < 70     → suma 30 puntos
#    - pagos_al_dia False  → suma 30 puntos
# 4. Identifica estudiantes en "alerta roja" — score >= 70
# 5. Estadísticas generales:
#    - Promedio grupal de notas
#    - Promedio grupal de asistencia
#    - Cuántos en cada categoría de rendimiento
#    - Cuántos en alerta roja
# 6. Reporte por semestre — agrupa estudiantes por semestre y muestra
#    promedio de notas y asistencia de cada grupo

'''