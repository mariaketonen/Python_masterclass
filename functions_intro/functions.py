def multiply(x, y):
    """
    Multiplying two given `int` values.
    :param x: First integer
    :param y: Second integer
    :return: Return result of the mathematical calculation
    """
    result = x * y
    return result
# adding two empty lines after the function
# variable result disappears after the function has executed
def is_palindrome(string):
    """
    To check if a `String` word is a palindrome.
    Word comes from user input.
    :param string: Input string
    :return: True or False
    """
    #backwards = string[::-1]
    #return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence):
    """
    To check if a `String` sentence is a palindrome.
    Sentence comes from user input.
    :param sentence: Input String
    :return: True or False
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))


# use the next lines to test the sentences:
word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)

