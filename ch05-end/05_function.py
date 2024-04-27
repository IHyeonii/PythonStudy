def print_3():
    print("3")
    print("3")
    print("3")
    
# print_3() 함수 호출
print_3()

print('--------------------------------------------------')

def f(x):
    return 2 * x + 1

print(f(10))

def f(x):
    return x ** 2 + (2 * x) + 1

print(f(10))

print('--------------------------------------------------')

def mul(*val):
    result = 1
    
    for i in val:
        result *= i
    return result

print(mul(5, 7, 9, 10))

print('--------------------------------------------------')

