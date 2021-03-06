# python2
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
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

    def in_order(self):
        self.result = []
        self._in_order(0)
        return self.result

    def _in_order(self, node):
        if node is -1:
            return
        self._in_order(self.left[node])
        self.result.append(self.key[node])
        self._in_order(self.right[node])

    def pre_order(self):
        self.result = []
        self._pre_order(0)
        return self.result

    def _pre_order(self, node):
        if node is -1:
            return
        self.result.append(self.key[node])
        self._pre_order(self.left[node])
        self._pre_order(self.right[node])

    def post_order(self):
        self.result = []
        self._post_order(0)
        return self.result


    def _post_order(self, node):
        if node is -1:
            return
        self._post_order(self.left[node])
        self._post_order(self.right[node])
        self.result.append(self.key[node])

def main():
    tree = TreeOrders()
    tree.read_tree()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))

threading.Thread(target=main).start()
