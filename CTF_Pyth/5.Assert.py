# aplicacion de descuento cambiar la linea 7 cambia el texto por este.. 
# aplicar_descuento(100, 1.5)
def aplicar_descuento(precio, descuento):
    assert 0 <= descuento <= 1, "El descuento debe estar entre 0 (0%) y 1 (100%)"
    return precio * (1 - descuento)

print(f"Precio con descuento: ${aplicar_descuento(100, 1.5)}")




