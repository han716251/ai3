#E4-1
'''for i in range(1,10,1) :
    print(i)'''

#E4-2
'''sum=0
for i in range(3,101,3) :
    sum=sum+i
print('1~100까지의 3의 배수 합계 : %d'%sum)'''

#E4-3
'''for i in range(5,101,5) :
    print(i,end=' ')'''

#E4-4
'''count=0
for i in range(5,101,5) :
    if count%5==0 :
        print()
    print(i,end=' ')
    count=count+1'''

#E4-5
'''sum= 0
for i in range(4,101,4) :
    sum=sum+i
    print('%d --> %d'%(i,sum))'''

#E4-6
'''sum=1
a=10
for i in range(1,1+a,1) :
    sum=sum*i
print('!%d = %d'%(a,sum))'''

#4-7
'''a=1
sum=1

while a<10 :
    a=a+1
    sum = sum*a
print('!%d = %d'%(a,sum))'''

#E4-8
'''print('-'*50)
print('    cm    mm    m    inch')
print('-'*50)
for cm in range(1,51,1) :
    mm = 10*cm
    m = 0.01*cm
    inch = 0.3937*cm
    print('%4.0f %5.0f %7.2f %7.2f'%(cm,mm,m,inch))
    cm = cm+1
print('-'*50)'''

#E4-9
'''print('-'*50)
print('    cm    mm    m    inch')
print('-'*50)
cm=1

while cm <= 50 :
    mm = 10*cm
    m = 0.01*cm
    inch = 0.3937*cm
    print('%4.0f %5.0f %7.2f %7.2f'%(cm,mm,m,inch))
    cm = cm+1
print('-'*50)'''

#S4-1
'''a=1
count=0
while a<=1000 :
    if  a % 3 != 0 :
        print(a,end=' ')
    a=a+1
    count=count+1
    if count %15 == 0 :
        print()'''

#S4-2
'''qy = 'y'

while qy == 'y' :
    score=int(input('성적을 입력하세요 : '))
    if score >= 90 :
        print('등급 : 수')
    elif score >= 80 :
        print('등급 : 우')
    elif score >= 70 :
        print('등급 : 미')
    elif score >= 60 :
        print('등급 : 양')
    else :
        print('등급 : 가')
    qy = input('계속하시겠습니까?(중단:q, 계속:y)')'''

#S4-3 미완성.1
'''start_number = int(input('시작 수를 입력해주세요 : '))
last_number = int(input('끝 수를 입력해주세요 : '))

for i in range(start_number,last_number+1,1) :
    if i > 1 :
        for j in range(2,i+1,1) :
            if i % j == 0 and i==j :
                print(i)'''
    

'''start_number = int(input('시작 수를 입력해주세요 : '))
last_number = int(input('끝 수를 입력해주세요 : '))

for i in range(start_number,last_number+1,1) :
    if i > 1 :
        if i ==2 or i==3 or i==5 or i==7 :
            print(i,end=' ')
        elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
            print(i,end=' ')'''

