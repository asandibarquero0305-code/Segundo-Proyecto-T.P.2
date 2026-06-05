#elaborado por Aaron Sandi y Brandon Coronado
from tkinter import *
from tkinter import messagebox
from funciones import *


baseDatos = cargarDatos()


def ventanaGenerarDonadores():
    '''
    Funcionalidad: Abre ventana para generar donadores.
    Entrada: No recibe entradas.
    Salida: Genera donadores nuevos.
    '''

    ventana = Toplevel()
    ventana.title("Generar donadores")
    ventana.geometry("300x200")

    Label(ventana,text="Cantidad de donadores").pack()

    cantidad = Entry(ventana)
    cantidad.pack()


    def generar():

        mensaje = generarDonadores(
            baseDatos,
            int(cantidad.get())
        )

        messagebox.showinfo(
            "Resultado",
            mensaje
        )


    Button(
        ventana,
        text="Generar",
        command=generar
    ).pack()



def ventanaInsertarDonador():
    '''
    Funcionalidad: Abre ventana para insertar donadores.
    Entrada: No recibe entradas.
    Salida: Registra un donador.
    '''

    ventana = Toplevel()
    ventana.title("Insertar donador")
    ventana.geometry("400x500")


    datos=[
        "Nombre",
        "Apellido 1",
        "Apellido 2",
        "Cédula",
        "Tipo sangre",
        "Sexo 1 hombre / 0 mujer",
        "Día nacimiento",
        "Mes nacimiento",
        "Año nacimiento",
        "Peso",
        "Correo",
        "Teléfono"
    ]


    entradas=[]


    for dato in datos:

        Label(
            ventana,
            text=dato
        ).pack()

        entrada=Entry(ventana)

        entrada.pack()

        entradas.append(entrada)



    def insertar():

        donador=[
            [
                entradas[0].get(),
                entradas[1].get(),
                entradas[2].get()
            ],

            entradas[3].get(),

            entradas[4].get(),

            True if entradas[5].get()=="1" else False,

            (
                int(entradas[6].get()),
                int(entradas[7].get()),
                int(entradas[8].get())
            ),

            float(entradas[9].get()),

            entradas[10].get(),

            entradas[11].get(),

            1,

            0
        ]


        mensaje=insertarDonador(
            baseDatos,
            donador
        )


        messagebox.showinfo(
            "Resultado",
            mensaje
        )


    Button(
        ventana,
        text="Registrar",
        command=insertar
    ).pack()



def ventanaActualizarDonador():
    '''
    Funcionalidad: Abre ventana para actualizar donador.
    Entrada: No recibe entradas.
    Salida: Actualiza datos.
    '''

    ventana=Toplevel()

    ventana.title("Actualizar")

    ventana.geometry("350x350")


    textos=[
        "Cédula",
        "Nombre",
        "Peso",
        "Correo",
        "Teléfono"
    ]


    entradas=[]


    for texto in textos:

        Label(
            ventana,
            text=texto
        ).pack()


        entrada=Entry(ventana)

        entrada.pack()
        entradas.append(entrada)

    def actualizar():
        mensaje=actualizarDonador(
            baseDatos,
            entradas[0].get(),
            [entradas[1].get(),"",""],
            float(entradas[2].get()),
            entradas[3].get(),
            entradas[4].get()
        )

        messagebox.showinfo(
            "Resultado",
            mensaje
        )

    Button(
        ventana,
        text="Actualizar",
        command=actualizar
    ).pack()

def ventanaEliminarDonador():
    '''
    Funcionalidad: Abre ventana para eliminar donador.
    Entrada: No recibe.
    Salida: Elimina donador.
    '''
    ventana=Toplevel()
    ventana.title("Eliminar")
    ventana.geometry("300x250")

    Label(
        ventana,
        text="Cédula"
    ).pack()

    cedula=Entry(ventana)
    cedula.pack()

    Label(
        ventana,
        text="Justificación"
    ).pack()

    justificacion=Entry(ventana)
    justificacion.pack()

    def eliminar():
        mensaje=eliminarDonador(
            baseDatos,
            cedula.get(),
            int(justificacion.get())
        )

        messagebox.showinfo(
            "Resultado",
            mensaje
        )

    Button(
        ventana,
        text="Eliminar",
        command=eliminar
    ).pack()

def ventanaInsertarLugar():
    '''
    Funcionalidad: Abre ventana para insertar lugares.
    Entrada: No recibe.
    Salida: Agrega un lugar.
    '''
    ventana=Toplevel()
    ventana.title("Insertar lugar")
    ventana.geometry("300x250")

    Label(
        ventana,
        text="Provincia"
    ).pack()
    provincia=Entry(ventana)
    provincia.pack()
    Label(
        ventana,
        text="Lugar"
    ).pack()
    lugar=Entry(ventana)
    lugar.pack()

    def agregar():
        mensaje=insertarLugar(
            lugaresDonacion,
            int(provincia.get()),
            lugar.get()
        )

        messagebox.showinfo(
            "Resultado",
            mensaje
        )

    Button(
        ventana,
        text="Agregar",
        command=agregar
    ).pack()

def ventanaReportes():
    '''
    Funcionalidad: Muestra menú de reportes.
    Entrada: No recibe.
    Salida: Genera reportes.
    '''
    ventana=Toplevel()
    ventana.title("Reportes")
    ventana.geometry("400x600")

    Button(
        ventana,
        text="Tipo sangre",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteTipoSangre(baseDatos)
        )
    ).pack()

    Button(
        ventana,
        text="Mujeres O-",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteMujeresONegativo(baseDatos)
        )
    ).pack()

    Button(
        ventana,
        text="Donadores provincia",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteDonadoresProvincia(baseDatos)
        )
    ).pack()

    Button(
        ventana,
        text="Lugares",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteLugares()
        )
    ).pack()

    Button(
        ventana,
        text="No activos",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteNoActivos(baseDatos)
        )
    ).pack()

    Button(
        ventana,
        text="Lista completa",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteListaCompleta(baseDatos)
        )
    ).pack()

    Label(
        ventana,
        text="Tipo sangre"
    ).pack()

    tipo=Entry(ventana)
    tipo.pack()

    Button(
        ventana,
        text="¿A quién puede donar?",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteAQuienPuedeDonar(tipo.get())
        )
    ).pack()

    Button(
        ventana,
        text="¿De quién puede recibir?",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reportePuedeRecibir(tipo.get())
        )
    ).pack()

    Label(
        ventana,
        text="Rango edad"
    ).pack()

    edad1=Entry(ventana)
    edad1.pack()
    edad2=Entry(ventana)
    edad2.pack()

    Button(
        ventana,
        text="Reporte edad",
        command=lambda:
        messagebox.showinfo(
            "Reporte",
            reporteRangoEdad(
                baseDatos,
                int(edad1.get()),
                int(edad2.get())
            )
        )
    ).pack()

def cerrarPrograma():
    '''
    Funcionalidad: Cierra el programa.
    Entrada: No recibe.
    Salida: Termina ejecución.
    '''
    messagebox.showinfo(
        "Mensaje",
        salir()
    )
    ventanaPrincipal.destroy()

ventanaPrincipal=Tk()
ventanaPrincipal.title("Banco de Sangre")
ventanaPrincipal.geometry("400x450")

Label(
    ventanaPrincipal,
    text="BANCO DE SANGRE",
    font=("Arial",18)
).pack()

Button(
    ventanaPrincipal,
    text="Generar donadores",
    command=ventanaGenerarDonadores
).pack()

Button(
    ventanaPrincipal,
    text="Insertar donador",
    command=ventanaInsertarDonador
).pack()

Button(
    ventanaPrincipal,
    text="Actualizar donador",
    command=ventanaActualizarDonador
).pack()

Button(
    ventanaPrincipal,
    text="Eliminar donador",
    command=ventanaEliminarDonador
).pack()

Button(
    ventanaPrincipal,
    text="Insertar lugar",
    command=ventanaInsertarLugar
).pack()

Button(
    ventanaPrincipal,
    text="Reportes",
    command=ventanaReportes
).pack()

Button(
    ventanaPrincipal,
    text="Salir",
    command=cerrarPrograma
).pack()
ventanaPrincipal.mainloop()
