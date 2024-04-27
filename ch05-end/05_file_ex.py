num = list(range(1, 10, +1))

# 홀수 추출
def number(i):
    return i % 2 != 0

result_a = filter(number, num)
print(list(result_a))

# map, filter 함수는 리스트를 인자로 받아서 리스트 요소를 하나씩 처리

# 3이상, 7미만 추출
def filter_num(i):
    return i >= 3 and i < 7
    
re_b = filter(filter_num, num)
print(list(re_b))