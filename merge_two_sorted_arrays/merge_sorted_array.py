class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2, p = m-1, n-1, m+n-1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # If there are still elements left in nums2, copy them into nums1
        # No need to do this for nums1, as those elements are already in place
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]


# nums1 = [1, 2, 3, 0, 0, 0]
# nums2 = [2, 5, 6]
# n = len(nums2)
# m = n + len(nums1)


# def merge(nums1, nums2, m, n):


#     compare_val = 0
#     for i in nums2:
#         while i is > nums1[compare_val]:
#             compare_val += 1



