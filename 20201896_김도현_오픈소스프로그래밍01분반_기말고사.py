#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : ________ 이름 : ______

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_strung, target):
    answer = 0
    return answer

# q1 답:

def solution(my_string, target):
    answer = 0
    if target in my_string:        # if 조건문을 사용하여 참과 거짓을 판별함.
        answer = 1                 # 만약 target이 문자열 my_string의 부분 문자열이라면 1을 return함.
    return answer                             
    
print(solution("abcdefghijk","abcdef")) # "abcdef"는 "abcdefghijk"에 포함되는 부분 문자열이므로 1을 리턴함.
print(solution("abcdefghijk","aehj"))   # "aehj"는 "abcdefghijk"에 포함되는 부분 문자열이 아니므로 0을 리턴함.


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''
    return answer

# q2 답:

def solution(letter):

  letter = letter.split(" ")          # 문자열 letter을 split을 이용하여 공백을 이용하여 나누어서 리스트로 저장함.

  answer = ''
  morse = {
     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
  for i in letter:                        # for문을 이용하여 모스부호를 영어로 변환.
    if i in morse:                        # if문을 이용하여 i가 morse에 포함된다면 answer += morse[i].
      answer += morse[i]

  return answer

print(solution("--. .-. . .- - .--. --- .-- . .-. -.-. --- -- . ... --. .-. . .- - .-. . ... .--. --- -. ... .. -... .. .-.. .. - -.--"))
                            # 제한사항에 맞추어 제한된 길이에 맞고, 내가 인상깊었던 말을 예시로 출력.




# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    answer = ''
    return answer


# q3 답:

def solution(age):
  answer = ''
  PROGRAMMERS ={                      # 각 숫자에 맞는 알파벳들을 할당함.
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd',
    '4': 'e',
    '5': 'f',
    '6': 'g',
    '7': 'h',
    '8': 'i',
    '9': 'j'
}
  for i in age:                              # for문을 이용하여 각 숫자를 영어로 변환.
    if i in PROGRAMMERS:                     # if문을 이용하여 i가 PROGRAMMERS에 포함된다면 answer += PROGRAMMERS[i].
      answer += PROGRAMMERS[i]
  return answer

print(solution("23"))                        # 문제에 나왔던 예시를 직접 프린트하여 맞는지 확인.
print(solution("51"))









# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
    answer = 0
    return answer

# q4 답:

import math

def solution(r1, r2):                     # r1, r2는 원의 반지름.
  answer = 0
  for i in range(-r2, r2+1):              # i와 j는 현재 위치, for문을 두 번 사용하여 2차원 직교 좌표계의 모든 정수 좌표를 반복함.
    for j in range(-r2, r2+1):
      radius = i**2 + j**2                # 현재 위치에서 원점까지의 거리를 제곱함. 

      if r1**2 <= radius <= r2**2:        # 현재 위치가 두 원 사이에 속하는지 확인함.
        answer += 1                       # 현재 위치가 두 원 사이에 있다면 정수 좌표의 개수를 증가함.

  return answer

print(solution(15, 21))                   # 예시로 반지름 15와 21을 이용하여 프린트함.






# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    answer = ''
    return answer


# q5 답:

def solution(numbers):
  answer = ''
  array = []                      # 각 정수를 문자열로 변환하여 저장하는 리스트다.
  for i in numbers:               # for문을 이용하고, array.append(str(i))를 이용하여 숫자열을 스트링으로 변환하여 리스트에 추가함.
    array.append(str(i))

  array.sort(reverse= True)       # array.sort(reverse= True)를 이용하여 앞자리중에 가장 큰 수로 정렬시킴.
  for i in array:                 # for문을 사용하여 문자들을 이어붙임.
    answer += i

  return answer

numbers1 = [8, 30, 17, 2, 23]     # [8, 30, 17 2, 23]을 이용하여 가장 큰 수를 만드는 예시.
print(solution(numbers1))
numbers2 = [6, 10, 2]             # [6, 10, 2]를 이용하여 가장 큰 수를 만드는 예시.
print(solution(numbers2))