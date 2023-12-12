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