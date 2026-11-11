# Tree Data Structure – Quick Revision Notes
# 1. What is a Tree?
# A Tree is a non-linear, hierarchical data structure consisting of nodes connected by edges.
# - Root: Topmost node.
# - Parent: Node having child nodes.
# - Child: Node directly connected below a parent.
# - Leaf: Node with no children.
# - Sibling: Nodes sharing the same parent.
# - Ancestor: Any node above a given node.
# - Descendant: Any node below a given node.
# - Subtree: A tree formed from a node and its descendants.
# - Edge: Connection between two nodes.
# - Height: Longest path from a node to a leaf.
# - Depth: Number of edges from root to a node.
# - Level: Usually depth + 1 (root at level 1).
# 2. Types of Trees
# General Tree
# A node can have any number of children.

# Binary Tree
# Each node can have at most two children: left and right.

# Binary Search Tree (BST)
# Left subtree values are smaller; right subtree values are greater than the node (assuming unique keys).

# AVL Tree
# Self-balancing BST. Balance factor must be -1, 0, or +1.

# Heap
# Complete binary tree. Min-heap: parent ≤ children. Max-heap: parent ≥ children.

# Trie
# Stores strings character by character. Useful for autocomplete and prefix searching.


# 3. Binary Tree Types
# - Full: Every node has either 0 or 2 children.
# - Complete: All levels are full except possibly the last, which fills left to right.
# - Perfect: All internal nodes have 2 children and all leaves are at the same level.
# - Balanced: Left and right subtree heights remain within a defined balance constraint.
# - Skewed: Every node has only one child (like a linked list).
# 4. Tree Traversals
# Consider this tree:
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6


# Traversal	Order	Output
# Preorder	Root → Left → Right	1,2,4,5,3,6
# Inorder	Left → Root → Right	4,2,5,1,3,6
# Postorder	Left → Right → Root	4,5,2,6,3,1
# Level Order	Level by level	1,2,3,4,5,6

# Remember:
# - DFS: Preorder, Inorder, Postorder.
# - BFS: Level Order (uses a Queue).
# - DFS commonly uses recursion or a Stack.
# 5. Important Binary Tree Operations
# Operation	Average / Typical	Worst case
# Search (BST)	O(log n)	O(n)
# Insert (BST)	O(log n)	O(n)
# Delete (BST)	O(log n)	O(n)
# Traversal	O(n)	O(n)
# Height calculation	O(n)	O(n)

# For a balanced BST, search, insertion and deletion are O(log n).
# 6. Important BST Concepts

# Searching
# 1. Compare target with current node.
# 2. If equal, return node.
# 3. If smaller, move left.
# 4. If greater, move right.

# Deletion – Three cases:
# 1. Leaf node: Simply remove it.
# 2. One child: Replace node with its child.
# 3. Two children: Replace with inorder successor (smallest in right subtree) or inorder predecessor (largest in left subtree).
# 7. Important Formulas

# For a binary tree:
# - Maximum nodes at level \(L\) (root at level 1): \(2^{L-1}\)
# - Maximum nodes in height \(h\) (height measured in edges): \(2^{h+1}-1\)
# - Minimum height for \(n\) nodes: approximately \(\lceil\log_2(n+1)\rceil-1\) edges.
# - Number of edges in a tree with \(n\) nodes: \(n-1\).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(1)
root.left=TreeNode(2)
root.left.right=TreeNode(3)
root.right=TreeNode(4)
root.right.left=TreeNode(5)

# here the function asks for a list which is the inorder traversal of the tree, we initialize a list if it is not defined and if it is then we append to the list, in the end we return the list
def inorderTraversal(root=TreeNode | None,l=None)->list[int]:
  if root is None: # even for an empty list we no root we have to return empty array
    return []
  if l is None: # initialize l if not passed
    l=[]
  inorderTraversal(root.left,l)
  l.append(root.val)
  inorderTraversal(root.right,l)
  return l

def preorderTraversal(self, root: TreeNode | None, l=None) -> list[int]:
    if l is None:
        l=[]
    if root is None:
        return []
    l.append(root.val)
    self.preorderTraversal(root.left,l)
    self.preorderTraversal(root.right,l)
    return l

def postorderTraversal(self, root: TreeNode | None, l=None) -> list[int]:
    if l is None:
        l=[]
    if root is None:
        return []
    self.postorderTraversal(root.left,l)
    self.postorderTraversal(root.right,l)
    l.append(root.val)
    return l
