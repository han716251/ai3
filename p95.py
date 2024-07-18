# 키보드로 이름을 입력 받아 보세요
'''name = input('이름은? ')
print('입력한 이름은 %s 입니다' %name)'''

#키보드로 포인트 점수를 입력 받아 보세요
'''point=int(input('포인트 점수는? '))
print('입력한 포인트 점수는 %d점 입니다.' %point)'''

#포인트 점수의 20%는 600점 입니다
'''point=int(input('포인트 점수는? '))
print('입력한 포인트 점수의 20%', '는 %.2f점 입니다.' %(point*0.2), sep='')'''

#당신의 주소는? 강동구
'''address=input('당신의 주소는? ')
number=int(input('몇번 반복 하겠습니까? '))
print(address*number)'''

#당신의 주소는? 강동구 천호동 : ~글자입니다.
address=input('당신의 주소는?(띄어쓰기 미포함) : ')
print('당신의 주소의 글자는 %s 글자입니다.'%(len(address)))