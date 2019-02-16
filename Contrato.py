class Contrato:
    def __init__(self, codigo, fecha, valor, propietario, inmueble):
        self._coido = codigo
        self._fecha = fecha#fecha de pubicacion del contrato
        self._valor = valor
        self._inmueble = inmueble

    def getCodigo(self):
        return self._coido

    def setCodigo(self, codigo):
        self._coido = codigo

    def getFecha(self):
        return self._fecha

    def setFecha(self, fe):
        self._fecha = fe

    def getValor(self):
        return self._valor

    def setVAlor(self, val):
        self._valor = val
        
    def getPropietario(self):
        return self._propietario

    def setPropietario(self,propietario):
        self._propietario = propietario

    def getInmbueble(self):
        return self._inmueble

    def setInmueble(self, inmueble):
        self._inmueble = inmueble
        
    @staticmethod
    def precioMasBajo(contratos):
        menor=contratos[0]
        for Contrato in contratos:
            if Contrato.getValor<menor.getValor:
                menor=Contrato
        return menor

    @staticmethod
    def precioMasAlto(contratos):
        mayor=contratos[0]
        for Contrato in contratos:
            if Contrato.getValor>mayor.getValor:
                mayor=Contrato
        return mayor
    
    @staticmethod
    def mostrarValoresContratos(contratos):
        for contrato in contratos:
            print(contrato.toString())
    
