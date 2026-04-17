
######----------------EJERCICIO 3------------------######
###### “Agenda de Turnos con Nombres (sin listas)” ######

## 1. Pedir nombre del operador (solo letras).

operador = input("INGRESA TU NOMBRE: ")
while not operador.isalpha():
    print("!ERROR¡, debe ingresar solo letras, sin espacios")
    operador = input("INGRESA TU NOMBRE: ")

## 2. Menú repetitivo hasta salir:
# 1. Reservar turno
# 2. Cancelar turno (por nombre)
# 3. Ver agenda del día
# 4. Ver resumen general
# 5. Cerrar sistema

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("\nMENU")
    print("1. Reservar turno: ")
    print("2. Cancelar turno:")
    print("3. Ver agenda del día:")
    print("4. Ver resumen general:")
    print("5. Cerrar sistema:")

    ## Validacion del menu
    opcion = input("\nINGRESA UNA OPCION:")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("!ERROR¡, debe ser solo numero (entre 1 - 5) y sin espacios")
        opcion = input("INGRESA UNA OPCION:")
    opcion = int(opcion)

    ## Reservar
    if opcion == 1:
        dia = input("1=Lunes, 2=Martes: ")
        while dia not in ["1", "2"]:
            print("!ERROR¡, opcion valida 1 o 2.")            
            dia = input("1=Lunes, 2=Martes: ")
        dia = int(dia)
        
        nombre = input("\nINGRESA NOMBRE DEL PACIENTE: ")
        while not nombre.isalpha():
            print("!ERROR¡, ingresa solo letras")            
            nombre = input("INGRESA NOMBRE DEL PACIENTE: ")

        if dia == 1:
            if nombre==lunes1 or nombre==lunes2 or nombre==lunes3 or nombre==lunes4:
                print("Ya existe ese turno")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre    
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos para dar.")
        
        if dia == 2:
            if nombre==martes1 or nombre==martes2 or nombre==martes3:
                print("Ya existe ese turno")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre    
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos para dar.")
    
    ## Cancelar turno
    if opcion == 2:
        print("\n-------------Cancelar Turnos-------------\n")
        dia = input("INGRESA EL DIA QUE QUIERES CANCELAR (1=Lunes, 2=Martes): ")
        while dia not in ["1", "2"]:
            print("!ERROR¡, opcion valida 1 o 2.")
            dia = input("INGRESA EL DIA QUE QUIERES CANCELAR (1=Lunes, 2=Martes): ") 
        dia = int(dia)

        nombre = input("\nINGRESA NOMBRE DEL PACIENTE: ")
        while not nombre.isalpha():
            print("!ERROR¡, ingresa solo letras")            
            nombre = input("INGRESA NOMBRE DEL PACIENTE: ")
            
        if dia == 1:
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
            else:
                print("No encontrado")
        
        elif dia == 2:
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
            else:
                print("No encontrado")
    
    ## Ver agenda
    if opcion == 3:
        print("\n------------Agenda de Turnos------------\n")    
        dia = input("INGRESA EL DIA QUE QUIERES VER (1=Lunes, 2=Martes): ")
        while dia not in ["1", "2"]:
            print("!ERROR¡, opcion valida 1 o 2.")
            dia = input("INGRESA EL DIA QUE QUIERES VER (1=Lunes, 2=Martes): ") 
        dia = int(dia)

        if dia == 1:
            print("\nLUNES:\n")
            print("1:", lunes1 if lunes1 != "" else "(libre)")
            print("2:", lunes2 if lunes2 != "" else "(libre)")
            print("3:", lunes3 if lunes3 != "" else "(libre)")
            print("4:", lunes4 if lunes4 != "" else "(libre)")
        elif dia == 2:
            print("\MARTES:\n")
            print("1:", martes1 if martes1 != "" else "(libre)")
            print("2:", martes2 if martes2 != "" else "(libre)")
            print("3:", martes3 if martes3 != "" else "(libre)")
    
    
    ## Resumen General
    if opcion == 4:

        turnosLunes = 0
        turnosMartes = 0
        
        if lunes1 != "": turnosLunes += 1
        if lunes2 != "": turnosLunes += 1
        if lunes3 != "": turnosLunes += 1
        if lunes4 != "": turnosLunes += 1
        
        if martes1 != "": turnosMartes += 1
        if martes2 != "": turnosMartes += 1
        if martes3 != "": turnosMartes += 1
    
        print(f"Dia Lunes {turnosLunes} turnos ocupados, {4 - turnosLunes} turnos libres.")
        print(f"Dia Martes {turnosMartes} turnos ocupados, {4 - turnosMartes} turnos libres.")

        if turnosLunes > turnosMartes:
            print("El dia Lunes tiene mas turnos.")
        elif turnosMartes > turnosLunes:
            print("El dia Martes tiene mayores turnos.")
        else:
            print("!Empate¡, ambos dias tienen la misma cantidad de turnos.")

    ## Cierre del sistema
    if opcion == 5:
        print("\n!Muchas gracias por su visita¡\n")
        break