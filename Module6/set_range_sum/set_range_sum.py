# python3

from sys import stdin
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
    # print("updating")
    if v == None:
        return
    # update sums on v, and parent pointers on its children
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    # rotate to the right; so the previous right child of v is now the left child
    # of v's parent (which is now v's right child)
    m = v.right
    v.right = parent
    parent.left = m
  else:
    # similarly, rotate v to the left; so now its parent becomes its left child
    # and any left child of v becomes the former parent's right child
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  # if "straight" up either left or right, zig-zig
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  # otherwise zig-zag -- see slides for pictures
  else:
    # Zig-zag
    smallRotation(v)
    smallRotation(v)

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    # as long as grandparent exists, bigRotation is always called
    # -- small rotation gets called once at the end, followed by loop break
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  # return the new root node after splay
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v != None:
    # if still above the key value, and a smaller value is encountered, update
    # next with this tighter upper bound node
    if v.key >= key and (next == None or v.key < next.key):
      next = v
    # last is the pointer to the current node
    last = v
    if v.key == key:
      break
    # binary search tree property still holds for these even if they aren't AVL trees
    if v.key < key:
      v = v.right
    else:
      v = v.left
  # after the loop terminates (either because we found the key and broke, or because
  # v == None so no value found), splay the final visited node
  root = splay(last)
  # if the key is found, result and root will be the same
  # if not, and if there is a bigger value in the tree, they may or may not be the
  # same
  # if no such value exists, next is None and root is just the last visited node
  return (next, root)






def split(root, key):
  (result, root) = find(root, key)
  # if find returned result = None, there are no nodes in the tree with keys above
  # the given key, so just return the root node for the single tree and do no
  # updates
  if result == None:
    return (root, None)

  # otherwise, splay the next bigger node and set right new tree node to that node
  right = splay(result)
  # left is a temp var for the child to the left of the splayed node
  left = right.left
  # then set right.left = None to split the trees effectively
  right.left = None
  # and ensure that left is now root node for its own tree too
  if left != None:
    left.parent = None
  # update the values on these two nodes
  update(left)

  update(right)
  # return pointers to the root nodes for two new trees
  return (left, right)


def merge(left, right):


    # if either of the nodes don't exist, just return the one that does
    if left == None:
        return right
    if right == None:
        return left


    while right.left != None:
        right = right.left
  # splay the leftmost node on the "right" tree being merged -- so, the smallest
  # value on the bigger tree is now root
    right = splay(right)
    # the right side of the right tree is still good, need to set its left side to
    # be the left tree
    right.left = left
    # update the whole tree (this will take care of sum and settings its chidlrens
    # parent pointers) and return
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None

def pre_order():
    # print pre-order tree traversal for debugging
    def _pre_order(r):
        if r is None:
            return
        key_result.append(r.key)
        sum_result.append(r.sum)
        _pre_order(r.left)
        _pre_order(r.right)
        return

    global root
    key_result = []
    sum_result = []
    _pre_order(root)
    return key_result, sum_result



def insert(x):
  # print("inserting value: %f" % x)
  global root
  # split the tree starting at root for value x
  (left, right) = split(root, x)
  new_vertex = None
  # if x is bigger than the whole tree, or if the right tree doesn't happen to have
  # key=x, need to create a new vertex with key (and current sum) of x
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  # then merge left with the new_vertex if it was created, then merge again with right
  # -- NOTE, this means that if right.key == x aobve, you just merge the two trees
  # without creating a new vertex
  root = merge(merge(left, new_vertex), right)

def erase(x):
  # print("***ERASING***: %f" % x)
  global root
  this, root = find(root, x)

  if (this is None) or (this.key != x):
      # print("condition 0")
      return
  next, root = find(root, x+1)
  if next is None:
      splay(this)
      if this.left is None:
          # if node with key x was only node in the tree
          # print("condition 1")
          root = None
          return
      # if x was largest key in the tree

      # print("condition 2")
      newroot = this.left
      # print(newroot.key)
      newroot.parent = None
      root = splay(newroot)
      # root.right = None
      return
  else:
      # print("condition 3")
      splay(next)
      splay(this)
      next.parent = None
      if this.left is not None:
          next.left = this.left
          this.left.parent = next
      root = next
      return

def search(x):
  # print("searching for %f" % x)
  global root
  (result, root) = find(root, x)
  if (result is not None) and (result.key == x):
      return True
  else:
      return False

  return

def sum(fr, to):
  # print("sum from %f to %f" % (fr, to))
  global root
  (left, middle) = split(root, fr)


  if middle is None:
      # print("all values are smaller than fr")
      root = merge(left, middle)
      return 0
  (middle, right) = split(middle, to + 1)


  if middle is None:
      # print("all values are smaller than to")
      root = (merge(left, right))
      return 0

  # print("there is a sum value")
  ans = middle.sum
  root = merge(left, merge(middle, right))
  return ans

# if __name__ == "__main__":
def main():
    # f = open('out.log', 'w+')

    MODULO = 1000000001
    n = int(stdin.readline())
    last_sum_result = 0

    for i in range(n):
      # print(i)
      line = stdin.readline().split()
      if line[0] == '+':
        x = int(line[1])

        insert((x + last_sum_result) % MODULO)
        # keys, sums = pre_order()
        # print(keys)
        # print(sums)

      elif line[0] == '-':
        x = int(line[1])
        erase((x + last_sum_result) % MODULO)
        # keys, sums = pre_order()
        # print("keys after erase:")
        # print(keys)
        # print(sums)
      elif line[0] == '?':
        x = int(line[1])
        print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        # f.write('Found \t %d \n' % op_ct if search((x + last_sum_result) % MODULO) else 'Not found \t %d \n' % op_ct)


        # keys, sums = pre_order()
        # print(keys)
        # print(sums)
      elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        # f.write('%d \t %d \n' % (res, op_ct))

        last_sum_result = res % MODULO
        # keys, sums = pre_order()
        # print(keys)
        # if root is not None:
        #     print("root plus left / right after sum")
        #     print(root.key)
        #     print(root.left)
        #     print(root.right)
        # print(sums)
      # print(keys)

    # f.close()
threading.Thread(target=main).start()
