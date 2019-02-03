from Usuario import Usuario
from Usuario import Usuario
class Funcionario(Usuario):
    def __init__(self,cedula,nombre,apellido, contrasena,sueldo,comision,correo="No"):
        super().__init__(cedula,nombre,apellido,contrasena,correo)
        self._sueldo=sueldo
        self._comision=comision
        self._clientes=[]

    def getSueldo(self):
        return self._sueldo
    def setSueldo(self,sueldo):
        self._sueldo=sueldo
    def getComision(self):
        return self._comision
    def setComision(self,comision):
        self._comision=comision
    def getListaClientes(self):
        return self._clientes
    def addCliente(self,cliente):
        self._clientes.append(cliente)

    def toString(self):
        printer = "{"+"cedula: "+str(self._cedula)+", nombre: "+str(self._nombre)+", apellido: "+str(self._apellido)+", correo: "+str(self._correo)+", contraseña: "+str(self._contrasena)+", sueldo: "+str(self._sueldo)+", comision: "+str(self._comision)+" }"
        return printer
        
    @staticmethod    
    def funcionarioMayorSueldo(funcionarios):
        mayor=funcionarios[0].getSueldo()
        for funcionario in funcionarios:
            if mayor< funcionario.getSueldo():
                mayor=funcionario
        return mayor




