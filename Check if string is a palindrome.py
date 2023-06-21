def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

print(is_palindrome("radar"))
print(is_palindrome("python"))
