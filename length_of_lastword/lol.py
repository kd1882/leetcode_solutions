s_input = "   fly me   to   the moon  "

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp_list = s.split(' ')
        new_list = []
        for i in temp_list:
            if i == '':
                continue
            else:
                new_list.append(i)
                
        print(new_list)
        return len(new_list[-1])
    
test_obj = Solution()

print(test_obj.lengthOfLastWord(s_input))

