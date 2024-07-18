'''sum=0
i=1
while i <=10 :
    sum=sum+i
    print('i의 값 : %2d => 합계 : %d'%(i,sum))
    i=i+1
print('합계는 : %d'%(sum))'''

#500~600까지의 정수 중 5의 배수 합게를 구하는 프로그램
'''sum=0
i=500
while i<=600 :
    if i % 5 ==0 :
        sum=sum+i
print('5의 배수 합계 : %d'%(sum))'''

'''for i in range(1,1001) :
    print(i)
    if i == 10 :
        break'''

#1~1000까지 정수 중 100의 배수를제외하고 합계를 구하기
'''sum=0
i=1

while i<=1000 :
    if i%100 != 0 :
        sum=sum+i
    i=i+1
print('합계 : %d'%sum)'''

#영어 모음 개수 구하기
'''s='Python is widely used by a number of big companies'
i=0
count=0
print('모음 : ', end='')

while i <=len(s) -1 :
    if( s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or  s[i]=='O' or s[i]=='u' or s[i]=='U') :
        count=count+1
        print(s[i],end=' ')
    i=i+1
print()
print('모음 개수 : %d'%count)'''

# 자음만 
'''s="Python is widely used by a number of big companies"
i=0
count=0
print("자음 :", end=" ")

while i <= len(s)-1 : 
    if( s[i] != " " and not( s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or  s[i]=='O' or s[i]=='u' or s[i]=='U') ):
       count = count + 1
       print(s[i], end=" ")
    i = i + 1
print()
print("자음 갯수 : %d"%count) '''

#숫자 두개 입력 받아서 덧셈하기
'''yn='y'
while yn=='Y' or yn=='y' :
    num1=int(input('첫 번째 숫자를 입력하세요 : '))
    num2=int(input('두 번째 숫자를 입력하세요 : '))
    sum=num1+num2
    print('합계 : %d'%sum)
    yn = input('계속하시겠습니까? : Y(계속) or N(그만)')'''

#문자열을 2개 입력 받아서 합치기 #미완성
'''text1=input('첫번째 문자를 입력하세요 : ')
text2=input('두번째 문자를 입력하세요 : ')
i=0
while i <= len(text2) -1 :
    while i <= len(text1) -1 :
        print(text1[i],end=' ')
        print(text2[i],end=' ')
        i=i+1'''

# 문자열을 2개 입력 받아서 합치기
# 예 문자1 : Hello
#    문자2 : Love
# 출력 결과 : H L e o l v l e o
# 계속 하시겠습니까?(y/n)
# 전체 반복횟수 = 문자1의 길이(5글자) + 문자2의 길이(4글자)
'''yN = "y"
while( yN=="y" ) :
    w=input("문자1 : " )
    s=input("문자2 : ")
    ws = ""
    for i in range( len(w) + len(s)) : # 0, 1, 2, .... 8
        if i <= len(w)-1 : # i<=4 0, 1, 2, 3, 4
           ws = ws + w[i]
        if i <= len(s)-1 : # i<=3 0, 1, 2, 3 
           ws = ws + s[i]
    print(ws)
    yN = input("계속하실래요?(y/n)")'''

'''while True :
    w=input("문자1 : " )
    s=input("문자2 : ")
    ws = ""
    for i in range( len(w) + len(s)) : # 0, 1, 2, .... 8
        if i <= len(w)-1 : # i<=4 0, 1, 2, 3, 4
           ws = ws + w[i]
        if i <= len(s)-1 : # i<=3 0, 1, 2, 3 
           ws = ws + s[i]
    print(ws)
    yN = input("계속하실래요?(y/n)")
    if yN =='n' :
        break'''
#C4-9
'''n=1
sum=0
count=0

while n <=100 :
    if n % 2 == 1 :
        sum = sum+n
        print('%6d'%sum,end=' ')
        count=count+1

        if count % 10 == 0 :
            print()
    n= n+1'''

#C4-10
'''print('-'*30)
print('    달러    원화    유로')
print('-'*30)

dollar=10

while dollar <= 100 :
    won = dollar*1080
    euro = dollar*0.81
    print('%7d%8.0f%7.1f'%(dollar,won,euro))
    dollar=dollar+10
print('-'*30)'''

#C4-11
'''sentence=input('문장을 입력해주세요 : ')

i=len(sentence)-1

while i>=0 :
    if sentence[i] == '':
        print('-',end='')
    else :
        print('%s'%sentence[i],end='')
    i=i-1'''

#100이면 빠지기
#100이면 찍지 않고 건너뛰기(반복문 계속) 101 찍기
print('-'*183)
for i in range(1,201,1) :
    if i!=100 :
        print(i,end=' ')

for i in range(1,201,1) :
    if i == 100 :
        continue
    print(i,end=' ')
print()
print('-'*183)

#while문
i=0
while i<200 :
    i=i+1
    if i == 100 :
        continue
    print(i,end=' ')