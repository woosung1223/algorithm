# Page 314 문자열 뒤집기
# Page 508 답안

string = input()

def ChangeString(string):
    # min(연속된 1 count, 연속된 0 count)
    # 1 count와 0 count는 항상 1차이 날 수 밖에 없음!
    # 1개 - 2개, 3개 - 4개... 

    # 압축
    new_string = "-"
    for idx in range(len(string)):
        if new_string[-1] != string[idx]:
            new_string += string[idx]
    
    # new_string에는 압축된(연속적이지 않은) 숫자들이 저장됨
    result = min(new_string.count('0'), new_string.count('1'))
    return result

print(ChangeString(string))