j = 1

while j > 0: # 좀더 좋은 코드로는 j is not 0
    print("구구단 몇 단을 계산할까요(1~9)? ")
    num = int(input())
    
    if 0 < num and num < 10 :
        print(f"구구단 {num}단을 계산합니다.")
        i = 1    
        while i < 10 :
            num_gugu = num * i
            print(f"{num} X {i} = {num_gugu}") 
            i += 1
        #for 문을 사용하고 문자열 덧셈 방식도 좋은 아이디어인 듯
        #for i in range(1, 10):
        #   print (str(num) + "X" + str(i) + "=" + str(num_gugu))
        j += 1
    elif 10 <= num or num < 0 :
        print("범위 밖의 숫자를 입력하셨습니다.")
        j += 1
    else :
        j = 0
        break
 
print("구구단 게임을 종료합니다")

""" # 강사님의 예시코드

while True: # 무한 loop로 될 수 있으므로 좋은 코드는 아니다!
    print("구구단 몇 단을 계산할까요?(1~9) ")
    dan = int(input())
    if 1 <=dan and dan <=9:
        print(f"구구단 {dan}단을 계산합니다.")
        for i in range(1, 10):
            print(f"{dan} X {i} = {dan*i}")
    elif dan == 0:
        print("구구단 게임을 종료합니다.")
        break
    else: 
        print("잘못 입력하셨습니다.")


"""