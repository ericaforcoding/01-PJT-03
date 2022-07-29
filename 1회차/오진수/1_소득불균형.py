import sys

sys.stdin = open("_소득불균형.txt")

# 3
# 7  -->평균 15 -->n = 7
# 15 15 15 15 15 15 15

# 10 -->평균 10.9 -->n = 9
# 1 1 1 1 1 1 1 1 1 100

# 7 -->평균 4.57 -->n = 4
# 2 7 1 8 2 8 4

#map ->list->sort

cnt = list(map(int,input().split()))
cnt.sort()
#print(cnt)
arr = []

for i in cnt:
    arr.append()
    print(arr)