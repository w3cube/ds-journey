import sys

'''
Implement run-length encoding.
For example, the string "aabcccccaaa" would become a2b1c5a3. 
If the “compressed” string would not become smaller than the original string, 
your method should return the original string
'''

def run_length_encoding(content):
    encoded_content = ''

    previous_character = content[0]
    character_count = 1
    for c in content[1:]:
        if previous_character == c:
            character_count += 1
        else:
            encoded_content = encoded_content + previous_character + str(character_count)
            previous_character = c
            character_count = 1

    encoded_content = encoded_content + previous_character + str(character_count)

    if len(encoded_content) < len(content):
        return encoded_content
    
    return content


def main(argv=None):
    print (" string to be encoded using run-length encoding.", sys.argv[1])
    print (" encoded string function return value ", run_length_encoding(sys.argv[1]))
    
if __name__ == "__main__":
    sys.exit(main())


