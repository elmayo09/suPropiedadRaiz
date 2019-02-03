class Usuario:
    def __init__(self,cedula,nombre,apellido,contrasena,correo="No"):
        self._cedula=cedula
        self._nombre=nombre
        self._apellido=apellido
        self._correo=correo
        self._contrasena=contrasena
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre=nombre
    def getCedula(self):
        return self._cedula
    def setCedula(self, cedula):
        self._cedula=cedula
    def getCorreo(self):
        return self._correo
    def setCorreo(self, correo):
        self._correo=correo
    

