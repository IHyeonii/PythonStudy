dic = {
    'name': '망고',
    'ingredients': ['망고', '설탕', '색소']
}

print(dic['name'])
print(dic['ingredients'])
print(dic['ingredients'][1])

# 값 변경하기 : 망고 -> 건망고
dic['name'] = '건망고'
print(dic)

# 값을 추가, 제거하기

dic['price'] = 1000
print(dic)

del dic['price']
print(dic)

print('-------------------------------------------------')

# 선언만 하고 요소추가 가능
dictionary = {}

dictionary['name'] = 'aa'
dictionary['ingredients'] = 'bb'
print(dictionary)

key = 'name'

if key in dictionary:
    print('해당 키가 존재함')
else:
    print('해당 키는 존재하지 않음')