

def is_palindrome(word):
    if len(word) <  2:
        return True
    elif word[0] != word[len(word)-1]:
        return False
    return is_palindrome(word[1:len(word)-1])
print(is_palindrome('fadedaf'))