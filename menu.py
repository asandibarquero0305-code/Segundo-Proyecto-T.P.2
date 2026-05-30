#elaborado por Aaron Sandi y Brandon Coronado
import pickle
import random

TIPOSSANGRE = (
    "O+", "O-",
    "A+", "A-",
    "B+", "B-",
    "AB+", "AB-"
)

donadores = []

lugaresDonacion = {
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


def cargarDatos():
    '''
    Funcionalidad: Carga la base de datos de los donadores.
    Entrada: No recibe entradas.
    Salida: Retorna la lista de donadores.
    '''
    try:
        archivo = open("donadores.dat", "rb")
        datos = pickle.load(archivo)
        archivo.close()
        print("\nBase de datos cargada correctamente.")
        return datos
    except:
        print("\nNo existe una base de datos aún.")
        return []


def guardarDatos(donadores):
    '''
    Funcionalidad: Guarda los donadores en memoria secundaria.
    Entrada: Recibe la lista de donadores.
    Salida: Guarda los datos en un archivo.
    '''
    archivo = open("donadores.dat", "wb")
    pickle.dump(donadores, archivo)
    archivo.close()
    print("\nDatos guardados correctamente.")


def generarDonadores(donadores):
    '''
    Funcionalidad: Genera donadores aleatoriamente.
    Entrada: Recibe la lista de donadores.
    Salida: Agrega nuevos donadores a la lista.
    '''
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

            tipoSangre = random.choice(TIPOSSANGRE)
            sexo = random.choice([True, False])
            dia = random.randint(1, 28)
            mes = random.randint(1, 12)
            annio = random.randint(1960, 2007)
            fechaNacimiento = (dia, mes, annio)
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
                tipoSangre,
                sexo,
                fechaNacimiento,
                peso,
                correo,
                telefono,
                estado,
                justificacion
            ]

            donadores.append(donador)
        guardarDatos(donadores)
        print("\nDonadores generados correctamente.")
    except:
        print("\nError al generar donadores.")


def mostrarDonadores(donadores):
    '''
    Funcionalidad: Muestra todos los donadores registrados.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra la información de los donadores.
    '''
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


def mostrarLugares():
    '''
    Funcionalidad: Muestra los lugares de donación por provincia.
    Entrada: No recibe entradas.
    Salida: Muestra los lugares de donación.
    '''
    print("---------------------------------------------")
    print("       LUGARES DE DONACION")
    print("---------------------------------------------")
    for provincia in lugaresDonacion:
        print("\nProvincia:", provincia)
        for lugar in lugaresDonacion[provincia]:
            print("-", lugar)


def actualizarDonador(donadores):
    '''
    Funcionalidad: Actualiza la información de un donador.
    Entrada: Recibe la lista de donadores.
    Salida: Modifica los datos de un donador.
    '''
    cedulaBuscar = input("Ingrese la cédula del donador: ")
    encontrado = False
    for donador in donadores:
        if donador[1] == cedulaBuscar:
            encontrado = True
            print("Donador encontrado.")
            print("Nombre actual:", donador[0])
            print("Peso actual:", donador[5])
            print("Correo actual:", donador[6])
            print("Teléfono actual:", donador[7])
            print("------------------------------------")
            nuevoNombre = input("\nNuevo nombre: ")
            nuevoPeso = float(input("Nuevo peso: "))
            nuevoCorreo = input("Nuevo correo: ")
            nuevoTelefono = input("Nuevo teléfono: ")
            print("------------------------------------")
            donador[0] = nuevoNombre
            donador[5] = nuevoPeso
            donador[6] = nuevoCorreo
            donador[7] = nuevoTelefono
            guardarDatos(donadores)
            print("\nDatos actualizados correctamente.")
    if encontrado == False:
        print("\nLa persona no está registrada.")


def reporteTipoSangre(donadores):
    '''
    Funcionalidad: Muestra la cantidad de donadores por tipo de sangre.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra un reporte de tipos de sangre.
    '''
    print("---------------------------------------------")
    print("       REPORTE POR TIPO DE SANGRE")
    print("---------------------------------------------")
    for tipo in tiposSangre:
        cantidad = 0
        for donador in donadores:
            if donador[2] == tipo:
                cantidad += 1
        print(tipo, ":", cantidad)


def reporteActivos(donadores):
    '''
    Funcionalidad: Muestra los donadores activos.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra los donadores activos registrados.
    '''
    print("---------------------------------------------")
    print("         DONADORES ACTIVOS")
    print("---------------------------------------------")
    encontrados = False
    for donador in donadores:
        if donador[8] == 1:
            encontrados = True
            print("\nNombre:", donador[0])
            print("Cédula:", donador[1])
            print("Tipo:", donador[2])
    if encontrados == False:
        print("\nNo hay donadores activos.")


def reporteMujeresONegativo(donadores):
    '''
    Funcionalidad: Muestra las mujeres con tipo de sangre O-.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra las mujeres O- registradas.
    '''
    print("---------------------------------------------")
    print("          MUJERES O-")
    print("---------------------------------------------")
    encontradas = False
    for donador in donadores:
        if donador[2] == "O-" and donador[3] == False:
            encontradas = True
            print("\nNombre:", donador[0])
            print("Cédula:", donador[1])
            print("Correo:", donador[6])
    if encontradas == False:
        print("\nNo existen mujeres O-.")


def reporteProvincias():
    '''
    Funcionalidad: Muestra la cantidad de lugares por provincia.
    Entrada: No recibe entradas.
    Salida: Muestra un reporte de lugares de donación.
    '''
    print("---------------------------------------------")
    print("      LUGARES POR PROVINCIA")
    print("---------------------------------------------")
    for provincia in lugaresDonacion:
        cantidad = len(lugaresDonacion[provincia])
        print("\nProvincia", provincia)
        print("Cantidad de lugares:", cantidad)
   

def reporteDonadoresProvincia(donadores):
    '''
    Funcionalidad: Muestra la cantidad de donadores por provincia.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra la cantidad de donadores registrados por provincia.
    '''
    print("---------------------------------------------")
    print("      DONADORES POR PROVINCIA")
    print("---------------------------------------------")
    for provincia in range(1, 8):
        cantidad = 0
        for donador in donadores:
            cedula = donador[1]
            if cedula.startswith(str(provincia) + "-"):
                cantidad += 1
        print("Provincia", provincia, ":", cantidad)


def reporteNoActivos(donadores):
    '''
    Funcionalidad: Muestra los donadores no activos.
    Entrada: Recibe la lista de donadores.
    Salida: Muestra los donadores no activos registrados.
    '''
    print("---------------------------------------------")
    print("       DONADORES NO ACTIVOS")
    print("---------------------------------------------")
    encontrados = False
    for donador in donadores:
        if donador[8] == 0:
            encontrados = True
            print("\nNombre:", donador[0])
            print("Cédula:", donador[1])
            print("Tipo de sangre:", donador[2])
    if encontrados == False:
        print("\nNo hay donadores no activos.")


def menuPrincipal():
    '''
    Funcionalidad: Controla el menú principal del sistema.
    Entrada: No recibe entradas.
    Salida: Ejecuta las opciones del programa.
    '''
    donadores = cargarDatos()
    while True:
        print("---------------------------------------------")
        print("            BANCO DE SANGRE")
        print("---------------------------------------------")
        print("1. Generar donadores")
        print("2. Mostrar donadores")
        print("3. Mostrar lugares de donación")
        print("4. Actualizar donador")
        print("5. Reporte por tipo de sangre")
        print("6. Reporte de donadores activos")
        print("7. Reporte mujeres O-")
        print("8. Reporte lugares por provincia")
        print("9. Reporte donadores por provincia")
        print("10. Reporte donadores no activos")
        print("11. Salir")
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            generarDonadores(donadores)
        elif opcion == "2":
            mostrarDonadores(donadores)
        elif opcion == "3":
            mostrarLugares()
        elif opcion == "4":
            actualizarDonador(donadores)
        elif opcion == "5":
            reporteTipoSangre(donadores)
        elif opcion == "6":
            reporteActivos(donadores)
        elif opcion == "7":
            reporteMujeresONegativo(donadores)
        elif opcion == "8":
            reporteProvincias()
        elif opcion == "9":
            reporteDonadoresProvincia(donadores)
        elif opcion == "10":
            reporteNoActivos(donadores)
        elif opcion == "11":
            print("\nDonar sangre es donar vida.")
            print("Gracias.\n")
            break
        else:
            print("\nOpción inválida.")


menuPrincipal()
