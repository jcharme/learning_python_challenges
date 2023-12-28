"""
This program checks to see if the given words are palindromes,
it ignores capitals, spaces and punctuation
"""

# Function to test if it is a palindrome
import string

def is_palindrome(teststr):
    s = str.lower(teststr)
    s = s.replace(" ", "")
    s = s.translate(str.maketrans('', '', string.punctuation))
    if s == s[::-1]:
        return True
    return False

# This is how your code will be called.
# Your function should return whether a string is a palindrome.
# The code will count the number of correct answers.
total = 0
test_words = ["Hello World!","Radar","Mama?","Madam, I'm Adam.",
    "Race car!"]
for word in test_words:
    if is_palindrome(word):
        print(word)
        total += 1
print(total)
