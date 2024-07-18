#점수의 따라 학점 판정하기
'''score=int(input('점수를 입력하세요 : '))
if score >= 90 :
    print('등급 : A')
elif score >= 80 :
    print('등급 : B')
elif score >= 70 :
    print('등급 : C')
elif score >= 60 :
    print('등급 : D')
else :
    print('등급 : E')
print('등급 판단 끝')'''

'''score= int(input('점수는? '))
if score >=90 :
    grade='A'
elif score >=80 :
    grade='B'
elif score >=70 :
    grade='C'
elif score >=60 :
    grade='D'
else :
    grade='F'
print('등급 :',grade)'''

#간단 계산기 만들기
'''print('기능 선택')
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')
print()
s= input('계산기 기능을 선택하세요(1/2/3/4) : ')
num1= int(input('첫 번째 숫자를 입력하세요 : '))
num2= int(input('두 번째 숫자를 입력하세요 : '))

if s== '1' :
    print('%d + %d = %d'%(num1,num2,num1+num2))
elif s=='2' :
    print('%d - %d = %d'%(num1,num2,num1-num2))
elif s=='3' :
    print('%d × %d = %d'%(num1,num2,num1*num2))
elif s=='4' :
    print('%d ÷ %d = %d'%(num1,num2,num1/num2))
elif s!='1' or s!='2' or s!='3' or s!='4' :
    print('입력 숫자가 잘못되었습니다!')'''

#간단 계산기 만들기 ver.2
'''print('기능 선택')
print('1. 더하기')
print('2. 빼기')
print('3. 곱하기')
print('4. 나누기')
print()
s= input('계산기 기능을 선택하세요(1/2/3/4) : ')

if s== '1' :
    num1= int(input('첫 번째 숫자를 입력하세요 : '))
    num2= int(input('두 번째 숫자를 입력하세요 : '))
    print('%d + %d = %d'%(num1,num2,num1+num2))
elif s=='2' :
    num1= int(input('첫 번째 숫자를 입력하세요 : '))
    num2= int(input('두 번째 숫자를 입력하세요 : '))
    print('%d - %d = %d'%(num1,num2,num1-num2))
elif s=='3' :
    num1= int(input('첫 번째 숫자를 입력하세요 : '))
    num2= int(input('두 번째 숫자를 입력하세요 : '))
    print('%d × %d = %d'%(num1,num2,num1*num2))
elif s=='4' :
    num1= int(input('첫 번째 숫자를 입력하세요 : '))
    num2= int(input('두 번째 숫자를 입력하세요 : '))
    print('%d ÷ %d = %d'%(num1,num2,num1/num2))
elif s!='1' or s!='2' or s!='3' or s!='4' :
    print('입력 숫자가 잘못되었습니다!')'''

#만 나이 구하기
print('='*50)
year=int(input('현재년은? '))
month=int(input('현재월은? '))
day=int(input('현재일은? '))
birth_year=int(input('출생년은? '))
birth_month=int(input('출생월은? '))
birth_day=int(input('출생일은? '))

if birth_month < month :
    age=year-birth_year
elif birth_month == month :
    if birth_day < day :
        age=year-birth_year
    elif birth_day == month :
        age=year-birth_day
    else :
        age=month-birth_month-1
else :
    age=year-birth_year-1
print('='*50)
print('오늘날짜 : %s년 %s월 %s일'%(year,month,day))
print('생년월일 : %s년 %s월 %s일'%(birth_year,birth_month,birth_day))
print('-'*50)
print('만 나이 : %s세'%age)