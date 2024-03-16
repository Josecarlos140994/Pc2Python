##Escriba una función de Python que tome un número como parámetro y verifique que el número sea
##primo o no.

## definimos la funcion

def es_primo(numero):

    if numero <= 1:
        return False
    
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")
