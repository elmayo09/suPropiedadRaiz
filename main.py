from Arriendo import Arriendo
from Cliente import Cliente
from Compraventa import Compraventa
from Funcionario import Funcionario
from Inmueble import Inmueble
from Usuario import Usuario
from mensaje import Mensaje as msg
codigos_unicos = 1000 #main
lista_funcionarios = []
primer_funcionario = Funcionario(999, "Karl", "111", 660000, 40000, "abc@sp.com")
lista_funcionarios.append(primer_funcionario)

primer_inmueble = Inmueble(3, "falsa", "si", "si", "si", 5, 2, 1, None)
Inmueble.listaInmuebles.append(primer_inmueble)

lista_clientes = []
lista_compraventas = []


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
        print(msg.err[idioma])
        
    elif(opcion1 == 2): #segunda opcion menu principal
        print("ingres nombre")
        nomb = str(input())
        print(msg.ingreso_contra[idioma])
        contra = str(input())

        logeado = Usuario.login(nomb, contra, lista_funcionarios)
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
                                elif(opcion3 ==1):
                                    print("ingrese datos arrendamiento")
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
                      
                        else:
                            print("no opcion valida")
                            break

  
                        
                            
                                   
                            
                    
                elif(opcion2 == 5): #Registrar nuevo arriendo
                    Funcionario.mostrarFuncionarios(lista_funcionarios)

                elif(opcion2 == 6): #Aprobar compraventas
                    Funcionario.mostrarFuncionarios(lista_funcionarios)

                elif(opcion2 == 7): #Aprobar arriendos
                    Funcionario.mostrarFuncionarios(lista_funcionarios)


                    

        else:
            print(msg.err_datos[idioma]) #Datos erroneos funcionario
                
    elif(opcion1 == 3):
        print(msg.err[idioma])
        
    elif(opcion1 == 4):
        print(msg.err[idioma])
        
    elif(opcion1 == 5):
        print(msg.err[idioma])
        
