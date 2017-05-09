def prime_numbers(n):
    prime = True
    for i in range(0,n):
    	if (num%i==0):
    		prime = False
    	if prime:
    		print (num)
