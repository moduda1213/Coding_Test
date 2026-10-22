'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
import re
def solution(new_id):
    print(new_id)
    
    # 1단계 : 대문자 -> 소문자
    filter_id = new_id.lower()
    # filter_id = re.sub(r"[A-Z]", lambda x: x.group().lower, filter_id)
    print(filter_id)
    
    # r"..."의 r은 Python이 문자열 안의 백슬래시를 처리하지 않게 하는 표시
    # 2단계 : 특정 문자 제거
    filter_id = re.sub(r"[^a-z0-9-_.]", "", filter_id)
    print(filter_id)
    
    '''
    3단계 : 연속된 마침표 한개로 차환
    | (.)$ | 마지막 문자 한 개를 찾음 | "abb"에서 마지막 "b" |
    | (.)\1$ | 마지막 두 문자가 같은지 찾음 | "abb"에서 "bb" |
    | (.)$\1 | 끝에 도달한 뒤 문자를 또 찾으려 함 | 일치할 수 없음 |
    '''
    filter_id = re.sub(r"\.+", ".", filter_id)
    print(filter_id)
    
    # 4단계: 첫, 끝 위치 마침표 제거
    # filter_id = re.sub(r"^\.|\.$", "", filter_id)
    
    # strip() : 양쪽 끝 공백 or 문자 제거
    # lstrip() : 왼쪽 끝 공백 or 문자 제거
    # rstrip() : 오른쪽 끝 공백 or 문자 제거
    filter_id = filter_id.strip(".")
    print(filter_id)
    
    
    # 5단계: 빈 문자열 
    # '==' != is는 같은 객체인지 확인하는 법
    # if filter_id == "":
    #     filter_id = 'a'
        
    '''
    | x or y | x가 참이면 x, 거짓이면 y 반환 |
    | x and y | x가 거짓이면 x, 참이면 y 반환 |
    '''
    filter_id = filter_id or "a"
    
    print(filter_id)
    
    
    # 6단계: id > 15, 첫 15개의 문자를 제외한 나머지 제외, 끝에 '.' 위치한다면 제거
    # filter_id = re.sub(r"\.$", "", filter_id[:15])
    filter_id = filter_id[:15].strip('.')
    print(filter_id)
    
    # 7단계: id < 3, 마지막 문자를 길이 3 될때까지 끝에 붙임
    while len(filter_id) < 3:
        filter_id += filter_id[-1]
    print(filter_id)
    
    return filter_id

if __name__ == "__main__":
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    pass
