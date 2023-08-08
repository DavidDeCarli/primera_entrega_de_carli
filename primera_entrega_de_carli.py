import json

miData={}

def leerArchivo():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return {"user": [], "password": []}

def guardarArchivo(miData):
    with open("data.json", "w") as file:
        json.dump(miData, file)
        print("Informacion guardada con éxito")


def nuevoUsuario():
    leerArchivo()
    usuario = input(f"Ingresa el nombre de usuario: ")
    contrasenia = input(f"Ingresa la contraseña: ")
    miData["user"].append(usuario)
    miData["password"].append(contrasenia)
    guardarArchivo(miData)
    input(f"Se registró el usuario {usuario} correctamente")

def login():
    intento = 3
    while intento >0:
        intento -=1 
        user = input(f"Ingrese el usuario: ")
        password = input(f"Ingrese la contraseña: ")
        data = leerArchivo()

        usersList = data["user"]
        passwdList = data["password"]

        for i, usuario in enumerate(usersList):
            if user == usuario and password == passwdList[i]:
                print("Usuario correcto!")
                return
        print(f"Usuario o contraseña incorrecto, te quedan {intento}")
    else:
        print("Usuario bloqueado. Contacte al administrador")


miData = leerArchivo()
salir = 0

while salir !=1:
    select = int(input("Seleccione una opcion: \n 1. Nuevo usuario \n 2. Ingresar a la Aplicación \n 3. Salir de la Aplicación \n \n Opción: "))
    if(select == 1):
        nuevoUsuario()
    elif(select == 2):
        login()
    elif(select == 3):
        print("Que tenga un buen día")
        exit()
    else:
        print("Opcion inválida")