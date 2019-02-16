class Contrato:
    def __init__(self, codigo, fecha, valor, propietario, inmueble):
        self._coido = codigo
        self._fecha = fecha
        self._valor = valor
        self._propietario = propietario
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
        return self._inmueble = inmueble
        
    def toString(self):
        printer = "{"+"fecha: "+str(self._fecha)+", valor: "+str(self._valor)+", propietario: "+str(self._propietario)+", inmueble: "+str(self._inmueble.toString())+" }"
        return printer
        
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
    def mostrarValorContrato(contratos):
        for contrato in contratos:
            print(contrato.toString())
    
