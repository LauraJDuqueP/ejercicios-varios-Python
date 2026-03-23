'''
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

'''
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

# 1. Promedio de cada signo vital por paciente durante los 3 días

dias_calcular = 3

   ## Aqui calculo la suma de los signos por los 3 dias
sumaDe_signos = []
def promedio_vital (dia1, dia2, dia3):
    
    for x in range(len(pacientes)): #01234
        lista_signos = []
        suma = 0
        for y in range(len(signos)): #0123
            suma = round(dia1[x][y] + dia2[x][y] + dia3[x][y] , 2)
            lista_signos.append(suma)
        sumaDe_signos.append(lista_signos)
        
promedio_vital(dia_1,dia_2,dia_3)
# print(sumaDe_signos)

   ## aqui / 3 para calcular el promedio de los signos de 3 dias
promedio_vital = []
for x in sumaDe_signos:
    lista = []
    for y in x:
        
        z = round((y/dias_calcular), 2)
        lista.append(z)
    promedio_vital.append(lista)

  ## aqui vamos a unir toda la informacion para imprimir
  ## promedio_vital = [[120.33, 36.53, 80.33, 97.67], [137.67, 38.27, 95.67, 94.33], [118.0, 36.73, 78.0, 98.67], [145.0, 39.03, 98.33, 92.33], [125.67, 37.13, 85.67, 96.67]]
  ## pacientes = ["Paciente_1", "Paciente_2", "Paciente_3", "Paciente_4", "Paciente_5"]
  ## signos = ["Presión", "Temperatura", "Pulso", "Oxigenación"]

print('\t\t------ Promedio de cada signo vital por paciente durante los 3 días ------ ')
for x in range(len(pacientes)): #01234 paciente x
    print(f'\t\t\tPaciente: {pacientes[x]}')
    for y in range(len(signos)): #0123 signo y
        z = promedio_vital[x][y]
        print(f'\t\t\t\t{signos[y]}: {z}')

# 2 Alertas críticas — cada vez que un signo vital esté fuera del rango normal imprime: "🚨 ALERTA: Paciente_X - Día Y - [signo] fuera de rango: [valor]"

print('\t\t------ Alertas críticas ------')
contador = -1
contador_alertas = []
nombres_dias = [f'Día {i+1}' for i in range(len(dias))]
def alertas_criticas(dia):
    lista = []
    global contador
    contador += 1
    for x in range(len(pacientes)): # 01234 pacientes
        suma = 0
        for y in range(len(signos)): # 0123 signos
            if y == signos.index("Presión"):
                z = dia[x][y]
                if 90 <= z <= 130:
                    continue
                else:
                    suma += 1
                    print(f'\t\t\t🚨 ALERTA: {pacientes[x]} - {nombres_dias[contador]} - {signos[y]} fuera de rango: {z}')
            
            elif y == signos.index("Temperatura"):
                z = dia[x][y]
                if 36.0 <= z <= 37.5:
                    continue
                else:
                    suma += 1
                    print(f'\t\t\t🚨 ALERTA: {pacientes[x]} - {nombres_dias[contador]} - {signos[y]} fuera de rango: {z}')
                
            elif y == signos.index("Pulso"):
                z = dia[x][y]
                if 60 <= z <= 100:
                    continue
                else:
                    suma += 1
                    print(f'\t\t\t🚨 ALERTA: {pacientes[x]} - {nombres_dias[contador]} - {signos[y]} fuera de rango: {z}')
                
            elif y == signos.index("Oxigenación"):
                z = dia[x][y]
                if 95 <= z <= 100:
                    continue
                else:
                    suma += 1
                    print(f'\t\t\t🚨 ALERTA: {pacientes[x]} - {nombres_dias[contador]} - {signos[y]} fuera de rango: {z}')
        lista.append(suma)
    contador_alertas.append(lista)     
            
alertas_criticas(dia_1)  
alertas_criticas(dia_2)
alertas_criticas(dia_3) 

#print(contador_alertas)

# 3 Paciente más crítico — el que acumuló más alertas en los 3 días

paciente_critico = []

for i in range(len(pacientes)): #01234  pacientes i
    suma = 0
    for x in range(len(contador_alertas)): #012 alertas x
        suma = suma + contador_alertas[x][i]   
    paciente_critico.append(suma)

#print(paciente_critico)

maximo = max(paciente_critico)
#print(maximo)

print('\t\t------ Los pacientes mas criticos ------')
for paciente, valor in zip(pacientes, paciente_critico):
    if valor == maximo:
        print(f'\t\t\tEl paciente mas critico: {paciente} con {valor} alertas en {contador + 1} dias')

# 4 Tendencia por paciente — comparar el promedio del día 1 vs día 3 de todos sus signos: ¿mejoró o empeoró?
print('\t\t------ Tendencia por paciente ------')
def comprando(dia1, dia2):
    for x in range(len(pacientes)):
        print(f'\t\t\t{pacientes[x]}')
        for y in range(len(signos)):
            if y == signos.index("Presión"):
                if dia1[x][y] > dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Mejoro')
                elif dia1[x][y] < dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Empeoro')
                else:
                     print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Estable')
            elif y == signos.index("Temperatura"):
                if dia1[x][y] > dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Mejoro') 
                elif dia1[x][y] < dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Empeoro')
                else:
                     print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Estable')
            elif y == signos.index("Pulso"):
                if dia1[x][y] > dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Mejoro')
                elif dia1[x][y] < dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Empeoro')
                else:
                     print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Estable')
            elif y == signos.index("Oxigenación"):
                if dia1[x][y] < dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Mejoro')
                elif dia1[x][y] > dia2[x][y]:
                    print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Empeoro')
                else:
                     print(f'\t\t\t\t{signos[y]}: {dia1[x][y]} --> {dia2[x][y]}: Estable')

comprando(dia_1, dia_3)    

           
