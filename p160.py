#구구단
'''a=2
for b in range(1,10) :
    print('%d x %d = %d'%(a,b,a*b))'''

'''print('-'*30)
for a in range(2,10) :
    for b in range(1,10) :
        print('%d x %d = %d'%(a,b,a*b))
    print()'''

#구구단 ver.2
'''cnt =0
for a in range(2,10) :
    for b in range(1,10) :
        print('%3d x %3d = %3d'%(a,b,a*b),end=' ')
        cnt = cnt+1
        if cnt % 9 == 0 :
            print()'''

#구구단 ver.3
'''cnt =0
for a in range(1,10) :
    for b in range(2,10) :
        print('%3d x %3d = %3d'%(b,a,a*b),end=' ')
        cnt = cnt+1
        if cnt % 8 == 0 :
            print()'''

#C4-7
'''for i in range(5) :
    for j in range(10) :
        print('*',end=' ')
    print()'''

#C4-8
''' for i in range(9,0,-1) :
    for j in range(i,0,-1) :
        print(i,end=' ')
    print()'''

'''for i in range(5) :
    for j in range(1,6,1) :
        print(j,end=' ')
    print()'''

'''for i in range(5) :
    for j in range(i+1,i+6,1) :
        print(j,end=' ')
    print()'''

'''for i in range(5) :
    for j in range(1,6-i,1) :
        print(j,end=' ')
    print()'''