import os
#Archivo función para guardar los datos del Usuario
def crearArchivo():
    file=open("RegistrarUsuario.txt","w")
    file.close
contraseña=0
def registrarUsuario():
    nombre = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")
    pruebaContraseña = input("Ingrese su contraseña: ")
    contraseña = input("Confirme su contraseña: ")
    while pruebaContraseña != contraseña:
        print("Intente nuevamente")
        pruebaContraseña = input("Ingrese su contraseña: ")
        contraseña = input("Confirme su contraseña: ")
    file=open("RegistrarUsuario.txt","a")
    file.write("Nombre: ")
    file.write(nombre)
    file.write("\n")
    file.write("Teléfono: ")
    file.write(telefono)
    file.write("\n")
    file.write("Dirección de correo: ")
    file.write(correo)
    file.write("\n")
    file.write("Contraseña: ")
    file.write(contraseña)
    file.close()
def mostrarInformacion():
    file=open("RegistrarUsuario.txt","r")
    mensaje=file.read
    print(mensaje)

costo=0
horas=0
#Archivo función para guardar las reserva Curso Teórico
def reservaCursoTeorico():
    print("La hora tiene un costo de 2000 colones")
    horas=int(input("Seleccione la cantidad de horas que desea reservar: "))
    #Verificar la validación de las horas y calcular costo
    if horas<1:
        print("La cantidad de horas mínima es de 1")
        return
    costo=horas*2000
    print("Costo total: ",costo,"colones")
    #Días reserva
    print("Contamos con un horario de Lunes a Sábado de 8:00 a 21:00")
    dia=input("Ingrese los días en que desea asistir a las clases (ejemplo: L, K, M, J, V, S): ")
    diasValidos=["L","K","M","J","V","S"]
    while dia not in diasValidos:
        print("Día inválido")
        dia = input("Ingrese nuevamente los días en que desea asistir a las clases (ejemplo: L, K, M, J, V, S): ") 

monto=0
horas1=0
def reservaClasesManejo():
    horas1=int(input("Seleccione la cantidad de horas que desea reservar: "))
    vehiculoPropio = input("¿Usará un vehículo propio (P) o desea que se le proporcione uno (S)? ")
    #Verificar horas,calcular costo y el vehículo
    if horas1<1:
        print("La cantidad mínimma de horas es de 1")
    elif vehiculoPropio not in ["P", "S"]:
        print("Opción de vehiculo no válida.")
    else:
        print("Contamos con un horario de Martes a Domingo de 8:00 a 17:00")
        dias = input("Ingrese los días en que desea asistir a las clases (ejemplo: K, M, J, V, S, D): ")
        #Verificar días válidos
        diasValidos=["K","M","J","V","S","D"]
        while dias not in diasValidos:
            print("Día inválido")
            dias = input("Ingrese nuevamente los días en que desea asistir a las clases (ejemplo: K, M, J, V, S, D): ")
        #Verificar horario
        horario=int(input("Ingrese el horario que al que desea asistir: "))
        if horario<8 and horario>17:
            int(input("Ingrese otro horario: "))
        #Calcular el costo
        monto = horas1 * (4000 if vehiculoPropio == "S" else 3000)
        print(f"Costo total: {monto} colones")
    
def reservaDictamenMedico():
    print("GENERACIÓN DE DICTAMEN MÉDICO")
    nombreUsuario = input("Ingrese su nombre completo: ")
    telefonoUsuario = input("Ingrese su número de teléfono: +506 ")
    direccionCorreo = input("Ingrese su dirección de correo electrónico: ")
    tipoSangre = input("Ingrese su tipo de sangre: ")
    peso = float(input("Ingrese su peso (kg): "))
    estatura = float(input("Ingrese su estatura (m): "))
    donador = input("¿Desea ser donador? (S/N): ")

    # Generar el dictamen médico
    print("--- DICTAMEN MÉDICO ---\n""Nombre: ",nombreUsuario,"\n""Teléfono: ",telefonoUsuario,"\n""Correo Electrónico: ",direccionCorreo,"\n""Tipo de Sangre: ",tipoSangre,"\n""Peso: ",peso,"\n""Estatura: ",estatura,"\n""Donador de Órganos: ",donador)
           
#Archivo función para guardar la factura electrónica
import os
def crearArchivo2():
    file=open("Facturaelectronica.txt","w")
    file.close
def facturaelectronica():
    file=open("Facturaelectronica.txt","a")
    nombre1=input("Ingrese su nombre: ")
    telefono1=input("Ingrese su número de teléfono: ")
    correo1=input("Ingrese su dirección de correo: ")
    file.write("Nombre: ")
    file.write(nombre1)
    file.write("\n")
    file.write("Número de teléfono: ")
    file.write(telefono1)
    file.write("\n")
    file.write("Dirección de correo electrónico: ")
    file.write(correo1)
    file.write("\n")
    file.write("SubTotal Curso Teórico: ")
    file.write(costo)
    file.write("\n")
    file.write("SubTotal Clases de Manejo: ")
    file.write(monto)
    file.write("\n")
    IVA=(costo+monto)*0.13
    file.write("SubTotal IVA: ")
    file.write((costo+monto)*0.13)
    file.write("\n")
    file.write("Total: ")
    file.write(costo+monto+IVA)
    file.close()
def mostrarFacturaelectronica():
    file=open("Facturaelectronica.txt","r")
    mensaje1=file.read
    print(mensaje1)

#Archivo función para guardar la factura electrónica
import os
def crearArchivo3():
    file=open("FuncionesAdministrativas.txt","w")
    file.close
def funcionesAdministrativas():
    file=open("FuncionesAdministrativas.txt","a")
    ingresocontraseña=input("Ingrese su contraseña para ingresar a las funciones administrativas: ")
    while ingresocontraseña != contraseña:
        print("Contraseña incorrecta")
        ingresocontraseña=input("Ingrese nuevamente la contraseña: ")
    while True:
        print("Funciones Administrativas"+"\n1. Cantidad de dinero recolectado"+"\n2. Número de reservas"+"\n3. Salir")
        opcion1=input("Seleccione una opción: ")
        if opcion1=="1":
            file.write("La cantidad de dinero recolectado es de:")
            file.write(costo+monto)
            file.write("\n")
            file.close
        elif opcion1=="2":
            file.write("El número de reservas son: ")
            file.write(horas+horas1)
            file.write("\n")
            file.close
        elif opcion1=="3":
             break
        else:
            file.write("Opción no válida. Intente nuevamente.")
def mostarFuncionesAdministrativas():
    file=open("FuncionesAdministrativas.txt","r")
    mensaje2=file.read
    print(mensaje2)

# Menú Principal
while True:
    print("\nMenú Principal: "
          + "\n1. Registrar usuario"
          + "\n2. Reservar curso teórico"
          + "\n3. Reservar clases de manejo"
          + "\n4. Reservar dictamen médico"
          + "\n5. Factura electrónica"
          + "\n6. Funciones Administrativas"
          + "\n0. Salir")
    opcion = input("Seleccion una opción: ")
    
    if opcion == "1":
        registrarUsuario()
    elif opcion == "2":
        reservaCursoTeorico()
    elif opcion == "3":
        reservaClasesManejo()
    elif opcion == "4":
        reservaDictamenMedico()
    elif opcion == "5":
        facturaelectronica()
    elif opcion == "6":
        funcionesAdministrativas()
    elif opcion == "0":
        break
    else:
        print("Opción no válida. Intente nuevamente.")
