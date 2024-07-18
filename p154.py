#C4-1
'''count = 0
for i in range(200,801) :
    if i % 5 != 0 :
        print('%d'%i,end=' ')
        count=count+1
    if count % 10 == 0 :
        print()'''

#C4-2
'''print('-'*40)
print('      cm     mm     m      inch')
print('-'*40)

for cm in range(1,101) :
    mm= cm * 10.0
    m= cm *0.01
    inch=cm*0.3937
    print('%7.0f %7.0f %7.2f %7.1f'%(cm,mm,m,inch))
print('-'*40)'''

#C4-3
'''for i in range(1,11) :
    print('*'*i)
    print()'''

#C4-4
'''for i in range(10) :
    print('*'*(10-i))
    print()'''

#C4-5
'''number= input('숫자를 입력하세요 : ')

total=0
for a in number :
    a=int(a)
    if a % 2 != 0 :
        total+=1
print('홀수의 개수 : %d 개'%total)'''

#C4-6
'''print('-'*50)
print('%7s %7s %7s'%('킬로그램','파운드','온스'))
print('-'*50)

for kg in range(100,201,2) :
    pound=kg*2.204623
    ounce=kg*35.273962
    print('%7s %8.1f %8.1f'%(kg,pound,ounce))
print('-'*50)'''

