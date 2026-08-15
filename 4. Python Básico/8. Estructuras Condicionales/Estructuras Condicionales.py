#Estructuras Condicionales

#El bloque if
weather = "rainy"

if weather == "rainy":
    # Este código solo se ejecuta si el clima es "rainy"
    print("Me quedo en casa jugando 🎮")
#////////////////////////////////////////////////////////////////
weather = "sunny"

if weather == "rainy":
    print("Me quedo en casa jugando 🎮")


#Alternativas else
weather = "sunny"

if weather == "rainy":
    print("Me quedo en casa jugando 🎮")
else:
    print("Tomo un paseo por el parque 🍃")

#////////////////////////////////////////////////////////////////
temperature = 15

if temperature >= 18:
    print("El día está caliente ☀️")
else:
    print("El día está frío ❄️")

#Múltiples Opciones elif

traffic_light = "red"

if traffic_light == "green":
    print("Avanza 🟢")
elif traffic_light == "yellow":
    print("Precaución 🟡")
elif traffic_light == "red":
    print("Detente 🔴")
else:
    print("Señal desconocida ⚠️")

#Condicionales Anidados

has_ticket = True
age = 16
min_age = 18

if has_ticket:
    print("Tienes boleto, verifiquemos tu edad... 🎟️")

    # Este if vive dentro del anterior
    # Solo se ejecuta si has_ticket es True
    if age >= min_age:
        print("¡Bienvenido a la función! 🍿")
    else:
        print("Lo sentimos, eres menor de edad para esta película 🔞")

else:
    print("Por favor compra un boleto en taquilla 🎫")
    
#Match Case

# Solicitamos la opción al usuario
option = int(input("Selecciona una opción (1-3): "))

# Siempre validamos el valor de la variable option
match option:
    case 1:
        print("Ver perfil 👤")
    case 2:
        print("Ir a Configuración ⚙️")
    case 3:
        print("Cerrar sesión 👋")
    case _:
        print("Opción no válida 🚫")
        
#Buenas prácticas 
is_raining = True

# Redundante (Evita esto)
if is_raining == True:
    print("Está lloviendo")

# Correcto
# "Si está lloviendo..."
if is_raining:
    print("Está lloviendo")
#///////////////////////////////////////////////////////////////////
#Cuando queremos validar si es False:
is_sunny = False

# Redundante
if is_sunny == False:
    print("No hay sol")

# Correcto
# "Si NO hay sol..."
if not is_sunny:
    print("No hay sol") 