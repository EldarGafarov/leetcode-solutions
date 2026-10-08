class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for character in s:
            if character.isalnum():
                new_s+=character
        new_s=new_s.lower()
        for i in range(len(new_s)):
            if new_s[i]!=new_s[len(new_s)-i-1]:
                return False
        return True