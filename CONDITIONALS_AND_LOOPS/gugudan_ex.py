print("구구단 몇 단을 계산할까요?")
num = int(input())
print(f"구구단 {num}단을 계산합니다.")

i = 1
while i < 10 :
    num_gugu = num * i
    print(f"{num} X {i} = {num_gugu}")
    i += 1


""" for 문 사용 시
for i in range(1, 10):
    print(f"{num} X {i} = {num * i}")
"""