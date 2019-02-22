
from Contrato import Contrato
class Arriendo(Contrato):
    def __init__(self, codigo, fechainicio,fechafin, valor, inmueble, agencia, arrendatario=None):
        super().__init__(codigo,fechainicio,valor,inmueble)
        self._arrendatario=arrendatario
        self._agencia=agencia
        self._fechafin=fechafin


    def getArrendatario(self):
        return self._arrendatario

    def setArrendatario(self,arrendatario):
        self._arrendatario=arrendatario
        
    def __str__(self):
        printer = "Arriendo: {"+"codigo: "+str(self._codigo)+", fecha inicio: "+str(self._fecha)+", costo mensual: "+str(self._valor)+", fechafin: "+str(self._fechafin)+", inmueble: "+str(self._inmueble.__str__())+", arrendatario: "+str(self._arrendatario.__str__())+", agencia: "+str(self._agencia)+" }"
        return printer
    
    @staticmethod
    def mostrarArriendos(arriendos):
        r=""
        for arriendo in arriendos:
            r+=arriendo.__str__()+"\n"
        return r
    #Metodo para buscar arriendos disponibles
    @staticmethod
    def arriendosDisponibles(arriendos):
        r=""
        for arriendo in arriendos:
            if arriendo.getDisponible():
                r+=arriendo.__str__()+"\n"
        return r

    #Buscar arriendos por codigo
    @staticmethod
    def buscarArriendo(arriendos, codigo):
        for arriendo in arriendos:
            if arriendo.getCodigo()==codigo:
                return arriendo
        return None

    @staticmethod
    def buscarArriendoPorEstrato(arriendos,estradoIni, estratoTop):
        r=""
        for arriendo in arriendos:
            if estradoIni <= arriendo.getInmueble().getEstrato() <= estratoTop:
                r+=arriendo.__str__()+"\n"
        return r
       

    @staticmethod
    def buscarArriendoPorNumeroCuartos(arriendos,cuartosIni, cuartosTop):
        r=""
        for arriendo in arriendos:
            if cuartosIni <= arriendo.getInmueble().getCuartos() <= cuartosTop:
                r+=arriendo.__str__()+"\n"
        return r

    @staticmethod
    def buscarArriendoPorNumeroBanios(arriendos,baniosIni, baniosTop):
        r=""
        for arriendo in arriendos:
            if baniosIni <= arriendo.getInmueble().getBanos() <= baniosTop:
              r+=arriendo.__str__()+"\n"
        return r
