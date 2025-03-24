inventario = {}
def agregar_producto():
    """Esta función agrega un nuevo producto al invetario"""
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = input("Ingrese la cantidad inicial: ")
    inventario[nombre] = cantidad
        
def eliminar_producto():
    """Esta función elimina un producto existente del inventario"""
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    if nombre in inventario:
        del inventario[nombre]
    else:
        print(f"No se encontro {nombre.lower()} en el inventario")

def mostrar_inventario():
    """Esta función va a mostrar el inventario actual"""
    inventario_items = inventario.items()
    for i in inventario_items:
        print(i)

# Imprimir opciones del menú
num = input("""Elija una opción:
    (1) Agreagar un nuevo producto
    (2) Eliminar un producto
    (3) Mostrar inventario
    (4) Salir
    """
)

while num != "4":
    if num == "1":
        agregar_producto()
    elif num == "2":
        eliminar_producto()
    elif num == "3":
        mostrar_inventario()
    else:
        print("Opción inválida")
        exit(1)
    num = input("""Elija una opción:
    (1) Agreagar un nuevo producto
    (2) Eliminar un producto
    (3) Mostrar inventario
    (4) Salir
    """
    )
