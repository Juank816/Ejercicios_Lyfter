#TEMA: Scope
#En todos los lenguajes hay un concepto muy importante llamado scope, o alcance en español.

def declare_variable():
  variable_inside_function_scope = 8
  print(f'Inside function: {variable_inside_function_scope}')


declare_variable()
print(f'Out of function: {variable_inside_function_scope}')

#Scope Global
# La jerarquía de los scopes va de afuera hacia adentro.
# Es decir que las variables declaradas dentro de una función no son accesibles desde afuera, pero las 
# declaradas desde afuera sí son accesibles desde adentro.
# A este alcance le llamamos el scope global, y contiene todas las variables declaradas fuera de funciones.
# Consideremos el siguiente código:
variable_outside_function_scope = 7

def print_variable():
  print(f'Inside function: {variable_outside_function_scope}')


print_variable()
print(f'Outside function: {variable_outside_function_scope}')
