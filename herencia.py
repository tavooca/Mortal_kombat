class Humano:
	def __init__(self,edad):
		self.edad = edad

	def hablar(self,mensaje):
		print mensaje


class IngSistemas(Humano):
	def __init__(self):
		print 'Hola'

	def programar(self,lenguaje):
		print 'voy a Programar en ', lenguaje
	
class LicDerecho(Humano):
	def estudiaCaso(self, de):
		print 'Debo estudiar el caso de ', de

pedro = IngSistemas()
raul = LicDerecho(27)



pedro.programar('Python')

raul.estudiaCaso('Pedro')

pedro.hablar('Hola')
raul.hablar('Hola, Pedro')

