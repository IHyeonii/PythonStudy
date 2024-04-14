score = input('학점 입력하세여 >')
score = float(score)

if score == 0 :
    print('바보')
elif score <= 0.5 :
    print('플랑크톤')
elif score <= 1.0 :
    print('자벌레')
elif score <= 1.75 :
    print('천민')
elif score <= 2.3 :
    print('선구자')
elif score <= 2.8 :
    print('소시민')
else :
    print('너무 길어서 패스')