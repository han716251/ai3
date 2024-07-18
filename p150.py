'''word= input('영어문장을 입력하세요 : ')
for x in word :
    print(x,end='')'''

'''
phone=input('하이픈(-)을 포함한 휴대폰 번호를 입력하세요 : ')
for x in phone :
    if x != '-' :
        print('%s'%x, end='')'''

'''print('-'*30)
print('섭씨 화씨')
print('-'*30)
for c in range(-20,31,) :
    f=c*9/+32
    print('%5d %6.1f'%(c,f))
print('-'*30)'''

#break로 멈추기
'''phone='010-6555-2142'
cnt=0

for i in phone :
    if i=='5' :
        print('있어요')
    else :
        print('없어요')
        cnt=cnt+1
        if cnt == 1 :
            break'''

#flag 변수
'''phone='010-6555-2142'
cnt=0
flag=0

for i in phone :
    if i=='5' :
        print('있어요')
        flag=1
if flag == 0:
    print('없어요')
else :
    print('있어요')'''

#영어문장에 'a'가 있나요?
'''word=input('영어단어를 입력하세요 : ')
cnt=0

for i in word :
    if i =='a' :
        cnt=cnt+1
if cnt < 1:
    print('답은 없어요')
else :
    print('답은 %d개 있어요'%cnt)'''

'''word=input('영어단어를 입력하세요 : ')
cnt=0

for i in word :
    if i =='a' :
        cnt=cnt+1
if cnt < 1:
    print('답은 없어요')
else :
    print('답은 %d개 있어요'%cnt)'''

'''word=input('영어단어를 입력하세요 : ')
cnt=0

for i in word :
    if i =='a' :
        cnt=cnt+1
if cnt < 1:
    print('답은 없어요')
else :
    print('답은 %d개 있어요'%cnt)'''

'''for i in range(3) :
    word = input("영어 단어는")
    flag = 0 # 있으면 1로 없으면 0으로 됨 
    cnt = 0 # a의 갯수를 세어주는 변수 
    for i in word :
        if i == 'a' :
            flag=1
            cnt += 1
    if flag == 0 :
        print("a가 없어요")       
    else :
        print("%d개 있습니다"%cnt)'''

#핸드폰 데이터 안에 숫자 말고 다른 문자가 섞여있어서 숫자만 나오게 하기
'''phone=input('입력하세요 : ')

for i in phone :
       if '0' <= i <= '9' : 
               print('%s'%i,end='')'''

phone=input('입력하세요 : ')

for i in phone :
       if not('a' <= i <= 'z' or '0' <= i <= '9' or 'A' <= i <= 'Z') :
              print('%s'%i,end='')