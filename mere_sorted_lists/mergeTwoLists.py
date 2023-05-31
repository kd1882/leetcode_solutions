# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        for i in list1:
            new_list.append(i)
        for i in list2:
            new_list.append(i)
            
        new_list = new_list.sort()
        return new_list