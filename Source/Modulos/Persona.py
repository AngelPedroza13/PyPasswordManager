'''Define la clase persona con sus respectivos
atributos y metodos'''
class Persona:
	'''Constructor de la clase'''
	def __init__(self, oid=0, nombres='',apellidos='',fecha_nacimiento=None):
		self.Oid = oid
		self.Nombres = nombres
		self.Apellidos = apellidos
		self.FechaNacimiento = fecha_nacimiento

	'''Oid'''
	@property
	def Oid (self):
		return self.Oid

	@Oid.setter
	def Oid(self, oid):
		self.Oid = oid

	'''Nombres'''
	@property
	def Nombres(self):
		return self._Nombres

	@Nombres.setter
	def Nombres(self, nombres):
		self.Nombres = nombres

	'''Apellidos'''
	@property
	def Apellidos(self):
		return self._Apellidos

	@Apellidos.setter
	def Apellidos(self, apellidos):
		self.Apellidos = apellidos
	
	'''Fecha Nacimiento'''
	@property
	def FechaNacimiento(self):
		return self._FechaNacimiento

	@FechaNacimiento.setter
	def FechaNacimiento(self, fecha_nacimiento):
		self.FechaNacimiento = fecha_nacimiento