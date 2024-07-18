'''#문제 1
year=input('년은? ')
month=input('월은? ')
day=input('일은? ')
print(year,month,day,sep='.')

#문제 2
width=int(input('사각형의 너비는? '))
height=int(input('사각형의 높이는? '))
length=2*width+2*height
area=width*height
print('사각형의 너비: %dcm'%width)
print('사각형의 높이 :%dcm'%height)
print('둘레 길이: %dcm'%length)
print('면적: %dcm2'%area)'

#문제 3
r=float(input('반지름을 입력하세요 : '))
length=(2*r*3.14)
area=r*r*3.14
print('반지름 : %.2fcm'%r)
print('원의 둘레 : %.2fcm'%length)
print('원의 면적 : %.2fcm2'%area)

#문제 4
inch=float(input('인치는? '))
cm=inch*2.54
print('%.1finch'%inch, '%.1fcm'%cm,sep=' => ')

#문제 5
price=int(input('책 값은? '))
discount=int(input('할인율은? '))
delivery=int(input('배송료는? '))

pay= price-(price*(discount/100))+delivery

print('책 값 : %d원'%price)
print('할인율 : %d'%discount)
print('배송료 : %d원'%delivery)
print('결제 금액 : %d원'%pay)
'''
#E2-1.
'''x=10
y=20
print('두 수의 합 :',x+y)'''

#E2-2.
'''x=10
y=20
print('%s+%s ='%(x,y),x+y)'''

#E2-3.
'''x=10
y=20
print(int(x),'+',int(y),'=',x+y)'''

#E2-4.
'''fruit1=input('첫 번째 과일을 입력하세요 : ')
fruit2=input('두 번째 과일을 입력하세요 : ')
print(fruit1,'와(과)',fruit2,'은(는) 내가 좋아하는 과일이다.')'''

#E2-5.
'''fruit1=input('첫 번째 과일을 입력하세요 : ')
fruit2=input('두 번째 과일을 입력하세요 : ')
print(fruit1,'와(과) ',fruit2,'은(는) 내가 좋아하는 과일이다.',sep='')'''

#E2-6.
'''fruit1=input('첫 번째 과일을 입력하세요 : ')
fruit2=input('두 번째 과일을 입력하세요 : ')
print('%s와(과) %s은(는) 내가 좋아하는 과일이다.'%(fruit1,fruit2))'''

#E2-7.
'''number1=input('첫 번째 숫자를 입력하세요 : ')
number2=input('두 번째 숫자를 입력하세요 : ')
result=int(number1)/int(number2)
print(number1,'/',number2,'=','%.6f'%result)'''

#E2-8.
'''number1=input('첫 번째 숫자를 입력하세요 : ')
number2=input('두 번째 숫자를 입력하세요 : ')
result=int(number1)/int(number2)
print(number1,'/',number2,'=','%.2f'%result)'''

#E2-9.
'''front_email=input('이메일 주소 앞 부분은? ')
behind_email=input('이메일 주소 뒷 부분은? ')
print('-이메일 주소 : %s@%s'%(front_email,behind_email))'''

#E2-10.
'''name=input('이름을 입력하세요 : ')
address=input('주소를 입력하세요 : ')
phone=input('전화번호를 입력하세요 : ')
print('- 이름 :',name)
print('- 주소 :',address)
print('- 전화번호 :',phone)'''

#E2-11.
'''upper_length=input('윗변의 길이는? ')
base_length=input('밑변의 길이는? ')
height=input('높이는? ')
area=(int(upper_length)+int(base_length))*int(height)/2
print('- 사다리꼴의 면적 :',area)'''

#E2-12.
'''x='가는 말이 고와야 오는 말이 곱다.'
print(x)
print('-추출 문자 :',x[10:14])'''

#E2-13.
'''number10=input('열 자리의 숫자를 입력하세요 : ')
print('추출된 두 숫자 :',number10[8:10])'''

#S2-1.
'''kg=input('변환할 킬로그램(kg)은? ')
pound=int(kg)*2.204623
ounce=int(kg)*35.273962
print('킬로그램\t 파운드\t\t         온스')
print(kg,'\t\t',pound,'\t',ounce )'''

#S2-2.
number11=input('하이픈(-)이 포함된 11자리의 휴대폰 번호는? ')
print('- 입력된 휴대폰 번호 :',number11)
print('- 하이픈 삭제된 휴대폰 번호 :',number11[0:3],number11[4:8],number11[9:13],sep="")
