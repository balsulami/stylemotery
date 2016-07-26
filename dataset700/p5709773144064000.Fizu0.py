import sys

def readint():
    return int(sys.stdin.readline())

def readfloatarray():
    return list(map(float, sys.stdin.readline().strip().split()))

def readintarray():
    return list(map(int, sys.stdin.readline().strip().split()))

def readpairs(start=0):
    elems = readintarray()[start:]
    return [elems[i:i+2] for i in range(0, len(elems), 2)]

def readstring():
    return sys.stdin.readline()[:-1]

