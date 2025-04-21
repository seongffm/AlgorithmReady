#내장함수1
from datetime import datetime
name = input()
age = int(input())
#2019년에 나온문제라 올해가 2019년이여서 -6해줌줌
print(f"{name}(은)는 {datetime.now().year+(100-age)-6}년에 100세가 될 것입니다.")