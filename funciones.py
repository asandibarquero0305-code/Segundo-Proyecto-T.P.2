#elaborado por Aaron Sandi y Brandon Coronado
import pickle
import random
from datetime import datetime

tiposSangre = (
    "O+", "O-",
    "A+", "A-",
    "B+", "B-",
    "AB+", "AB-"
)

lugaresDonacion = {
    1:[
        "Banco Nacional de Sangre",
        "Hospital México",
        "Hospital San Juan de Dios"
    ],
    2:[
        "Hospital San Rafael de Alajuela"
    ],
    3:[
        "Hospital Max Peralta"
    ],
    4:[
        "Hospital San Vicente de Paúl"
    ],
    5:[
        "Hospital La Anexión"
    ],
    6:[
        "Hospital Monseñor Sanabria"
    ],
    7:[
        "Hospital Tony Facio"
    ]
}

justificaciones = {
    1:"Enfermedad infecciosa o crónica.",
    2:"Conducta de riesgo.",
    3:"Problema de salud física.",
    4:"Procedimiento médico reciente.",
    5:"Uso de medicamentos.",
    6:"Viaje o estilo de vida de riesgo.",
    7:"Situación específica."
}

puedeDonarA = {
    "O-":["O-","O+","A-","A+","B-","B+","AB-","AB+"],
    "O+":["O+","A+","B+","AB+"],
    "A-":["A-","A+","AB-","AB+"],
    "A+":["A+","AB+"],
    "B-":["B-","B+","AB-","AB+"],
    "B+":["B+","AB+"],
    "AB-":["AB-","AB+"],
    "AB+":["AB+"]
}

puedeRecibirDe = {
    "O-":["O-"],
    "O+":["O-","O+"],
    "A-":["O-","A-"],
    "A+":["O-","O+","A-","A+"],
    "B-":["O-","B-"],
    "B+":["O-","O+","B-","B+"],
    "AB-":["O-","A-","B-","AB-"],
    "AB+":["O-","O+","A-","A+","B-","B+","AB-","AB+"]
}

def cargarDatos():
    '''
    Funcionalidad: Carga los datos almacenados.
    Entrada: No recibe entradas.
    Salida: Retorna la base de datos.
    '''
    try:
        archivo = open("donadores.dat","rb")
        datos = pickle.load(archivo)
        archivo.close()
        return datos
    except:
        return []

def guardarDatos(baseDatos):
    '''
    Funcionalidad: Guarda la información en memoria secundaria.
    Entrada: Recibe la base de datos.
    Salida: Guarda el archivo.
    '''
    archivo = open("donadores.dat","wb")
    pickle.dump(baseDatos,archivo)
    archivo.close()

def calcularEdad(fecha):
    '''
    Funcionalidad: Calcula la edad del donador.
    Entrada: Recibe la fecha de nacimiento.
    Salida: Retorna la edad.
    '''
    dia=fecha[0]
    mes=fecha[1]
    anno=fecha[2]
    hoy=datetime.now()
    edad=hoy.year-anno

    if hoy.month<mes:
        edad-=1

    elif hoy.month==mes and hoy.day<dia:
        edad-=1
    return edad

def generarDonadores(baseDatos,cantidad):
    '''
    Funcionalidad: Genera donadores aleatorios.
    Entrada: Recibe la base de datos y cantidad.
    Salida: Agrega donadores.
    '''
    for i in range(cantidad):
        numero=len(baseDatos)+1
        donador=[
            ["Donador",str(numero),"Sistema"],
            str(random.randint(1,7))+"-"+str(random.randint(1000,9999))+"-"+str(random.randint(1000,9999)),
            random.choice(tiposSangre),
            random.choice([True,False]),

            (
                random.randint(1,28),
                random.randint(1,12),
                random.randint(1960,2007)
            ),

            random.randint(45,120),
            "donador"+str(numero)+"@gmail.com",
            "8888-"+str(random.randint(1000,9999)),
            1,

            0
        ]

        baseDatos.append(donador)
    guardarDatos(baseDatos)
    return "Donadores generados correctamente."

def insertarDonador(baseDatos,donador):
    '''
    Funcionalidad: Inserta un nuevo donador.
    Entrada: Recibe la base de datos y el donador.
    Salida: Retorna mensaje.
    '''
    for persona in baseDatos:
        if persona[1]==donador[1]:
            return "La persona ya está registrada."

    baseDatos.append(donador)
    guardarDatos(baseDatos)
    return "Donador registrado correctamente."

def actualizarDonador(baseDatos,cedula,nombre,peso,correo,telefono):
    '''
    Funcionalidad: Actualiza los datos de un donador.
    Entrada: Recibe los nuevos datos.
    Salida: Retorna mensaje.
    '''
    for donador in baseDatos:
        if donador[1]==cedula:
            donador[0]=nombre
            donador[5]=peso
            donador[6]=correo
            donador[7]=telefono
            guardarDatos(baseDatos)
            return "Datos actualizados correctamente."
    return "La persona no está registrada."

def eliminarDonador(baseDatos,cedula,justificacion):
    '''
    Funcionalidad: Cambia un donador a estado inactivo.
    Entrada: Recibe cédula y justificación.
    Salida: Retorna mensaje.
    '''
    for donador in baseDatos:
        if donador[1]==cedula:
            donador[8]=0
            donador[9]=justificacion
            guardarDatos(baseDatos)
            return "Donador eliminado correctamente."
    return "La persona no está registrada."

def insertarLugar(lugares,provincia,lugar):
    '''
    Funcionalidad: Agrega lugares de donación.
    Entrada: Recibe provincia y lugar.
    Salida: Retorna mensaje.
    '''
    if provincia not in lugares:
        lugares[provincia]=[]
    if lugar in lugares[provincia]:
        return "El lugar ya existe."
    lugares[provincia].append(lugar)
    return "Lugar agregado correctamente."

def reporteTipoSangre(baseDatos):
    '''
    Funcionalidad: Genera reporte por tipo de sangre.
    Entrada: Recibe la base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for tipo in tiposSangre:
        cantidad=0
        for donador in baseDatos:
            if donador[2]==tipo:
                cantidad+=1
        texto+=tipo+" : "+str(cantidad)+"\n"
    return texto

def reporteMujeresONegativo(baseDatos):
    '''
    Funcionalidad: Busca mujeres con sangre O-.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for donador in baseDatos:
        if donador[2]=="O-" and donador[3]==False:
            texto+=str(donador[0])+"\n"
    return texto

def reporteDonadoresProvincia(baseDatos):
    '''
    Funcionalidad: Cuenta donadores por provincia.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for provincia in range(1,8):
        cantidad=0
        for donador in baseDatos:
            if donador[1][0]==str(provincia):
                cantidad+=1
        texto+="Provincia "+str(provincia)+": "+str(cantidad)+"\n"
    return texto

def reporteLugares():
    '''
    Funcionalidad: Muestra lugares registrados.
    Entrada: No recibe.
    Salida: Retorna reporte.
    '''
    texto=""
    for provincia in lugaresDonacion:
        texto+="Provincia "+str(provincia)+"\n"
        for lugar in lugaresDonacion[provincia]:
            texto+="- "+lugar+"\n"
    return texto

def reporteNoActivos(baseDatos):
    '''
    Funcionalidad: Muestra donadores inactivos.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for donador in baseDatos:
        if donador[8]==0:
            texto+=str(donador[0])+"\n"
    return texto

def reporteAQuienPuedeDonar(tipo):
    '''
    Funcionalidad: Muestra a quién puede donar.
    Entrada: Recibe tipo de sangre.
    Salida: Retorna compatibilidad.
    '''
    if tipo in puedeDonarA:
        return str(puedeDonarA[tipo])
    return "Tipo de sangre inválido."

def reportePuedeRecibir(tipo):
    '''
    Funcionalidad: Muestra de quién puede recibir sangre.
    Entrada: Recibe tipo de sangre.
    Salida: Retorna compatibilidad.
    '''
    if tipo in puedeRecibirDe:
        return str(puedeRecibirDe[tipo])
    return "Tipo de sangre inválido."

def reporteListaCompleta(baseDatos):
    '''
    Funcionalidad: Lista todos los donadores.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for donador in baseDatos:
        texto+=str(donador)+"\n"
    return texto

def reporteRangoEdad(baseDatos,edadInicial,edadFinal):
    '''
    Funcionalidad: Filtra donadores por edad.
    Entrada: Recibe edades.
    Salida: Retorna reporte.
    '''
    texto=""
    for donador in baseDatos:
        edad=calcularEdad(donador[4])
        if edad>=edadInicial and edad<=edadFinal:
            texto+=str(donador[0])+" Edad: "+str(edad)+"\n"
    return texto

def salir():
    '''
    Funcionalidad: Finaliza el programa.
    Entrada: No recibe.
    Salida: Retorna mensaje.
    '''
    return "Donar sangre es donar vida."
