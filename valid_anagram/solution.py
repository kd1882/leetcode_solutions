class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check base case
        if len(s) != len(t):
            return False
        
        # Create a frequency hashmap to count occurences of chars
        frequency = {}
        for letter in s:
            frequency[letter] = frequency.get(letter, 0) + 1
        
        # Decrement the count of characters for each character in t
        for letter in t:
            if letter not in frequency or frequency[letter] == 0:
                return False
            frequency[letter] -= 1
        
        # If all chars in t are used then it's an anagram
        return True

# Test cases
test_output = Solution()
print(test_output.isAnagram("anagram", "nagaram"))  # Output: True
print(test_output.isAnagram("rat", "car"))         # Output: False
