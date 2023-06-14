# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
list1 = [3, 2, 2, 3]
list2= [0, 1, 2, 2, 3, 0, 4, 2]

def removeElement(self, nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i


