class Compraventa:
    def __init__(self, codigo, propietario, fecha, valor, fechafin, inmueble, valorVenta, comprador=None):
        self._codigo=codigo
        self._fecha = fecha #fecha de pubicacion de la venta
        self._valor = valor
        self._fechafin = fechafin 
        self._inmueble=inmueble
        self._propietario=propietario
        self._comprador=comprador
        self._valorVenta = valorVenta

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
    
    def setInmueble(self,inmueble):
        self._inmueble=inmueble

    def getValorVenta(self):
        return self._valorVenta

    def setCodigo(self, ValVen):
        self._valorVenta = ValVen
        
    def toString(self):
        printer = "{"+"codigo: "+str(self._codigo)+", fecha: "+str(self._fecha)+", valor: "+str(self._valor)+", fechafin: "+str(self._fechafin)+", inmueble: "+str(self._inmueble.toString())+", propietario: "+str(self._propietario)", valor_venta: "+str(self._valorVenta)+", comprador: "+str(self._comprador)+" }"
        return printer
    
    @staticmethod
    def precioMasBajo(compraventas):
        menor=compraventas[0]
        for Compraventa in compraventas:
            if Compraventa.getValor<menor.getValor:
                menor=compraventa
        return menor

    @staticmethod
    def precioMasAlto(compraventas):
        mayor=compraventas[0]
        for Compraventa in compraventas:
            if Compraventa.getValor>mayor.getValor:
                mayor=Compraventa
        return mayor
    
    @staticmethod
    def mostrarCompraventas(compraventas):
        for compraventa in compraventas:
            print(compraventa.toString())
