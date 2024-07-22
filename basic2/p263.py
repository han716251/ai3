def average(*args) :
    num_args = len(args)
    sum = 0
    for i in range(num_args) :
        sum = sum + args[i]

    avg = sum/num_args
    print('%d과목 평균 : %.1f'%(num_args,avg))

average(85,96,87)
average(77,93,85,97,72)

'''def func(food) :
    for x in food :
        print(x,end=' ')

fruits = ['사과','배', '오렌지', '바나나']
numbers = (1,2,3,4,5)

func(fruits)
func(numbers)'''

def func(food) : 
    food.append('딸기')
    food.append('수박')

fruits = ['사과','오렌지','바나나']

print(fruits)
func(fruits)
print(fruits)

