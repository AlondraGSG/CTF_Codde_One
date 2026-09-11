# en la linea 11, cambiaremos el numero del parentesis para definir si es mayor e ingresa o no.
class MenorDeEdadError(Exception):
    pass

def entrar_al_club(edad):
    if edad < 18:
        raise MenorDeEdadError("Acceso denegado: Debes ser mayor de 18 años.")
    print("Bienvenido al club.")

try:
    entrar_al_club(12)
except MenorDeEdadError as e:
    print(f"Entrada rechazada: {e}")
    
    
    
    