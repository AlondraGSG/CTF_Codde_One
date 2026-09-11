# en la linea 9 agregar una contraseña de 8 o mas caracteres para validar.
# si son menos caracteres no la validara y dara un error.
def validar_password(password):
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    print("Contraseña válida.")

try:
    validar_password("12345")
except ValueError as error:
    print(f"Error de validación: {error}")
    
    
    