# C3-7
'''spend=int(input('구매 금액은? '))
if spend < 50000 and spend >= 10000 :
    rate= 5.0
elif spend < 300000 and spend >= 50000 :
    rate= 7.5
elif spend > 300000 :
    rate = 10.0
else :
    rate = 0

dc=spend*rate/100
pay=spend-dc

print('구매금액 : %.0f'%spend)
print('할인율 : %.1f'%rate)
print('할인금액 : %0f'%dc)
print('지불금액 : %0f'%pay)'''

#C3-8
'''print('서비스 만족도 :')
print('1:매우만족')
print('2:만족')
print('3:불만족')
a=input('서비스 만족도는?(1/2/3) ')
price=int(input('음식값은? '))

if a=='1' :
    tip = int(price*0.2)
    service = '매우만족'
elif a=='2' :
    tip = int(price*0.1)
    service = '만족'
else :
    tip =0
    service = '불만족'
print()
print('서비스 만족도 : %s, 팁 : %d원'%(service,tip))'''

#C3-9
'''num1=int(input('첫 번째 정수는? '))
num2=int(input('두 번째 정수는? '))
num3=int(input('세 번째 정수는? '))

if num1 > num2 and num1 > num3 :
    largest=num1
elif num2 > num1 and num2 > num3 :
    largest=num2
else :
    largest=num3
print('%d, %d, %d 중에서 가장 큰 수는 %d 입니다.'%(num1,num2,num3,largest))'''

#C3-10
'''id=input('아이디는? ')

if id=='admin' :
    print('콘텐츠 이용이 가능합니다!')
else :
    level=int(input('회원 레벨은?(1~9) '))
    if level >= 4 :
        print('콘텐츠를 이용할 수 없습니다!')
    elif 1<=level<=3 :
        print('콘텐츠 이용이 가능합니다!')'''

#C3-11
'''unit=input('단위를 입력해 주세요(1:섭씨,2:화씨): ')
temp=int(input('온도를 입력해 주세요 : '))

if unit =='2' :
    temp = (temp-32)*5/9

if temp <= 0 :
    state = '고체'
elif temp <100 :
    state = '액체'
else :
    state='기체'

print('물의 섭씨 온도 : %.1f도, 상태 : %s'%(temp,state))'''
