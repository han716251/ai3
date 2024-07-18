# 짝수 홀수 판별하기
'''x=int(input('양의 정수를 입력하세요 : '))
if x%2 :
    print('짝수입니다.')
else :
    print('홀수입니다.')'''

#합격 불합격 판별하기
'''pilgi=int(input('필기시험 점수를 입력하세요 : '))
silgi=int(input('실기시험 점수를 입력하세요 : '))
if pilgi >= 80 and silgi >= 80 :
    result='합격'
else :
    result='불합격'
print('- 필기시험 점수 : %d'%pilgi)
print('- 실기시험 점수 : %d'%silgi)
print('- 판정 : %s'%result)'''

#영어 소문자 자음 모음 판별하기
'''char = input('영문 하나를 입력하세요 : ')
if char == 'a'  or char == 'e'  or char == 'o'  or char == 'i'  or char == 'u' :
    print('%s는 모음이다.'%char)
else :
    print('%s는 자음이다.'%char)'''

#C3-4
'''char = input('영문 하나를 입력하세요 : ')
if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'o' or char == 'O' or char == 'i' or char == 'I' or char == 'u' or char == 'U' :
    print('%s는 모음이다.'%char)
else :
    print('%s는 자음이다.'%char)'''

#C3-5
'''height=int(input('키는? '))
weight=int(input('몸무게는? '))

s=(height-100)*0.9

print('='*50)
print('키 :',height)
print('몸무게 :',weight)

if weight > s :
    print('건강을 위해 다이어트가 필요합니다!')
else :
    print('표준 또는 마른 체형입니다!')'''

#C3-6
print('아르바이트 급여 계산 프로그램')
print('※ 시급')
print('- 주간 근무 : 9,500원')
print('- 야간 근무 : 주간시급 * 1.5')

a= int(input('1(주간 근무) 또는 2(야간 근무)을 입력해주세요 : '))
time = int(input('근무 시간을 입력해주세요 : '))

if a==1 :
    print('%d시간 동안 일한 주간 급여는 %d원 입니다.'%(time,time*9500))
else :
    print('%d시간 동안 일한 주간 급여는 %d원 입니다.'%(time,time*9500*1.5))

