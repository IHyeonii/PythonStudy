# 반복문으로 파일 한 줄씩 읽기

with open('info.csv', 'r') as file:
    for line in file:
        
        # 변수 선언
        # split -> 문자열 변수에 대입
        name, weight, height = line.strip().split(',')
        
        # 데이터 검증
        if (not name) or (not weight) or (not height):
            continue
        
        # 한 줄씩 읽어서 처리하기
        # print('\n'.join([
        #     '이름: {}',
        #     '몸무게: {}',
        #     '키: {}'
        # ]).format(name, weight, height))