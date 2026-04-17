
### Ejercicio 4  — “Escape Room: La Bóveda” ###

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzarSeguida = 0

print("\n----------“Escape Room: La Bóveda”--------------------\n")
nombre = input("\nINGRESA EL NOMBRE: \n")
while not nombre.isalpha():
    print("\n!ERROR¡, Ingresa solo letras para el nombre.")
    nombre = input("\nINGRESA EL NOMBRE: ")

while (energia>0 and tiempo>0 and cerraduras_abiertas<3 and not alarma):
    print("\nESTADO JUGADOR:")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")


    print("\nMENU")
    print("1. FORZAR CERRADURA (costo: -20 energia, -2 tiempo): ")
    print("2. HACKEAR PANEL (costo: -10 energia, -3 tiempo):")
    print("3. DESCANSAR (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra):")


    ## Validacion del menu
    opcion = input("\nINGRESA UNA OPCION:")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("!ERROR¡, debe ser solo numero (entre 1 - 3) y sin espacios")
        opcion = input("INGRESA UNA OPCION:")
    opcion = int(opcion)

    ## FORZAR CERRADURA OPCION 1
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzarSeguida += 1
        print(f"Seguidas de forzadas {forzarSeguida}")
        
        if forzarSeguida == 3:
            print("!ERROR¡ Forzaste 3 veces seguidas. La cerradura se trabó.")
            alarma = True
            continue
        
        while not energia<20 and tiempo<2:
            print("!LO SIENTO¡ Ya no tienes recursos para esto.")
            continue
        
        if energia < 40 and energia > 0:
            print("!PRECAUCION¡ Riesgo de alarma.")
            numero = input("Ingresa un numero del 1 al 3: ")
            
            while not numero.isdigit():
                print("!ERROR¡ ")
                numero = input("Ingresa un numero del 1 al 3: ")
            if int(numero) == 3:
                print("!Se activo la alarma¡")
                alarma = True
                continue
        if not alarma:
            print("!GENIAL¡ Abriste una cerradura")
            cerraduras_abiertas += 1   
    else:
        forzarSeguida = 0
        
        if alarma==True and tiempo<=3 and cerraduras_abiertas<3:
            print("\n!PERDISTE¡ Sistema bloqueado por alarma")
            break
    
    # HACKEAR PANEL OPCION 2
    if opcion == 2: # (costo: -10 energia, -3 tiempo)
        energia -= 10
        tiempo -= 3
        
        print("\n Iniciando Hackeo...\n")
        for i in range(4):
            
            print(f"Progeso: Paso {i+1}/4")
            codigo_parcial += 'A'
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("!EXITO¡ Cerradura abierta")
        if alarma==True and tiempo<=3 and cerraduras_abiertas<3:
            print("\n!PERDISTE¡ Sistema bloqueado por alarma")
            break
    
    # DESCANSAR  OPCION 3 (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)
    if opcion == 3:
        energia += 15
        tiempo -= 1
        
        if energia > 100:
            energia = 100
        
        if alarma == True:
            energia -= 10
            print("\n!CUIDADO¡ La alarma activada gasta energía.")
        print("\n!Descansaste y recuperaste¡\n")
        
        if alarma==True and tiempo<=3 and cerraduras_abiertas<3:
            print("\n!PERDISTE¡ Sistema bloqueado por alarma")
            break
        
print("\n----------RESULTADO FINAL-------------")
if cerraduras_abiertas == 3:
    print("\n!VICTORIA¡ Lograste abrir las 3 cerraduras.\n")
elif energia <= 0 or tiempo <= 0:
    print("\n!DERROTA¡ Por falta de recursos.\n")
elif alarma == True:
    print("\n!DERROTA¡ Por bloqueo.\n")

