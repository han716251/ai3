score=80
print('성적:'+str(score))
x="산토끼"*10
print(x)
print("-- "*20)
print('토끼'*10)
n=str(100)*20
print(n)
print("100 "*10)
n200=200
print(str(200)*15)

x='수학성적:'
print(type(x))
y=str(80)
print(type(y))
z=x+y
print(type(x))
print(z)

date='20220301'
year=date[0:4]
month=date[4:6]
day=date[6:]
date2=year+"-"+month+"-"+day
print(date2)

x='가는 말이 고와야 오는 말이 곱다.'
n=len(x)
print('문자열의 길이 : '+str(n))

#자기이름 핸드폰번호 마지막자리의 갯수 반복하기
name= '한상준'
phone='01065552142'
print(int(phone[-1])*name)
'''
phone1='82-10-8744-3334'
phone2='82-02-123-4567'
if len(phone1)==15 :
    print('한국 핸드폰번호입니다')
else :
    print('한국 집번호입니다')

if len(phone2)==15 :
    print('한국 핸드폰번호입니다')
else :
    print('한국 집번호입니다')

if len(phone2)==15 and phone2[0:2]==82 :
    print('한국 핸드폰번호입니다')
else :
    print('한국 집번호입니다')
'''

phone1='82-10-8744-3334'
phone2='82-12-123-4567'

if len(phone1)==15 and len(phone2)==15 :
    print('phone1은 핸드폰 번호입니다')
    print('phone2는 핸드폰 번호입니다')
elif len(phone1)==15 and len(phone2)==14 :
    print('phone1은 핸드폰 번호입니다')
    print('phone2는 집 번호입니다')
elif len(phone1)==14 and len(phone2)==15 :
    print('phone1은 집 번호입니다')
    print('phone2는 핸드폰 번호입니다')
elif len(phone1)==14 and len(phone2)==14 :
    print('phone1은 집 번호입니다')
    print('phone2는 집 번호입니다')

if phone1[3:5]==int(10) and phone2[3:5]==int(10) :
    print('phone1은 핸드폰 번호입니다')
    print('phone2은 핸드폰 번호입니다')
elif phone1[3:5]==int(10) and phone2[3:5]==int(12) :
    print('phone1은 핸드폰번호입니다')
    print('phone2은 집번호입니다')
elif phone1[3:5]==int(12) and phone2[3:5]==int(10) :
    print('phone1은 핸드폰번호입니다')
    print('phone2은 핸드폰번호입니다')
elif phone1[3:5]==int(12) and phone2[3:5]==int(12) :
    print('phone1은 집번호입니다') 
    print('phone2은 집번호입니다')

