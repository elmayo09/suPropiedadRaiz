class Compraventa:
    def __init__(self,codigo, propietario, fecha, valor, fechafin,inmueble,comprador=None):
        self._codigo=codigo
        self._fecha = fecha #fecha de pubicacion de la venta
        self._valor = valor
        self._fechafin = fechafin 
        self._inmueble=inmueble
        self._propietario=propietario
        self._comprador=comprador

    def getCodigo(self):
        return self._codigo

    def setCodigo(self, codigo):
        self._codigo = codigo

    def getFecha(self):
        return self._fecha

    def setFecha(self, fe):
        self._fecha = fe

    def getValor(self):
        return self._valor

    def setValor(self, va):
        self._valor = va

    def getFechafin(self):
        return self._fechafin

    def setFechafin(self, fef):
        self._fechafin = fef
        
    def getPropietario(self):
        return self._propietario

    def setPropietario(self,cliente):
        self._propietario=cliente

    def getComprador(self):
        return self._comprador

    def setComprador(self,cliente):
        self._comprador=cliente

    def getInmbueble(self):
        return self._inmueble

    @staticmethod
    def sinComprador(compraventas):
        lista=[]
        for compraventa in compraventas:
            if compraventa.getComprador==None:
                lista.append(compraventa)
    
    @staticmethod
    def compraventaPorPropietario(compraventas, propietario):
        lista=[]
        for compraventa in compraventas:
            if compraventa.getPropietario==propietario:
                lista.append(compraventa)
        return lista