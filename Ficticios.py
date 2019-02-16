from Cliente import Cliente
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