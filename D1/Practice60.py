# #함수의 기초 9
# words = input()
# word_lst = words.split(', ')
# result=''
# for i in word_lst:
#     if len(result)<len(i):
#         result=i
# print(result)

#함수로 변환
def longer_string(s1,s2):
    if len(s1)>len(s2):
        return s1
    else:
        return s2
words = input()
word_lst = words.split(', ')
if len(word_lst) == 2:
    print(longer_string(word_lst[0], word_lst[1]))