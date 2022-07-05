f = open("yesterday.txt", "r")  # 파일을 불러오기
yesterday_lyric = ""

while True:
    line = f.readline()  # 한 줄씩 읽어오기
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
# print(yesterday_lyric)
# print(type(yesterday_lyric)) #string 타입으로 저장되어있음

n1_of_yestrday = yesterday_lyric.count("Yesterday")  # 각 타입별로 구분
n2_of_yestrday = yesterday_lyric.count("yesterday")
n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")  # 대소문자 구분 제거
print("Number of a word 'Yesterday'", n1_of_yestrday)
print("Number of a word 'yesterday'", n2_of_yestrday)
print("Number of a word 'YESTERDAY'", n_of_yesterday)
