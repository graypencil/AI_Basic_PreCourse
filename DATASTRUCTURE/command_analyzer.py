import csv

def getKey(item):  # 정렬을 위한 함수
    return item[1]

# 파일을 읽어오기 (한 줄씩 읽어오는 코드)
command_data = []
with open("command_data.csv", "r", encoding= "utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)

# dict 생성
command_counter = {} 
for data in command_data: # 2차원 배열의 형태 list 데이터를 dict로 변경
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1 # 기존 출현한 id에는 key 값 넣지 않음
    else:
        command_counter[data[1]] = 1  # 기존 출현한 id는 나온 key 값을 넣어줌
# print(command_counter) # 확인을 위한 print

# dict를 list로 변경
dictlist = []
for key, value in command_counter.items():
    temp = [key, value]
    dictlist.append(temp)
# print(dictlist) # 확인을 위한 print

sorted_dict = sorted(dictlist, key=getKey, reverse=True) # sorted 넣을 때 key 값을 이용해야 함(sort 기준) 
print(sorted_dict[:100])   # list의 상위 100개 값만 출력