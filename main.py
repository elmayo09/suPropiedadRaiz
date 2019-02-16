
from Arriendo import Arriendo
from Cliente import Cliente
from Compraventa import Compraventa
from Inmueble import Inmueble
from Propietario import Propietario
from Ficticios import Ficticios
from mensaje import Mensaje as msg
from random import *

codigos_unicos = 1000 #main

lista_propietarios=[]
lista_clientes = []
lista_compraventas = []
lista_arriendos= []
lista_compraventas=[]
lista_inmuebles=[]
valoresPassword = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
nombres=["Andres Gimenez","Maria Taja","Lina Gutierrez","Juan Sarrias","Carlos inut","Pepe Grillo","Sara Macias","Eduardo Mejia","Yeremi Guarin","Martina Tamayo",
    "Martin Correa","Cristina Mejia", "Emanuel Valencia", "Cristopher Amaya","Jose Mercado","Josue Galindo","Natalia Osorio","Edgar Aguirre","Emilio del monte","Miranda Rodas"]
codigo_contrato=1000

def agregarDatosFicticios():
    primer_propietario = Propietario(1234, "admin", "1234", "car40A12", "abc@sp.com")
    lista_propietarios.append(primer_propietario)
    inmu=Inmueble(0,"car."+str(randint(160,250)),False,True,randint(300,500),3,1,"enArriendo",9,"Medellin",primer_propietario)#Creacion de inmueble
    arrie=Arriendo(0,"20-11-1900","21-12-1990",randint(1000,150000),inmu,primer_propietario,False)#Creacion de contrato de arriendo enlazado a propietario e inmueble
    inmu.addArriendo(arrie)#enlace inmueble con arriendo
    primer_propietario.addInmueble(inmu)
    lista_arriendos.append(arrie)
    lista_inmuebles.append(inmu)
    clientePrueba=Cliente(99,"prueba","1234", "car."+str(randint(60,150)))
    lista_clientes.append(clientePrueba)
    #Funcionarios----------------------------------------------------
    cc=0;
    #Propietarios con inmuebles en arriendo   ----------------------
    while cc< 10:
        p=""
        #Generador de contrasenas aleatorias
        p = p.join([choice(valoresPassword) for i in range(5)])
        c=Propietario(cc,nombres[cc],p, "car."+str(randint(60,150)))#Creacion de propietario
        inmu=Inmueble(cc+1,"car."+str(randint(160,250)),False,True,randint(300,500),3,1,"enArriendo",9,"Medellin",c)#Creacion de inmueble
        c.addInmueble(inmu)#enlace propietario con inmueble
        arrie=Arriendo(cc,"20-11-1990","21-12-1992",randint(1000,150000),inmu,c,False)#Creacion de contrato de arriendo enlazado a propietario e inmueble
        inmu.addArriendo(arrie)#enlace inmueble con arriendo
        lista_inmuebles.append(inmu)
        lista_arriendos.append(arrie)
        lista_propietarios.append(c)
        cc=cc+1

    #Propietarios con inmuebles en venta---------------------------
    while cc<20:
        p=""
        #Generador de contrasenas aleatorias
        p = p.join([choice(valoresPassword) for i in range(5)])
        c=Propietario(cc,nombres[cc],p, "car."+str(randint(60,150)))#Creacion de propietario
        inmu=Inmueble(cc+1,"car."+str(randint(160,250)),False,True,randint(300,500),3,1,"enArriendo",9,"Medellin",c)#Creacion de inmueble
        c.addInmueble(inmu)#enlace propietario con inmueble
        compraV=Compraventa(cc,c,"20-11-1990",randint(1000,150000),inmu,"Efectivo")#Creacion de contrato de compraventa enlazado a propietario e inmueble
        inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
        lista_inmuebles.append(inmu)
        lista_compraventas.append(compraV)
        lista_propietarios.append(c)
        cc=cc+1


#comienza el programa
print(msg.title)
print(msg.bienv)
idioma = 0 #idioma = 1 para ingles, idioma = 2 para español
while(True):
    print(msg.en_es)
    idioma = int(input())
    if(idioma == 1 or idioma == 2):
        break
    else:
        print(msg.err[1]+" / "+msg.err[2])
idioma = str(idioma)
opcion1 = -1 #opcion1 = opciones del menu principal

while(True):
    print(msg.menu_principal[idioma])
    opcion1 = int(input())
    
    if(opcion1 == 0): #Salir del programa
        print(msg.gracias[idioma]) 
        break
    
    elif(opcion1 == 1):#primera opcion agregar datos ficticios
        agregarDatosFicticios()
        Ficticios.datos_desde_txt("ficticios.txt",lista_clientes) #agrega clientes ficticios desde txt
        print(msg.datosFicticios[idioma])
        
    elif(opcion1 == 2): #segunda opcion menu principal #ingreso propietario
        print("Ingresar cedula:")
        ced = int(input())
        print(msg.ingreso_contra[idioma])
        contra = str(input())

        logeado = Propietario.login(ced, contra, lista_propietarios)
        if(logeado != None):
            print(msg.bienv_fun[idioma]+logeado.getNombre()) #Ingreso exitoso como propietario

            opcion2 = -1  #opcion2 = opciones del menu funcionario
            while(True):  # Ingreso al menu funcionario
                print(msg.menu_funcionario[idioma])
                opcion2 = int(input())

                if(opcion2 == 0): #Salir del menu funcionario
                    break
    
                elif(opcion2 == 1): #Registrar inmueble
                    print("Estrato:")
                    estrato = str(input())
                    print("Direccion")
                    direccion = str(input())
                    for inmueble in lista_inmuebles:  #busca la direccion entre los inmuebles existentes
                        if(inmueble.getDireccion() == direccion):
                            print("El inmueble ya existe")
                            direccion=0
                            break
                    if direccion!=0:
                        print("Tiene vigilancia?(s|n):")
                        vigilancia = str(input())
                        if vigilancia=="s":
                            vigilancia=True
                        else: vigilancia=False
                        print("Tiene ascensor?(s|n):")
                        ascensor = str(input())
                        if ascensor=="s":
                            ascensor=True
                        else: ascensor=False
                        print("Area en metros cuadrados:")
                        area = int(input())
                        print("Cantidad de cuartos:")
                        cuartos = int(input())
                        print("Cantidad de baños:")
                        banos = int(input())
                        print("para arriendo o compraventa:")
                        tipo = str(input())
                        print("Años de antiguedad del inmueble:")
                        antiguedad = int(input())
                        print("Ciudad donde esta ubicado de inmueble:")
                        ciudad = str(input())
                        inmu=Inmueble(estrato,direccion,vigilancia,ascensor,area,cuartos,banos,tipo,antiguedad,ciudad,logeado)#Creacion de inmueble
                        logeado.addInmueble(inmu)#enlace propietario con inmueble
                        if tipo=="arriendo":
                            #creacion arriendo
                            print("Creacion de contrato de arriendo")
                            codigo_contrato+=1
                            print("Fecha donde inicia arriendo(dd/mm/aaaa):")
                            fechainicio = str(input())
                            print("Fecha donde finaliza el arriendo(dd/mm/aaaa):")
                            fechafin = str(input())
                            print("Valor de la mensulidad:")
                            valor = int(input())
                            print("Estara por medio de Agencia?(s|n)")
                            agencia = str(input())
                            if agencia=="s":
                                agencia=True
                            else: agencia=False
                            arrie=Arriendo(codigo_contrato,fechainicio,fechafin,valor,inmu,logeado,agencia)#Creacion de contrato de arriendo enlazado a propietario e inmueble
                            lista_inmuebles.append(inmu)
                            lista_arriendos.append(arrie)
                        else:
                            #Creacion compraventa
                            print("Creacion de contrato de compra-venta")
                            codigo_contrato+=1
                            print("Fecha (dd/mm/aaaa):")
                            fecha = str(input())
                            print("Valor de la mensulidad:")
                            valor = int(input())
                            print("Medio de pago:")
                            medioPago = str(input())
                            compraV=Compraventa(codigo_contrato,logeado,fecha,valor,inmu,medioPago)#Creacion de contrato de compraventa enlazado a propietario e inmueble
                            inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
                            lista_inmuebles.append(inmu)
                            lista_compraventas.append(compraV)

                elif(opcion2 == 2):  #Ver los inmuebles del propietario actual
                    Inmueble.verListaInmuebles(logeado.getInmuebles())

  
                        

                elif(opcion2 == 6): #opcion 6 menu propietario Aprobar compraventas
                    print("aprobar compraventas")

                elif(opcion2 == 7): #opcion 7 menu propietario Aprobar arriendos
                    print("aprobar arriendos")


                    

        else:
            print(msg.err_datos[idioma]) #Datos erroneos funcionario
                
    elif(opcion1 == 3): #opcion 3 menu principal registrtar cliente
        print("Para registrarse como cliente, por favor digite los siguientes datos: ")
        print("Ingrese su cedula: ")
        cedula_cliente = int(input())
        encontrado = False
        for client in lista_clientes:
            if (client.getCedula() == cedula_cliente): #encuentra un cliente con esa cedula
                print("Ya existe un cliente con esa cedula")
                encontrado = True
                break
        if(encontrado == False):  #No hay un cliente con esa cedula
            print("Ingrese su nombre: ")
            nombre_cliente = str(input())
            print("Ingrese su contraseña: ")
            contrasena_cliente = str(input())
            print("Ingrese su direccion: ")
            direccion_cliente = str(input())
            

            while(True):  #Correo opcional
                print("Desea agregar correo para contacto? :\n1. Si\n2. No")
                opcion_correo = int(input())

                if(opcion_correo == 1):  #Pide correo y registra cliente con correo
                    print("Ingrese su correo: ")
                    correo_cliente = str(input())
                    cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente, correo_cliente)
                    lista_clientes.append(cliente_nuevo)
                    print("Cliente registrado correctamente: \n"+cliente_nuevo.__str__())
                    break

                elif(opcion_correo == 2): #Registra cliente sin correo
                    cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente)
                    lista_clientes.append(cliente_nuevo)
                    print("Cliente registrado correctamente: \n"+cliente_nuevo.__str__())
                    break

                else: #No ingresa 1 o 2
                    print("No es una opcion valida")

    elif(opcion1 == 4):  #opciop 4 del menu principal Ingreso Como Cliente
        print("Para ingresar como cliente, por favor digite los siguientes datos: ")

        print(msg.in_cedula[idioma])
        ced = int(input())
        print(msg.in_contrasena[idioma])
        contra = str(input())

        logeado = Usuario.login(ced, contra, lista_clientes)
        if(logeado != None):
            print(msg.bienv_fun[idioma]+logeado.getNombre()) #Ingreso exitoso como cliente

            opciones_cliente = -1  #opcion2 = opciones del menu cliente
            while(True):  # Ingreso al menu cliente
                print("Seleccione una de las siguientes opciones: ")
                print(" 1. Ver ofertas de arrendamiento. \n 2. Ver ofertas de compraventa. \n 0. Regresar al menú principal")
                opciones_cliente = int(input())

                if(opciones_cliente == 0): #Salir del menu cliente
                    break

                elif(opciones_cliente == 1):  #Mostrar arriendos disponibles
                    print("Los arrendamientos disponibles son: ")
                    Arriendo.mostrarArriendos(lista_arriendos)
                
                elif(opciones_cliente == 2):  #Mostrar compraventas disponibles
                    print("Las compraventas disponibles son: ")
                    Compraventa.mostrarCompraventas(lista_compraventas)
            
        else:
            print(msg.err_datos[idioma]) #Datos erroneos cliente
            
    elif(opcion1 == 5): #Opcion 5 del menu principal
        print(msg.err[idioma])
