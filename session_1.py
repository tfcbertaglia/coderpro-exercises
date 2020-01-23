"""Validate Binary Search Tree: given a binary tree, determine if it is a valid BST."""
from typing import List


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def insert(root: TreeNode, node: TreeNode):
    if not root:
        root = node
    else:
        if root.value < node.value:
            if not root.right:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)


def insert_list(nodes: List) -> TreeNode:
    root = TreeNode(nodes[0])
    for t in nodes[1:]:
        insert(root, TreeNode(t))
    return root


def is_bst(root: TreeNode) -> bool:
    def helper(node, lower, upper):
        if not node:
            return True
        if node.value <= lower or node.value >= upper:
            return False
        if not helper(node.right, node.value, upper):
            return False
        if not helper(node.left, lower, node.value):
            return False
        return True

    return helper(root, float("-inf"), float("inf"))
