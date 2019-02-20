from Contrato import Contrato
class Compraventa(Contrato):
    def __init__(self, codigo, fecha, valor, inmueble, medioPago, comprador=None):
        super().__init__(codigo,fecha,valor,inmueble)
        self._comprador=comprador
        self._medioPago=medioPago


    def getComprador(self):
        return self._comprador

    def setComprador(self,cliente):
        self._comprador=cliente

    def getMedioPago():
        return self._medioPago

    def setMedioPago(self,medioPago):
        self._medioPago=medioPago

    def __str__(self):
        printer = "Compraventa: {"+"codigo: "+str(self._codigo)+", fecha: "+str(self._fecha)+", costo total: "+str(self._valor)+", inmueble: "+str(self._inmueble.__str__())+", propietario: "+str(self._propietario)+", comprador: "+str(self._comprador)+" }"
        return printer
    
    @staticmethod
    def mostrarCompraventas(compraventas):
        for compraventa in compraventas:
            print(compraventa.__str__())

    #Metodo para buscar compraventas disponibles
    @staticmethod
    def compraventasDisponibles(compraventas):
        for compraventa in compraventas:
            if compraventa.getDisponible():
                print(compraventa.__str__())

    #Buscar compraventa por codigo
    @staticmethod
    def buscarCompraventa(compraventas, codigo):
        for compraventa in compraventas:
            if compraventa.getCodigo()==codigo:
                return compraventa
        return None

