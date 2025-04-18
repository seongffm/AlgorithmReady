#흐름과 제어 - if 4
Man1 = input()
Man2 = input()
if Man1 == Man2:
    print("Result : Draw")
else:
    if Man1 == "가위":
        if Man2 =="보":
            print("Result : Man1 Win!")
        else:
            print("Result : Man2 Win!")
    if Man1 == "바위":
        if Man2 =="가위":
            print("Result : Man1 Win!")
        else:
            print("Result : Man2 Win!")
    if Man1 == "보":
        if Man2 =="바위":
            print("Result : Man1 Win!")
        else:
            print("Result : Man2 Win!")


# #규칙을 딕셔너리로 정의하면 간결해짐->
# Man1 = input()
# Man2 = input()
# # 게임의 승패를 결정하는 규칙을 딕셔너리로 정의
# rules = {
#     ("가위", "보"): "Man1 Win!",
#     ("보", "가위"): "Man2 Win!",
#     ("바위", "가위"): "Man1 Win!",
#     ("가위", "바위"): "Man2 Win!",
#     ("보", "바위"): "Man1 Win!",
#     ("바위", "보"): "Man2 Win!"
# }
# # 만약 두 사람이 같으면 Draw, 아니면 rules 딕셔너리를 통해 승패 결정
# if Man1 == Man2:
#     print("Result : Draw")
# else:
#     딕셔너리 바로 조회가 아닌 get함수 이용하면 잘못된 입력 들어와도 예외처리가능능
#     print(f"Result : {rules.get((Man1, Man2), 'Invalid Input')}")