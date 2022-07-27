print("당신이 태어난 년도를 입력하세요.")
birth = int(input())
age = 2022 - birth + 1

message = ""

if 20 <= age and age <= 26:
    message = "대학생"

elif 17 <= age and age < 20:
    message = "고등학생"

elif 14 <= age and age < 17:
    message = "중학생"

elif 8 <= age and age < 14:
    message = "초등학생"

else :
    print("학생이 아닙니다.")

print(message)


""" 처음 작성 버젼. 
if age >= 20 and age <= 26:
    print("대학생")

elif age >= 17 and age < 20:
    print("고등학생")

elif age >= 14 and age < 17:
    print("중학생")

elif age >= 8 and age < 14:
    print("초등학생")

else :
    print("학생이 아닙니다.")

"""