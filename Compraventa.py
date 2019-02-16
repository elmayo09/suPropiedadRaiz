from Contrato import Contrato
class Compraventa(Contrato):
    def __init__(self, codigo, propietario, fecha, valor, inmueble, medioPago, comprador=None):
        super().__init__(codigo,fecha,valor,propietario,inmueble)
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
        printer = "{"+"codigo: "+str(self._codigo)+", fecha inicio: "+str(self._fechainicio)+", costo total: "+str(self._valor)+", inmueble: "+str(self._inmueble.toString())+", propietario: "+str(self._propietario)+", comprador: "+str(self._comprador)+" }"
        return printer
    
    @staticmethod
    def mostrarCompraventas(compraventas):
        for compraventa in compraventas:
            print(compraventa.toString())
