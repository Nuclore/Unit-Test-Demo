import unittest # Module for creating unit tests.
from dog import Dog # Class to be tested.

class DogTestCase(unittest.TestCase): # The testing class must inherit from the unittest.TestCase class.
	'''
	This class is used for testing methods in the Dog class, located in dog.py
	By convention, the name of the testing class should be related to what is being tested, with the suffix "TestCase" e.g DogTestCase.
	The methods in this testing class must start with "test_", to allow the tests to be automatically executed when this file is run e.g. test_bark.
	'''
	def setUp(self):
		'''
		The setUp method is the first method to run before any of the test cases.
		In this case, a Dog instance is created with the required attributes.
		'''
		name = 'rover' # Name of dog.
		age = 5 # Age of dog.
		breed = 'german shepherd' # Breed of dog.
		self.rover = Dog(name, age, breed) # Creates a Dog instance with the attributes.

	def test_bark(self):
		'''Test to check if "Woof" is present in the sounds list of the instance.'''
		sound = 'Woof!' # Expected item in the sounds list of the instance.
		self.assertIn(sound, self.rover.sounds) # Checks if "Woof" is present in the sounds list of the instance.

	def test_roll_over(self):
		'''Test to check if the roll_over method returns the expected message.'''
		message = 'Rover rolls over.' # Expected result for the roll_over method.

		# Compares the expected result with the actual result to check if they are equal.
		self.assertEqual(message, self.rover.roll_over())

	def test_info(self):
		'''Test to check if the get_info method returns the expected information.'''
		info = 'Name: Rover, Age: 5, Breed: German Shepherd' # Expected result for the get_info method.

		# Compares the expected result with the actual result to check if they are equal.
		self.assertEqual(info, self.rover.get_info())
		
if __name__ == '__main__':
	unittest.main() # Runs the test cases within the testing class.
	# The output would provide information on which tests passed, failed or produced an error.
	# A passing test would be represented by a dot.
	# A failing test would be represented by an 'F'.
	# A test that produced an error would be represented by an "E".
	# If a test fails, fix the method(s) that caused the test to fail.

	# There are other assert methods besides assertEqual() and assertIn().
	# These include: assertNotEqual() which verifies that the actual result does NOT equal the expected result.
	#                assertTrue(x) which verifies that the actual result is True.
	#                assertFalse(x) which verifies that the actual result is False.
	#                assertNotIn(item, list) which verifies that an item is NOT present in a list.