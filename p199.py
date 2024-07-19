'''person1=['kim',24,'kim@naver.com']
person2=['lee',35,'lee@hanmail.com']
person=person1 +person2
print(person)

scores=[80,90,85,95,100]
sm=sum(scores)
avg=sm/len(scores)
print('합계 :',sm)
print('평균 :',avg)

data=[10,20,30,40,50,]
data.reverse()
print(data)

fruits=['apple','banana','orange']
print(fruits)

x= fruits.copy()
print(x)

data=[12,8,15,32,-3,-20,15,34,6]
print(data)

data.sort()
print(data)
data.sort(reverse=True)
print(data)

string1='Python is fun!'
print(string1)

x=string1.find('fun')
print(x)

string1='사과는 맛있다. 나는 사과를 제일 좋아한다.'
print(string1)

x=string1.replace('사과', '딸기')
print(x)

string1=['사과는 맛있다. 나는 사과를 제일 좋아한다.']
print(string1)

x=string1[0].replace('사과','딸기')
string1=x
print(string1)

phone1='010-3654-2637'
print(phone1)

phone2=phone1.replace('-','')
print(phone2)

hello='have a nice day'
print(hello)
list1=hello.split(' ')
print(list1)
print(type(list1))
for i in range(0,len(list1)) :
    print('list1[%d] : %s'%(i,list1[i]))

names=['황예린','홍지수','안지영']
print(names)

x=' '.join(names)
print(x)

phone1 =['010','1234','5678']
print(phone1)
phone2='-'.join(phone1)
print(phone2)

phone_list1=['010-3654-2637','010-3984-5377','010-3554-0973']
print(phone_list1)
phone_list2=[]
for number in phone_list1 :
    x=number.replace('-','')
    phone_list2.append(x)
print(phone_list2)

sentences=['Love me, love my dog','No news is good news','Blood is thicker than water']
for sentence in sentences :
    x= sentence.replace(' ','_')
    print(x)

numbers=[[10,20,30],[40,50,60,70,80]]
print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

data=[[10,20],[30,40],[50,60],[70,80]]
for i in range(4) :
    for j in range(2) :
        print('data[%d][%d] = %d' %(i,j,data[i][j]))

scores=[[75,95,83],[86,86,73],[76,95,83],[89,96,69],[89,76,93]]

for i in range(len(scores)) :
    sum = 0
    for j in range(len(scores[i])) :
        sum=sum+scores[i][j]
    
    avg= sum/len(scores[i])
    print('%d번째 학생의 합계 : %d, 평균 : %.2f'%(i+1,sum,avg))

list1='a,b,c,d,e,f'

list2=list1.split(',')
print(list2)

list=[]
list1=['홍길동:100:20','이순신:90:80','최수연:100:75']
for i in list1 :
    list2= i.split(':')
    for j in list2 :
        list.append(j)
print(list)'''

'''list7=[]
list5=['kbs-사장-200,mbc-부장-100','kbs-사원-50,sbs-대리-80']
for i in list5 :    
    list6 = i.split('-')
    for j in list6 :
        list6 = j.split(',') 
        for k in list6 :
            list7.append(k)
print(list7)'''

#데이터를 사이트에서 검색해오기
'''import  requests as req
url = 'http://search.naver.com/search.naver'
rdata = req.get(url,params = {'query' : '백일해 증상'})
print(rdata.text)'''

'''strings = [['원두커피','라떼','콜라'],['우동','국수','피자','파스타']]

for i in range(len(strings)) :
    for j in range(len(strings[i])) :
        print(strings[i][j])'''

