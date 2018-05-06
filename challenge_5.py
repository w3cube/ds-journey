import sys

'''
prints all of the numbers from 1 to 100. 
For multiples of 3, instead of the number, print "Fizz;" 
for multiples of 5, print "Buzz." 
For numbers that are multiples of both 3 and 5, print "FizzBuzz."
'''

def is_multiple(number, multiple_off):
    if number % multiple_off == 0:
        return True

    return False


def main(argv=None):
    for num in range (1, 101):
        if is_multiple(num, 3 * 5):
            print("FizzBuzz.")
        elif is_multiple(num, 3):
            print ("Fizz;")
        elif is_multiple(num, 5):
            print ("Buzz.")
        else:
            print (num)
         

if __name__ == "__main__":
    sys.exit(main())


