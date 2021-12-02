import math

def calculate_triangle_area(base=1, height=1):
	'''Calculates the area of a triangle and return the result.'''
	area = (base * height) / 2 
	return area

def calculate_circle_area(radius=1):
	'''Calculates the area of a circle and return the result.'''
	area = math.pi * (radius ** 2)
	return area

def calculate_square_area(side=1):
	'''Calculates the area of a square and return the result.'''
	area = side ** 2
	return area

def calculate_rectangle_area(width=1, height=1):
	'''Calculates the area of a rectangle and return the result.'''
	area = width * height
	return area