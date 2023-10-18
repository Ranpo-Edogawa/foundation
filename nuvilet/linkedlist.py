# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None


# class Link_list:
#     def __init__(self) -> None:
#         self.head = None

#     def insert(self, newNode):
#         if self.head is None:
#             self.head = newNode

#         else:
#             last_node = self.head
#             while True:
#                 if last_node.next is None:
#                     break
#                 last_node = last_node.next
#             last_node.next = newNode
    
#     def printList(self):
#         cur_node = self.head
#         while cur_node:
#             print(cur_node.data)
#             cur_node = cur_node.next
            
#     def push(self, new_data):
#         new_node = Node(new_data)        
#         new_node.next = self.head        
#         self.head = new_node

#     def insertAfter(self,prev_node, new_data):
#         if prev_node is None:
#             print("this node does not exist")    
#             return
#         new_node = Node(new_data)
#         new_node.next = prev_node.next
#         prev_node.next = new_node 
        
#     def delete(self, data):
#         cur_node = self.head
        
#         if cur_node and cur_node.data == data:
#             self.head = cur_node.next
#             cur_node = None
#             return
        
#         while cur_node:
#             if cur_node.data == data:
#                 break
#             prev = cur_node
#             cur_node = cur_node.next
            
#         if cur_node is None:
#             return
        
#         prev.next = cur_node.next
#         cur_node = None
         

#     def lens(self):
#         len = 0
#         cur_node = self.head
#         while cur_node:
#             len+=1
#             cur_node = cur_node.next
#         return len
    
    # def appendList(self):
    #     nums = list()
    #     cur_node = self.head
    #     while cur_node:
    #         nums.append(cur_node.data)
    #         cur_node = cur_node.next
    #     return nums


    # def isthispalindrome(self):
    #     nums = self.appendList()
    #     for i in range(len(nums)//2):
    #         if nums[i] != nums[len(nums)-i-1]:
    #             return False
    #     return True
    
# l1 = Node(121)
# l2 = Node(12321)
# l3 = Node(12)
# ll = Link_list()
# ll.insert(l1)
# print(ll.isthispalindrome())
# ll.insert(l3)
# print(ll.isthispalindrome())









class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        head = self.append_linkedlist_to_list(head)
        return head[::-1]
    
    def append_linkedlist_to_list(self, head):
        cur_node = head
        nums = list()
        while cur_node:
            nums.append(cur_node.val)
            cur_node = cur_node.next        
        return nums
        
        
        
        


s = Solution()
print(s.reverseList(ListNode(1,2)))
        








