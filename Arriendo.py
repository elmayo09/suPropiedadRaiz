class Arriendo:
    def __init__(self, codigo, fechainicio, costomensual, fechafin, inmueble, propietario, arrendatario=None):
        self._codigo = codigo
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

    def getPropietario(self):
        return self._propietario

    def setPropietario(self,propietario):
        self._propietario=propietario

    def getArrendatario(self):
        return self._arrendatario

    def setArrendatario(self,arrendatario):
        self._arrendatario=arrendatario

    def getInmbueble(self):
        return self._inmueble
    def setInmueble(self, inmueble):
        return self._inmueble
        
    def toString(self):
        printer = "{"+"codigo: "+str(self._codigo)+", fecha inicio: "+str(self._fechainicio)+", costo mensual: "+str(self._costomensual)+", fechafin: "+str(self._fechafin)+", inmueble: "+str(self._inmueble.toString())+", propietario: "+str(self._propietario)+", arrendatario: "+str(self._arrendatario)+" }"
        return printer
        
    @staticmethod
    def arriendoMasBajo(arriendos):
        menor=arriendos[0]
        for arriendo in arriendos:
            if arriendo.getCostomensual<menor.getCostomensual:
                menor=arriendo
        return menor

    @staticmethod
    def arriendoMasAlto(arriendos):
        mayor=arriendos[0]
        for arriendo in arriendos:
            if arriendo.getCostomensual>mayor.getCostomensual:
                mayor=arriendo
        return mayor
    
    @staticmethod
    def mostrarArriendos(arriendos):
        for arriendo in arriendos:
            print(arriendo.toString())

        
