
from Contrato import Contrato
class Arriendo(Contrato):
    def __init__(self, codigo, fechainicio,fechafin, valor, inmueble, propietario, agencia, arrendatario=None):
        super().__init__(codigo,fechainicio,valor,propietario,inmueble)
        self._arrendatario=arrendatario
        self._agencia=agencia
        self._fechafin=fechafin


    def getArrendatario(self):
        return self._arrendatario

    def setArrendatario(self,arrendatario):
        self._arrendatario=arrendatario
        
    def __str__(self):
        printer = "{"+"codigo: "+str(self._codigo)+", fecha inicio: "+str(self._fechainicio)+", costo mensual: "+str(self._valor)+", fechafin: "+str(self._fechafin)+", inmueble: "+str(self._inmueble.toString())+", propietario: "+str(self._propietario)+", arrendatario: "+str(self._arrendatario)+" }"
        return printer
    
    @staticmethod
    def mostrarArriendos(arriendos):
        for arriendo in arriendos:
            print(arriendo.toString())
