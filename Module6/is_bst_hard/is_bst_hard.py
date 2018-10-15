#!/usr/bin/python2

# python2

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:

    def read_tree(self):
        self.n = int(raw_input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, raw_input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def is_BST(self):
        self.is_bst = True
        if self.n is 0:
            return
        min = -2**31
        max = +2**31
        self.check_node(0, min, max)


    def check_node(self, node, min, max):
        # print("check_node called")
        # print(self.key[node])
        if (node is -1) or (self.is_bst is False):
            return

        cmin = min
        cmax = max

        if ((self.key[node] >= cmax) or (self.key[node] < cmin)):
            self.is_bst = False

        if self.is_bst is True:
            self.check_node(self.left[node], cmin, self.key[node])
            self.check_node(self.right[node], self.key[node], cmax)

        # Q: why can't I just say else: instead of the last logical condition above?
        # A: it's not a local problem with the condition but rather that the recursive
        # calls continue unless explicitly checked ... try a while loop?

        # ^^ a while loop doesn't seem to work... is there any way to break the
        # recursion in order to be more efficient in a case where the condition
        # is failed deep in the tree while the recursive stack is is very deep

def main():
    tree = Tree()
    tree.read_tree()
    tree.is_BST()
    if tree.is_bst is True:
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
