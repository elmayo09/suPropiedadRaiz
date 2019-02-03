from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self,cedula,nombre,apellido, contrasena,direccion,correo="No"):
        super().__init__(cedula,nombre,apellido,contrasena,correo)
        self._direccion=direccion
        self._arriendos=[]
        self._compraventas=[]
        self._funcionario=None

    def toString(self):
        printer = "Usuario: {"+self._nombre+", "+self._apellido+", "+self._direccion+", "+self._correo+" }"
        return printer
        
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    def getArriendos(self):
        return self._arriendos
    def addArriendo(self, nuevoArriendo):
        self._arriendos.append(nuevoArriendo)
    def getCompraventas(self):
        return self._compraventas
    def addCompraventa(self, nuevaCompraventa):
        self._compraventas.append(nuevaCompraventa)
    def setFuncionario(self,funcionario):
        self._funcionario=funcionario
    def getFuncionario(self):
        return self._funcionario



