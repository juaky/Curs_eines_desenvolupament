from LluitadorRandom import LluitadorRandom
from IRing import IRing
from Ring import Ring
from contrasenya import Password

lluitador1 = LluitadorRandom("DestrossaCervells")
lluitador2 = LluitadorRandom("MatxacaPilotes")

ring = Ring()

contrasenya = Password.llegeix_password()
ring.EntradaLluitadors(lluitador1, lluitador2)
resultat = ring.Lluiteu()
print(resultat[0], "vs", resultat[1])