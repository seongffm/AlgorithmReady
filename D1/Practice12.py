#알파벳을 숫자로 변환
#알파벳 숫자 -> 유니코드를 활용한 문자열-숫자 변환
#ord(), chr()
sentence=input()
for alphabet in sentence:
    print(ord(alphabet)-65+1,end=" ")
print()