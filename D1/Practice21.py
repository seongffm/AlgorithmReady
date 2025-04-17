#연산자1
inch = int(input())
print(f"{inch}.00 inch => {inch*2.54} cm")

#문자열로 .00받지 말고 입력을 실수로 받아서 2번째 자리수까지 출력되게게
inch = float(input())
cm = inch * 2.54
print(f"{inch:.2f} inch =>  {cm:.2f} cm")