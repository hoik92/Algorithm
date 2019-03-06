# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
def preorder(t):
    if t:
        print(t, end=' ')
        preorder(m[t][0])
        preorder(m[t][1])

V = int(input())
m = [[0] * 2 for _ in range(V + 1)]

M = list(map(int, input().split()))
for i in range(len(M) // 2):
    if not m[M[2 * i]][0]:
        m[M[2 * i]][0] = M[2 * i + 1]
    else:
        m[M[2 * i]][1] = M[2 * i + 1]

preorder(1)

# class Node:
#     def __init__(self, item, left=None, right=None):
#         self.item = item
#         self.left = left
#         self.right = right
#
# class LinkedBinaryTree:
#     def __init__(self):
#         self.head = Node(1)
#
#     def add(self, par, chi):
#         new = Node(chi)
#         if par.left == None:
#             par.left = new
#         else:
#             par.right = new
#
#     def preorder(self, t):
#         if t:
#             print(t.item, end=' ')
#             preorder(t.left)
#             preorder(t.right)
#
# tree = LinkedBinaryTree()
# for i in range(len(M) // 2):
#     tree.add(M[2 * i], M[2 * i + 1])