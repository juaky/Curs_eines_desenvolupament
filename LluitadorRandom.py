from random import seed
from random import randrange, choice
from llocOnPicar import LlocOnPicar
from ILluitador import ILluitador


class LluitadorRandom(ILluitador):

    def __init__(self, nom):
        self._nom = nom
        self._copsPossibles = [ n for n in list(LlocOnPicar) if n != LlocOnPicar.ILEGAL ]

    def get_nom(self) -> str:
        """retorna el nom del lluitador."""
        return self._nom

    def Protegeix(self) -> list:
        """Llista de llocs on es protegeix"""
        llocs = self._copsPossibles.copy()
        llocs.pop(randrange(len(llocs)))
        return llocs

    def Pica(self):
        """Determina on pica el lluitador"""
        pica = choice(self._copsPossibles)
        return pica

    def get_Forca(self) -> int:
        """Determina la força del cop"""
        return 1
