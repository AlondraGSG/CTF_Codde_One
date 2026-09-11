#en la linea de codigo 5 cambia el numerode posicion para imprimir el numero de la lista
try:
    lista = [10, 20, 30]
    # Accedemos al índice 0 (el numero es 10
    elemento = lista[0]
    print(f"Ingresaste con éxito a la lista. El elemento en esa posición es: {elemento}")
except IndexError:
    print("Error: Intentaste acceder a una posición fuera del rango de la lista.")
    
    
    
    