#성적 관리 시스템
name = []
menu=1
kor = []
eng = []
math = []

while menu != 5 :
    print('-'*50)
    print('성적관리 프로그램')
    print('-'*50)
    print()
    print('1. 학생 이름 삽입하기')
    print('2. 성적 입력하기')
    print('3. 통계자료 보기')
    print('4. 학생 자료 삭제하기')
    print('5. 프로그램 종료하기 ')
    print()
    menu = int(input('===> 메뉴를 선택하세요(1/2/3/4/5) '))
    if menu == 1 :
        print()
        print('1. 학생 이름 삽입하기')
        newname = input('이름 : ')
        name.append(newname)
        print()

    elif menu == 2 :
        print()
        print('2. 성적 입력하기')
        k = int(input('국어 점수 : '))
        e = int(input('영어 점수 : '))
        m = int(input('수학 점수 : '))
        kor.append(k)
        eng.append(e)
        math.append(m)
        print()

    elif menu == 3 :
        print('3. 통계자료 보기')
        print('1) 반 전체 통계')
        print('2) 학생 통계')
        menu1=int(input('메뉴를 선택하세요(1/2/3) '))
        
        if menu1 == 1 :
            print()
            print(' 이름   국어   영어   수학')
            for i in range(0,len(name)) :
                print('%s  %d  %d  %d'%(name[i],kor[i],eng[i],math[i]))
            print()

        elif menu1 == 2 :
            print()
            print('-'*30)
            name1=input('학생이름을 입력하세요')
            print(' 이름   국어   영어   수학')
            try :
                inx = name.index(name1)
                print('%s  %d  %d  %d'%(name[inx],kor[inx],eng[inx],math[inx]))
            except ValueError :
                print('%s은(는) 우리반 학생이 아닙니다.'%name1)
            print('-'*30)

    elif menu == 4 :
        print('학생 자료 삭제하기')
        print()
        name2=input('지우려고 하는 학생이름을 입력하세요.')
        try :
            ninx = name.index(name2)
            name.pop(ninx)
            kor.pop(ninx)
            eng.pop(ninx)
            math.pop(ninx)
            print('%s의 학생 자료를 삭제하였습니다.'%name2)
        except ValueError :
            print('%d은(는) 우리반 학생이 아닙니다.'%name2)
        print()

    elif menu == 5 : 
        print()
        print('프로그램을 종료합니다.')
    
    else :
        print('오류! 입력이 잘못되었습니다!')
        print('1/2/3/4/5 중 하나를 입력해주세요!')
        

#정책
# 1. 입력할 때 이름을 한번 치고 성적을 3개 입력한다.




#3-2 완
'''elif menu1 == '2' :
            sname=input("점수를 알고 싶은 학생이름은?")  
            okname = -999
            for i in range( len(name ) ) :
                    if sname == name[i] :
                        okname = i
                        break
            if okname == -999 :
                print("%s는 우리반 학생 아닙니다."%sname)  
            else :
                print("%s   %d   %d   %d"%( name[okname], kor[okname], eng[okname], math[okname] ))'''