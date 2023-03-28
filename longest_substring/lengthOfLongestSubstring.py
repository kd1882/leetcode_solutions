def lengthOfLongestSubstring(s: str) -> int:
    """
    :type s: str
    :rtype: int
    """
    str_dict = {}
    max_len = start = 0
    # i being index, char being value
    for i, char in enumerate(s):
        if char in str_dict and str_dict[char] >= start:
            start = str_dict[char] + 1
        max_len = max(max_len, i - start + 1)
        str_dict[char] = i

    return max_len