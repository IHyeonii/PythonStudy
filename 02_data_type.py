print('이름 \t 나이 \t 지역')
print('윤인성 \t 25 \t 강서구')
print('윤아린 \t 24 \t 강서구')

# 문자열 연결
a = '안녕'
b = '바보야'

print(a+b)

# 문자열이랑 숫자를 더히려면?
print(a + str(1111))
print(a + '1111')

# 바보만 인덱싱하기
print(b[:2])

c = '안녕하세요'

# -는 뒤에서 부터 추출
print(c[-1])
print(c[-2])
print(c[-3])

print(123)
print(123.456)

print(type(123)) # int
print(type(123.456)) # float

print('5 * 7 = ', 5 * 7)
print('5 / 7 = ', 5 / 7) # 0.71428xx
print('5 // 7 = ', 5 // 7) # 몫만 반환 = 0
print('5 % 7 = ', 5 % 7)

# 제곱 연산자
print('3 ** 3 = ', 3 ** 3)