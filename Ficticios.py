from Cliente import Cliente
from Compraventa import Compraventa
from Inmueble import Inmueble
from Propietario import Propietario
from Contrato import Contrato
from Arriendo import Arriendo
from random import *
class Ficticios:
	inicio = 0
	fin = 0

	@staticmethod
	def buscador(palabra, texto):
		Ficticios.inicio = texto.find(palabra, Ficticios.inicio)
		if (Ficticios.inicio < 0): #indice negativo = no encontrado
			return None
		Ficticios.inicio += len(palabra) #comienza el string atributo
		Ficticios.fin = texto.find(",",Ficticios.inicio) #finaliza el string atributo en coma
		punto_final = texto.find(".",Ficticios.inicio)  #finalizan datos de cada objeto en punto
		if(punto_final<=Ficticios.fin):  #diferencia entre fin de atributo y fin de objeto
			encontrada = texto[Ficticios.inicio:punto_final]
			Ficticios.fin = punto_final
			return encontrada

		encontrada = texto[Ficticios.inicio:Ficticios.fin]
		return encontrada

	@staticmethod
	def datos_desde_txt(nombre_txt, lista_objetos):
		file = open(nombre_txt, "r")
		linea = file.read()
		file.close()
		while(Ficticios.inicio>=0):
			#busca cedulas
			cedula = Ficticios.buscador("cedula: ",linea)
			if (cedula==None): #None = ya no hay mas datos en el archivo
				break
			#busca nombres
			nombre = Ficticios.buscador("nombre: ",linea)
			#busca contrasenas
			contrasena = Ficticios.buscador("contrasena: ",linea)
			#busca direcciones
			direccion = Ficticios.buscador("direccion: ",linea)
			#busca correos
			correo = Ficticios.buscador("correo: ",linea)

			nuevo_cliente = Cliente(cedula,nombre,contrasena,direccion,correo)
			lista_objetos.append(nuevo_cliente)

	@staticmethod
	def agregarDatosFicticios(lista_clientes,lista_propietarios,lista_compraventas,lista_inmuebles,lista_arriendos):
		valoresPassword = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		nombres=["Andres Gimenez","Maria Taja","Lina Gutierrez","Juan Sarrias","Carlos inut","Pepe Grillo","Sara Macias","Eduardo Mejia","Yeremi Guarin","Martina Tamayo",
    		"Martin Correa","Cristina Mejia", "Emanuel Valencia", "Cristopher Amaya","Jose Mercado","Josue Galindo","Natalia Osorio","Edgar Aguirre","Emilio del monte","Miranda Rodas"]
		codigo_contrato=100
		primer_propietario = Propietario(1234, "admin", "1234", "car40A12", "abc@sp.com")
		lista_propietarios.append(primer_propietario)
		inmu=Inmueble(0,"car."+str(randint(160,250)),False,True,randint(300,500),3,1,"enArriendo",9,"Medellin",primer_propietario)#Creacion de inmueble
		arrie=Arriendo(1,"20-11-1900","21-12-1990",randint(1000,150000),inmu,False)#Creacion de contrato de arriendo enlazado a propietario e inmueble
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
			arrie=Arriendo(cc,"20-11-2000","21-12-2012",randint(1000,150000),inmu,False)#Creacion de contrato de arriendo enlazado a propietario e inmueble
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
			compraV=Compraventa(cc,"20-11-2010",randint(1000,150000),inmu,"Efectivo")#Creacion de contrato de compraventa enlazado a propietario e inmueble
			inmu.setCompraventa(compraV)#enlace inmueble con la compraventa
			lista_inmuebles.append(inmu)
			lista_compraventas.append(compraV)
			lista_propietarios.append(c)
			cc=cc+1