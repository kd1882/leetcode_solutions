class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest_string = min(strs, key=len)

        common_prefix = ""

        # Iterate through the characters of the shortest string
        for i in range(len(shortest_string)):
            current_char = shortest_string[i]

        # Check if the current character is common across all strings
            if all(string[i] == current_char for string in strs):
                common_prefix += current_char
            else:
                break

        return common_prefix