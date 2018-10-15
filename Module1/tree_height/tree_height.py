# python2

import sys
import threading
import timeit



ct = 0

class Node(object):
    def __init__(self, index):
        self.index = index
        self.children = []

    def addChild(self, n):
        self.children.append(n)

    def printChildren(self):
        if not self.children:
            print("no children")
        for i in self.children:
            print(i.index)

def compute_tree_height(n, ct):
    ct = ct + 1
    # print(ct)
    if not n:
        return 0
    if n.children == []:
        return 1
    else:
        heights = []
        for i in n.children:
            # print("children: %d\n" % i.index)
            heights.append(compute_tree_height(i, ct))
        return max(heights) + 1


def main():

    # start = timeit.default_timer()
    n = int(raw_input())
    parents = list(map(int, raw_input().split()))
    nodes = []
    for i in range(n):
        nodes.append(Node(i))
    root = []
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].addChild(nodes[child_index])

    height = compute_tree_height(nodes[root], 0)
    print(height)
    # stop = timeit.default_timer()
    # print(stop - start)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
