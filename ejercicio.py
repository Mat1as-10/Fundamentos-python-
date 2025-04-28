# Necesitamos generar un programa en python que permita generear numeros aleatorios dentro de un rango definido por el usuario y ajustarlos dividiendolos entre 4
# Luego el usuario debe dar un numero para luego dividirlo nuevamente entre un macimo de 3 intentos 
#Condiciones del juego:
# 1. Ingreso de datos: 
# A: el usuario ingresa dos numeros entereos que representanel rango numerico
# B: El primer numero debe ser menor que el segundo
# 2. Generacion del numero aleatorio:
# A: Si se eligierse un numero aleatorio dentro del rango ingresado 
# B: El numero se ajusta dividiendolo entre 4 y redondeandolo al multiplo de 4 mas cercano 
# 3. Inteno del usuario 
# A: Primer intento: si el usuario acierta se muestra el mensaje "Felicitaciones, adivinaste al primer intento"
# B: Segundo intento: si el usuario no acierta se indicara si el numero es mayor o menor 
# C: Tercer intento: si no acierta se le devuelve a dar una pista 
# D: Resultado final:  si no acierta en los 3 intentos el programa muestra el mensaje "Perdiste, el numero es incorrecto"


import random

def ajustar_a_multiplo_4(numero):
    return round(numero / 4) * 4

def juego_adivinanza():
    print("Bienvenido al juego de adivinanza de números.")
    
   
    while True:
        try:
            minimo = int(input("Ingresa el valor mínimo del rango: "))
            maximo = int(input("Ingresa el valor máximo del rango: "))
            if minimo >= maximo:
                print("El primer número debe ser menor que el segundo. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor ingresa solo números enteros.")
    
    
    numero_aleatorio = random.randint(minimo, maximo)
    
    
    numero_ajustado = ajustar_a_multiplo_4(numero_aleatorio)
    
    print(f"Un número aleatorio ha sido generado dentro del rango {minimo} y {maximo}. El número ha sido ajustado.")

   
    intentos = 0
    while intentos < 3:
        intento_usuario = int(input(f"Intento {intentos + 1}: Ingresa tu adivinanza (debes adivinar el número ajustado): "))
        intentos += 1
        
        if intento_usuario == numero_ajustado:
            print("¡Felicitaciones, adivinaste al primer intento!")
            break
        elif intentos == 1:
            if intento_usuario < numero_ajustado:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        elif intentos == 2:
            print("Último intento.")
            if intento_usuario < numero_ajustado:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        elif intentos == 3:
            print(f"Perdiste, el número era {numero_ajustado}.")
            break


juego_adivinanza()