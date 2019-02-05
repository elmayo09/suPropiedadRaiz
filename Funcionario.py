from Usuario import Usuario
class Funcionario(Usuario):
    def __init__(self,cedula,nombre, contrasena,sueldo,comision,correo="No"):
        super().__init__(cedula,nombre,contrasena,correo)
        self._sueldo=sueldo
        self._comision=comision
        self._compraventas=[]
        self._arriendos=[]

    def getSueldo(self):
        return self._sueldo
    def setSueldo(self,sueldo):
        self._sueldo=sueldo
    def getComision(self):
        return self._comision
    def setComision(self,comision):
        self._comision=comision
    def getListaConmpraventas(self):
        return self._compraventas
    def addCompraventa(self,contrato):
        self._arriendos.append(contrato)
    def getListaArriendos(self):
        return self._arriendos
    def addCArriendo(self,contrato):
        self._arriendos.append(contrato)

    def toString(self):
        printer = "Funcionario: {"+"cedula: "+str(self._cedula)+", nombre: "+str(self._nombre)+", correo: "+str(self._correo)+", sueldo: "+str(self._sueldo)+", comision: "+str(self._comision)+" }"
        return printer
           
    @staticmethod    
    def funcionarioMayorSueldo(funcionarios):
        mayor_sueldo = funcionarios[0].getSueldo()
        mayor = funcionarios[0]
        for funcionario in funcionarios:
            if mayor_sueldo < funcionario.getSueldo():
                mayor = funcionario
        return mayor
    
    @staticmethod
    def mostrarFuncionarios(lista):
        for u in lista:
            print(u.toString())




