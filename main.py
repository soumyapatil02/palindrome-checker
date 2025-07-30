def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    word = "madam"
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
