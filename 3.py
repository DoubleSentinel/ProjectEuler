#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import sys
import math

def is_prime(a):
    return all(a % i for i in range(2, a))

def biggestprime(n):
	largest = 0
	max = n
	#this condition is used because using the square root of a number as a relatively good guess 
	#only becomes useful when the natural number becomes really large (5 digits is a good starting point
	if len(str(n)) >= 5:
		max = math.ceil(math.pow(n,0.5))
	#the reason we're looking at the square root of the value is described in the Quadratic Sieve algorithm
	#also, general modular mathematics and Fermat Theorem
	for i in range(2,max):
		if not n%i:
			if is_prime(i):
				largest = i
	return largest
	
if __name__ == '__main__':
	print(biggestprime(int(sys.argv[1])))
	
	