# se intenta el ingreso a un servidor pero como no tiene acceso 
# muestra un aviso denegado.
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def conectar_servidor():
    logging.info("Intentando conectar con el servidor...")
    conexion_exitosa = False
    
    if not conexion_exitosa:
        logging.error("No se pudo establecer conexión con el servidor.")

conectar_servidor()




