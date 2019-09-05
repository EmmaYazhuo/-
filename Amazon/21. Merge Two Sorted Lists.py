# # https://www.1point3acres.com/bbs/thread-547015-1-1.html
# # https://www.1point3acres.com/bbs/thread-547029-1-1.html
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
# Close Two Sum
# findOptimalWeights,但大致是這樣:
#
# /* 一個已經預設好的class */
#
# class Container {
#     public double first;
#     public double second;
# }
# 現在給某個容量(double capacity), 還有一個array(double[] weights), 和int numOfContainers
#
# 主要是要在array中選出兩個weights總和小於等於capacity但最接近capacity 然後指定到一個Container object並且return
#
# first和second的順序並不影響，numOfContainer在java裡好像也是沒有用的,因為double[]本身就自帶length資訊
#
# public Container findOptimalWeights(double capacity, double[] weights, int numOfContainers)
#
# 最後用了最簡單的方法兩個 for loop找總和最接近capacity的pair
# 總共8個test cases直接就過了
#
#  public static void findOptimalWeights(double capacity, double[] weights, int numOfContainers){
#         double min = 0.0;
#         int minPos = 0;
#         int maxPos = weights.length - 1;
#         int i =0 , j =weights.length-1;
#
#         Arrays.sort(weights);
#
#         while(i < j){
#             double sum = weights[i] + weights[j];
#
#             if(sum > min && sum <= capacity){
#                 min = sum;
#                 minPos = i;
#                 maxPos = j;
#             }
#
#             if(sum > capacity){
#                 j--;
#             }else {
#                 i++;
#             }
#         }
#
#         System.out.println("The two numbers for which sum is closest to target are "
#                 + weights[minPos] + " and " + weights[maxPos]);
#     }
