class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum_string = ""
        for char in s:
            if char.isalnum():
                alnum_string += char
        reverse_alnum_string = alnum_string[::-1]
        return alnum_string == reverse_alnum_string