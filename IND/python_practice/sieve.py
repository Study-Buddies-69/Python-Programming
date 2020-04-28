import math
import logging


#Code using List comprehension, Logging Function, Optimized way of finding Prime or Not
#usr_input = int(input("Enter the Number"))
class sieve_operation:

	def input_fn():
		while True:
			usr_input = int(input("Enter the Number"))
			if usr_input >2:
				break
			else:
				print("There is no Sieve of Eratosthenes for 0,1,2")
				continue
		return usr_input


	logging.basicConfig(filename = "Logger.txt",level = logging.DEBUG)
	logger = logging.getLogger()
	logger.info("Program Starts")

	def sieve(usr_input):
		if usr_input == 1:
			return None
		divider = math.floor(math.sqrt(usr_input))
		for div in range(2,divider+1):
			if usr_input % div ==0:
				return None
		return usr_input

inp = sieve_operation.input_fn()
out = [sieve_operation.sieve(a) for a in range(1,inp) if sieve_operation.sieve(a)]
sieve_operation.logger.info(out)
print(out)
sieve_operation.logger.info("Program Completed")
