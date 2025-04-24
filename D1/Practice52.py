#자료구조 - 리스트,튜플 1
scores = [(90,80),(85,75),(90,100)]
for i in range(len(scores)):
    print(f"{i+1}번 학생의 총점은 {sum(scores[i])}점이고, 평균은 {sum(scores[i])/len(scores[i]):.1f}입니다.")