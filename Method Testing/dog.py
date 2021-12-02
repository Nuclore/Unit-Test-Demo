class Dog:
	'''Class to represent a dog.'''

	def __init__(self, name, age, breed):
		'''Initialze the required  attributes..'''
		self.name = name # Dog name.
		self.age = age # Dog age.
		self.breed = breed # Dog breed.
		self.sounds = ['Bark!', 'Woof!', 'Roof!'] # List to store dog sounds.

	def sit(self):
		'''Returns a statement that the dog sits.'''
		return f'{self.name.title()} sits.'

	def roll_over(self):
		'''Returns a statement that the dog rolls over.'''
		return f'{self.name.title()} rolls over.'

	def get_info(self):
		'''Returns information about the dog.'''
		return f'Name: {self.name.title()}, Age: {self.age}, Breed: {self.breed.title()}'