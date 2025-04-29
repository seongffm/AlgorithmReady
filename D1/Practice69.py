#자료구조 - 리스트,튜플2
# sentence ='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
# mo = 'aeiou'
# result=''

# for i in sentence:
#     flag = True
#     for j in mo:
#         if i==j:
#             flag =False
#     if flag:
#         result+=i
# print(result)

#리스트 내포기능 이용 코드 =>?
sentence ='Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
mo = 'aeiou'
result = ''.join([ch for ch in sentence if ch not in mo])
print(result)