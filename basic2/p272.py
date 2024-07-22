'''def func(n) :
    x= n+5
    return x
a= func(10)
print(a)
b=func(20)
print(b)'''

'''def inch_to_cm(inch) :
    cm =  inch*2.54
    return cm

num = int(input('인치를 입력하세요 : '))
result = inch_to_cm(num)
print('%d inch => %.2f cm'%(num,result))'''

#C7-5
'''def tri_area(w,h) :
    result = w*h*0.5
    return result

width = int(input('너비를 입력하세요 : '))
height = int(input('높이를 입력하세요 : '))

print('- 삼각형의 넓이 :',width)
print('- 삼각형의 높이 :',height)
print('- 삼각형의 면적',tri_area(width,height))'''

#C7-6
'''def sum_besu(n) :
    sum=0
    for i in range(1,101) :
        if i % n == 0 :
            sum = sum+ i
    return sum

besu = int(input('구하고자 하는 배수를 입력하세요 : '))
total = sum_besu(besu)

print('1~100 사이 %d의 배수의 합계 : %d'%(besu,total))'''

#C7-7
'''def count_space(a) :
    count = 0
    for x in a :
        if x == ' ' :
            count = count + 1
    return count

sentence = 'Python is easy and powerful.'

print(sentence)
num_space = count_space(sentence)
print('- 공백의 개수 :',num_space)'''

#C7-8
def get_item(userid) :
    game_items = {'kim':'총','lee':'대포','choi':'전투기','hwang':'병사'}

    for key in game_items :
        if userid == key :
            item = game_items[key]

    return item

user1 = 'kim'
user2 = 'hwang'

print('%s의 게임 아이템 : %s' %(user1,get_item))
print('%s의 게임 아이템 : %s' %(user2,get_item))


def p(x) :
    a = 1
    b = 0
    cnt=0
    for i in range (x,0,-1) :
        a = a * i
        b += i
        cnt+=1
    list1 = [a,b,cnt]
    return list1

print(p(5))
        