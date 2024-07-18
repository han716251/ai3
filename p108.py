#3또는 4의 배수 판별하기
'''num=int(input('양의 정수를 입력하세요'))
result='3의 배수도 4의 배수도 아니다'
if num%3==0 and num%4==0 :
    print('3의 배수이면서 4의 배수이다.')
elif num%3==0 :
    print('3의 배수이다.')
elif num%4==0 :
    print('4의 배수이다.')
else :
    print(result)'''

#짝수이고 4의 배수인 숫자이면 "행운의 수"
'''num=int(input('숫자를 입력하세요 : '))
if num%2==0 or num%4==0 :
    print('행운의 수')
else :
    print(num)'''

#영어 퀴즈 1
'''ans1= input("'사자'의 영어 단어는 무엇일까요? : ")
if ans1== "lion" :
    print('정답입니다!')
else :
    print('오답입니다. 다시 생각해보세요')'''

'''ans1= input("'사자'의 영어 단어는 무엇일까요? : ")
result1= '정답입니다!'
result2= '오답입니다. 다시 생각해보세요!'
if ans1== "lion" :
    print(result1)
else :
    print(result2)'''

#영어 퀴즈 2
'''ans2= input("'오렌지'의 영어 단어는 무엇일까요?")
if ans2 == 'orange' :
    print('정답입니다!')
else :
    print('오답입니다. 다시 생각해보세요!')'''

#영어 퀴즈 3
'''ans3= input("'기차'의 영어 단어는 무엇일까요?")
if ans3 == 'train' :
    print('정답입니다!')
else :
    print('오답입니다. 다시 생각해보세요!')'''

#C3-1
'''start=int(input('시작 수는? '))
end=int(input('끝 수는? '))
num=int(input('정수를 입력하세요 : '))

result='%d은(는) %d~%d 사이에 없다.'%(num,start,end)

if num <= end and num >= start :
    result = '%d은(는) %d~%d 사이에 있다.'%(num,start,end)

print(result)'''

#C3-2
'''month= input('월을 숫자로 입력하세요 : ')

if month == '3' or month == '4' or month == '5' :
    print('%s월은 봄입니다.'%month)
if month == '6' or month == '7' or month == '8' :
    print('%s월은 여름입니다.'%month)
if month == '9' or month == '10' or month == '11' :
    print('%s월은 가을입니다.'%month)
if month == '12' or month == '1' or month == '2' :
    print('%s월은 겨울입니다.'%month)'''

#C3-3
'''a=input('주민번호 뒷자리 첫번째 숫자를 입력해 주세요 : ')

if a=='1' or a=='3' :
    print('남성입니다!')
if a=='2' or a=='4' :
    print('여성입니다!')
else :
    print('입력이 잘못되었습니다!')'''
