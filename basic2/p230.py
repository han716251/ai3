animals = ('토끼', '거북이', '사자', '여우')
print(animals)
numbers = tuple(range(10))
print(numbers)
print(animals[3])
print(animals[1:])
print(numbers[1:3])

n=tuple(range(10,21))
print(n)
print('n[0]=',n[0])

tup1=(10,20,30)
tup2=(40,50,60)
tup3=tup1+tup2
print(tup3)

s=0
count=0
n2=tuple(range(101))
for i in n2 :
    s= i+s
print(sum(n2))
print(s)
