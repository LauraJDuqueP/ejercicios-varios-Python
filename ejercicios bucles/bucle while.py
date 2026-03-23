## 🏋️ DESAFÍO 2 — Bucle while

'''
Vas a simular un cajero automático:

saldo = 850000 # Saldo inicial de la cuenta
retiros = [] # Lista vacía donde guardarás cada retiro

El cajero debe funcionar así:

Mientras el saldo sea mayor a cero, preguntar cuánto quiere retirar el usuario con input()
Si el retiro es mayor al saldo disponible → mostrar mensaje de error y volver a preguntar
Si el retiro es válido → descontar del saldo, guardar el valor en la lista retiros
Si el usuario escribe 0 → salir del cajero
Al terminar, mostrar cuántos retiros hizo y el saldo final

Pistas:

Recuerda que input() devuelve texto — necesitas convertirlo a número con int()
Necesitarás break en algún momento
La lista retiros guarda historial — para agregar elementos usa retiros.append(valor)
''' 

saldo = 850000 # Saldo inicial de la cuenta
retiros = [] # Lista vacía donde guardarás cada retiro

print('\tEste es un cajero automatico \n\tQuieres retirar dinero?')
c = input('\ts para si - n para n: ')

if c == 's':
    while(saldo > 0):
        valor = int(input('\t\tCuanto dinero quieres retirar: '))
        
        if valor == 0:
            print(f'\t--Gracias por sus servicios-- \n\t\tSu nuevo saldo es de {saldo} \n\t\tHizo {len(retiros)} retiros')
            
            break
        elif valor <= saldo:
            saldo = saldo - valor
            retiros.append(valor)
            print(f'\t\tEl valor a retirar es de {valor} \n\t\tSu nuevo saldo es de: {saldo}')
            
        elif valor > saldo:
            print(f'\t\t\tEl valor que quiere retirar excede el monto. Su saldo disponible es: {saldo}')
else:
    print('Vuelva a intentarlo')