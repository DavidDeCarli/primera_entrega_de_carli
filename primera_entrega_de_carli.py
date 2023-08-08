import json

miData=[]

def leerArchivo():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return []

def guardarArchivo(miData):
    with open("data.json", "w") as file:
        json.dump(miData, file)
        print("Informacion guardada con éxito")

def nuevoUsuario():
    data=leerArchivo()
    usuario = input(f"Ingresa el nombre de usuario: ")
    contrasenia = input(f"Ingresa la contraseña: ")
    data.append({"user": usuario, "password": contrasenia})
    guardarArchivo(data)
    input(f"Se registró el usuario {usuario} correctamente")

def login():
    intento = 3
    while intento >0:
        intento -=1 
        user = input(f"Ingrese el usuario: ")
        password = input(f"Ingrese la contraseña: ")
        data = leerArchivo()

        for usuario in data:
            if user == usuario["user"] and password == usuario["password"]:
                print("Usuario correcto!")
                return
        print(f"Usuario o contraseña incorrecto, te quedan {intento}")
    else:
        print("Usuario bloqueado. Contacte al administrador")

salir = 0

while salir !=1:
    select = int(input("Seleccione una opcion: \n 1. Nuevo usuario \n 2. Ingresar a la Aplicación \n 3. Salir de la Aplicación \n \n Opción: "))
    if select == 1:
        nuevoUsuario()
    elif select == 2:
        login()
    elif select == 3:
        print("Que tenga un buen día")
        exit()
    else:
        print("Opcion inválida")