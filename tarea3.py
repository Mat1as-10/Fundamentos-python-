lista_producto = []

print (" Bienvenido haz tu lista.")

producto1 = input("ingresa tu producto: ")
producto2 = input("ingresa tu producto: ")

lista_producto.append (producto1) 
lista_producto.append (producto2)

print (f"Tu lista es {lista_producto}")

mod_producto = input ("quieres cambiar un producto? Escribelo:")
lista_producto[1] = mod_producto


print (f"esta es tu nueva lista: {lista_producto}")

