
######----------------EJERCICIO 2------------------######
###### “Acceso al Campus y Menú Seguro” ######


## 1. Definir credenciales fijas en el código: ##
# usuario = "alumno"
# clave = "python123"

## 2. Permitir máximo 3 intentos para ingresar usuario y clave.
intentos = 3

while intentos > 0:
    usuario = input("\nINGRESA EL USUARIO: ")
    clave = input("INGRESA LA CLAVE: ")
    if usuario == "alumno" and clave == "python123":
        print("\nBIENVENIDO AL CAMPUS")
        break
    else:
        print("\nUSUARIO O CLAVE INCORRECTA")
    intentos -= 1

## 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
    if intentos == 0:
        print("\nCuenta bloqueada")
        exit()   

## 4. Si ingresa bien: mostrar un menú repetitivo
acceso = 0
while acceso != 4:
    print("\nMENU")
    print("1. Ver estado de inscripción.")
    print("2. Cambiar clave.")
    print("3. Mostrar mensaje motivacional.")
    print("4. Salir.")
    
    ## Validacion del menu   
    acceso = (input("\nINGRESA UNA OPCION: "))
    while not acceso.isdigit() or int(acceso) == 0:
        print("!ERROR¡, debe ser solo numero (entre 1 - 4) y sin espacios")
        acceso = input("INGRESA UNA OPCION: ")
    acceso = int(acceso)
    
    while acceso < 1 or acceso > 4:
        print("Error: opción inválida (1-4)")
        acceso = input("Ingrese una opción: ")

    if acceso == 1:
        print("\nESTADO: INSCRIPTO")
    elif acceso == 2:
        print("\nCAMBIAR CLAVE")
        claveNueva = input("INGRESA LA NUEVA CLAVE: ")
        
        #validar longitud
        while len(claveNueva) < 6:
            print("!ERROR¡, la clave debe tener al menos 6 caracteres")
            claveNueva = input("INGRESA LA NUEVA CLAVE: ")
        
        confirmacion = input("CONFIRMA LA NUEVA CLAVE: ")
        
        #validar misma clave
        while claveNueva != confirmacion:
            print("!ERROR¡, las claves no coinciden")
            confirmacion = input("CONFIRMA LA NUEVA CLAVE: ")
        
        claveCorrecta = confirmacion
        print("\n CLAVE ACTUALIZADA DE FORMA EXITOSA.")

    elif acceso == 3:
        print("\n!!! No programes para que la computadora te entienda, programa para construir el mundo que imaginas. !!!")
    elif acceso == 4:
        print("\nGRACIAS POR USAR EL CAMPUS...")
        
    
