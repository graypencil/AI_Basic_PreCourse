print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨 온도를 입력해 주세요: ")
cel_temp = float(input()) 
fah_temp = ( (9/5) * cel_temp ) + 32

print(f"섭씨온도: {cel_temp:.2f}")
print(f"화씨온도: {fah_temp:.2f}")


"""
# 첫 번째 풀이방법(내가 하는 것)

def c_to_f(temp):
    return ((9/5) * temp) + 32

print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
temp = float(input("변환하고 싶은 섭씨 온도를 입력해 주세요: ")) 
print("섭씨온도: ", temp)
print(type(temp))

print("화씨온도: ", c_to_f(temp))
print(type(temp))

"""
