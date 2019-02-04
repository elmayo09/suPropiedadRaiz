class Usuario:
    def __init__(self,cedula,nombre,contrasena,correo="No"):
        self._cedula=cedula
        self._nombre=nombre
        self._correo=correo
        self._contrasena=contrasena
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
    @staticmethod
    def login(nom, contra, lista):
        for x in lista:
            if x.getNombre()==nom:                
                if x.getContrasena()==contra:
                    return x
                else:
                    return None
        return None

