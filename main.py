
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


if __name__ == '__main__':
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
            Ficticios.agregarDatosFicticios(lista_clientes,lista_propietarios,lista_compraventas,lista_inmuebles,lista_arriendos)
            print(msg.datosFicticios)
        #----------------------------------------------------------------------------
        elif(opcion1 == 2): #segunda opcion menu principal ingreso propietario
            print(msg.ingreso)
            print(msg.cedula)
            ced = int(input())
            print(msg.contrasena)
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
                        print(msg.para_reg+msg.inmueble+"\n"+msg.ing)
                        print(msg.estrato)
                        estrato = str(input())
                        print(msg.direccion)
                        direccion = str(input())
                        for inmueble in lista_inmuebles:  #busca la direccion entre los inmuebles existentes
                            if(inmueble.getDireccion() == direccion):
                                print(msg.inmueble_existe)
                                direccion=0
                                break
                        if direccion!=0:
                            print(msg.in_vigilancia)
                            vigilancia = str(input())
                            if (vigilancia == "s" or vigilancia == "y"):
                                vigilancia=True
                            else: vigilancia=False
                            print(msg.in_ascensor)
                            ascensor = str(input())
                            if (ascensor == "s" or ascensor == "y"):
                                ascensor=True
                            else: ascensor=False
                            print(msg.area)
                            area = int(input())
                            print(msg.cuartos)
                            cuartos = int(input())
                            print(msg.banos)
                            banos = int(input())
                            print(msg.tipo)
                            tipo = str(input())
                            if(tipo == "rent"):
                                tipo = "arriendo"
                            elif (tipo == "sale"):
                                tipo = "compraventa"
                            print(msg.antiguedad)
                            antiguedad = int(input())
                            print(msg.ciudad)
                            ciudad = str(input())
                            inmu=Inmueble(estrato,direccion,vigilancia,ascensor,area,cuartos,banos,tipo,antiguedad,ciudad,logeado)#Creacion de inmueble
                            logeado.addInmueble(inmu)#enlace propietario con inmueble
                            if (tipo == "arriendo"):
                                #creacion arriendo
                                print(msg.creando_contrato+msg.arriendo)
                                codigo_contrato+=1
                                print(msg.fecha_inicio)
                                fechainicio = str(input())
                                print(msg.fecha_fin)
                                fechafin = str(input())
                                print(msg.valor_mensual)
                                valor = int(input())
                                print(msg.in_agencia)
                                agencia = str(input())
                                if (agencia == "s" or agencia == "y"):
                                    agencia=True
                                else: agencia=False
                                arrie=Arriendo(codigo_contrato,fechainicio,fechafin,valor,inmu,agencia)#Creacion de contrato de arriendo enlazado a propietario e inmueble
                                inmu.addArriendo(arrie)#enlace inmueble con arriendo
                                lista_inmuebles.append(inmu)
                                lista_arriendos.append(arrie)
                            else:
                                #Creacion compraventa
                                print(msg.creando_contrato+msg.compraventa)
                                codigo_contrato+=1
                                print(msg.fecha_actual)
                                fecha = str(input())
                                print(msg.valor)
                                valor = int(input())
                                print(msg.medio_pago)
                                medioPago = str(input())
                                compraV=Compraventa(codigo_contrato,fecha,valor,inmu,medioPago)#Creacion de contrato de compraventa enlazado a propietario e inmueble
                                inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
                                lista_inmuebles.append(inmu)
                                lista_compraventas.append(compraV)
                            print(msg.regd)

                    elif(opcion2 == 2):  #Ver los inmuebles del propietario actual
                        Inmueble.verListaInmuebles(logeado.getInmuebles())

                    elif(opcion2 == 3): #opcion 3 menu propietario Aprobar compraventas

                        print(msg.aprobar_comp)
                        lista = logeado.getInmuebles()
                        for inmueble in lista:
                            if(inmueble.getTipo() == "solicitado_compraventa"):
                                contrato_actual = inmueble.getCompraventa()
                                print(msg.desea_comp + contrato_actual.__str__() + "\n 1. Si \n 2. No")
                                opcion = int(input())
                                if(opcion == 1):
                                    inmueble.setTipo("Vendido")
                                    print(msg.vendido)
                                elif(opcion == 2):
                                    comprador = contrato_actual.getComprador()
                                    comprador.getContratos().remove(contrato_actual)
                                    contrato_actual.setComprador(None)
                                    inmueble.setTipo("compraventa")
                                    contrato_actual.setDisponible(True)
                                    print(msg.anulada_comp)
                                else:
                                    print(msg.err)
                        print(msg.no_mas_comp)               

                    elif(opcion2 == 4): #opcion 4 menu propietario Aprobar arriendos
                        print(msg.aprobar_arr)
                        lista = logeado.getInmuebles()
                        for inmueble in lista:
                            if(inmueble.getTipo() == "solicitado_arriendo"):
                                contrato = inmueble.getArriendo()
                                arriendo_actual = contrato[-1]
                                print(msg.desea_arr + arriendo_actual.__str__() + "\n 1. Si \n 2. No")
                                opcion = int(input())
                                if(opcion == 1):
                                    inmueble.setTipo("Arrendado")
                                    print(msg.arrendado)
                                elif(opcion == 2):
                                    arrendatario = arriendo_actual.getArrendatario()
                                    arrendatario.getContratos().remove(arriendo_actual)
                                    arriendo_actual.setArrendatario(None)
                                    inmueble.setTipo("arriendo")
                                    arriendo_actual.setDisponible(True)
                                    print(msg.anulada_arr)
                                else:
                                    print(msg.err)
                        print(msg.no_mas_arr)               

                #Fin menu propietario----------------------------------------------------------------------------

                        
            #----------------------------------------------------------------------------
            else:
                print(msg.err_datos) #Datos erroneos funcionario
       
        #----------------------------------------------------------------------------           
        elif(opcion1 == 3): #opcion 3 menu principal registrtar cliente
            print(msg.registro)
            print(msg.cedula)
            cedula_cliente = int(input())
            encontrado = False
            for client in lista_clientes:
                if (client.getCedula() == cedula_cliente): #encuentra un cliente con esa cedula
                    print(msg.existe)
                    encontrado = True
                    break
            if(encontrado == False):  #No hay un cliente con esa cedula
                print(msg.nombre)
                nombre_cliente = str(input())
                print(msg.contrasena)
                contrasena_cliente = str(input())
                print(msg.direccion)
                direccion_cliente = str(input())
                

                while(True):  #Correo opcional
                    print(msg.opcional_correo)
                    opcion_correo = int(input())

                    if(opcion_correo == 1):  #Pide correo y registra cliente con correo
                        print(msg.correo)
                        correo_cliente = str(input())
                        cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente, correo_cliente)
                        lista_clientes.append(cliente_nuevo)
                        print(msg.regd+cliente_nuevo.__str__())
                        f = open('ficticios.txt','a')
                        f.write('\n' + 'cedula: '+str(cedula_cliente)+', nombre: '+nombre_cliente+', contrasena: '+contrasena_cliente+', direccion: '+direccion_cliente+', correo: '+correo_cliente+'.')
                        f.close()
                        break

                    elif(opcion_correo == 2): #Registra cliente sin correo
                        cliente_nuevo = Cliente(cedula_cliente, nombre_cliente, contrasena_cliente, direccion_cliente)
                        lista_clientes.append(cliente_nuevo)
                        print(msg.regd+cliente_nuevo.__str__())
                        f = open('ficticios.txt','a')
                        f.write('\n\n' + 'cedula: '+str(cedula_cliente)+', nombre: '+nombre_cliente+', contrasena: '+contrasena_cliente+', direccion: '+direccion_cliente+', correo: No.')
                        f.close()
                        break

                    else: #No ingresa 1 o 2
                        print(msg.err)
        #--------------------------------------------------------
        elif(opcion1 == 4):  #opciop 4 del menu principal Ingreso Como Cliente
            print(msg.ingreso)

            print(msg.cedula)
            ced = int(input())
            print(msg.contrasena)
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
                        print(msg.ing)
                        print(msg.sel_compraventa)
                        codigo_compraventa=int(input())
                        compraventa_actual=Compraventa.buscarCompraventa(lista_compraventas,codigo_compraventa)
                        if compraventa_actual==None or not compraventa_actual.getDisponible():
                            print(msg.codigo_invalido)
                        else:
                            print(compraventa_actual.__str__())
                            oferta=input(msg.in_aplicar_compraventa)
                            if (oferta == "s" or oferta == "y"):
                                compraventa_actual.setDisponible(False)
                                compraventa_actual.setComprador(logeado)#enlace entre compraventa y el comprador
                                logeado.addContrato(compraventa_actual)
                                compraventa_actual.getInmueble().setTipo("solicitado_compraventa")
                                print(msg.apli_com)
                            else:
                                print(msg.no_apli_com+str(compraventa_actual.getCodigo()))

                    elif(opciones_cliente == 4): #Seleccionar arriendo
                        print(msg.sel_arriendo)
                        codigo_arriendo=int(input())
                        arriendo_actual=Arriendo.buscarArriendo(lista_arriendos,codigo_arriendo)
                        
                        if arriendo_actual==None or not arriendo_actual.getDisponible():
                            print(msg.codigo_invalido)
                        else:
                            print(arriendo_actual.__str__())
                            oferta=input(msg.in_aplicar_arriendo)
                            if (oferta == "s" or oferta == "y"):
                                arriendo_actual.setDisponible(False)
                                arriendo_actual.setArrendatario(logeado)#enlace entre arriendo y el arrendatario
                                logeado.addContrato(arriendo_actual)#se anade el contrato de arrendamieno a la lista de contratos del cliente
                                arriendo_actual.getInmueble().setTipo("solicitado_arriendo")
                                print(msg.apli_arr)
                            else:
                                print(msg.no_apli_arr+str(arriendo_actual.getCodigo()))

                    elif(opciones_cliente == 5):#ver mis contratos actuales
                        print(Contrato.mostrarValoresContratos(logeado.getContratos()))

                    elif (opciones_cliente == 6):#ver ofertas de arrendamiento por estrato. 
                        print(msg.estrato_ini)
                        estratoIni=int(input())
                        print(msg.estrato_top)
                        estratoTop=int(input())
                        Arriendo.buscarArriendoPorEstrato(lista_arriendos,estratoIni,estratoTop)
                         
                        
                    elif (opciones_cliente == 7):#ver ofertas de arrendamiento por numero de cuartos
                        print(msg.cuartos_ini)
                        cuartosIni=int(input())
                        print(msg.cuartos_top)
                        cuartosTop=int(input())
                        Arriendo.buscarArriendoPorNumeroCuartos(lista_arriendos,cuartosIni,cuartosTop)
                        
                    elif (opciones_cliente == 8):#ver ofertas de arrendamiento por numero de banos. 
                        print(msg.banios_ini)
                        baniosIni=int(input())
                        print(msg.banios_top)
                        baniosTop=int(input())
                        Arriendo.buscarArriendoPorNumeroBanios(lista_arriendos,baniosIni,baniosTop)
                        
                    elif (opciones_cliente == 9):#ver ofertas de arrendamiento por ciudad.
                        print(msg.ciudad)
                        ciudad = str(input())
                        print(Contrato.buscarPorCiudad(lista_arriendos,ciudad))
                    
                    elif (opciones_cliente == 10):#ver arriendo mas barato
                        menor=Contrato.precioMasBajo(lista_arriendos)
                        print(menor.__str__())

                    elif (opciones_cliente == 11):
                        #ver compraventa mas barata
                        mayor=Contrato.precioMasBajo(lista_compraventas)
                        print(mayor.__str__())
            else:
                print(msg.err_datos) #Datos erroneos cliente
                
        elif(opcion1 == 5): #Opcion 5 del menu principal registrar nuevo propietario
            print(msg.registro)
            print(msg.cedula)
            cedula_propietario = int(input())
            encontrado = False
            for prop in lista_propietarios:
                if (prop.getCedula() == cedula_propietario): #encuentra un propietario con esa cedula
                    print(msg.existe)
                    encontrado = True
                    break
            if(encontrado == False):  #No hay un propietario con esa cedula
                print(msg.nombre)
                nombre_propietario = str(input())
                print(msg.contrasena)
                contrasena_propietario = str(input())
                print(msg.direccion)
                direccion_propietario = str(input())
                while(True):  #Correo opcional
                    print(msg.opcional_correo)
                    opcion_correo = int(input())

                    if(opcion_correo == 1):  #Pide correo y registra propietario con correo
                        print(msg.correo)
                        correo_propietario = str(input())
                        break

                    elif(opcion_correo == 2): #Registra cliente sin correo
                        correo_propietario = "No"
                        break

                    else: #No ingresa 1 o 2
                        print(msg.err)
                print(msg.reg_inmueble)
                print(msg.ing)
                print(msg.estrato)
                estrato = str(input())
                print(msg.direccion)
                direccion = str(input())
                for inmueble in lista_inmuebles:  #busca la direccion entre los inmuebles existentes
                    if(inmueble.getDireccion() == direccion):
                        print(msg.inmueble_existe)
                        direccion=0
                        break
                if direccion!=0:
                    logeado=Propietario(cedula_propietario,nombre_propietario,contrasena_propietario,direccion,correo_propietario)
                    lista_propietarios.append(logeado)
                    print(msg.in_vigilancia)
                    vigilancia = str(input())
                    if (vigilancia == "s" or vigilancia == "y"):
                        vigilancia=True
                    else: vigilancia=False
                    print(msg.in_ascensor)
                    ascensor = str(input())
                    if (ascensor == "s" or ascensor == "y"):
                        ascensor=True
                    else: ascensor=False
                    print(msg.area)
                    area = int(input())
                    print(msg.cuartos)
                    cuartos = int(input())
                    print(msg.banos)
                    banos = int(input())
                    print(msg.tipo)
                    tipo = str(input())
                    if(tipo == "rent"):
                        tipo = "arriendo"
                    elif(tipo == "sale"):
                        tipo = "compraventa"
                    print(msg.antiguedad)
                    antiguedad = int(input())
                    print(msg.ciudad)
                    ciudad = str(input())
                    inmu=Inmueble(estrato,direccion,vigilancia,ascensor,area,cuartos,banos,tipo,antiguedad,ciudad,logeado)#Creacion de inmueble
                    logeado.addInmueble(inmu)#enlace propietario con inmueble
                    if (tipo == "arriendo"):
                        #creacion arriendo
                        print(msg.creando_contrato+msg.arriendo)
                        codigo_contrato+=1
                        print(msg.fecha_inicio)
                        fechainicio = str(input())
                        print(msg.fecha_fin)
                        fechafin = str(input())
                        print(msg.valor_mensual)
                        valor = int(input())
                        print(msg.in_agencia)
                        agencia = str(input())
                        if (agencia == "s" or agencia == "y"):
                            agencia=True
                        else: agencia=False
                        arrie=Arriendo(codigo_contrato,fechainicio,fechafin,valor,inmu,logeado,agencia)#Creacion de contrato de arriendo enlazado a propietario e inmueble
                        inmu.addArriendo(arrie)#enlace inmueble con arriendo
                        lista_inmuebles.append(inmu)
                        lista_arriendos.append(arrie)                    
                    else:
                        #Creacion compraventa
                        print(msg.creando_contrato+msg.compraventa)
                        codigo_contrato+=1
                        print(msg.fecha_actual)
                        fecha = str(input())
                        print(msg.valor)
                        valor = int(input())
                        print(msg.medio_pago)
                        medioPago = str(input())
                        compraV=Compraventa(codigo_contrato,logeado,fecha,valor,inmu,medioPago)#Creacion de contrato de compraventa enlazado a propietario e inmueble
                        inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
                        lista_inmuebles.append(inmu)
                        lista_compraventas.append(compraV)
                    print(msg.regd)
        
        #--------------------------------------------------------------------------------------
        elif(opcion1 == 6):#Opcion 6 del menu principal datos ficticios de clientes desde txt
            Ficticios.datos_desde_txt("ficticios.txt",lista_clientes) #agrega clientes ficticios desde txt
            print(msg.datosFicticios)
            Cliente.mostrarClientes(lista_clientes)
        #---------------------------------------------------------------------------------------
        else:
            print(msg.err)
