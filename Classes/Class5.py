'''
How would you test if a string is a palindrome?
ignore non-aplhanumeric characters.
'''

def checkPalindrome(s: str):
    
    def isalnumeric(c):
        return (ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z') or ord('0') <= ord(c) <= ord('9'))

    l, r = 0, len(s)-1
    while l<=r:
        if not isalnumeric(s[1]):
            l += 1
        if not isalnumeric(s[r]):
            r -= 1

        if s[l] != s[r]:
            return False
        l += 1
        r -= 1      
    return True

if __name__ == "__main__":
    s = "raceaecar"
    print(checkPalindrome(s))