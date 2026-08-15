user_name = "Andrés"
user_age = 26

#Creamos el mensaje usando f-strings para unir los valores 
Welcome_message = f"¡Hola {user_name}! Tienes {user_age} años."

#Mostramos el mensaje fomrateado 
print(Welcome_message)

#/////////////////////////////////////////////////////////////////////////////////////
item_name = "PC Gamer"

item_price = 800

# Formateamos el texto con el método format

price_tag = "El {} tiene un costo de {} USD.".format(item_name, item_price)

# Mostramos el mensaje final

print(price_tag)