##Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
##ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
##números.
##Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
##números pares e impares.
##
##
##


# Lista para almacenar los números ingresados por el usuario
numeros = []

while True:
    
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    

    if respuesta == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)

    elif respuesta == "NO":
        break
    
    else:
        print("Respuesta no válida. Por favor, ingrese SI o NO.")

# numeros de pares e impares
        
pares = 0
impares = 0

# Iterar sobre la lista de números y contar pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares += 1            ##contador
    else:
        impares += 1          ##contador

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
