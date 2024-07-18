year=2024
month=7
day=12
print(year,month,day)
print(year,month,day,sep="/")
a='010'
b='6555'
c='2142'
print(a,b,c,sep="-")

price=1000
print(price,'원')
print(price,'원',sep='')

print('안녕하세요\n반갑습니다')
print('안녕하세요\t반갑습니다')
print('\\')
print('\'')
print('\'안녕\'')
print('\"안녕\"')

#퀴즈
phone1='010'
phone2='1234'
phone3='5678'
print(phone1,phone2,phone3,sep='-')

kor=input("국어성적을 입력하세요")
eng=input("영어성적을 입력하세요")
math=input("수학성적을 입력하세요")
sum= int(kor)+int(eng)+int(math)
avg=sum/3
print('합계: %d, 평균: %.2f' %(sum,avg))