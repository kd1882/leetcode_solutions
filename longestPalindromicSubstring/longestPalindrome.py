class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        res = ''
        
        def expandPalindrome(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        for i in range(len(s)):
            # we assume that the longest palindrome can be odd
            odd_palindrome = expandPalindrome(i, i)
            if len(odd_palindrome) > len(res):
                res = odd_palindrome
                
            # we assume that the longest palindrome can be even
            even_palindrome = expandPalindrome(i, i + 1)
            if len(even_palindrome) > len(res):
                res = even_palindrome
                
        return res