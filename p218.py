#C5-5
'''questions = ['s_holl','compu_er','deco_ation','windo_','hi_tory']
answers = ['c','t','r','w','s']
for i in range(len(questions)) :
    q = '%s : 밑줄에 들어갈 알파벳은?' %questions[i]
    guess = input(q)

    if guess == answers[i] :
        print('정답!')
    else :
        print('틀렸어요!')'''

#C5-6
'''scores=[]

while True :
    x=int(input('성적을 입력하세요(종료 시 -1 입력) : '))

    if x== -1 :
        break
    else :
        scores.append(x)

sum =0
for score in scores :
    sum= sum+score

avg= sum/len(scores) 
print('합계 : %d, 평균 : %.2f'%(sum,avg))'''

#C5-7
'''s= [61,89,100,85,77,58,79,67,96,87,87,36,82,98,84,76,63,69,53,22]
soo = 0
woo=0
mi=0
yang=0
ga=0

i=0
while i < len(s) :
    if 90 <= s[i] <= 100 :
        soo = soo +1
    if 80 <= s[i] < 90 :
        woo = woo +1
    if 70 <= s[i] < 80 :
        mi=mi+1
    if 60 <= s[i] < 70 :
        yang=yang+1
    if 0 <= s[i] < 59 :
        ga = ga+1
    i=i+1

print('수 : %d명'%soo)
print('우 : %d명'%woo)
print('미 : %d명'%mi)
print('양 : %d명'%yang)
print('가 : %d명'%ga)'''

#C5-8
'''seats= [[0,0,0,0,0,0,0,0,0,0],\
     [0,0,0,0,0,0,0,0,0,0],\
     [0,0,0,0,0,0,0,0,0,0],\
     [1,1,1,0,0,0,0,0,1,0],\
     [0,0,0,0,0,1,0,0,0,0],\
     [0,1,0,0,0,1,0,1,0,0],\
     [0,0,0,0,0,0,1,0,0,0],\
     [1,0,1,0,0,0,0,0,0,1]]
for i in range(len(seats)) :
    for j in range(len(seats[i])) :
        if seats[i][j] == 0 :
            print('%3s' % '□',end='')
        else :
            print('%3s' % '■',end='')
    print()'''

#E5-1~E5-4
'''my_list = ['p','y','t','h','o','n','i','s','f','u','n','!']

print(my_list[5:11])
print(my_list[-5,-2])
print(my_list[8:])
print(my_list[:4])'''

#E5-5
'''sentence = 'I am a genius!'
a=[]
for i in sentence :
    a.append(i)
print(a)'''

#E5-6
'''sentence = 'I am a genius!'
a=[]
i=0

while i < len(sentence) :
    a.append(sentence[i])
    i=i+1
print(a)'''

#E5-7
'''numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
for i in range(len(numbers)) :
    sum = sum + numbers[i]
print('합계 : %d'%sum)'''

#E5-8
'''numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i=0
while i < len(numbers) :
    sum = sum + numbers[i]
    i=i+1
print('합계 : %d'%sum)'''

#E5-9
numbers=[7,9,15,18,30,-3,7,12,-16,-12]
sum=0
i = 0
a=[]
while i < len(numbers) :
    if i+1 % 2 == 0 :
        sum = sum + numbers[i]
        i = i +1
        a.append(numbers[i])
print('짝수 번째 요소 :',a)
print('합계 : %d'%sum)

