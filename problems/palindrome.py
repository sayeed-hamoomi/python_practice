def is_palindrome(word:str):
    return word==word[::-1]

palindrome= input("enter the word: ")

print( is_palindrome(palindrome))
