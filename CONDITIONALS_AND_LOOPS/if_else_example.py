print("Tell me your age.")
myage = input()   # input()으로 받는다면 str으로 받는 것
myage = eval(myage)

#myage = int(input()) 숫자 입력을 받는 더 간단한 방법임.

if myage < 30 :
    print("Welcome to the Club!")
else:
    print("Oh! No You are not accepted.")