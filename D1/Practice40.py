#흐름과 제어 - 반복 6
datas = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
##문제에서 for문 이용하라고 해서 아래처럼
# count_A,count_O,count_B,count_AB=0,0,0,0
# for data in datas :
#     if data =='A':
#         count_A +=1
#     elif data =='O':
#         count_O +=1
#     elif data =='B':
#         count_B +=1
#     else:
#         count_AB +=1
# ddic = {'A':count_A,'O':count_O,'B':count_B,'AB':count_AB}
# print(ddic)

#1.Counter함수 이용 #2.딕셔너리 이용
#1.
from collections import Counter
dic = dict(Counter(datas))
print(dic)

#2.
ddic = {}
for data in datas:
    #.get() 이용해서 있으면 (그값,  없으면 초기값(0)) + 1
    ddic[data] = ddic.get(data,0) + 1
print(ddic)