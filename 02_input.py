# input('입력해 >')

# 사용자 입력 내용 = input 함수의 결과 -> 이 값을 다른 변수에 대입해서 사용하기

str = input('여자야 남자야 >')
print('str 결과 : ', str)

# 문자열 양옆 공백 제거
a = '   안녕  '
print(a)
print(a.strip())

# 문자열 찾기
b = '안녕하세요'
print(b.find('안녕')) # 시작위치인 0이 반환

# 문자열 내부에 특정 문자 포함여부 확인
print('안녕' in b) # True
print('몰라' in b) # False