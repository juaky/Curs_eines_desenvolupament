from random import randrange, choice


class ILluitador:
    def get_nom(self) -> str:
        return self._nom

    def Protegeix(self) -> list:
        llocs = self._copsPossibles.copy()
        llocs.pop(randrange(len(llocs)))
        return llocs

    def Pica(self):
        pica = choice(self._copsPossibles)
        return pica

    def get_Forca(self) -> int:
        return 1