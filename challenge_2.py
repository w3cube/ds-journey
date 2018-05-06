import sys

'''
Find the sum of all the primes below 2,000

'''

def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False

    return True


def main(argv=None):
    sum_of_all_primes_below_2000 = 0
    for num in range (2, 2000):
        if is_prime(num):
            sum_of_all_primes_below_2000 += num
         
    print (" sum of all the primes below 2,000 is : {0}"
                    .format(sum_of_all_primes_below_2000))

if __name__ == "__main__":
    sys.exit(main())


