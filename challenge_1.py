import sys

'''
Find the largest palindrome made from the 
product of two three-digit numbers. 


'''

def is_palindrome(number):
    reverse_number = ""
    for i in number:
        reverse_number = i + reverse_number

    if int(number) == int(reverse_number):
        return True

    return False


def main(argv=None):
    largest_palindrome_product_of_two_three_digit_number = 0
    three_digit_number_1 = 0
    three_digit_number_2 = 0
    found_it = False
    for num_1 in range (1000, 99, -1):
        for num_2 in range (999, num_1, -1):
            product_of_two_nums = num_1 * num_2
            if is_palindrome(str(product_of_two_nums)) and product_of_two_nums >= largest_palindrome_product_of_two_three_digit_number:
                largest_palindrome_product_of_two_three_digit_number = product_of_two_nums
                three_digit_number_1 = num_1
                three_digit_number_2 = num_2
    
    print (" Largest Palindrome Product of two Three digit numbers is : num_1 = {0} * num_2 = {1} = {2}"
                    .format(three_digit_number_1, three_digit_number_2, 
                            largest_palindrome_product_of_two_three_digit_number))

if __name__ == "__main__":
    sys.exit(main())


