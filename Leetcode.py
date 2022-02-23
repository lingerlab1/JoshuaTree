def myPow(x, n):
	if n == 0: 
		return 1
	lower = myPow(x, n//2)
	if n % 2 == 0: 
		return lower*lower
	if n % 2 == 1: 
		return lower*lower*x

myPow(x = 2.00000, n = 10)

