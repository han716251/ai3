#E3-1
'''num=int(input('숫자를 입력하세요 : '))
if num > 10 :
    print('%d은(는) 10보다 크다.'%num)
elif num < 10 :
    print('%d은(는) 10보다 크지 않다.'%num)'''

#E3-2
'''num1=int(input('첫 번째 숫자를 입력하세요 : '))
num2=int(input('두 번째 숫자를 입력하세요 : '))
if num1 > num2 :
    print('%d 은(는) %d 보다 크다.'%(num1,num2))
elif num1 < num2 :
    print('%d 은(는) %d 보다 크다.'%(num2,num1))
else :
    print('%d 은(는) %d와(과) 같다.'%(num1,num2))'''

#E3-3
'''num = input('숫자를 입력하세요 : ')
num3 = int(num[4])
if num3%2 == 0 :
    print('%d은(는) 짝수이다.'%num3)
elif num3%2 == 1 :
    print('%d은(는) 홀수이다.'%num3)
else :
    print('오류! 입력이 잘못되었습니다!')'''

#E3-4
'''num1=int(input('첫 번째 숫자를 입력하세요 : '))
num2=int(input('두 번째 숫자를 입력하세요 : '))
plus=num1+num2
print('%d + %d = %d'%(num1,num2,plus))

if plus % 3 == 0 : 
    print('%d은(는) 3의 배수이다.'%plus)
else :
    print('%d은(는) 3의 배수가 아니다.'%plus)'''

#E3-5
'''age= int(input('당신의 나이는? '))
if age >= 35 : 
    print('당신은 평균 나이(35세) 이상이다.')
else :
    print('당신은 평균 나이(35세) 미만이다.')'''

#E3-6
'''num=input('수를 입력하세요 : ')
if len(num) == 1 :
    print('%s 은(는) 한 자리 숫자이다.'%num)
elif len(num) == 2 :
    print('%s 은(는) 두 자리 숫자이다.'%num)
elif len(num) == 3 :
    print('%s 은(는) 세 자리 숫자이다.'%num)
else :
    print('오류! %s 은(는) 범위(0~999) 이외의 숫자이다.'%num)'''

#E3-7
'''text=input('문자열을 입력하세요 : ')
num=len(text)
print('문자열의 개수 : %d'%num)
if num%2==0 :
    print('문자열의 개수는 짝수이다.')
else :
    print('문자열의 개수는 홀수이다.')'''

#E3-8
'''num1=int(input('첫 번째 숫자를 입력하세요 : '))
num2=int(input('두 번째 숫자를 입력하세요 : '))
print('원하는 연산은?')
a=input('+,-,*,/ 중 하나를 선택하세요 : ')
if not(a== '+' or a== '-' or a== '*' or a== '/') :
    print('오류! 잘못된 입력입니다!')
elif a == '+' :
    print('%d + %d = %d'%(num1,num2,num1+num2))
elif a == '-' :
    print('%d - %d = %d'%(num1,num2,num1-num2))
elif a == '*' :
    print('%d * %d = %d'%(num1,num2,num1*num2))
elif a == '/' :
    print('%d / %d = %d'%(num1,num2,num1/num2))'''

#E3-9
'''score=int(input('점수를 입력하세요 : '))

if score > 100 or score < 0 :
    print('오류! 입력이 잘못되었습니다!')
elif 90 <= score <= 100 :
    print('성적 : %d, 등급 : 수'%score)
elif 80 <= score <= 89 :
    print('성적 : %d, 등급 : 우'%score)
elif 70 <= score <= 79 :
    print('성적 : %d, 등급 : 미'%score)
elif 60 <= score <= 69 :
    print('성적 : %d, 등급 : 양'%score)
else :
    print('성적 : %d, 등급 : 가'%score)'''

#S3-1
'''rate=input('등급을 입력해 주세요(A+,A,B+,...,F) : ')
if not(rate=='A+' or rate=='A' and rate=='B+' and rate=='B' and rate=='C+' and rate=='C' and rate=='D+' and rate=='D' and rate=='F') :
    print('오류! 입력이 잘못되었습니다!')
elif rate == 'A+' :
    print('등급 : A+, 평점 : 4.5')
elif rate == 'A' :
    print('등급 : A, 평점 : 4.0')
elif rate == 'B+' :
    print('등급 : B+, 평점 : 3.5')
elif rate == 'B' :
    print('등급 : B, 평점 : 3.0')
elif rate == 'C+' :
    print('등급 : C+, 평점 : 2.5')
elif rate == 'C' :
    print('등급 : C, 평점 : 2.0')
elif rate == 'D+' :
    print('등급 : D+, 평점 : 1.5')
elif rate == 'D' :
    print('등급 : D, 평점 : 1.0')
elif rate == 'F' :
    print('등급 : F, 평점 : 0')'''

#S3-2
'''hour1=int(input('첫 번째 시간의 시를 입력하세요 : '))
minute1=int(input('첫 번째 시간의 분을 입력하세요 : '))
hour2=int(input('두 번째 시간의 시를 입력하세요 : '))
minute2=int(input('두 번째 시간의 분을 입력하세요 : '))
print()

if not(0<=hour1<=24 and 0<=hour2<=24 and 0<=minute1<=59 and 0<=minute2<=59 ) :
    print('오류! 입력이 잘못 되었습니다!')
elif hour1 > hour2 :
    print('-빠른 시간 : %d:%d'%(hour2,minute2))
    print('-늦은 시간 : %d:%d'%(hour1,minute1))
elif hour2 > hour1 :
    print('-빠른 시간 : %d:%d'%(hour1,minute1))
    print('-늦은 시간 : %d:%d'%(hour2,minute2))
elif hour1 == hour2 :
    if minute1 > minute2 :
        print('-빠른 시간 : %d:%d'%(hour2,minute2))
        print('-늦은 시간 : %d:%d'%(hour1,minute1))
    elif minute2 > minute1 :
        print('-빠른 시간 : %d:%d'%(hour1,minute1))
        print('-늦은 시간 : %d:%d'%(hour2,minute2))
    else :
        print('시간이 %d:%d로 동일합니다!'%(hour1,minute1))'''

#S3-3
name=input('이름을 입력하세요 : ')
work_time=int(input('일주일간 일한 시간을 입력하세요 : '))
pay=12000

if work_time < 1 :
    print('오류! 입력이 잘못되었습니다!')
elif 1 <= work_time <=40 :
    week_pay=work_time*pay
elif work_time > 40 :
    over_time=work_time-40
    week_pay=(over_time*pay*1.5) + 40*pay

print()
print('- 이름 : %s'%name)
print('- 일주일간 일한 시간 : %d시간'%work_time)
print('- 오버타임 : %s시간'%over_time)
print('- 주급 : %d'%week_pay)