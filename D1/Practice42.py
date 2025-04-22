#흐름과 제어 - 반복 13
n = int(input())
print(bin(n)[2:] if n>=0 else '-'+bin(-n)[2:])
#이진수: bin(), 8진수: oct(), 16진수:hex()