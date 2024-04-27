dic = {
    'name': '망고',
    'ingredients': ['망고', '설탕', '색소']
}

dic['price'] = 1000

# print(dic)

for key in dic:
    print(key, ' : ', dic[key])
    
print('--------------------------------------------------')
# 확인문제 03 (p.172)
# 딕셔너리의 리스트 선언

pets = [
    {'name' : '나나', 'age' : 2},
    {'name' : '구름', 'age' : 5},
    {'name' : '하늘', 'age' : 3},
    {'name' : '아지', 'age' : 6},
    {'name' : '호야', 'age' : 7},
]

for key in pets:
    print (key['name'], (str(key['age']) + '살'))
    
    
print('--------------------------------------------------')
# 확인문제 03 (p.172)
# 리스트 안에 반복되는 숫자 개수 세기
numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

# numbers 를 반복문으로 돌면서 
# 첫 번째 요소를 counter의 key로 저장
# key와 일치하는 개수를 카운트해서 키의 값으로 저장

for key in numbers:
    counter[key] = numbers.count(key)

print(counter)
    
print('--------------------------------------------------')

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

# 딕셔너리의 키만 꺼내옴 -> name, level, items, skill
for i in character:
    print(i)

print('-------------------------------------------')

for key in character:
    if type(character[key]) == type([]):
        for i in character[key]:
            print(key, ":", i)
            
    elif type(character[key]) == type({}):
        for i in character[key]:
            print(i,":", character[key][i])
        
    else:
        print(key, ":", character[key])