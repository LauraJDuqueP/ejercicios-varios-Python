--------------------------------------------------------------
🏋️ Ejercicio 2 — Nivel medio | Monitoreo de pacientes
Un hospital registra 4 signos vitales de 5 pacientes durante 3 días:

pacientes = ["Paciente_1", "Paciente_2", "Paciente_3", "Paciente_4", "Paciente_5"]

signos = ["Presión", "Temperatura", "Pulso", "Oxigenación"]

# Cada elemento es [Presión, Temperatura, Pulso, Oxigenación]
dia_1 = [[120, 36.5, 80, 98], [135, 37.2, 92, 96], [118, 36.8, 78, 99], [142, 38.1, 95, 94], [125, 37.0, 85, 97]]
dia_2 = [[122, 36.7, 82, 97], [138, 38.5, 96, 94], [116, 36.5, 76, 99], [145, 39.2, 98, 92], [128, 37.3, 88, 96]]
dia_3 = [[119, 36.4, 79, 98], [140, 39.1, 99, 93], [120, 36.9, 80, 98], [148, 39.8, 102, 91], [124, 37.1, 84, 97]]

dias = [dia_1, dia_2, dia_3]

# Rangos normales
rangos = {
    "Presión":      [90, 130],
    "Temperatura":  [36.0, 37.5],
    "Pulso":        [60, 100],
    "Oxigenación":  [95, 100]
}

Calcula:

Promedio de cada signo vital por paciente durante los 3 días
Alertas críticas — cada vez que un signo vital esté fuera del rango normal imprime: "🚨 ALERTA: Paciente_X - Día Y - [signo] fuera de rango: [valor]"
Paciente más crítico — el que acumuló más alertas en los 3 días
Tendencia por paciente — comparar el promedio del día 1 vs día 3 de todos sus signos: ¿mejoró o empeoró?

----------------------------------------------------------------------------------------

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

---------------------------------------------------------

🔥 Ejercicio 4 — Nivel difícil | Análisis financiero

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

departamentos = ["Ventas", "Marketing", "Tecnología", "RRHH", "Operaciones"]

# Ingresos mensuales por departamento
ingresos = [
    [85, 92, 78, 95, 88, 102, 98, 105, 91, 87, 115, 125],   # Ventas
    [45, 48, 42, 51, 49, 55,  52, 58,  47, 44, 62,  68 ],   # Marketing
    [62, 65, 70, 68, 72, 75,  71, 78,  69, 67, 80,  85 ],   # Tecnología
    [28, 29, 27, 31, 30, 32,  29, 33,  28, 27, 35,  38 ],   # RRHH
    [95, 98, 88, 102,96, 108, 104,112, 99, 93, 118, 130],   # Operaciones
]

# Presupuesto mensual por departamento
presupuesto = [90, 50, 65, 30, 100]  # uno por departamento

Calcula:

Variación mensual de cada departamento — diferencia entre cada mes y el anterior. ¿En qué mes tuvo su mayor crecimiento cada departamento?
Meses deficitarios por departamento — meses donde el ingreso estuvo por debajo del presupuesto. Imprime cuántos meses estuvo por debajo y el promedio de déficit
Trimestres — agrupa los meses en 4 trimestres y calcula el total por departamento por trimestre
Departamento más consistente — el que tiene menor desviación entre sus meses. Fórmula desviación: sqrt(suma((x - promedio)²) / n) — impleméntala sin importar librerías
Proyección anual — usando el promedio de crecimiento mensual de cada departamento, proyecta cuánto generaría el mes 13