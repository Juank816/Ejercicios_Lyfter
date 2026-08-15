#Ejercicios Extras de Sintaxis: CALCULAR DESCUENTO DE PRODUCTO FINAL
'''Cree un programa que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
Si el precio es menor a 100, el descuento es del 2%.
Si el precio es mayor o igual a 100, el descuento es del 10%.'''

print ("---- Calcula descuento de producto ----")


#Declaración de variables
#////////////////////////////////////////////////
product_price = float
discount = float
final_price = float

product_price = 0
discount = 0
final_price = 0

#Pedir información a cliente
product_price = float(input("Ingrese el precio del producto: "))

#Condición
if product_price < 100:
    discount = product_price * 0.02
else:
    discount = product_price * 0.10

#Operación final
final_price = product_price - discount

#Inforamción a mostrar 
print(f"El precio final con el descuento del producto es: {final_price}")