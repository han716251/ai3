'''member={'name':'황예린','age':22,'email':'yerin@hanmail.net'}
print(member)
print(member['name'])
print(member['age'])
print(member['email'])
score = dict([('국어',80),('영어',90),('수학',100)])
print(score['국어'])
print(score)
print(score['수학'])
score2 = dict([('국어',80),('영어',90),('수학',100)])
print(score2['수학'])
score2['국어']=90
print(score2['국어'])'''

#C6-1
'''dans=(2,3,4,5,6,7,8,9)

print('구구단표')
print('='*30)

for dan in range(2,10) :
    print(str(dan) + '단')
    for i in range(1,10) :
        print('%d x %d = %d'%(dan,i,dan*i))
    print('-'* 30)'''

#C6-2
'''scores = {'김채린':85,'박수정':98,'함소희':94,'안예린':90,'연수진':93}
sum=0
for key in scores :
    sum = sum + int(scores[key])
    print('%s : %d'%(key,scores[key]))
avg = sum / len(scores)

print('합계 : %d, 평균 : %.2f'%(sum,avg))'''

#C6-3
'''admin_info = {'id':'admin','password':'12345'}

input_id=input('아이디를 입력하세요 : ')
input_pass=input('비밀번호를 입력하세요 : ')

if input_id == admin_info['id'] and input_pass == admin_info['password'] :
    print('정보의 권한이 있습니다!')
else :
    print('정보의 권한이 없습니다!')'''

#C6-4
'''words ={'꽃':'flower','나비':'butterfly','학교':'school','자동차':'car','비행기':'airplane'}
print('<영어 단어 맞추기 퀴즈>')
for kor in words :
    input_word = input("'%s'에 해당되는 영어 단어를 입력해주세요: "%kor)

    if input_word == words[kor] :
        print('정답입니다!')
    else :
        print('틀렸습니다!')'''

#E6-1
'''year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
for key in year_sale :
    if key == '2017' :
        print('%s년 자동차 판매량 : %d대'%(key,year_sale['2017']))'''

#E6-2
'''year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
sm=0
for key in year_sale :
    if key =='2018' or key == '2019' :
        print('%s년 자동차 판매량 : %d'%(key,year_sale[key]))
        sm = sm + year_sale[key]
print('2년간 자동차 판매량 : %d대'%sm)'''

#E6-3
'''year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}
sm =0
for key in year_sale :
    sm = sm + year_sale[key]
avg = sm/len(year_sale)

print('5년간 총 판매량 : %d' %sm)
print('5년간 연 평평균 판매량 : %d' %avg)'''

#E6-4
'''year_sale = {'2016':237,'2017':98,'2018':158,'2019':233,'2020':120}

big_year = 2016
biggest = year_sale['2016']
for key in year_sale :
    if year_sale[key] > biggest :
        big_year = key
        biggest = year_sale[key]
print('판매량이 가장 많은 해 : %s년' %big_year)
print('판매량 : %d대'%biggest)'''

#E6-5~E6-6
'''person = {'name':'홍길동','age':30,'family':5,'children':['선미','성진','소영'],'pets':['강아지','고양이','이구아나'] }
print(person['age'])
print(len(person))'''

#E6-7
'''person = {'name':'홍길동','age':30,'family':5,'children':['선미','성진','소영'],'pets':['강아지','고양이','이구아나'] }

for key in person :
    if key =='pets' :
        for name in person[key] :
            print(name,end='/')'''
#6-8
'''person = {'name':'홍길동','age':30,'family':5,'children':['선미','성진','소영'],'pets':['강아지','고양이','이구아나'] }
for key in person :
    if key =='children' :
        print('자녀수 : %d'%(len(person[key])))'''

#S6-1
'''temp = {'월':15.5,'화':17.0,'수':16.2,'목':12.9,'금':11.0,'토':10.5,'일':13.3}
print('-'*50)
print(' 월   화   수   목   금   토   일')
print('-'*50)
for key in temp :
    print(temp[key],end=' ')
print()
print('-'*50)'''

#S6-2
'''temp = {'월':15.5,'화':17.0,'수':16.2,'목':12.9,'금':11.0,'토':10.5,'일':13.3}
low_temp = '월'
lowst = 15.5

for key in temp :
    if lowst > temp[key] :
        low_temp = key
        lowst = temp[key]
print('요일 : %s, 최저기온:%.1f'%(low_temp,lowst))'''

#S6-3
'''temp = {'월':15.5,'화':17.0,'수':16.2,'목':12.9,'금':11.0,'토':10.5,'일':13.3}
sum = 0
for key in temp :
    sum = sum + temp[key]
avg = sum / len(temp)
print('일주일간 기온 평균 : %.1f'%avg)'''