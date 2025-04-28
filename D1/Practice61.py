#자료구조 - 리스트,튜플 3
gogodan=[]
for i in range(2,10):
    lst=[]
    for j in range(1,10):
        if (i*j)%3 !=0 and (i*j)%7 != 0:
            lst.append(i*j)
    gogodan.append(lst)
print(gogodan)
#구구단 단별로 출력
# for idx,line in enumerate(gogodan,start=2):
#     print(idx,line)
