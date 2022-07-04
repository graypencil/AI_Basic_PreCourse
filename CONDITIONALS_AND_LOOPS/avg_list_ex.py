kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
#print(midterm_score)

# 사람 별 평균 구하기

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:   # 각 학생마다 갭멸로 교과 점수를 저장
        student_score[i] += score # 학생 개별로 index 
        i += 1
        # print(i, subject, student_score) 중간 지표 확인
    i = 0

for value in student_score:
    print("{0}번째 사람의 평균 점수는 {1:.2f}점입니다.".format(i, value / 3))
    i += 1

"""
else: 
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
"""