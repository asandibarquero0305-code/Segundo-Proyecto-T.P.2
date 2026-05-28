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

def crearHtml(nombreArchivo,titulo,encabezados,datos):
    archivo=open(nombreArchivo,"w",encoding="utf-8")

    archivo.write("<!DOCTYPE html>\n")
    archivo.write("<html>\n")
    archivo.write("<head>\n")
    archivo.write("<meta charset='UTF-8'>\n")
    archivo.write("<title>"+titulo+"</title>\n")
    archivo.write("</head>\n")
    archivo.write("<body>\n")

    archivo.write("<h1>"+titulo+"</h1>\n")
    archivo.write("<p>Fecha y hora: "+str(datetime.now())+"</p>\n")

    archivo.write("<table border='1'>\n")
    archivo.write("<tr>\n")

    for encabezado in encabezados:
        archivo.write("<th>"+encabezado+"</th>\n")

    archivo.write("</tr>\n")

    for fila in datos:
        archivo.write("<tr>\n")

        for dato in fila:
            archivo.write("<td>"+str(dato)+"</td>\n")

        archivo.write("</tr>\n")

    archivo.write("</table>\n")
    archivo.write("</body>\n")
    archivo.write("</html>\n")

    archivo.close()

    return "Reporte creado satisfactoriamente."

def reporteRangoEdad(baseDatos,edadInicial,edadFinal):
    datos=[]

    for donador in baseDatos:
        edad=calcularEdad(donador[4])

        if donador[8]==1 and edad>=edadInicial and edad<=edadFinal:
            datos.append([
                donador[1],
                donador[0][0]+" "+donador[0][1]+" "+donador[0][2],
                donador[4],
                donador[7],
                donador[6]
            ])

    encabezados=["Cédula","Nombre completo","Fecha de nacimiento","Teléfono","Correo"]

    return crearHtml("reporte_rango_edad.html","Reporte por rango de edad",encabezados,datos)

def reporteListaCompleta(baseDatos):
    datos=[]

    for donador in baseDatos:
        if donador[3]==True:
            sexo="Masculino"

        else:
            sexo="Femenino"

        datos.append([
            donador[1],
            donador[0][0]+" "+donador[0][1]+" "+donador[0][2],
            donador[2],
            donador[4],
            donador[5],
            sexo,
            donador[7],
            donador[6]
        ])

    encabezados=["Cédula","Nombre completo","Tipo de sangre","Fecha de nacimiento","Peso","Sexo","Teléfono","Correo"]

    return crearHtml("reporte_lista_completa.html","Lista completa de donadores",encabezados,datos)