# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:
class Solution:
    def primeSubOperation(self, numbers):
        largest_number = max(numbers)

        # Sieve of Eratosthenes
        prime_sieve = [False] * (largest_number + 1)
        prime_sieve[0] = prime_sieve[1] = True

        for i in range(2, int(largest_number**0.5) + 1):
            if not prime_sieve[i]:
                for j in range(2 * i, largest_number + 1, i):
                    prime_sieve[j] = True

        prime_numbers = [i for i in range(2, len(prime_sieve)) if not prime_sieve[i]]

        index = self.find_max_subtraction(prime_numbers, 0, numbers[0])
        if index != -1:
            numbers[0] -= prime_numbers[index]

        for i in range(1, len(numbers)):
            index = self.find_max_subtraction(prime_numbers, numbers[i - 1], numbers[i])

            if index == -1 and numbers[i] <= numbers[i - 1]:
                return False
            elif index != -1:
                numbers[i] -= prime_numbers[index]

        return True

    def find_max_subtraction(self, primes, previous_value, current_value):
        if not primes:
            return -1

        left_index, right_index = 0, len(primes) - 1

        while left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if current_value - primes[mid_index] <= previous_value:
                right_index = mid_index - 1
            else:
                if mid_index == len(primes) - 1 or current_value - primes[mid_index + 1] <= previous_value:
                    return mid_index
                else:
                    left_index = mid_index + 1

        mid_index = right_index
        return -1 if mid_index >= 0 and current_value - primes[mid_index] <= previous_value else mid_index