turno=1
class Rain:
	vida=100
	ataque=60
	msn="Rain ha Ganado"
	pass

class Scorpion:
	vida=100
	ataque=40
	msn="Scorpion ha Ganado"
	pass

while Rain.vida>0 and Scorpion.vida>0:
	if turno == 1:
		Scorpion.vida = Scorpion.vida - Rain.ataque
		turno = 2
		print ("Scorpion ahora tiene menos vida")
		print Scorpion.vida
	else:
		Rain.vida = Rain.vida - Scorpion.ataque
		turno = 1
		print ("Rain ahora tiene menos vida")
		print Rain.vida

if Rain.vida >= 0 :
	print Rain.msn
else:
	print Scorpion.msn
