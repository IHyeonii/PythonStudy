tuple = (1, 2, 3)
print(tuple[0])
print(tuple[1])
print(tuple[2])

# 리스트
print([273])

# 튜플
print((273,))

print('--------------------------------------------------')

# 리스트와 튜플의 특이한 사용
[a, b] = [1, 2]
(c, d) = (3, 4)

print(a) # 1
print(b) # 2
print(c) # 3
print(d) # 4

print('--------------------------------------------------')
# 괄호 없는 튜플
tu_test = 10, 20, 30, 40, 50

print(tu_test)
print(type(tu_test)) # <class 'tuple'>

# 변수의 값을 교환 가능
(a, b) = (10, 20)

print(a, b) # 10 20

a, b = b, a
print(a, b) # 20 10

print('--------------------------------------------------')

# 튜플로 값을 여러개 리턴 가능
def test():
    return (10, 20)

print(test())
