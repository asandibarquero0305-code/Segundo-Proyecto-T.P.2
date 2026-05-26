#elaborado por Aaron Sandi y Brandon Coronado
import pickle
import random

TIPOS_SANGRE = (
    "O+", "O-",
    "A+", "A-",
    "B+", "B-",
    "AB+", "AB-"
)

donadores = []

lugares_donacion = {
    1: [
        "Banco Nacional de Sangre",
        "Hospital México",
        "Hospital San Juan de Dios"
    ],
    2: [
        "Hospital San Rafael de Alajuela",
        "Hospital de San Ramón",
        "Hospital del Cantón Norteño"
    ],
    3: [
        "Hospital Max Peralta"
    ],
    4: [
        "Hospital San Vicente de Paúl"
    ],
    5: [
        "Hospital La Anexión",
        "Hospital Enrique Baltodano"
    ],
    6: [
        "Hospital Monseñor Sanabria"
    ],
    7: [
        "Hospital Tony Facio",
        "Hospital de Guápiles"
    ]
}


def cargar_datos():
    try:
        archivo = open("donadores.dat", "rb")
        datos = pickle.load(archivo)
        archivo.close()
        print("\nBase de datos cargada correctamente.")
        return datos
    except:
        print("\nNo existe una base de datos aún.")
        return []


def guardar_datos(donadores):
    archivo = open("donadores.dat", "wb")
    pickle.dump(donadores, archivo)
    archivo.close()
    print("\nDatos guardados correctamente.")


def generar_donadores(donadores):
    try:
        cantidad = int(input("\nIngrese la cantidad de donadores: "))
        if cantidad <= 0:
            print("\nLa cantidad debe ser mayor a 0.")
            return
        for i in range(cantidad):
            numero = len(donadores) + 1
            nombre = "Donador " + str(numero)
            cedula = (
                str(random.randint(1, 7))
                + "-"
                + str(random.randint(1000, 9999))
                + "-"
                + str(random.randint(1000, 9999))
            )

            tipo_sangre = random.choice(TIPOS_SANGRE)
            sexo = random.choice([True, False])
            dia = random.randint(1, 28)
            mes = random.randint(1, 12)
            annio = random.randint(1960, 2007)
            fecha_nacimiento = (dia, mes, annio)
            peso = random.randint(45, 120)
            correo = (
                "donador"
                + str(numero)
                + "@gmail.com"
            )

            telefono = (
                str(random.choice([2,4,6,7,8,9]))
                + str(random.randint(100,999))
                + "-"
                + str(random.randint(1000,9999))
            )
            
            estado = random.choice([0,1])
            justificacion = random.randint(1,7)
            donador = [
                nombre,
                cedula,
                tipo_sangre,
                sexo,
                fecha_nacimiento,
                peso,
                correo,
                telefono,
                estado,
                justificacion
            ]
            
            donadores.append(donador)
        guardar_datos(donadores)
        print("\nDonadores generados correctamente.")
    except:
        print("\nError al generar donadores.")


def mostrar_donadores(donadores):
    if len(donadores) == 0:
        print("\nNo hay donadores registrados.")
    else:
        print("---------------------------------------------")
        print("         LISTA DE DONADORES")
        print("---------------------------------------------")
        for donador in donadores:
            print("\nNombre:", donador[0])
            print("Cédula:", donador[1])
            print("Tipo de sangre:", donador[2])
            if donador[3] == True:
                print("Sexo: Masculino")
            else:
                print("Sexo: Femenino")
            print("Fecha nacimiento:", donador[4])
            print("Peso:", donador[5])
            print("Correo:", donador[6])
            print("Teléfono:", donador[7])


def mostrar_lugares():
    print("---------------------------------------------")
    print("       LUGARES DE DONACION")
    print("---------------------------------------------")
    for provincia in lugares_donacion:
        print("\nProvincia:", provincia)
        for lugar in lugares_donacion[provincia]:
            print("-", lugar)


def menu_principal():
    donadores = cargar_datos()
    while True:
        print("---------------------------------------------")
        print("            BANCO DE SANGRE")
        print("---------------------------------------------")
        print("1. Generar donadores")
        print("2. Mostrar donadores")
        print("3. Mostrar lugares de donación")
        print("4. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            generar_donadores(donadores)
        elif opcion == "2":
            mostrar_donadores(donadores)
        elif opcion == "3":
            mostrar_lugares()
        elif opcion == "4":
            print("\nDonar sangre es donar vida.")
            break
        else:
            print("\nOpción inválida.")


menu_principal()
