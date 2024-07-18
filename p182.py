#리스트 수정
'''flowers=['목련', '벚꽃', '장미', '백일홍']
print(flowers)
flowers[1] = '무궁화'
print(flowers)'''

#리스트 추가
'''arr = [5,3,12.9,2]
print(arr)

arr.append(10)
print(arr)'''

#빈 리스트에 요소 추가
'''scores = []

while True :
    score = int(input('성적을 입력하세요(종료 : -1) : '))

    if score == -1 :
        break
    else :
        scores.append(score)
print(scores)'''

#insert() 메소드로 요소 삽입하기
'''fruits = ['apple', 'orange', 'banana', 'cherry']
print(fruits)

fruits.insert(1, 'mellon')
print(fruits)

fruits.insert(1, 'strawberry')
print(fruits)'''

#index()메소드로 요소 인덱스구하기
'''number = [5,20,13,7,8,22,7,17]
print(number)

idx = number.index(7)
print(idx)'''

#remove()메소드로 리스트 요소 지우기
'''member = ['홍지웅',20,'경기도 김포시', 'jiwoong@naver.com', '010-1234-5678']
print(member)

member.remove(20)
print(member)'''

#
'''list1=[3,15,-12.5,'사과','딸기', True, False]
list2=[list(range(1,21,2))]
print(list1)
print(list2)
for i in range(7) :
    print(list1[6-i],end=' ')
print()
print('-'*50)
print(list2[: :2])
print(list2[-1: :-2])'''

#
'''for i in range(100,201,10) :
    list3=[i]
    print(list3,end=' ')
print()
list4= list(range(100,201,10))
print(list4)'''

#갯수 구하기
'''list4= list(range(100,201,10))
print(list4)

cnt=0
for i in list4 :
    cnt+=1
print('리스트의 갯수는 %d개 입니다.'%cnt)

print(len(list4))'''

#합계 구하기
'''list4= list(range(100,201,10))
print(list4)

sum=0
for i in list4 :
    sum=sum+i
print('리스트의 합계는 %d 입니다.'%sum)'''

#pop()메소드로 리스트 요소 삭제
'''data=[10,20,30,40,50,60,70,80]
print(data)

x= data.pop(2)
print(x)
print(data)

x=data.pop(3)
print(x)
print(data)'''

#모든 리스트 요소 삭제하기 clear
'''data=[3,12,7,-3,9]
print(data)

data.clear()
print(data)'''

'''list1=['홍길동', 100, 80, 180, 90]
list2=['이순신', 90, 75, 165, 82.5]
list3=['최경미', 75, 100, 175, 87.5]
print(' 이름    국어점수   수학점수   합계   평균')
for i in range(0,len(list1)) :
    print('%s'%list1[i],end='       ')
print()
for a in range(0,len(list2)) :
    print('%s'%list2[a],end='       ')
print()
for b in range(0,len(list2)) :
    print('%s'%list2[b],end='       ')'''

'''list1=['홍길동', 100, 80]
list2=['이순신', 90, 75]
list3=['최경미', 75, 100]
print(' 이름    국어점수   수학점수   합계   평균')
print(list1[0],'   ',list1[1],'   ', list1[2],'   ',(list1[1]+list1[2]),'   ',((list1[1]+list1[2])/2))
print(list2[0],'   ',list2[1],'   ', list2[2],'   ',(list2[1]+list2[2]),'   ',((list2[1]+list2[2])/2))
print(list3[0],'   ',list3[1],'   ', list3[2],'   ',(list3[1]+list3[2]),'   ',((list3[1]+list3[2])/2))

print('우리반 이름 : %s, %s, %s'%(list1[0],list2[0],list3[0]))
print('우리반 국어점수 합계 : %d'%(list1[1]+list2[1]+list3[1]))
print('우리반 수학점수 합계 : %d'%(list1[2]+list2[2]+list3[2]))

if list1[1] > list2[1] and list1[1] > list3[1] :
    print('우리반에서 국어점수가 가장 높은 사람의 이름은? %s'%list1[0])
elif list2[1] > list1[1] and list2[1] > list3[1] :
    print('우리반에서 국어점수가 가장 높은 사람의 이름은? %s'%list2[0])
elif list3[1] > list2[1] and list3[1] > list1[1] :
    print('우리반에서 국어점수가 가장 높은 사람의 이름은? %s'%list3[0])

name=input('찾고 싶은 사람은? ')
if name == list1[0] or name == list2[0] or name == list3[0] :
    print('우리반에 %s이(가) 있어요.'%name)
else :
    print('우리반에는 %s이(가) 없어요.'%name)'''

