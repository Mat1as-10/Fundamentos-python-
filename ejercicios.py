# La empresa certifica necesita de nuestros servicios como desarrolladores y nos solicita realizar un programa que cumpla con las siguientes condiciones: 
# Alumnos con calificaciones mayor a 6.0 recibiran un dcto del 20%
# Alumnos con calificaciones mayores a 5.0 obtendran un dcto del 15% 
# Alumnos con calificaciones mayores a 4.0 recibiran solo un 10% 
# El que no cumpla con estos requisitos lo ivitamos a seguir esforzandose... 


Nombre = (input("Bienvenido, ingresa tu nombre: "))

Nota = float(input(f"Bienvenido {Nombre} , ingresa tu calificacion: "))

if Nota > 4.0:
    print ("Bien, has obtenido un descuento del 10%")
elif Nota > 5.0:
    print ("Felicitaciones, has obtenido un descuento del 15%")
elif Nota > 6.0:
    print ("Excelente, Felicidades has obtenido un descuento del 20%")
else: 
    print ("Has reprobado, sigue intentandolo. ") 