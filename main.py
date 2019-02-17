
from Arriendo import Arriendo
from Cliente import Cliente
from Compraventa import Compraventa
from Inmueble import Inmueble
from Propietario import Propietario
from Ficticios import Ficticios
from Contrato import Contrato
from mensaje_espanol import Mensaje as msg
from random import *

codigos_unicos = 1000 #main

lista_propietarios=[]
lista_clientes = []
lista_compraventas = []
lista_arriendos= []
lista_compraventas=[]
lista_inmuebles=[]
codigo_contrato=1000


#comienza el programa
print(msg.title)
print(msg.bienv)
idioma = 0 #idioma = 1 para ingles, idioma = 2 para espanol
while(True):
    print(msg.en_es)
    idioma = int(input())
    if(idioma == 1): #selecciona ingles
        from mensaje_ingles import Mensaje as msg
        break
    elif(idioma ==2): #ya esta por default en espanol
        break
    else: #opcion incorrecta
        print(msg.err)

opcion1 = -1 #opcion1 = opciones del menu principal--------------------------------------

while(True):
    print(msg.seleccion)
    print(msg.menu_principal)
    opcion1 = int(input())
    
    if(opcion1 == 0): #Salir del programa --------------------------------------
        print(msg.gracias) 
        break
    #----------------------------------------------------------------------------
    elif(opcion1 == 1):#primera opcion agregar datos ficticios
        #agregarDatosFicticios()
        Ficticios.datos_desde_txt("ficticios.txt",lista_clientes) #agrega clientes ficticios desde txt
        Ficticios.agregarDatosFicticios(lista_clientes,lista_propietarios,lista_compraventas,lista_inmuebles,lista_arriendos)
        print(msg.datosFicticios)
    #----------------------------------------------------------------------------
    elif(opcion1 == 2): #segunda opcion menu principal ingreso propietario
        print(msg.ingreso)
        print(msg.in_cedula)
        ced = int(input())
        print(msg.in_contrasena)
        contra = str(input())

        logeado = Propietario.login(ced, contra, lista_propietarios)
        if(logeado != None):
            print(msg.bienv_usuario+logeado.getNombre()) #Ingreso exitoso como propietario

            opcion2 = -1  #opcion2 = opciones del menu funcionario
            #Menu propietario----------------------------------------------------------------------------
            while(True):  # Ingreso al menu funcionario
                print(msg.menu_propietario)
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
                            inmu.addArriendo(arrie)#enlace inmueble con arriendo
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
                        print("inmueble registrado")

                elif(opcion2 == 2):  #Ver los inmuebles del propietario actual
                    Inmueble.verListaInmuebles(logeado.getInmuebles())

                elif(opcion2 == 6): #opcion 6 menu propietario Aprobar compraventas
                    print("aprobar compraventas")

                elif(opcion2 == 7): #opcion 7 menu propietario Aprobar arriendos
                    print("aprobar arriendos")
            #Fin menu propietario----------------------------------------------------------------------------

                    
        #----------------------------------------------------------------------------
        else:
            print(msg.err_datos) #Datos erroneos funcionario
   
    #----------------------------------------------------------------------------           
    elif(opcion1 == 3): #opcion 3 menu principal registrtar cliente
        print(msg.registro)
        print(msg.in_cedula)
        cedula_cliente = int(input())
        encontrado = False
        for client in lista_clientes:
            if (client.getCedula() == cedula_cliente): #encuentra un cliente con esa cedula
                print(msg.existe)
                encontrado = True
                break
        if(encontrado == False):  #No hay un cliente con esa cedula
            print(msg.in_nombre)
            nombre_cliente = str(input())
            print(msg.in_contrasena)
            contrasena_cliente = str(input())
            print(msg.in_direccion)
            direccion_cliente = str(input())
            

            while(True):  #Correo opcional
                print(msg.opcional_correo)
                opcion_correo = int(input())

                if(opcion_correo == 1):  #Pide correo y registra cliente con correo
                    print(msg.in_correo)
                    correo_cliente = str(input())
                    cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente, correo_cliente)
                    lista_clientes.append(cliente_nuevo)
                    print(msg.regd+cliente_nuevo.__str__())
                    break

                elif(opcion_correo == 2): #Registra cliente sin correo
                    cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente)
                    lista_clientes.append(cliente_nuevo)
                    print(msg.regd+cliente_nuevo.__str__())
                    break

                else: #No ingresa 1 o 2
                    print(msg.err)
    #--------------------------------------------------------
    elif(opcion1 == 4):  #opciop 4 del menu principal Ingreso Como Cliente
        print(msg.ingreso)

        print(msg.in_cedula)
        ced = int(input())
        print(msg.in_contrasena)
        contra = str(input())

        logeado = Cliente.login(ced, contra, lista_clientes)
        if(logeado != None):
            print(msg.bienv_usuario+logeado.getNombre()) #Ingreso exitoso como cliente

            opciones_cliente = -1  #opcion2 = opciones del menu cliente
            #Menu cliente--------------------------------------------------------
            while(True):  
                print(msg.seleccion)
                print(msg.menu_cliente)
                opciones_cliente = int(input())

                if(opciones_cliente == 0): #Salir del menu cliente
                    break

                elif(opciones_cliente == 1):  #Mostrar arriendos disponibles
                    print(msg.arriendos_disp)
                    Arriendo.arriendosDisponibles(lista_arriendos)
                
                elif(opciones_cliente == 2):  #Mostrar compraventas disponibles
                    print(msg.compraventas_disp)
                    Compraventa.compraventasDisponibles(lista_compraventas)

                elif(opciones_cliente == 3):  #Seleccionar compraventa
                    print(msg.sel_compraventa)
                    codigo_compraventa=int(input())
                    compraventa_actual=Compraventa.buscarCompraventa(lista_compraventas,codigo_compraventa)
                    if compraventa_actual==None or not compraventa_actual.getDisponible():
                        print("Debe ingresar un codigo de compraventa valido")
                    else:
                        print(compraventa_actual.__str__())
                        oferta=input("Desea aplicar a esta compraventa:(s|n)")
                        if oferta=="s":
                            compraventa_actual.setDisponible(False)
                            compraventa_actual.setComprador(logeado)#enlace entre compraventa y el comprador
                            logeado.addContrato(compraventa_actual)
                            compraventa_actual.getInmueble().setTipo("Vendido")
                            print("aplico")
                        else:
                            print("No aplico a la compraventa de cogigo: "+str(compraventa_actual.getCodigo()))

                elif(opciones_cliente == 4): #Seleccionar arriendo
                    print(msg.sel_arriendo)
                    codigo_arriendo=int(input())
                    arriendo_actual=Arriendo.buscarArriendo(lista_arriendos,codigo_arriendo)
                    
                    if arriendo_actual==None or not arriendo_actual.getDisponible():
                        print("Debe ingresar un codigo de arriendo valido")
                    else:
                        print(arriendo_actual.__str__())
                        oferta=input("Desea aplicar a este arriendo:(s|n)")
                        if oferta=="s":
                            arriendo_actual.setDisponible(False)
                            arriendo_actual.setArrendatario(logeado)#enlace entre arriendo y el arrendatario
                            logeado.addContrato(arriendo_actual)#se añade el contrato de arrendamieno a la lista de contratos del cliente
                            arriendo_actual.getInmueble().setTipo("arrendado")
                            print("Aplico")
                        else:
                            print("No aplico al arriendo de codigo "+str(arriendo_actual.getCodigo()))

                elif(opciones_cliente == 5):#ver mis contratos actuales
                    print(Contrato.mostrarValoresContratos(logeado.getContratos()))
        else:
            print(msg.err_datos) #Datos erroneos cliente
            
    elif(opcion1 == 5): #Opcion 5 del menu principal registrar nuevo propietario
        print(msg.registro)
        print(msg.in_cedula)
        cedula_propietario = int(input())
        encontrado = False
        for prop in lista_propietarios:
            if (prop.getCedula() == cedula_propietario): #encuentra un propietario con esa cedula
                print(msg.existe)
                encontrado = True
                break
        if(encontrado == False):  #No hay un propietario con esa cedula
            print(msg.in_nombre)
            nombre_propietario = str(input())
            print(msg.in_contrasena)
            contrasena_propietario = str(input())
            print(msg.in_direccion)
            direccion_propietario = str(input())
            while(True):  #Correo opcional
                print(msg.opcional_correo)
                opcion_correo = int(input())

                if(opcion_correo == 1):  #Pide correo y registra propietario con correo
                    print(msg.in_correo)
                    correo_propietario = str(input())
                    break

                elif(opcion_correo == 2): #Registra cliente sin correo
                    correo_propietario = "No"
                    break

                else: #No ingresa 1 o 2
                    print(msg.err)
            print("Debe registrar un inmueble")
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
                logeado=Propietario(cedula_propietario,nombre_propietario,contrasena_propietario,direccion,correo_propietario)
                lista_propietarios.append(logeado)
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
                    inmu.addArriendo(arrie)#enlace inmueble con arriendo
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
                print(msg.regd)
    else:
        print(msg.err)
