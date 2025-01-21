class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    
    # Swap the left and right children
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)
    
    return root


# # Helper function to build the tree from a list
# def buildTree(nodes, idx=0):
#     if idx >= len(nodes) or nodes[idx] is None:
#         return None
#     root = TreeNode(nodes[idx])
#     root.left = buildTree(nodes, 2 * idx + 1)
#     root.right = buildTree(nodes, 2 * idx + 2)
#     return root


# # Helper function to print the tree in level order (for verification)
# def levelOrderTraversal(root):
#     if not root:
#         return []
#     result = []
#     queue = [root]
#     while queue:
#         node = queue.pop(0)
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
#     return result


# Test case: root = [1, 2, 3, 4, 5, 6, 7]
root = TreeNode([1, 2, 3, 4, 5, 6, 7])

# Invert the tree
inverted_root = invertTree(root)

# Print the level order traversal of the inverted tree
# print(levelOrderTraversal(inverted_root))
print(inverted_root.)

