# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
import re
from fractions import Fraction
from math import gcd
class Solution:
	FRACTION_PATTERN = r'([+-]?[^+-]+)'
	
	# First solution
	def fractionAddition(self, expression: str) -> str:
		result_fraction = Fraction(0)

		for exp in re.findall(self.FRACTION_PATTERN, expression):
			n, d = map(int, exp.split('/'))
			result_fraction += Fraction(n, d)

		return f'{result_fraction.numerator}/{result_fraction.denominator}'

	# Second solution
	def fractionAddition(self, expression: str) -> str:
		result_fraction = sum(
			(Fraction(*map(int, exp.split('/'))) for exp in re.findall(self.FRACTION_PATTERN, expression)),
			Fraction(0)
		)
		return f'{result_fraction.numerator}/{result_fraction.denominator}'


# Another way:

def lcm(a, b):
    return a * b // gcd(a, b)

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall('[+-]?\\d+/\\d+', expression)
        current_numerator, current_denomerator = 0, 1

        for frac in fractions:
            numerator, denomerator = map(int, frac.split('/'))

            lcm_denominator = current_denomerator * denomerator // gcd(current_denomerator, denomerator)

            current_numerator = (current_numerator * (lcm_denominator // current_denomerator) +
                                 numerator * (lcm_denominator // denomerator))

            current_denomerator = lcm_denominator

        if current_numerator == 0:
            return '0/1'

        common_divisor = gcd(abs(current_numerator), current_denomerator)
        simplified_numerator = current_numerator // common_divisor
        simplified_denominator = current_denomerator // common_divisor

        return f"{simplified_numerator}/{simplified_denominator}"