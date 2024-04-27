key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

# 리스트 수 만큼 반복문 돌면서
# 첫 번째 리스트의 값을 key
# 두 번째 리스트 요소를 값으로 딕셔너리에 저장

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)

print('--------------------------------------------------')

# 1부터 숫자를 하나씩 증가시킬 때, 몇을 더할 때 1000을 넘는지 구해
limit = 1000
i = 1
sum_val = 0

while sum_val <= limit :
    sum_val += i
    i += 1

# 10000 초과할 때 i가 증가되서 루프 종료되서 -1    
print('{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.'.format(i-1, limit, sum_val))
        
# 이 전 코드
# while sum_val <= limit :
#     i += 1
#     sum_val = i

print('--------------------------------------------------')

# 범위 1 ~ 99(100-1)
num = list(range(1, 100, 1))
num_reverse = list(reversed(num)) # num.reverse() -> None 출력

max_val = 0
val = 0

# i = 1 ~ 99
for i in num:
    val = num[i-1] * num_reverse[i-1]
    
    if max_val < val:
        max_val = val
    else :
        print('최대가 되는 경우: {} * {} = {}'.format(num[i-2], num_reverse[i-2], max_val))
        break
