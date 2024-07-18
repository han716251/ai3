'''for x in range(5) :
    print('안녕하세요!')

for x in range(1,11) :
    print(x)

sum=0
for a in range(2,51) :
    sum = sum + a
    print('a의 값 : %d => 합계 : %d'%(a,sum))'''

'''sum = 0
for i in range(1,101,1) :
    sum = sum + i
print('합계 : %d'%sum)'''

#짝수의 합을 구하시오
'''sum=0

for a in range(2,10,2) :
    sum=sum+a
    print('짝수의 합 : %d'%sum)

for i in range(10) :
    print(i, end=' ')
print()

for i in range(1,11) :
    print(i,end=' ')
print()

for i in range(1,10,2) :
    print(i,end=' ')
print()

for i in range(20,0,-2) :
    print(i,end=' ')'''

#149p
'''sum = 0
for i in range(5,101,5) :
    print(i,end=' ')

sum = 0
for i in range(4,201,4) :
    print(i,end=' ')

sum = 0
for i in range(200,-201,-50) :
    print(i,end=' ')'''

'''count=0
for i in range(5,101,5) :
    count=count + 1
    print(i,end=' ')
print()
print('개수 :',count)'''

#20 22 24 26 ~ 50 출력
'''sum=0
count=0
for i in range(20,51,2) :
    print(i,end=' ')
    sum=sum+i
    count=count+1
print()
print('20~50까지의 2개씩 증가 숫자 갯수 : %s'%count)
print('20~50까지의 2개씩 증가 숫자의 합계 : %s'%sum)'''

#100 95 90 ... 0 출력하기
'''sum=0
cnt=0
for i in range(100,-1,-5) :
    print(i,end=' ')
    sum=sum+i
    cnt=cnt+1
print()
print('100~0까지의 5개씩 감소 숫자 갯수 : %s'%sum)
print('100~0까지의 5개씩 감소 숫자 갯수 : %s'%cnt)
print('100~0까지의 5개씩 감소 숫자의 평균 : %.0f'%(sum//cnt))'''

#1~100까지 숫자의 합을 구하되 400이 넘으면 멈추기
'''sum = 0

for i in range(1,101,1) :
    if sum < 400 :
        sum=sum+i
    elif sum >= 400 :
        break
    print('1~100까지 합 : %d'%sum)'''

'''sum = 0

for i in range(1,101,1) :
    if sum >= 400 :
        print('합계가 400넘는 순간 i값 : %d'%i) 
        break
    sum=sum+i
print('1~100까지 합에서 400이 넘는 순간까지 합은 %d'%sum)'''

#200~500까지 3개 증가하는 수를 출력하기 갯수가 20개 일때 멈추기
'''cnt = 0

for i in range(200,500,3) :
    if cnt == 20 :
        break
    cnt=cnt+1
print('갯수 : %d'%cnt)'''

#1~500까지 5의 배수를 출력하기
#합계가 1000이상이거나 갯수가 30개 이상이면 멈추기
sum=0
cnt=0

for i in range(5,501,5) :
    if cnt == 30 or sum >= 1000 :
        break
    cnt=cnt+1
    sum=sum+i
print(sum)
print(cnt)