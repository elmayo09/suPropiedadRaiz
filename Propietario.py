from Usuario import Usuario
class Propietario(Usuario):
    def __init__(self,cedula,nombre, contrasena,direccion,correo="No"):
        super().__init__(cedula,nombre,contrasena,correo)
        self._direccion=direccion
        self._compraventas=[]
        self._arriendos=[]

    def toString(self):
        printer = "Propietario: {"+self._nombre+", "+self._direccion+", "+self._correo+", "+str(self._cedula)+" }"
        return printer
    
    
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    def getListaConmpraventas(self):
        return self._compraventas
    def addCompraventa(self,contrato):
        self._arriendos.append(contrato)
    def getListaArriendos(self):
        return self._arriendos
    def addCArriendo(self,contrato):
        self._arriendos.append(contrato)
    
