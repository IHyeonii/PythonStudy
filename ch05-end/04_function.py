ex = ['A', 'B', 'C', 'D']

print(list(enumerate(ex)))

# enumerate 메서드 사용시 변수를 다음 과 같이 할당 가능
for i, val in enumerate(ex):
    print('{}번째 요소는 {}입니다.'.format(i, val))

dic = {
    'A': '값A',
    'B': '값B',
    'C': '값C',
    'D': '값D'
}

print(dic.items())

for key, val in dic.items():
    print('{} : {}'.format(key, val))

print('--------------------------------------------------')

array = []

for i in range(0, 20, 2):
    array.append(i * i)
print(array)

print('--------------------------------------------------')

# 위의 코드 변형 -> 리스트 안에 for문 사용하기

array2 = [i * i for i in range(0, 20, 2)]
print(array2)