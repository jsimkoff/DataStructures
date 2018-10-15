# python2

from math import floor

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self._size = []


  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in raw_input().split()]
    assert n == len(self._data)
    self._size = n


  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print("%d %d" % swap)
    #
    # f = open("04comp", "w+")
    # f.write("%d\n" % len(self._swaps))
    # for swap in self._swaps:
    #     f.write("%d %d\n" % swap)

  def GenerateSwaps(self):

      def leftchild(index):
          return 2*index + 1

      def rightchild(index):
          return 2*index + 2

      def SiftDown(index):
          min = index
          l = leftchild(index)
          r = rightchild(index)
          if (l < self._size) and (self._data[l] < self._data[min]):
              min = l
          if (r < self._size) and (self._data[r] < self._data[min]):
              min = r
          if index != min:
              self._swaps.append((index, min))
              self._data[index], self._data[min] = self._data[min], self._data[index]
              SiftDown(min)

      for i in range(int(floor(self._size/2)) - 1, -1, -1):
          SiftDown(i)


  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
