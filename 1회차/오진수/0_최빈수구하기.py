import sys

sys.stdin = open("_최빈수구하기.txt")
#10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
#최빈수는 8이 된다.


from collections import Counter

n = int(input())
math = list(map(int,input().split()))

for i in range(101):
    most_fre = Counter(math).most_common()[0][0]
    print("#"+str(n), str(most_fre)) 


#print(math)
#number_ = []
#cnt = 0
#set_math = set(math)
#set(math)
#print(set(math))
