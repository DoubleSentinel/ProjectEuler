#A palindromic number reads the same both ways. The largest palindrome 
#made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def ispal(n):
	return str(n) == str(n)[::-1]

if __name__ == '__main__':
	largest = 0
	pair = [0,0]
	for i in range(1000,99,-1):
		for j in range(1000,99,-1):
			if ispal(i*j) and largest < i*j:
				largest = i*j
				pair[0], pair[1] = i, j
	print("The palindrome pair is: %i, %i = %i"% (pair[0],pair[1],largest))	