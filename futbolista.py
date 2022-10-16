import string
from deportista import Deportista
from persona import Persona
class Futbolista(Persona,Deportista):
    listaFutbolistas=[]
    def __init__(self,nombre="",edad=0,altura="0",sexo="", añosPracticando=0,goles=0,tarjetas=0,pierna="derecha"):
        Persona.__init__(self,nombre,edad,altura,sexo)
        Deportista.__init__(self,"Futbol",añosPracticando)
        self._golesMarcados=goles
        self._tarjetasRojas=tarjetas
        self._piernaHabil=pierna
        self.listaFutbolistas.append(self)
    def getGolesMarcados(self):
        return self._golesMarcados
    def setGolesMarcados(self,goles):
        self._golesMarcados=goles
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def setTarjetasRojas(self,tarjetas):
        self._tarjetasRojas=tarjetas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setPiernaHabil(self,pierna):
        self._piernaHabil=pierna
    @classmethod
    def getListaFutbolistas(cls):
        return cls.listaFutbolistas
    def setListaFutbolistas(cls,lista):
        cls.listaFutbolistas=lista
    def __str__(self):
        return "Mi nombre es "+self._nombre+" soy profesional en el deporte "+self._deporte+" Tengo "+str(self._edad)+" años de edad y llevo "+str(self._añosPracticando)+" años en el deporte"