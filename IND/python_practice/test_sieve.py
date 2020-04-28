import math
import unittest
from sieve import *


class test_sieve(unittest.TestCase):

	def test_sieve_none():
		x = sieve_operation.sieve(1)
		y = None
		self.assertTrue(x,y)

	def test_sieve_prime():
		x = sieve_operation.sieve(6)
		y = [2, 3, 5]
		self.assertTrue(x,y)


