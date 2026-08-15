#Ejercicios de Manejo de JSON: Programa que permita agregar info al archivo de la lección de Manejo de JSON.
'''Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de Manejo de JSON.
Debe leer el archivo para importar los Pokémones existentes.
Luego debe pedir la información del Pokémon a agregar.
Finalmente debe guardar el nuevo Pokémon en el archivo.'''
#Importamos librería
import json


def add_json(file_patch, pokemon):
    with open(file_patch, 'w', encoding='utf-8') as file:
        data = json.dump(pokemon, file, indent=4)


def give_information():
    pokemon = {}

    name = input("Ingrese el nombre del nuevo pokemon: ")
    hp = int(input("Ingrese los HP: "))
    type = input("Ingrese el tipo: ")
    pokemon["name"] = name
    pokemon["hp"] = hp
    pokemon["type"] = type 
    
    return pokemon


def read_pokemon(file_patch):
    with open(file_patch, 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(data)
    return data


def main():
    data = read_pokemon('pokemon.json')
    new_pokemon = give_information()
    data.append(new_pokemon)
    add_json('pokemon.json', data)


if __name__ == "__main__":
    main()