import sys

sys.stdin = open("_직사각형길이찾기.txt")

#각 a = 4, b = 3, c = 4의 입력과 a = 5, b = 5, c = 5의 입력을 받았을 때 직사각형의 모습이다.
#빨간 숫자로 표시된 나머지 변의 길이를 출력하면 된다.



word = list(map(int,input().split())) #map 함수-<list로 만듦
#print(word)
word.sort() #정렬

for i in range(len(word)): #word안에서 for문을 돌려서, i가 word에 없으면 동일한 i를 출력. 
    if i[0] not in word:   #'int' object is not subscriptable 오류가 뜨는데 해결을 못했습니다.
        print(i[0])
    elif i[0] in word: # 동일한 숫자가 word에 3개가 있다면, 정사각형이 되어야하므로 i[0] =i[1]=i[2]
        print(i[2])
