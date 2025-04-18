#흐름과 제어 - if 3
T = int(input())
for tc in range(1,T+1):
    Alphabet = input()
    if ord("A")<= ord(Alphabet) <=ord("Z"):
        print(f"#{tc} {Alphabet} 는 대문자 입니다.")
    elif ord("a")<= ord(Alphabet) <=ord("z"):
        print(f"#{tc} {Alphabet} 는 소문자 입니다.")
    else:
        print(f"#{tc} {Alphabet} 는 알파벳이 아닙닙니다.")