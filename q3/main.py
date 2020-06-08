# all imports below
import math

"""
Any extra lines of code (if required)
as helper for this function.
"""

def findDelay(dist):
	'''
	Parameters
	----------
	dist : A `float`

	Returns
	-------
	A `float`
	'''
	M = 5.974e24 	# Mass of Earth
	c = 2.998e8  	# Speed of Light
	r = 6357000  	# Radius of Earth
	G = 6.674e-11	# Gravitational Constant

	num = 1-(2*G*M)/((dist)*(c*c))
	den = 1-(2*G*M)/(r*c*c)

	num = math.sqrt(num)
	den = math.sqrt(den)
	res = num/den
	res = res-1
	# print(res)

	T = dist/c
	ans = res*T
	return ans
