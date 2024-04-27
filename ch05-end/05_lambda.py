# 함수 선언
def power(item):
    return item * item

def under_3(item):
    return item < 3

# 변수 선언
list_a = [1, 2, 3, 4, 5]

# mpa() 사용해보기: 함수를 매개변수로 전달
# map(함수, 리스트)

output_a = map(power, list_a)
print(list(output_a))
# return [1, 4, 9, 16, 25]

# 리스트의 요소가 함수의 매개변수로 넘어간다?

output_b = filter(under_3, list_a)
print(list(output_b)) # return [1, 2]

