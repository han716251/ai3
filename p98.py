#수의 참 거짓 찾기
'''x=10
if x > 0 :
    print('양수')
    print('조건이 참일때 수행')
print('조건문 배워요')'''

#점수 찾기
'''y=100
if y>=90 :
    print("A+")
else :
    print('낮은 점수')
print('모두 실행되는 곳')'''

#큰 수 찾기
'''a,b = 8,10
if a>b :
    print('a가 더 큰 수')
else :
    print('b가 더 큰 수')
print('판단 끝')'''

#등급 계산기 1
'''score=int(input('점수를 입력하세요 : '))
if score >= 95 :
    print('A')
elif score < 55 :
    print('F')
else :
    print('B')
print('판단 끝')'''

#등급 계산기 2
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


# 양수 음수,0 구하기
'''x=int(input('숫자를 입력하세요'))
if x > 0 :
    print("양수이다!")
else :
    print('음수 또는 0이다!')'''

# 양수 음수 0 구하기
'''x=int(input('숫자를 입력하세요'))
if x > 0 :
    print("양수이다!")
elif x < 0 :
    print('음수이다!')
else :
    print('0이다!')'''

'''x=int(input('정수를 입력하세요.'))
if x>0 :
    print('입력된 수는 양수입니다.')
    print('입력된 수는 양수입니다.')'''

# not 써서 양수 음수 0 구하기
'''x=int(input('숫자를 입력하세요'))
if not x < 0 :
    print('양수이다!')
elif not x > 0 :
    print('음수이다!')
else :
    print('0이다!')'''

#p103
'''score1=75
score2=90
if score1 >= 80 and score2 >=80 :
    print('true')'''

'''score1=85
score2=95
if score1>=80 and score2>=80 :
    print('true')'''

# or 쓰기
'''x=10
x%2 == 0 or x%6 == 0

x=16
x%3 == 0 or x%5 == 0'''

#퀴즈
'''a=5
b=7
c=a+b
c==12
print(c==12)'''

'''hobby1='영화감상'
hobby2='수영'
my_hobby='독서'
my_hobby==hobby1 or my_hobby== hobby2
print(my_hobby==hobby1 or my_hobby== hobby2)'''

'''pilgi =90
silgi=70
pilgi >= 80 and silgi >= 80
print(pilgi >= 80 and silgi >= 80)'''

#65세 이상 입장료 무료
'''age=int(input('나이를 입력하세요 : '))
ticket=2000
if age >= 65 :
    print('65세 이상은 무료입니다.')
else :
    print('입장료는 %s원 입니다'%ticket)'''

'''age=int(input('나이를 입력하세요 : '))
ticket=2000
if age>=65 :
    print('입장료는 무료입니다.')
elif age>=21 :
    print('입장료는 %s원 입니다.'%ticket)
elif age>=10 :
    print('입장료는 %s원 입니다.'%(ticket-500))
elif age>=5 :
    print('입장료는 %s원 입니다.'%(ticket-800))
elif age>=0 :
    print('입장료는 %s원 입니다.'%(ticket-1000))'''

