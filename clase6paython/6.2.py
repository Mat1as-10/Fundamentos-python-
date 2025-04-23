Promedio = float(input("Ingresa tu calificacion: "))
Quintil = int(input("Ingresa el quintil: 1,2,3 etc  "))
Descuento_A = 0
Descuento_B = 1
Descuento_C = 2

if Quintil == 1:
    print (f"Felicidades {Descuento_A}")
if Quintil == 2:
    print (f"Felicitaciones {Descuento_B}")
if Quintil == 3:
    print (f"Felicitaciones {Descuento_C}")
if Quintil == 0:
    print ("Lo lamento.")