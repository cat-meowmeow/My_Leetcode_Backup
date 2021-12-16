# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:return False  # root 这里表示父节点
        if not root.left and not root.right:  # 父节点的左右子节点不存在时
            return targetSum == root.val    #进行比较
        targetSum -= root.val  # 目标值减节点值，从上而下
        left_ = self.hasPathSum(root.left,targetSum) # 左子节点 调用自身递归
        right_ =self.hasPathSum(root.right,targetSum)
        return left_ or right_  # 父节点左右子节点 有一个满足为真即可
