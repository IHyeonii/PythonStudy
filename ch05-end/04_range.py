# 0, 5 출력 -> 0에서 5까지의 범위 생성
print(range(5))

# List에 적용 : 0 ~ 9 까지 생성
print(list(range(10))) 

# 5 ~ 9까지 생성
print(list(range(5, 10)))

# 매개변수가 3개면 : 0 ~ 9까지의 범위를 생성하는데, 차이가 2씩 나도록
print(list(range(0, 10, 2)))

print('--------------------------------------------------')
array = [273, 32, 103, 57, 52]

# 문자열, 리스트 길이 -> len()
# count(3) : 리스트의 특정 요소의 개수
print(range(len(array)))

for i in range(len(array)):
    print('{}번째 반복: {}'.format(i, array[i]))

print('--------------------------------------------------')
# 역으로 반복하기

# 0을 출력하려면 두 번째 인자에 -1을 넣어줘야 함
a = range(4, -1, -1)

for i in a :
    print("반복 변수: {}".format(i))
    
for i in reversed(range(5)):
    print(i)
    
print('--------------------------------------------------')

i = 0
while i < 10:
    print('{}번째 반복'.format(i))
    i += 1

print('--------------------------------------------------')
# 리스트를 반복하는데 값이 10보다 작으면 다음 반복으로 넘어가도록
num = [5, 15, 6, 20, 7, 25]

for i in num:
    if i < 10:
        continue
    print(i)

