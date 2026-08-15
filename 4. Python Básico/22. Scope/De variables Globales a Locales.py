#TEMA: Scope
#De variables globales a variables locales

# Usar variables globales no es recomendado - siempre debemos usar variables locales (declaradas 
# dentro de funciones) y pasarlas de función a función usando parámetros y returns.
# Veamos este ejemplo donde tenemos una lista global que es referenciada en varias funciones.

numbers_list = [53, 60, 32, 62, 400, 10]


def remove_tenths():
  index = 0
  while (index < len(numbers_list)):
    if numbers_list[index] % 10 == 0:
      numbers_list.pop(index)
    else:
      index += 1


def multiply_numbers_by_2():
  for index, number in enumerate(numbers_list):
    numbers_list[index] = number * 2


def main():
  remove_tenths()
  multiply_numbers_by_2()
  print(numbers_list)


if __name__ == "__main__":
  main()



#La manera correcta de arreglar este común problema es convertirla en una variable local dentro del 
# entrypoint y pasarla al resto de funciones como un parámetro.
def remove_tenths(numbers_list):
    index = 0
    while (index < len(numbers_list)):
        if numbers_list[index] % 10 == 0:
         numbers_list.pop(index)
        else:
            index += 1


def multiply_numbers_by_2(numbers_list):
  for index, number in enumerate(numbers_list):
    numbers_list[index] = number * 2


def main():
  numbers_list = [53, 60, 32, 62, 400, 10]
  remove_tenths(numbers_list)
  multiply_numbers_by_2(numbers_list)
  print(numbers_list)


if __name__ == "__main__":
  main()