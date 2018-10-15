
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

    def pre_order(self):
        pass

    def in_order(self):
        pass

    def post_order(self):
        pass


if __name__ == "__main__":
    tree = TreeOrders()
    tree.read()

    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))
