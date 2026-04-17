
## Ejercicio 5  — “Escape Room:"La Arena del Gladiador" ##

print("\n********Escape Room:La Arena del Gladiador***********\n")

vidaGladiador = 100
vidaEnemigo = 100
pocionVida = 3
dañoAtaquePesado = 15
dañoEnemigo = 12
turnoGladiador = True

# CONFIGURACION DE PERSONAJE
print("\n-------BIENVENIDO AL ARENA------------\n")
nombre = input("\nINGRESA EL NOMBRE DE TU GLADIADOR: ")
while not nombre.isalpha():
    print("\n!ERROR¡ Ingresa solo letras y sin espacios.")
    nombre = input("\nINGRESA EL NOMBRE DE TU GLADIADOR: ")

# CICLO DE COMBATE
while vidaEnemigo > 0 and vidaGladiador > 0:
    print("\n-----DATOS ACTUALES--------\n")
    print(f"Gladiador {nombre} (HP: {vidaGladiador})")
    print(f"Enemigo: (HP: {vidaEnemigo})")
    print(f"Pociones de vida restantes: {pocionVida}")

    # MENU DE OPCIONES
    print("\n-----------INICIO DEL COMBATE------------\n")
    print("\nELIGE ACCIÓN:")
    print("1. Ataque Pesado.")
    print("2. Ráfaga Veloz.")
    print("3. Curar.")
    opcion = input("\nIngresa la opcion: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("!ERROR¡ Debes ingresar numero de 1 al 3: ")
        opcion = input("\nIngresa la opcion: ")
    opcion = int(opcion)

# ATAQUE PESADO - OPCION 1
    if opcion == 1:
        print("\n===INICIO DE ATAQUE PESADO===\n")
        if vidaEnemigo < 20:
            print("\nGOLPE CRÍTICO....\n")
            vidaEnemigo -= (dañoAtaquePesado*1.5)
            print(f"\n!Atacaste al enemigo por {dañoAtaquePesado+1*5} puntos de daño.¡ ")
            
        else:
            vidaEnemigo -= 15
        print(f"\n!Atacaste al enemigo por {dañoAtaquePesado} puntos de daño.¡ ")

# RAFAGA VELOZ - OPCION 2
    elif opcion == 2:
        print("\n===INICIO DE RÁFAGA DE GOLPES===\n")
        
        for i in range(3):
            vidaEnemigo -= 5
            print("Golpe conectado por 5 de daño.")

# CURAR - OPCION 3
    elif opcion == 3:
        if pocionVida > 0:
            vidaGladiador += 30
            pocionVida -= 1
        else:
            print("\n¡No quedan pociones!.")
            turnoGladiador = False

# ENEMIGO ATACA 
    print("\n¡El enemigo contraataca por 12 puntos!\n")
    vidaGladiador -= dañoEnemigo

    if vidaGladiador <= 0:
        break
    else:
        print("\n===NUEVO TURNO===\n")

# FINAL DEL JUEGO
if vidaGladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.\n")
elif vidaEnemigo <= 0:
    print("\nDERROTA. Has caído en combate.\n")


