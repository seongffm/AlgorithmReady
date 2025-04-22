#흐름과 제어 - 반복 7
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
high_scores = []
while scores:
    score = scores.pop()
    if score >= 80:
        high_scores.append(score)
    else:
        continue
print(sum(high_scores))