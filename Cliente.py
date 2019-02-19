
class Cliente:
    def __init__(self,cedula,nombre, contrasena,direccion,correo="No"):
        self._cedula=cedula
        self._nombre=nombre
        self._correo=correo
        self._contrasena=contrasena
        self._direccion=direccion
        self._contratos=[]
        #

    def __str__(self):
        printer = "Cliente: { cedula: "+str(self._cedula)+" ,nombre: "+str(self._nombre)+" ,direccion: "+str(self._direccion)+", correo: "+str(self._correo)+" }"
        return printer
          
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getContrasena(self):
        return self._contrasena
    def setContrasena(self, contra):
        self._contrasena=contra
    def getCedula(self):
        return self._cedula
    def setCedula(self, cedula):
        self._cedula=cedula
    def getCorreo(self):
        return self._correo
    def setCorreo(self, correo):
        self._correo=correo
    def addContrato(self, contrato):
        self._contratos.append(contrato)
    def getContratos(self):
        return self._contratos
    @staticmethod
    def mostrarClientes(lista):
        for u in lista:
            print(u.__str__())
    @staticmethod
    def login(ced, contra, lista):
        for x in lista:
            if x.getCedula()==ced:              
                if x.getContrasena()==contra:
                    return x
                else:
                    return None
        return None
