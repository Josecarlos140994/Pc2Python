def convertir_fecha(fecha_input):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
 
    try:
        partes = fecha_input.split('/')
        if len(partes) == 3:
            año, mes, dia = partes[2], partes[0].zfill(2), partes[1].zfill(2)
            return f"{año}-{mes}-{dia}"
    except ValueError:
        pass
    

    try:
        mes_texto, dia, año = fecha_input.replace(',', '').split()
        mes = str(meses.index(mes_texto) + 1).zfill(2)
        return f"{año}-{mes}-{dia.zfill(2)}"
    except ValueError:
        return "Formato de fecha no reconocido."


fecha_input = input("Ingrese una fecha: ")
fecha_output = convertir_fecha(fecha_input)
print(f"Output: {fecha_output}")