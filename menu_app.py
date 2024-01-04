# Funcion que permite almacenar en una lista
def agregar_compra(compras, total_gastado):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print("Compra agregada correctamente.")
    return total_gastado

# Funcion que muestra el numero y el monto de cada compra
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Listado de compras:")
        for i, compra in enumerate(compras, start=1):
            print(f"Compra {i}: ${compra}")

# Funcion para mostrar el total gastado
def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")


#--------------------------------------------------#
#Definir el metodo main
def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == '2':
            mostrar_compras(compras)
        elif opcion == '3':
            mostrar_total(total_gastado)
        elif opcion == '4':
            print("Salio del menu")
            break
        else:
            print("Opcion invalida. Por favor, elija una opcion valida.")


if __name__ == "__main__":
    main()
