import unittest # Module for creating unit tests.
from areas import calculate_triangle_area, calculate_square_area # Functions to be tested.

class AreasTestCase(unittest.TestCase): # The testing class must inherit from the unittest.TestCase class.
	'''
	This class is used for testing functions in areas.py
	By convention, the name of the testing class should be related to what is being tested, with the suffix "TestCase" e.g AreasTestCase.
	The methods in this testing class must start with "test_", to allow the tests to be automatically executed when this file is run e.g. test_triangle_area.	
	'''

	def test_triangle_area(self):
		'''Test to check if the calculate_triangle_area function returns the correct result.'''
		area = calculate_triangle_area(5, 4) # Actual result of the function.
		expected_area = 10 # Expected result of function.

		# Compares the expected result with the actual result to check if they are equal.
		self.assertEqual(area, expected_area) 

	def test_square_area(self):
		'''Test to check if the calculate_square_area function returns the correct result.'''
		area = calculate_square_area(5) # Actual result of the function.
		expected_area = 25 # Expected result of function.

		# Compares the expected result with the actual result to check if they are equal.
		self.assertEqual(area, expected_area)

	def test_square_area_default(self):
		'''Test to check if the calculate_square_area function returns the correct result, when no value is passed into the function.'''
		area = calculate_square_area() # Actual result of the function.
		expected_area = 1 # Expected result of the function.

		# Compares the expected result with the actual result to check if they are equal.
		self.assertEqual(area, expected_area)


if __name__ == '__main__':
	unittest.main() # Runs the test cases within the testing class.
	# The output would provide information on which tests passed, failed or produced an error.
	# A passing test would be represented by a dot.
	# A failing test would be represented by an "F".
	# A test that produced an error would be represented by an "E".
	# If a test fails, fix the function(s) that caused the test to fail.

	# There are other assert methods besides assertEqual().
	# These include: assertNotEqual() which verifies that the actual result does NOT equal the expected result.
	#                assertTrue(x) which verifies that the actual result is True.
	#                assertFalse(x) which verifies that the actual result is False.
	#                assertIn(item, list) which verifies that an item is present in a list.
	#                assertNotIn(item, list) which verifies that an item is NOT present in a list.