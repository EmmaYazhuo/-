# Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
'"""
class Solution:
    avg, node = 0, None
    def findSubtree2(self, root):
        if root is None:
            return 0
        self.findSubtree(root)
        return self.node

    def findSubtree(self, root):
        if root is None:
            return (0, 0)
        leftsum, leftcount = self.findSubtree(root.left)
        rightsum, rightcount = self.findSubtree(root.right)

        sumRoot = leftsum + rightsum + root.val
        sumCount = leftcount + rightcount + 1
        average = sumRoot/sumCount
        if self.node is None or average>self.avg:
            self.avg = average
            self.node = root
        return (leftsum+rightsum), (leftcount+rightcount)

        # self.res = 0
        # def helper(root):
        #     if not root: return [0, 0.0]
        #     n1, s1 = helper(root.left)
        #     n2, s2 = helper(root.right)
        #     n = n1 + n2 + 1
        #     s = s1 + s2 + root.val
        #     self.res = max(self.res, s / n)
        #     return [n, s]
        # helper(root)
        # return self.res