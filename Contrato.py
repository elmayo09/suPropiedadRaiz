class Contrato:
    def __init__(self, codigo, fecha, valor, inmueble,disponible=True):
        self._codigo = codigo
        self._fecha = fecha#fecha de pubicacion del contrato
        self._valor = valor
        self._inmueble = inmueble
        self._disponible = disponible

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

    def setValor(self, val):
        self._valor = val

    def getInmueble(self):
        return self._inmueble

    def setInmueble(self, inmueble):
        self._inmueble = inmueble

    def getDisponible(self):
        return self._disponible

    def setDisponible(self, disponible):
        self._disponible = disponible

    def __str__(self):
        printer = "{"+"codigo: "+str(self._codigo)+", fecha: "+str(self._fecha)+", valor: "+str(self._valor)+", inmueble: "+str(self._inmueble.__str__())+", propietario: "+str(self._propietario.__str__)+" }"
        return printer
        
    @staticmethod
    def precioMasBajo(contratos):
        menor=contratos[0]
        for contrato in contratos:
            if contrato.getValor() < menor.getValor():
                menor=contrato
        return menor

    @staticmethod
    def precioMasAlto(contratos):
        mayor=contratos[0]
        for contrato in contratos:
            if contrato.getValor()>mayor.getValor():
                mayor=contrato
        return mayor
    
    @staticmethod
    def mostrarValoresContratos(contratos):
        r= ""
        for contrato in contratos:
            r=r+contrato.__str__()+"\n"
        return r
    
    @staticmethod
    def buscarPorCiudad(contratos, ciudad):
        r = ""
        for contrato in contratos:
            if (contrato.getInmueble().getCiudad() == ciudad):
               r=r+contrato.__str__()+"\n"
        if len(r)<0:
            return "no"
        else:
            return r
        
