class Solution:
    def validPalindrome(self, s: str) -> bool:

        n = len(s)
        i,j = 0,n-1
        
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return is_palindrome(i + 1, j) or is_palindrome(i, j - 1)
        return True