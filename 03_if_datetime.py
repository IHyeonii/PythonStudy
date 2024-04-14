# 조건문으로 오전, 오후 출력하기
import datetime

now = datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)

hour = now.hour

if hour < 12 :
    print('지금 시간은 {}시로 오전임'.format(now.hour))

if hour >= 12 :
    print('지금 시간은 {}시로 오후임'.format(now.hour))

