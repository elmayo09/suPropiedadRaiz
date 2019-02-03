class Arriendo:
    def __init__(self, fechainicio, fechafin, costomensual,inmueble):
        self._fechainicio = fechainicio
        self._costomensual = costomensual
        self._fechafin = fechafin
        self._inmueble=inmueble
        self._cliente=None

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
        

    
