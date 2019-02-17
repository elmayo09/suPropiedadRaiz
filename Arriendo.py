
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
        printer = "Arriendo: {"+"codigo: "+str(self._codigo)+", fecha inicio: "+str(self._fecha)+", costo mensual: "+str(self._valor)+", fechafin: "+str(self._fechafin)+", inmueble: "+str(self._inmueble.__str__())+", propietario: "+str(self._propietario.__str__())+", arrendatario: "+str(self._arrendatario.__str__())+", agencia: "+str(self._agencia)+" }"
        return printer
    
    @staticmethod
    def mostrarArriendos(arriendos):
        for arriendo in arriendos:
            print(arriendo.__str__())

    #Metodo para buscar arriendos disponibles
    @staticmethod
    def arriendosDisponibles(arriendos):
        for arriendo in arriendos:
            if arriendo.getDisponible():
                print(arriendo.__str__())

    #Buscar arriendos por codigo
    @staticmethod
    def buscarArriendo(arriendos, codigo):
        for arriendo in arriendos:
            if arriendo.getCodigo()==codigo:
                return arriendo
        return None