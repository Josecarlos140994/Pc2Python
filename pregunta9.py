

def eliminar_vocales(texto):
    vocales = "aeiouAEIOU"
    tsin_vocales = ""

    for caracter in texto:

        if caracter not in vocales:
            tsin_vocales += caracter

    return tsin_vocales

t_usuario = input("Ingrese un texto: ")

print("Texto sin vocales:", eliminar_vocales(t_usuario))