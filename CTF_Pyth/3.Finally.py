# en la linea 4 se provocara un error ya que la division no se puede realizar
try:
    print("Abriendo sesión de usuario...")
    resultado = 10 / 0  
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
finally:
    print("Cerrando sesión de usuario de forma segura...")
    
    
    
    