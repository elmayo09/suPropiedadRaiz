
class Inmueble:
    listaInmuebles = []
    def __init__(self, estrato, direccion, vigilancia, ascensor, area, cuartos, banos, tipo,antiguedad,ciudad,propietario):
        self._estrato = estrato
        self._direccion = direccion
        self._vigilancia = vigilancia
        self._ascensor = ascensor
        self._area = area
        self._banos = banos
        self._cuartos = cuartos
        self._tipo = tipo    #El tipo es para saber ACTUALMENTE si esta en compra-venta o en arriendo
        self._arriendo=[]
        self._compraventa=None
        self._propietario=propietario
        self._ciudad=ciudad  
        self._antiguedad=antiguedad   

    def __str__(self):
        printer = "Inmueble: {"+"estrato: "+str(self._estrato)+", direccion: "+str(self._direccion)+", vigilancia: "+str(self._vigilancia)+", ascensor: "+str(self._ascensor)+", area: "+str(self._area)+", banios: "+str(self._banos)+", cuartos: "+str(self._cuartos)+", tipo: "+str(self._tipo)+" }"
        return printer
    
    def getEstrato(self):
        return self._estrato
    
    def setEstrato(self, est):
        self._estrato = est
        
    def getDireccion(self):
        return self._direccion
    
    def setDireccion(self,dire):
        self._direccion = dire
    
    def getVigilancia(self):
        return self._vigilancia

    def setVigilancia(self,vi):
        self._vigilancia = vi
    
    def getAscensor(self):
        return self._ascensor

    def setAscensor(self,asc):
        self._ascensor = asc
    
    def getArea(self):
        return self._area

    def setArea(self,ar):
        self._area = ar
    
    def getBanos(self):
        return self._banos

    def setBanos(self, ba):
        self._banos = ba

    def getCuartos(self):
        return self._cuartos

    def setCuartos(self,cu):
        self._cuartos = cu
    
    def getTipo(self):
        return self._tipo

    def setTipo(self,ti):
        self._tipo = ti

    def getCiudad(self):
        return self._ciudad

    def setCiudad(self, ciu):
        self._ciudad = ciu

    def getArriendo(self):
        return self._arriendo

    def addArriendo(self,contratoArriendo):
        if self._compraventa==None:
            self._arriendo.append(contratoArriendo)
        else:
            print("No se puede arendar,ya esta en venta")

    def getCompraventa(self):
        return self._compraventa

    def setCompraventa(self, compraventa):
        if self._compraventa==None:
            self._compraventa=compraventa
        else:
            print("Ya se vendio")


     
    @staticmethod
    def buscarInmueblesEnArriendo(lista):
        listaArriendo = []
        for inmuebles in lista:
            if(inmuebles.getTipo() == "enArriendo"):
                listaArriendo.append(inmuebles.toString())
        return listaArriendo

    @staticmethod
    def buscarInmueblesEnVenta(lista):
        listaArriendo = []
        for inmuebles in lista:
            if(inmuebles.getTipo() == "enVenta"):
                listaArriendo.append(inmuebles.toString())
        return listaArriendo

    @staticmethod
    def verListaInmuebles(lista):
        for inmueble in lista:
            print(inmueble.__str__())
