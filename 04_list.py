a = [1, 2, 3]
b = [4, 5, 6]

c = a + b

print(c)

# 이렇게 해도 되는데 굳이  append, extend 왜 쓰냐
# append(요소), extend(리스트)

print(a)
print(b)

# 변수 a 랑 b 찍어보면 기존 기존 값이 유지
# append랑 extend 는 기존의 값 자체를 변화

list_a = [1, 2, 3]
print(list_a)
print(list_a.append(4)) # return -> None

# append()은 추가만 해주고 return해주는게 없음
# 다시 list_a 를 찍어야 추가된 값이 나옴

print('list_a', list_a)

list_b = [5, 6, 7]
list_a.extend(list_b)
print('list_a',list_a)

# del, pop -> 인덱스의 요소를 제거
# remove(값)

for i in range(5) :
    print('*')

list = [1, 3, 4, 5, 6, 7]

for i in list :
    print(i)

# 100 이상의 숫자만 출력
num = [23, 45, 67, 100, 234, 500]

for number in num :
    if number >= 100 :
        print(number)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

#  홀수 짝수
for num in numbers :
    if num % 2 == 0 :
        print('{}는 짝수입니다.'.format(num))
    else:
        print('{}는 홀수입니다.'.format(num))

for num in numbers :
    print('{}은 {}자릿수 입니다.'.format(num, len(str(num))))

array = [
    [1, 2, 3],
    [4, 5, 6 ,7],
    [8,9]
]

print(array)
# arrays = array[0] + array[1] + array[2]
#
# for i in arrays :
#     print(i)

for i in array :
    # print(i)
    for j in i :
        print(j)