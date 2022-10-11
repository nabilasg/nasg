
def agregar_registro():
    global registros

    cod_articulo = int(input("introduzca el codigo del articulo:"))
    nombre = input("introduzca el nombre:")
    descripcion = input("introduzca la descripcion:")
    precio= int(input("introduzca el precio:"))

    registros[cod_articulo] = nombre, descripcion, precio
    print(registros)

def delete(cod_articulo):
    global registros
    del(registros[cod_articulo])
    print("Baja-Eliminado")

def listar():
    global registros
    for user in registros:
        print(
    """
    cod_articulo: {}
        nombre: {}
        descripcion: {}
        precio: {}
      """.format(user,registros[user][0],registros[user][1],registros[user][2]))




registros={}
while True:
    print ("------Aplicación en python------")
    print ("[1]--------Altas--------")
    print("[2]--------Bajas--------")
    print("[3]--------Modificaciones--------")
    print("[4]--------Búsquedas--------")
    print("[5]--------Listado--------")

    try:
        option = int(input("Selecciona una opción: "))

        if option == 1:
            agregar_registro()
        elif option == 2:
            cod_articulo = int(input("Ingrese el codigo del articulo"))
            delete(cod_articulo)
        


        elif option==5:
            listar()

        else:
            print("No está la opción en el menú")




    except:
        print("Porfavor ingrese datos válidos")

