# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

list2 = [1,3,4]
list1 = [1,2,4]

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = []

        for i, a in zip(list1, list2):
            merged_list.append(i)
            merged_list.append(a)

        return merged_list

        # Merged list is always head, so keep it at 0, followed by the head of the merging list.

        # then compare values in order, need to iterate over each value, check if it's bigger or not, then add it?

        # 

ret = Solution().mergeTwoLists(list1, list2)

print(ret)




class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next