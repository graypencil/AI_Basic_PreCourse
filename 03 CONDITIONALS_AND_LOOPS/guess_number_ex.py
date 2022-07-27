import random

true_value = random.randint(1, 100)

print("숫자를 맞춰보세요. (1~100)")
input_value = 9999999 # 선언이 안 되어 있으므로 임의의 수를 넣음

while true_value != input_value:
    input_value = int(input())
        
    if input_value > true_value :
        print("숫자가 너무 큽니다.")
    elif input_value < true_value :
        print("숫자가 너무 작습니다.")
    else : 
        break
        
print(f"정답입니다. 입력한 숫자는 {true_value} 입니다.")


"""" 내가 먼저 짠 코드 (임의의 수를 입력을 받을 수 없음.)

print("숫자를 맞춰보세요. (1~100)")
right_num = 48
i = 1  # loop을 위한 변수

while i > 0: 
    num = int(input())
    
    if num > right_num :
        print("숫자가 너무 큽니다.")
        i = 1
        
    elif num < right_num :
        print("숫자가 너무 작습니다.")
        i = 1

    else : 
        i = 0   
        print(f"정답입니다. 입력한 숫자는 {right_num} 입니다.")

"""