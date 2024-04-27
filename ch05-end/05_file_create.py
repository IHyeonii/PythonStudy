# 파일 생성하기
file = open('test.txt', 'w')

# 생성한 파일에 텍스트 작성
file.write('Hello World!')
file.close()


read = open('test.txt', 'r')
print(read.read())
read.close()

print('--------------------------------------------------')

with open('basic.txt', 'w') as file:
    file.write('아 지겨워 언제끝나냐')