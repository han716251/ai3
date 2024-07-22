def hello() :
    print('안녕하세요!')

#1~100까지 합
def usum() :
    sum =0
    for i in range(1,101) :
        sum = sum + i
    print(sum)

def hprint() :
    print('-'*50)

hprint()
usum()
hprint()
usum()
hprint()

def ifsum(number) :
    sum = 0
    for i in range(1,101) :
        if sum > number :
            break
        sum = sum + i
    print('%d이상일떄 항목의 값 : %d, 합계 : %d'%(number,i,sum))

ifsum(3000)


def say_hello(name) :
    print('%s님 안녕하세요!'%name)

say_hello('홍지수')
say_hello('한상준')
say_hello('안지영')
say_hello('황예린')

def asum(num1,num2) :
    sum = 0
    for i in range(num1,num2+1) :
        sum = sum +i
    print('%s 부터 %s 까지의 합 :  %s'%(num1,num2,sum))

asum(1,100)

