from Usuario import Usuario
class Propietario(Usuario):
    def __init__(self,cedula,nombre, contrasena,direccion,correo="No"):
        super().__init__(cedula,nombre,contrasena,correo)
        self._direccion=direccion
        self._inmuebles = []
        self._funcionario=None


    def toString(self):
        printer = "Propietario: {"+self._nombre+", "+self._direccion+", "+self._correo+", "+str(self._cedula)+" }"
        return printer
    
    
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    def getInmuebles(self):
        return self._inmuebles
    def addInmueble(self, nuevoInmueble):
        self._inmuebles.append(nuevoInmueble)
    def setFuncionario(self,funcionario):
        self._funcionario=funcionario
    def getFuncionario(self):
        return self._funcionario

    
