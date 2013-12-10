
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
import time
import string

# This is a simple meathod which uses normal process of modulus to calculate the answer.
def meathod1():
	i = 0
	counter = 0
	start_time = time.time()
	while (i<10000000):
		if (i%3==0 or i%5==0):
			counter += i
		i+=1
	timeTaken = time.time() - start_time, "seconds"
	print 'Time consumed by modulus meathod : {0}'.format(time.time() - start_time, "seconds")
	print 'Answer is : %d' %counter






def meathod2():
	start_time = time.time()
	counter = sum_of_number_divisible_by(3)+ sum_of_number_divisible_by(5) - sum_of_number_divisible_by(15)
	timeTaken = time.time() - start_time, "seconds"
	print 'Time consumed by modulus meathod : {0}'.format(time.time() - start_time, "seconds")
	print 'Answer is : %d' %counter

def sum_of_number_divisible_by(n):
	p = 1000000000/n
	return (n*(p*(p+1))) / 2


def main():
	#meathod1()
	meathod2()
if  __name__ =='__main__':main()