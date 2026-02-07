## Aplicacion de Alarma Simple en Python ##

import time
def alarma(hora, minuto):
    while True:
        tiempo_actual = time.localtime()
        hora_actual = tiempo_actual.tm_hour
        minuto_actual = tiempo_actual.tm_min
        
        if hora_actual == hora and minuto_actual == minuto:
            print("¡Alarma! Es hora de despertar.")
            break
        
        time.sleep(30)  # Verificar cada 30 segundos
# Solicitar al usuario la hora y minuto de la alarma
try:
    hora_alarma = int(input("Ingrese la hora de la alarma (0-23): "))
    minuto_alarma = int(input("Ingrese el minuto de la alarma (0-59): "))
    
    if 0 <= hora_alarma <= 23 and 0 <= minuto_alarma <= 59:
        print(f"Alarma configurada para las {hora_alarma:02d}:{minuto_alarma:02d}.")
        alarma(hora_alarma, minuto_alarma)
    else:
        print("Hora o minuto no válidos. Por favor, ingrese valores correctos.")
except ValueError:
    print("Entrada no válida. Por favor, ingrese números enteros para la hora y el minuto.")
    
    