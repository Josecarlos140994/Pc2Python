##Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
##en el rango de 1500 y 2700 (ambos incluidos).

n_divisibles = []

# Iterando en el rango dado

for numero in range(1500, 2701):  
    if numero % 7 == 0 and numero % 5 == 0:
        n_divisibles.append(numero)

print("Números que son divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")

print(n_divisibles)
