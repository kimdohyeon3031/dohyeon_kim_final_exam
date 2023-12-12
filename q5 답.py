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