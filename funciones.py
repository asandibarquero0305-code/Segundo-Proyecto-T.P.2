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
    1:["Banco Nacional de Sangre",
       "Hospital México",
       "Hospital San Juan de Dios"],

    2:["Hospital San Rafael de Alajuela"],
    3:["Hospital Max Peralta"],
    4:["Hospital San Vicente de Paúl"],
    5:["Hospital La Anexión"],
    6:["Hospital Monseñor Sanabria"],
    7:["Hospital Tony Facio"]
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
    Funcionalidad: Calcula la edad de un donador.
    Entrada: Recibe la fecha de nacimiento.
    Salida: Retorna la edad.
    '''
    dia = fecha[0]
    mes = fecha[1]
    anno = fecha[2]
    hoy = datetime.now()
    edad = hoy.year - anno
    if hoy.month < mes:
        edad -= 1
    elif hoy.month == mes and hoy.day < dia:
        edad -= 1
    return edad

def generarDonadores(baseDatos,cantidad):
    '''
    Funcionalidad: Genera donadores aleatoriamente.
    Entrada: Recibe la base de datos y cantidad.
    Salida: Agrega donadores generados.
    '''
    for i in range(cantidad):
        numero = len(baseDatos)+1

        donador = [
            ["Donador",str(numero),"Sistema"],
            str(random.randint(1,7))+
            "-"+
            str(random.randint(1000,9999))+
            "-"+
            str(random.randint(1000,9999)),
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
    Funcionalidad: Inserta un donador nuevo.
    Entrada: Recibe la base de datos y donador.
    Salida: Retorna resultado.
    '''
    for persona in baseDatos:
        if persona[1] == donador[1]:
            return "La persona ya está registrada."
    baseDatos.append(donador)
    guardarDatos(baseDatos)
    return "Donador registrado correctamente."

def actualizarDonador(baseDatos,cedula,nombre,peso,correo,telefono):
    '''
    Funcionalidad: Actualiza información de un donador.
    Entrada: Recibe datos nuevos.
    Salida: Retorna mensaje.
    '''
    for donador in baseDatos:
        if donador[1] == cedula:
            donador[0] = nombre
            donador[5] = peso
            donador[6] = correo
            donador[7] = telefono
            guardarDatos(baseDatos)
            return "Datos actualizados correctamente."
    return "La persona no está registrada."

def eliminarDonador(baseDatos,cedula,justificacion):
    '''
    Funcionalidad: Elimina un donador.
    Entrada: Recibe cédula y justificación.
    Salida: Retorna mensaje.
    '''
    for donador in baseDatos:
        if donador[1] == cedula:
            donador[8] = 0
            donador[9] = justificacion
            guardarDatos(baseDatos)
            return "Donador eliminado correctamente."
    return "La persona no está registrada."

def insertarLugar(lugares,provincia,lugar):
    '''
    Funcionalidad: Inserta lugar de donación.
    Entrada: Recibe provincia y lugar.
    Salida: Retorna mensaje.
    '''
    if provincia not in lugares:
        lugares[provincia] = []
    if lugar in lugares[provincia]:
        return "El lugar ya existe."
    lugares[provincia].append(lugar)
    return "Lugar registrado correctamente."

def reporteTipoSangre(baseDatos):
    '''
    Funcionalidad: Reporta cantidad por tipo de sangre.
    Entrada: Recibe la base de datos.
    Salida: Retorna reporte.
    '''
    texto = ""
    for tipo in tiposSangre:
        cantidad = 0
        for donador in baseDatos:
            if donador[2] == tipo:
                cantidad += 1
        texto += tipo+" : "+str(cantidad)+"\n"
    return texto

def reporteMujeresONegativo(baseDatos):
    '''
    Funcionalidad: Busca mujeres O negativo.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto = ""
    for donador in baseDatos:
        if donador[2]=="O-" and donador[3]==False:
            texto += str(donador[0])+"\n"
    return texto

def reporteDonadoresProvincia(baseDatos):
    '''
    Funcionalidad: Cuenta donadores por provincia.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""
    for provincia in range(1,8):
        contador=0
        for donador in baseDatos:
            if donador[1][0] == str(provincia):
                contador +=1
        texto+="Provincia "+str(provincia)+": "+str(contador)+"\n"
    return texto

def reporteLugares():
    '''
    Funcionalidad: Muestra lugares disponibles.
    Entrada: No recibe entradas.
    Salida: Retorna lugares.
    '''
    texto=""

    for provincia in lugaresDonacion:
        texto += str(provincia)+"\n"
        for lugar in lugaresDonacion[provincia]:
            texto += "- "+lugar+"\n"
    return texto

def reporteNoActivos(baseDatos):
    '''
    Funcionalidad: Reporta donadores inactivos.
    Entrada: Recibe base de datos.
    Salida: Retorna reporte.
    '''
    texto=""

    for donador in baseDatos:
        if donador[8]==0:
            texto += str(donador[0])+"\n"
    return texto

def reporteAQuienPuedeDonar(tipo):
    '''
    Funcionalidad: Indica a quién puede donar.
    Entrada: Recibe tipo de sangre.
    Salida: Retorna compatibilidad.
    '''
    return str(puedeDonarA[tipo])


def salir():
    '''
    Funcionalidad: Muestra mensaje de salida.
    Entrada: No recibe.
    Salida: Retorna mensaje.
    '''
    return "Donar sangre es donar vida."
