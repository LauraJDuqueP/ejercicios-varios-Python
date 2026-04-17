'''
🔴 EJERCICIOS PORTAFOLIO — Data Science

🏆 Ejercicio 3 — Sistema de análisis de ventas por región

# Eres analista de datos de una empresa con ventas en 4 ciudades
ventas_por_region = {
    "Bogotá": {
        "enero": 45000000, "febrero": 52000000, "marzo": 48000000,
        "abril": 61000000, "mayo": 58000000, "junio": 67000000
    },
    "Medellín": {
        "enero": 32000000, "febrero": 38000000, "marzo": 35000000,
        "abril": 41000000, "mayo": 44000000, "junio": 49000000
    },
    "Cali": {
        "enero": 28000000, "febrero": 31000000, "marzo": 27000000,
        "abril": 35000000, "mayo": 33000000, "junio": 38000000
    },
    "Barranquilla": {
        "enero": 21000000, "febrero": 24000000, "marzo": 22000000,
        "abril": 28000000, "mayo": 26000000, "junio": 31000000
    }
}

# Calcula y reporta:
# 1. Total de ventas por región en el semestre
# 2. Promedio mensual por región
# 3. Mes con mayores ventas para cada región
# 4. Región con mejor desempeño total
# 5. Mes donde TODAS las regiones crecieron respecto al mes anterior
# 6. Ranking de regiones de mayor a menor venta total
#    (sin usar sorted() — impleméntalo tú con listas)
# 7. Crea un reporte final así:
#    {
#      "region": "Bogotá",
#      "total": ...,
#      "promedio": ...,
#      "mejor_mes": ...,
#      "tendencia": "creciente" si el último mes > primero, si no "decreciente"
#    }
#    para cada región y guárdalos en una lista

'''
ventas_por_region = {
    "Bogotá": {
        "enero": 45000000, "febrero": 52000000, "marzo": 48000000,
        "abril": 61000000, "mayo": 58000000, "junio": 67000000
    },
    "Medellín": {
        "enero": 32000000, "febrero": 38000000, "marzo": 35000000,
        "abril": 41000000, "mayo": 44000000, "junio": 49000000
    },
    "Cali": {
        "enero": 28000000, "febrero": 31000000, "marzo": 27000000,
        "abril": 35000000, "mayo": 33000000, "junio": 38000000
    },
    "Barranquilla": {
        "enero": 21000000, "febrero": 24000000, "marzo": 22000000,
        "abril": 28000000, "mayo": 26000000, "junio": 31000000
    }
}

# 1. Total de ventas por región en el semestre -  2. Promedio mensual por región  - 3. Mes con mayores ventas para cada región


print('\n\t\t---- Reporte ----')
print('\n\t\t 1. El total de ventas por región en el semestre (6 meses), 2. Su promedio mensual, 3. Mes con mayores ventas para cada región \n')

dic1 = {}
for clave_1, clave_2 in ventas_por_region.items():
    
    ventas_region = sum(clave_2.values())
    dic1[clave_1] = ventas_region
    promedio = round(ventas_region/len(clave_1),2)
    formateado = "{:,}".format(ventas_region).replace(",", ".")
    maximo_mes = max(clave_2.values())
    print(f'\t\t- 1. {clave_1}: {formateado} ----- 2. su promedio mensual es de: {f"{promedio:,.2f}".replace(",", "~").replace(".", ",").replace("~", ".")}' \
        f'---- 3. el mes con mayor venta fue: {max(clave_2, key=clave_2.get)} con: {f'{maximo_mes:,.2f}'.replace(',','~').replace('.',',').replace("~", ".")}')
    
# 4. Región con mejor desempeño total
max_desempeno = max(dic1.values())
print(f'\n\t\t-- 4. La region con mejor desempeño este semestre fue: {max(dic1, key= dic1.get)} con {f"{max_desempeno:,.2f}".replace(",", "~").replace(".", ",").replace("~", ".")}')
