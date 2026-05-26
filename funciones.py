from datetime import datetime

tiposSangre=("O+","O-","A+","A-","B+","B-","AB+","AB-")

justificaciones={
    1:"Enfermedad infecciosa o crónica.",
    2:"Conducta de riesgo.",
    3:"Problema de salud física.",
    4:"Procedimiento médico reciente.",
    5:"Uso de medicamentos.",
    6:"Viaje o estilo de vida de riesgo.",
    7:"Situación específica."
}

puedeDonarA={
    "O-":["O-","O+","A-","A+","B-","B+","AB-","AB+"],
    "O+":["O+","A+","B+","AB+"],
    "A-":["A-","A+","AB-","AB+"],
    "A+":["A+","AB+"],
    "B-":["B-","B+","AB-","AB+"],
    "B+":["B+","AB+"],
    "AB-":["AB-","AB+"],
    "AB+":["AB+"]
}

def calcularEdad(fecha):
    dia=fecha[0]
    mes=fecha[1]
    anno=fecha[2]

    hoy=datetime.now()
    edad=hoy.year-anno

    if hoy.month<mes:
        edad=edad-1

    elif hoy.month==mes and hoy.day<dia:
        edad=edad-1

    return edad

def insertarDonador(baseDatos,donador):
    cedula=donador[1]

    for persona in baseDatos:
        if persona[1]==cedula:
            return "La persona ya está registrada."

    baseDatos.append(donador)

    return "Donador registrado correctamente."

def eliminarDonador(baseDatos,cedula,justificacion):
    for donador in baseDatos:
        if donador[1]==cedula:
            donador[8]=0
            donador[9]=justificacion

            return "Donador eliminado satisfactoriamente."

    return "La persona con el número de cédula "+cedula+" no está registrada."

def insertarLugar(lugares,provincia,nuevoLugar):
    if provincia not in lugares:
        lugares[provincia]=[]

    for lugar in lugares[provincia]:
        if lugar==nuevoLugar:
            return "El lugar ya está registrado."

    lugares[provincia].append(nuevoLugar)

    return "Lugar registrado correctamente."

