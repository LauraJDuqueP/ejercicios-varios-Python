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