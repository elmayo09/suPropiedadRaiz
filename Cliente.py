
from Usuario import Usuario
class Cliente(Usuario):
    def __init__(self,cedula,nombre, contrasena,direccion,correo="No"):
        super().__init__(cedula,nombre,contrasena,correo)
        self._direccion=direccion
        #self._arriendos=[]
        #self._compraventas=[]
        self._contratos=[]

    def __str__(self):
        printer = "Cliente: { cedula: "+str(self._cedula)+" ,nombre: "+str(self._nombre)+" ,direccion: "+str(self._direccion)+", correo: "+str(self._correo)+" }"
        return printer
          
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    #def getArriendos(self):
     #   return self._arriendos
    #def addArriendo(self, nuevoArriendo):
     #   self._arriendos.append(nuevoArriendo)
    #def getCompraventas(self):
     #   return self._compraventas
    #def addCompraventa(self, nuevaCompraventa):
     #   self._compraventas.append(nuevaCompraventa)
    def addContrato(self, contrato):
        self._contratos.append(contrato)
    @staticmethod
    def mostrarClientes(lista):
        for u in lista:
            print(u.toString())

