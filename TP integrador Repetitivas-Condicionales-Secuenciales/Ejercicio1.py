
#Ejercicio 1— “Caja del Kiosco”

# 1.Pedir Nombre del cliente

nombre = input("INGRESA TU NOMBRE: ")
while not nombre.isalpha():
    print("!ERROR¡, debe ingresar solo letras, sin espacios")
    nombre = input("INGRESA TU NOMBRE: ")

# 2.Cantidad de productos a comprar
numProductos =input("INGRESA LA CANTIDAD DE PRODUCTOS QUE VAS A COMPRAR (solo numeros): ")
while not numProductos.isdigit() or int(numProductos) == 0:
    print("!ERROR¡, debe ser solo numero mayor a cero y sin espacios")
    numProductos = input("INGRESA LA CANTIDAD DE PRODUCTOS QUE VAS A COMPRAR (solo numeros): ")
numProductos = int(numProductos)

totalSinDesc = 0
totalConDesc = 0
ahorro = 0
precioDescuento = 0

# 3.Usar For por cada producto
for i in range(numProductos):
    print(f"\nProducto {i+1}\n")
    precio = input("INGRESA EL PRECIO DEL PRODUCTO (solo numero):")
    while not precio.isdigit() or int(precio) == 0:
        print("!ERROR¡, debe ser solo numero y sin espacios")
        precio = input("INGRESA EL PRECIO DEL PRODUCTO (solo numero):")
    precio = int(precio)

    descuento = input("¿TIENE DESCUENTO? S/N: ").lower()
    while descuento not in ["s", "n"]:
        print("!ERROR¡, Ingrese S o N: ")
        descuento = input("¿TIENE DESCUENTO? S/N: ").lower()

    if descuento == "s":
         precioDescuento = precio * 0.9
         ahorro += precio * 0.10
    totalSinDesc += precio
    totalConDesc += precioDescuento


promedio = totalConDesc / numProductos

# 4. Mostrar los resultados
print(f"\nCLIENTE: {nombre}")
print(f"CANTIDAD DE PRODUCTOS: {numProductos}")

print("\n")
print(f"PRECIO TOTAL SIN DESCUENTO: ${totalSinDesc}")
print(f"PRECIO TOTAL CON DESCUENTO: ${totalConDesc:.2f}")
print(f"AHORRASTE UN TOTAL DE: ${ahorro:.2f}")
print(f"PROMEDIO POR PRODUCTO: ${promedio:.2f}")






