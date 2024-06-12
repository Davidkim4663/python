# 파이썬 자료형은 정수, 실수, 문자, 참과 거짓이 있다.

# 자료형
print(10)
print(10.3333)
print("안녕")
print(True)
print(False)

########################################################
# 산술 연산자 
print()
print("########################################")
print(10 + 3) # 더하기
print(10 - 3) # 빼기
print(10 * 3) # 곱하기
print(10 / 3) # 나누기(소수점이 생길 수 있다)
print(10 // 3) # 몫(소수점 제거)
print(10 % 3) # 나머지

########################################################
# 우선순위
'''
1. ()
2. *, /, // %
3. +, -

>> 괄호 먼저 계산을 한 뒤 곱셈, 나눗셈, 몫 혹은 나머지를 계산
>> +, - 
'''
########################################################
# 산술 연산자 
print()

# 소수점 제한 명령어
# round(실수, 자리수)
print("실수 출력 : ", 10 / 3)
print("실수 출력(round) 자리수 한 자리 : " , round(10 / 3 , 1))
print("실수 출력(round) 자리수 두 자리 : " , round(10 / 3 , 2))

print("-----------------------------------------------")
print("실수 출력 : ", 10.3 + 2.3)
print("실수 출력(round) : ", round(10.3 + 2.3, 1))