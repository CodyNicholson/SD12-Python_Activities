def reverse_string(test_string):
    if len(test_string) == 0 or len(test_string) == 1:
        return test_string
    else:
        return test_string[len(test_string) -1] + reverse_string(test_string[:len(test_string)-1])


test_string="hello"

print(reverse_string(test_string))