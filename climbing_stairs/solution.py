class Solution:
    def climbStairs(self, n: int) -> int:
        # initial check
        if n <= 2:
            return n

        # cover base cases
        temp_list = [0] * (n + 1)
        print(temp_list)
        temp_list[1] = 1
        temp_list[2] = 2

        for i in range(3, n + 1):
            temp_list[i] = temp_list[i - 1] + temp_list[i - 2]
            print(temp_list[i])

        return temp_list[n]

test_output = Solution()
print(test_output.climbStairs(3)) 