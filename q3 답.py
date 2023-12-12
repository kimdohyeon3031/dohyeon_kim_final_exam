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