"""
Practice with defining functions
lab2.py
Mason Renehan
2/14/2018

"""

def is_even (int):
	"""

	Detirmines if a given number is even or odd.
	n = integer
	Returns: True is n is even, False if not.
	"""

	n = input("Enter a number: ")

	n = int(n)
	
	if n % 2 == 0:
			
			return True
	else:
		
		return False 


if__name__ == '__main__':
	import doctest
	doctest.testmod()
