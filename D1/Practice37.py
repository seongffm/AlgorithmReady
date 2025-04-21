#함수의 기초2
# user1 = input()
# user2 = input()
# use1 = input()
# use2 = input()
# rules = {('가위','바위'):'바위가 이겼습니다!', ('바위','보'): '보가 이겼습니다!',
#          ('보','가위'):'가위가 이겼습니다!',
#          ('가위','보'):'가위가 이겼습니다!', ('바위','가위'): '바위가 이겼습니다!',
#          ('보','바위'):'보가 이겼습니다!'}
# print(rules[(use1,use2)])
#이렇게 규칙을 다 명명하지말고 조건문 써서 효율적으로 출력
user1 = input()
user2 = input()
use1 = input()
use2 = input()
rules = {('가위','바위'):'바위가 이겼습니다!', ('바위','보'): '보가 이겼습니다!',
         ('보','가위'):'가위가 이겼습니다!'}
if (use1,use2) in rules:
    print(rules[use1,use2])
elif (use2,use1) in rules:
    print(rules[use2,use1])
elif use1 == use2 :
    print('비겼습니다!')
else:
    print('잘못 입력했습니다.')