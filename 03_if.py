a = 10

if a < 10:
    print('a가 10보다 작음')
print('종료')

print('---------------------------')

number = input('정수 입력해 >')
int_num = int(number)

if int_num > 0 :
    print('number는 양수임')

if int_num < 0 :
    print('number는 음수임')

if int_num == 0 :
    print('number는 0임')

# 조건에 일치하는 코드만 실행 -> 코드의 실행 흐름을 변경(조건 분기)

if int_num % 2 == 0 :
    print(("짝수"))
else :
    print("홀수")