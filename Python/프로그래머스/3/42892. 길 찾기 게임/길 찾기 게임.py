import sys

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.l = None
        self.r = None

def insert_node(parent, child):
    if child.x < parent.x:
        if parent.l is None:
            parent.l = child
        else:
            insert_node(parent.l, child)
    else:
        if parent.r is None:
            parent.r = child
        else:
            insert_node(parent.r, child)

def preorder(node, res):
    if node is not None:
        res.append(node.id)
        preorder(node.l, res)
        preorder(node.r, res)

def postorder(node, res):
    if node is not None:
        postorder(node.l, res)
        postorder(node.r, res)
        res.append(node.id)

def solution(nodeinfo):
    node_list = [Node(i+1, x,y) for i, (x,y) in enumerate(nodeinfo)]

    node_list.sort(key=lambda node: (-node.y, node.x))

    root = node_list[0]

    for i in range(1, len(node_list)):
        insert_node(root, node_list[i])

    preorder_res = []
    postorder_res = []

    preorder(root, preorder_res)
    postorder(root, postorder_res)

    return [preorder_res, postorder_res]