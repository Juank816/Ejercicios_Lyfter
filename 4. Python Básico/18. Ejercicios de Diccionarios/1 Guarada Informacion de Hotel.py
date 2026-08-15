#Ejercicios de Diccionarios: DICCIONARIO QUE GUARDA LA INFORMACIÓN SOLCITADA
'''Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones'''


print("---- Diccionario que guarda la información de un Hotel  ----")

#Declaramos el diccionario que guarda la información solicita 
hotel = {
    "name" : "",
    "star_count" : 5,
    "hotel_rooms" : [
        {"number_room" : 10,
        "floor" : 3,
        "nightly_price" : 200,
        },
        
        {
        "number_room" : 10,
        "floor" : 3,
        "nightly_price" : 200,
        },
    ], 
}

#print(hotel['nightly_price']) # si queda esta línea se crashea
print(hotel.get('nightly_price'))

