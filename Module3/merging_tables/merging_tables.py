# python2

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

max_lines = max(lines)

def getParent(table):
    # find parent and compress path
    if parent[table] != table:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return lines[realDestination]

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

    # We are not really coping the lines from source to desintation since the one with
    # the higher rank becomes the new parent and collects the increase in lines
    # -- ordering of src/dest are arbitray here, it doesn't matter which ones has the
    # data and which contains the symbolic links

    if rank[realDestination] < rank[realSource]:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        return lines[realSource]
    else:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        if rank[realSource] == rank[realDestination]:
            rank[realDestination] += 1
        return lines[realDestination]


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    lines_m = merge(destination - 1, source - 1)
    max_lines = max(max_lines, lines_m)
    print(max_lines)
