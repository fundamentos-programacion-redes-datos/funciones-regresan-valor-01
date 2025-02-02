"""


"""

# Importa el módulo datetime para manejar fechas y obtener el año actual
import datetime

# Define una función en Python que devuelve un valor
def generar_reporte():
    """
    Función que recopila datos de empleados, calcula su edad
    en función del año de nacimiento ingresado y retorna una lista con los datos formateados.
    """
    lista_final = []  # Lista que almacenará los datos ingresados por el usuario
    bandera = True  # Controla la ejecución del bucle while para permitir múltiples ingresos de datos

    # Inicia un bucle para ingresar información de empleados
    while bandera:
        # Captura el nombre y apellido del empleado
        nombre = input("Ingrese nombre de empleado: ")
        apellido = input("Ingrese apellido de empleado: ")

        # Captura y convierte la entrada del año de nacimiento a entero
        anio_nacimiento = input("Ingrese año de nacimiento de empleado: ")
        anio_nacimiento = int(anio_nacimiento)  # Convierte la entrada a entero

        # Calcula la edad utilizando datetime.datetime.now().year
        # Obtiene el año actual y se resta el año de nacimiento
        edad = datetime.datetime.now().year - anio_nacimiento

        # Formatea los datos del empleado en un string y lo agrega a la lista
        datos_empleado = f"Nombre: {nombre}\n" \
                         f"Apellido: {apellido}\n" \
                         f"Edad: {edad}\n" \
                         f"----------||||--------\n"
        lista_final.append(datos_empleado)

        # Solicita al usuario si desea continuar o salir del ciclo
        opcion = input("Ingrese 1 si desea salir del ciclo: ")
        opcion = int(opcion)  # Convierte la entrada a entero

        # Si el usuario ingresa "1", la bandera se cambia a False y el ciclo termina
        if opcion == 1:
            bandera = False

    # Retorna la lista con todos los datos ingresados
    return lista_final

    # Esta función utiliza "return", lo que la convierte en una función que retorna un valor.
    # En este caso, retorna una lista con la información de los empleados.
    # Al ser una función con retorno, su resultado debe ser almacenado en una variable al momento de llamarla.


# Define el punto de entrada principal del script
# Garantiza que el código dentro de este bloque solo se ejecute si el script
# es ejecutado directamente y no si se importa como módulo en otro archivo
if __name__ == "__main__":
    #
    # Llamado a la función "generar_reporte"
    # La función devuelve una lista, por lo que es necesario almacenarla en una variable.
    lista = generar_reporte()

    # Se recorre la lista usando un ciclo for para imprimir cada elemento.
    #  Cada elemento de la lista corresponde a los datos de un empleado formateados.
    for i in lista:
        print(i)



