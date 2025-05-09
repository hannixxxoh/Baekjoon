import sys

input = sys.stdin.readline

class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = root

N = int(input().rstrip())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaList = [Node(alphabet[i]) for i in range(N)]

tree = BinaryTree(alphaList[0])

for _ in range(N):
    mid, left, right = input().rstrip().split()
    NodeMid = alphaList[alphabet.find(mid)]
    if left != '.':
        NodeMid.left = alphaList[alphabet.find(left)]
    if right != '.':
        NodeMid.right = alphaList[alphabet.find(right)]

def preorder(node):
    print(node.item, end='')
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

def inorder(node):
    if node.left:
        inorder(node.left)
    print(node.item, end='')
    if node.right:
        inorder(node.right)

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.item, end='')

preorder(tree.root)
print()
inorder(tree.root)
print()
postorder(tree.root)