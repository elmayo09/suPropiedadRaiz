from Arriendo import Arriendo
from Cliente import Cliente
from Compraventa import Compraventa
from Funcionario import Funcionario
from Inmueble import Inmueble
from Propietario import Propietario
from Usuario import Usuario
from mensaje import Mensaje as msg
from random import *

codigos_unicos = 1000 #main

lista_propietarios=[]
lista_funcionarios = []
lista_clientes = []
lista_compraventas = []
lista_arriendos= []
lista_compraventas=[]
lista_inmuebles=[]
valoresPassword = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
nombres=["Andres Gimenez","Maria Taja","Lina Gutierrez","Juan Sarrias","Carlos inut","Pepe Grillo","Sara Macias","Eduardo Mejia","Yeremi Guarin","Martina Tamayo",
    "Martin Correa","Cristina Mejia", "Emanuel Valencia", "Cristopher Amaya","Jose Mercado","Josue Galindo","Natalia Osorio","Edgar Aguirre","Emilio del monte","Miranda Rodas"]


def agregarDatosFicticios():
    primer_funcionario = Funcionario(1234, "admin", "1234", 660000, 40000, "abc@sp.com")
    lista_funcionarios.append(primer_funcionario)
    clientePrueba=Cliente(99,"prueba","1234", "car."+str(randint(60,150)))
    lista_clientes.append(clientePrueba)
    #Funcionarios----------------------------------------------------
    cc=0;
    while cc<10:
        p=""
        #Generador de contraseñas aleatorias
        p = p.join([choice(valoresPassword) for i in range(5)])
        #print(p)
        f= Funcionario(cc,nombres[cc], p,randint(600000,1500000),randint(10000,1000000),nombres[cc].replace(" ", "") +"@gmail.com")
        lista_funcionarios.append(f)
        cc=cc+1

    #Propietarios con inmuebles en arriendo   ----------------------
    while cc< 15:
        p=""
        #Generador de contraseñas aleatorias
        p = p.join([choice(valoresPassword) for i in range(5)])
        c=Propietario(cc,nombres[cc],p, "car."+str(randint(60,150)))#Creacion de propietario
        inmu=Inmueble(cc+1,"carr30","no","si","no",200,3,1,"enArriendo")#Creacion de inmueble
        arrie=Arriendo(cc,"20-11-1990",randint(1000,150000),"21-12-1992",inmu,c,)#Creacion de contrato de arriendo enlazado a propietario e inmueble
        inmu.addArriendo(arrie)#enlace inmueble con arriendo
        c.addArriendo(arrie)#enlace propietario con arriendo
        lista_inmuebles.append(inmu)
        lista_arriendos.append(arrie)
        lista_propietarios.append(c)
        cc=cc+1

    #Propietarios con inmuebles en venta---------------------------
    while cc<20:
        p=""
        #Generador de contraseñas aleatorias
        p = p.join([choice(valoresPassword) for i in range(5)])
        c=Propietario(cc,nombres[cc],p, "car."+str(randint(60,150)))#Creacion de propietario
        inmu=Inmueble(cc+1,"carr30","no","si","no",200,3,1,"enVenta")#Creacion de inmueble
        compraV=Compraventa(cc,c,"20-11-1990",randint(1000,150000),"21-12-1992",inmu)#Creacion de contrato de compraventa enlazado a propietario e inmueble
        inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
        c.addCompraventa(compraV)#enlace propietario con compraventa
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
    
    elif(opcion1 == 1):
        agregarDatosFicticios()
        print(msg.datosFicticios[idioma])
        
    elif(opcion1 == 2): #segunda opcion menu principal
        print("Ingresar cedula:")
        ced = int(input())
        print(msg.ingreso_contra[idioma])
        contra = str(input())

        logeado = Usuario.login(ced, contra, lista_funcionarios)
        if(logeado != None):
            print(msg.bienv_fun[idioma]+logeado.getNombre()) #Ingreso exitoso como funcionario

            opcion2 = -1  #opcion2 = opciones del menu funcionario
            while(True):  # Ingreso al menu funcionario
                print(msg.menu_funcionario[idioma])
                opcion2 = int(input())

                if(opcion2 == 0): #Salir del menu funcionario
                    break
    
                elif(opcion2 == 1): #Registrar otro funcionario
                    print(msg.in_nombre[idioma])
                    nombre = str(input())
                    print(msg.in_cedula[idioma])
                    cedula = int(input())
                    print(msg.in_correo[idioma])
                    correo = str(input())
                    print(msg.in_contrasena[idioma])
                    contrasena = str(input())
                    print(msg.in_sueldo[idioma])
                    sueldo = int(input())
                    print(msg.in_comision[idioma])
                    comision = int(input())
                    nuevo = Funcionario(cedula, nombre, contrasena, sueldo, comision, correo)
                    lista_funcionarios.append(nuevo)

                    print(msg.agg[idioma]+"\n"+nuevo.toString())

                elif(opcion2 == 2):  #Ver el que tiene mayor sueldo
                    print(msg.sueldo[idioma])
                    mayor = Funcionario.funcionarioMayorSueldo(lista_funcionarios)
                    print(mayor.getNombre()+" : "+str(mayor.getSueldo()))
                    
                elif(opcion2 == 3): #Ver lista de funcionarios
                    Funcionario.mostrarFuncionarios(lista_funcionarios)

                elif(opcion2 == 4): #Registrar nueva compraventa o nuevo arriendo
                    print("Ingrese la direccion del inmueble: ")
                    direccion = str(input())
                    encontrado = False
                    for inmueble in Inmueble.listaInmuebles:  #busca la direccion entre los inmuebles existentes
                        if(inmueble.getDireccion() == direccion):
                            encontrado = True  #Ya existe un inmueble con esa direccion, solo sirve para arriendo
                            print("Ya existe un inmueble con esa direccion.") 
                            if((inmueble.getTipo()!="compraventa") and (inmueble.getTipo()!="arriendo")): #comprueba si esta disponible
                                print("El inmueble solo esta disponible para arrendamiento.")
                                print("1. Arrendamiento con este inmueble.\n0. Regresar al menu principal")
                                opcion3 = int(input())  #Opciones para el menu de solo arrendamiento
                                if(opcion3 == 0):
                                    break
                                elif(opcion3 ==1):  #arrendamiento para inmueble existente (direccion)
                                    print("Ingrese los datos del arrendamiento")
                                    print("Diga la cedula del ACTUAL propietario del inmueble: ")
                                    cedula_propietario = int(input())
                                    print("Diga el costo mensual del arrendamiento: ")
                                    costo_mensual = int(input())
                                    print("Diga la fecha de arrendamiento en formato: 'dd/mm/aaaa'")
                                    fechainicio = str(input())
                                    print("Diga la fecha de finalizacion de arrendamiento en formato: 'dd/mm/aaaa'")
                                    fechafin = str(input())

                                    codigos_unicos  += 1 #aumenta en 1 los codigos en general de la clase compraventa
                                    codigo = codigos_unicos  #el codigo siempre sera diferente para cada compraventa
                                    arrendamiento_nuevo = Arriendo(codigo, fechainicio, costo_mensual, fechafin, inmueble, cedula_propietario)

                                    lista_arriendos.append(arrendamiento_nuevo) #la añade a la lista general
                                    print("Arrendamiento publicado exitosamente")
                                    print(arrendamiento_nuevo.toString())
                                    break
                                else:
                                    print("no valida opcion")
                            else:  #el inmueble no esta disponible
                                print("El inmueble no está disponible para arrendamiento ni compraventa")
                                break
                    if(encontrado == False):  #Si la direccion no aparece, el inmueble no existe
                        print("1. Compraventa.\n2. Arrendamiento.\n0. Regresar al menu")
                        opcion4 = int(input())  #opciones para el menu de registro compraventa o arriendo

                        
                        print("Ingrese el número de estrato del inmueble: ")
                        estrato = int(input())
                        print("Si el inmueble tiene vigilancia, escriba 'si', de lo contrario escriba 'no': ")
                        vigilancia = str(input())
                        print("Si el inmueble tiene servicios básicos, escriba 'si', de lo contrario escriba 'no': ")
                        servicios = str(input())
                        print("Si el inmueble tiene ascensor, escriba 'si', de lo contrario escriba 'no': ")
                        ascensor = str(input())
                        print("Ingrese el area del inmueble en metros cuadrados: ")
                        area = int(input())
                        print("Ingrese el número de baños del inmueble: ")
                        banos = int(input())
                        print("Ingrese el número de cuartos del inmueble: ")
                        cuartos = int(input())
                        
                        if(opcion4 == 0 ): #Regreso al menu funcionario
                            break
                        elif(opcion4==1):  #Pide los datos para registrar compraventa
                            tipo = "compraventa"
                            inmueble_nuevo = Inmueble(estrato, direccion, vigilancia, servicios, ascensor, area, cuartos, banos, tipo)
                            print("Diga la cedula del ACTUAL propietario del inmueble: ")
                            cedula_propietario = int(input())
                            print("Diga la fecha de publicacion en formato: 'dd/mm/aaaa'")
                            fechain = str(input())
                            print("Diga el precio del inmueble: ")
                            precio = int(input())
                            print("Diga la fecha de compra en formato: 'dd/mm/aaaa'")
                            fechacom = str(input())

                            codigos_unicos  += 1 #aumenta en 1 los codigos en general de la clase compraventa
                            codigo = codigos_unicos  #el codigo siempre sera diferente para cada compraventa
                            compraventa_nueva = Compraventa(codigo, cedula_propietario, fechain, precio, fechacom, inmueble_nuevo)

                            
                            print("Compraventa publicada exitosamente")
                            lista_compraventas.append(compraventa_nueva) #la añade a la lista general
                            Inmueble.listaInmuebles.append(inmueble_nuevo) #añade el inmueble a la lista inmuebles
                            print(compraventa_nueva.toString())
                            
                        elif(opcion4==2):  #Pide los datos para registrar arriendo
                            tipo = "arrendamiento"
                            inmueble_nuevo = Inmueble(estrato, direccion, vigilancia, servicios, ascensor, area, cuartos, banos, tipo)
                            print("Diga la cedula del ACTUAL propietario del inmueble: ")
                            cedula_propietario = int(input())
                            print("Diga el costo mensual del arrendamiento: ")
                            costo_mensual = int(input())
                            print("Diga la fecha de arrendamiento en formato: 'dd/mm/aaaa'")
                            fechainicio = str(input())
                            print("Diga la fecha de finalizacion de arrendamiento en formato: 'dd/mm/aaaa'")
                            fechafin = str(input())

                            codigos_unicos  += 1 #aumenta en 1 los codigos en general de la clase compraventa
                            codigo = codigos_unicos  #el codigo siempre sera diferente para cada compraventa
                            arrendamiento_nuevo = Arriendo(codigo, fechainicio, costo_mensual, fechafin, inmueble_nuevo, cedula_propietario)
                            lista_arriendos.append(arrendamiento_nuevo) #la añade a la lista general

                            
                            print("Arrendamiento publicado exitosamente")
                            print(arrendamiento_nuevo.toString())
                            Inmueble.listaInmuebles.append(inmueble_nuevo) #añade el inmueble a la lista inmuebles
                        else: #opcion no valida en el menu funcionario
                            print("no opcion valida")
                            break

  
                        

                elif(opcion2 == 6): #opcion 6 menu funcionario Aprobar compraventas
                    print("aprobar compraventas")

                elif(opcion2 == 7): #opcion 7 menu funcionario Aprobar arriendos
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
                    print("Cliente registrado correctamente: \n"+cliente_nuevo.toString())
                    break

                elif(opcion_correo == 2): #Registra cliente sin correo
                    cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente)
                    lista_clientes.append(cliente_nuevo)
                    print("Cliente registrado correctamente: \n"+cliente_nuevo.toString())
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
        
