import sys

'''
Find the sum of all the multiples of 3 or 5 below 1,000
'''

def is_multiple(number, multiple_off):
    if number % multiple_off == 0:
        return True

    return False


def main(argv=None):
    sum_of_all_multiples_of_3_or_5_below_1000 = 0
    for num in range (1, 1000):
        if is_multiple(num, 3) or is_multiple(num, 5):
            sum_of_all_multiples_of_3_or_5_below_1000 += num
         
    print (" sum of all the multiples of 3 or 5 below 1,000 is : {0}"
                    .format(sum_of_all_multiples_of_3_or_5_below_1000))

if __name__ == "__main__":
    sys.exit(main())


