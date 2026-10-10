class Solution:
    def isPalindrome(self, x: int) -> bool:
        Number = str(x)
        for i in range(len(Number)):
            if Number[i]!=Number[len(Number)-i-1]:
                return False
        return True