def solution(my_string, target):
    answer = 0
    if target in my_string:        # if 조건문을 사용하여 참과 거짓을 판별함.
        answer = 1                 # 만약 target이 문자열 my_string의 부분 문자열이라면 1을 return함.
    return answer                             
    
print(solution("abcdefghijk","abcdef")) # "abcdef"는 "abcdefghijk"에 포함되는 부분 문자열이므로 1을 리턴함.
print(solution("abcdefghijk","aehj"))   # "aehj"는 "abcdefghijk"에 포함되는 부분 문자열이 아니므로 0을 리턴함.