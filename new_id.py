import re

def solution(new_id):
    # 1단계
    new_id = new_id.lower() 

    # 2단계
    new_id = re.sub('[=+,#/$\?:^@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]','',new_id)

    # 3단계
    while (new_id.count('..') >= 1):
        new_id = new_id.replace('..', '.')

    # 4단계
    while (new_id[0] == '.'):
        new_id = new_id.lstrip('.') 
    while (new_id[-1] == '.'):
        new_id.rstrip('.')

    # 5단계
    if (new_id is None): 
        new_id = 'a'

    # 6단계
    if (len(new_id) > 15):
        new_id = new_id[0:15]
        if (new_id[14] == '.'):
            new_id = new_id[0:14]

    # 7단계
    elif (len(new_id) < 3):
        new_id = new_id * 2
        if (len(new_id) < 3):
            new_id = new_id * 2
    
    answer = new_id

    return answer

print(solution('a...fFWKDrtiwrth_rh@#7.2n'))
print(solution('a'))
print(solution('..sderghaADGERd2#@$TTRW^*_'))
