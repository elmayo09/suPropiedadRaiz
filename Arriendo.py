class Arriendo:
    def __init__(self, propietario, fechainicio, fechafin, costomensual,inmueble, arrendatario=None):
        self._fechainicio = fechainicio
        self._costomensual = costomensual
        self._fechafin = fechafin
        self._inmueble=inmueble
        self._propietario=propietario
        self._arrendatario=arrendatario

    def getFechainicio(self):
        return self._fechainicio

    def setFechainicio(self, fe):
        self._fechainicio = fe

    def getCostomensual(self):
        return self._costomensual

    def setCostomensual(self, co):
        self._costomensual = co
        
    def getFechafin(self):
        return self._fechafin

    def setFechafin(self, fef):
        self._fechafin = fef

    def getCliente(self):
        return self._cliente

    def setCliente(self,cliente):
        self._cliente=cliente

    def getInmbueble(self):
        return self._inmueble
        

    @staticmethod
    def arriendoMasBajo(arriendos):
        menor=arriendos[0]
        for arriendo in arriendos:
            if arriendo.getCostomensual<menor.getCostomensual:
                menor=arriendo
        return arriendo

    @staticmethod
    def arriendoMasAlto(arriendos):
        mayor=arriendos[0]
        for arriendo in arriendos:
            if arriendo.getCostomensual>mayor.getCostomensual:
                mayor=arriendo
        return arriendo

        
