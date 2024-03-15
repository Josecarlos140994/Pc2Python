##Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
##Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
##
##Ejemplo:
##Número ingresado: 15789000 y Dígito: 0
##Cantidad de veces 0 en el número: 4
##
##Nota: Para resolver este problema, algunos tipos de datos dentro de python contemplan un método
##count.

def contar_digito_en_numero(numero, digito):
    """
    Función para contar cuántas veces aparece un dígito específico dentro de un número entero.

    Parámetros:
    numero (int): El número entero en el que se buscará el dígito.
    digito (int): El dígito cuya cantidad de apariciones se desea contar.

    Retorna:
    int: La cantidad de veces que el dígito aparece dentro del número.
    """
    
    numero_str = str(numero)
    digito_str = str(digito)
    
    cantidad = numero_str.count(digito_str)
    
    return cantidad

resultado = contar_digito_en_numero(15789000, 0)

print(f"Cantidad de veces que el dígito aparece en el número: {resultado}")
