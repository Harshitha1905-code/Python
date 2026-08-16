#Sum of Prime Factors .Find the sum of the prime factors of a number.
n=int(input())#12
sum_of_prime_factors = 0#create a variable to store the sum of prime factors
i = 2#initialize the divisor to 2, the smallest prime number
while i * i <= n:#check if the divisor is less than or equal to the square root of n and checks factor upto n
    if n % i == 0:#% gives remainder, if remainder is 0 then it is a factor
        sum_of_prime_factors += i #add the prime factor to the sum
        while n % i == 0:#check if the number is divisible by the prime factor
            n //= i#divide the number by the prime factor
    i += 1#increment the divisor to check for the next prime factor
if n > 1:#if the number is greater than 1, it means it is a prime factor itself
    sum_of_prime_factors += n
print(sum_of_prime_factors)