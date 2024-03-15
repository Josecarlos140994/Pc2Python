##Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
##pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
##materias.
##Puede usar el siguiente esquema a manera de ejemplo
##{
##Alumno: Juan,
##Notas: [10, 12, 15]
##}
##Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
##completo de los alumnos.


# Paso 1: Solicitar cuántos alumnos se van a registrar
numero_alumnos = int(input("¿Cuántos alumnos se registraran? "))

lista_alumnos = []

for i in range(numero_alumnos):
    nombre = input(f"Nombre del alumno {i+1}: ")
    
    #lista vacía para las calificaciones

    notas = []
    
    # Solicitar las 3 calificaciones
    for j in range(3):
        nota = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        notas.append(nota)

    # Crear un diccionario 
    alumno = {"Alumno": nombre, "Notas": notas}
    lista_alumnos.append(alumno)

print("\nListado de alumnos y sus calificaciones:")
for alumno in lista_alumnos:
    print(alumno)