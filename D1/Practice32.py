#함수의 기초 1
word = input()
print(word)
if word == word[::-1]:
    print("입력하신 단어는 회문(Palindrome)입니다.")
else:
    print("입력하신 단어는 회문(Palindrome)이 아닙니다.")