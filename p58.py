s="안녕하세요. 반갑습니다"
print(s[0])
print(s[1])
print(s[3:10])
print(s[2:10])
print(s[0:2])
print(s[0]+s[1])
print(s[0],s[1])
print(s[6:10])
string="쥐 구멍에 볕들 날 있다."
print(string[2:8])
animal="tiger"
print(animal[0:2])

jumin="991013-3012456"
#99년 10월 13일
print(jumin[0:2]+"년 "+jumin[2:4]+"월 "+jumin[4:6]+"일")
sex=jumin[7]
print(sex)
#1,3인 경우 남자 출력 2,4인 경우 여자 출력
if sex=='1' or sex=='3' : 
    print('남자')
else :
    print('여자') 
#주민번호 마지막 부분에 짝수이면 O, 홀수이면 X
last_jumin=(jumin[13])
if int(last_jumin)%2==0 :
    print('O')
else :
    print('X')

last_jumin=int(jumin[13])
if last_jumin%2==0 :
    print('O')
else :
    print('X')

last_jumin=int(jumin[-1])%2
if last_jumin==0 :
    print('O')
else :
    print('X')

end=jumin[-1]
print(end)
endInt=int(end)
if endInt%2 == 0 :
    print('O')
else :
    print('X')
