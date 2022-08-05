import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


if __name__ == '__main__':
    phrase = input("Enter a word or phrase: ")
    print(fr"{phrase} is palindrome: {is_palindrome(phrase)}")
