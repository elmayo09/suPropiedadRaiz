class Propietario:
    def __init__(self,cedula,nombre, contrasena,direccion,correo="No"):
        self._cedula=cedula
        self._nombre=nombre
        self._correo=correo
        self._contrasena=contrasena
        self._direccion=direccion
        self._inmuebles=[]

    def __str__(self):
        printer = "{ Nombre: "+self._nombre+",Direccion: "+self._direccion+", Correo"+self._correo+", Cedula: "+str(self._cedula)+" }"
        return printer
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getContrasena(self):
        return self._contrasena
    def setContrasena(self, contra):
        self._contrasena=contra
    def getCedula(self):
        return self._cedula
    def setCedula(self, cedula):
        self._cedula=cedula
    def getCorreo(self):
        return self._correo
    def setCorreo(self, correo):
        self._correo=correo
    def getDireccion(self):
        return self._direccion
    def setDireccion(self,direccion):
        self._direccion=direccion
    def addInmueble(self,inmueble):
        self._inmuebles.append(inmueble)
    def getInmuebles(self):
        return self._inmuebles

    @staticmethod
    def login(ced, contra, lista):
        for x in lista:
            if x.getCedula()==ced:              
                if x.getContrasena()==contra:
                    return x
                else:
                    return None
        return None