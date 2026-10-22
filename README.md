# Herramientas para resolver errores
<p>Dentro de la programacion se sabe que los errores son inevitables, existen demasiados motivos para que esto pueda ocurrir, y gracias a estos, nustros programas pueden llegaar a tener un comportamiento diferente a como lo esperamos incluso llegar a detenerse por completo. por esta razon es muy importante aprender a identificarlos y responder ante ellospara asi poder crear un codigo estable, adaptable y facil de mantener.</p>

### Herramientas implementadas:

##### Try:
<p> en él se coloca el código “riesgo”,  es decir, las instrucciones que podrían fallar durante su ejecución (abrir archivos, conectarse a una red o dividir los números). en el python intentará ejecutar las líneas normalmente, pero si ocurre una falla o excepción durante su proceso, la ejecución se parará de inmediato y en ese momento buscará una solución. </p>

##### Except:
<p> se captura la gestión del problema por si algo sale mal dentro del bloque “try”. En este se define exactamente que debe de hacer el programa cuando ocurre una excepción específica (como mostrar un mensaje claro al usuario o usar un valor por defecto). esto para evitar que el programa colapse repentinamente y le permite recuperarse o continuar de manera ordenada.
 </p>

##### Finally:
<p> bloque de limpieza que se ejecuta siempre, sin importar si el bloque try funciono correctamente o si ocurre una excepción que detuvo el programa. Se utiliza para liberar recursos críticos que no deben quedar abiertos bajo ninguna circunstancia, como el cerrar archivos de texto, finalizar conexiones a bases de datos o desconectarse de servidores. </p>

##### Raise:
<p> Dentro de esta instrucción se permite provocar una excepción de forma manual en el momento que tu como programador lo decides, esta se utiliza cuando se detecta que una condición o lógica se ha violado y se necesita interrumpir el flujo normal para obligar a que la situación sea tratada como un error. </p>

##### Assert:
<p> sirve como herramienta de depuración integrada diseñada para verificar si se cumplen condiciones específicas durante la ejecución del programa, en ella se prueban suposiciones falsas dentro del código, generará de inmediato un AssertionError, esta herramienta se usa principalmente durante la fase de desarrollo para comprobar que los supuestos internos del código se mantengan correctos esto ayuda a los desarrolladores a identificar y resolver rápidamente los errores lógicos. </p>

##### Exc_Pers:
<p> además de manejar excepciones integradas, también podemos definir nuestras propias excepciones personalizadas, útil para representar errores específicos a la lógica de la aplicación, permitiendo gestionar errores con mayor precisión. </p>

##### Loggin:
<p>  los logging son herramientas que permiten registrar los eventos y acciones que ocurren durante la ejecución de un programa. Su principal función es ayudar a identificar, analizar y solucionar errores o fallas , en esos registros se pueden contener información como la fecha, la hora, tipo de evento y mensaje relacionado con el problema. también permite llevar un historial de lo que sucede dentro del sistema . </p>
