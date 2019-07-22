from Nguyen_Thai_StackClass import Stack


def main():
    str_input = get_input()
    palindrome_conversion(str_input)


def get_input():
    user_input = input('Enter a word, expression or number to see if it is a palindrome: ')
    return user_input


def palindrome_conversion(string):
    pal_stack = Stack()

    user_string1 = string.replace(' ', '')
    user_string2 = user_string1.replace("'", '')

    for i in string:
        pal_stack.push(i)

    stack_string = ''
    for index in range(pal_stack.size()):
        stack_string += pal_stack.top_stack()
        pal_stack.pop()

    string1 = stack_string.replace(' ', '')
    string2 = string1.replace("'", '')

    if user_string2.lower() == string2.lower():
        print('User Data:', string)
        print('Palindrome:', stack_string)
        print('Congratulations, it is a palindrome!')
    else:
        print('User Data:', string)
        print('Palindrome:', stack_string)
        print('Sorry, it is not a palindrome!')


main()
