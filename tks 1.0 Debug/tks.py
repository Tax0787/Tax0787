print('prints 정의 시작')
def prints(strs,time = 0.0625,print_for_new_line = True,dibug = False):
    if dibug: print('prints 호출 성공')
    if dibug: print('time 모듈의 sleep 를 s 로 가져오기 시작')
    from time import sleep as s
    if dibug: print('time 모듈의 sleep 를 s 로 가져오기 성공')
    if dibug: print('strs 삽입 시작')
    if dibug: print('strs : {}, strs 가 n 줄일때 n 만큼 나눠서 i개로 나누기 시작'.format(strs))
    if dibug: print('strs 삽입 성공')
    for i in strs:
        if dibug: print('strs 삽입 시작')
        if dibug: print('strs : {}, strs 가 n 줄일때 n 만큼 나눠서 i개로 나누기 성공'.format(strs))
        if dibug: print('strs 삽입 성공')
        if dibug: print('i 삽입 시작')
        if dibug: print('i : {}, i 가 n 글자일때 n 만큼 나눠서 j개로 나누기 시작'.format(i))
        if dibug: print('i 삽입 성공')
        for j in i:
            if dibug: print('i 삽입 시작')
            if dibug: print('i : {}, i 가 n 글자일때 n 만큼 나눠서 j개로 나누기 성공'.format(i))
            if dibug: print('i 삽입 성공')
            if dibug: print('i 삽입 시작')
            if dibug: print('j : {}, j 를 출력하고 끝에 개행문자 삭제 시작'.format(j))
            if dibug: print('i 삽입 성공')
            print(j, end = '')
            if dibug: print('i 삽입 시작')
            if dibug: print('j : {}, j 를 출력하고 끝에 개행문자 삭제 성공'.format(j))
            if dibug: print('i 삽입 성공')
            if dibug: print('time 삽입 시작')
            if dibug: print('{} : time, time 만큼 쉬기 시작'.format(str(time)))
            if dibug: print('time 삽입 성공')
            s(time)
            if dibug: print('time 삽입 시작')
            if dibug: print('{} : time, time 만큼 쉬기 성공'.format(str(time)))
            if dibug: print('time 삽입 성공')
        if dibug: print('if print_for_new_line: print() 시작')
        if print_for_new_line: print()
        if dibug: print('if print_for_new_line: print() 성공')
print('prints로 쓰기 시도')
prints('prints 정의 성공, 그래서 지금 prints로 씀', dibug = True)
print('prints로 쓰기 성공')
def helper():
    def inputs(strs,prints = prints,time = 0.0625,print_for_new_line = False,dibug = False):
        prints(strs,time = time,print_for_new_line = print_for_new_line,dibug = dibug)
        return input("")
    abcde = inputs("오류 해결 도우미를 키시겠습니까?(응 or 아니): >>> ")
    if abcde == "응":
        abcd = inputs("몇번 물어보시겠습니까?(숫자만): >>> ")
        for i in range(1, int(abcd) + 1):
            abcdef = inputs( str(i) + "번째 도움말은 무었입니까?: >>> ")
            prints("다음을 열린 웹사이트에서 변역하세요! , 도움말 : " + str(help(abcdef)))
            import webbrowser
            webbrowser.open("https://papago.naver.com")
        prints("./종료합니다./")
    else:
        prints("./종료합니다./")
print('prints로 format 포함으로 쓰기 시도 ( 하하와, 하하가 쓰였는지 알기 ) ')
prints('하하 를 쓰기 : {}, 성공? : {}'.format('하하',str('하하' == '하하')), dibug = True)
print('prints로 format 포함으로 쓰기 성공 ( 하하와, 하하가 쓰였는지 알기 ) ')
prints('Tks 리스트를 빈걸로 정의 시작')
tks = []
prints('Tks 리스트를 빈걸로 정의 성공')
prints('nom = -1로 정의 시작')
nom = -1 
prints('nom = -1로 정의 성공')
prints('Tks 정의 시작')
class Tks:
    prints('__init__ 정의 시작')
    def __init__(self,name,title,geometry,prints):
        prints('Tks 호출 성공, tks __init__ 호출 성공')
        prints('tks 리스트 가져오기 시작')
        global tks
        prints('tks 리스트 가져오기 성공')
        prints('nom 가져오기 시작')
        global nom
        prints('nom 가져오기 성공')
        prints('nom += 1 시작')
        nom += 1
        prints('nom += 1 성공')
        prints('메모리 코드 출력 시작')
        if prints: print(str(nom) + "is this Tks object's Memory code.")
        prints('메모리 코드 출력 성공')
        prints('Tks 리스트에 입력된 정보 입력 시작')
        tks.append({'name' : name, 'title' : '\'' +  title + '\'' , 'geometry' : '\'' + geometry + '\''})
        prints('Tks 리스트에 입력된 정보 입력 성공')
    prints('__init__ 정의 성공')
    prints('클래스 메소드 wiget 정의 시작')
    @classmethod
    def wiget(cls,name,command,option,memory_code):
        prints('wiget 호출 성공')
        prints('tks 리스트 가져오기 시작')
        global tks
        prints('tks 리스트 가져오기 성공')
        prints('tks 리스트 의 메모리 코드번재 항목, 즉 객체 대이터를 objects 로 지정 시작')
        objects = tks[memory_code]
        prints('tks 리스트 의 메모리 코드번재 항목, 즉 객체 대이터를 objects 로 지정 성공')
        prints('return "{} = {}({}{})\\n{}.pack()\\n".format(name,command,objects[\'name\'],option,name) 실행 시작')
        return "{} = {}({}{})\n{}.pack()\n".format(name,command,objects['name'],option,name)
    prints('클래스 메소드 wiget 정의 성공')
    prints('클래스 메소드 sose 정의 시작')
    @classmethod
    def sose(cls,option,wiget,sose,memory_code):
        prints('sose 호출 성공')
        prints('tks 리스트 가져오기 시작')
        global tks
        prints('tks 리스트 가져오기 성공')
        prints('tks 리스트 의 메모리 코드번재 항목, 즉 객체 대이터를 objects 로 지정 시작')
        objects = tks[memory_code]
        prints('tks 리스트 의 메모리 코드번재 항목, 즉 객체 대이터를 objects 로 지정 성공')
        prints('''return ''\'try:
    from Tkinter import *
except:
    from tkinter import *
{} = Tk()
{}.title({})
{}.geometry({})
{}
{}
{}
{}.mainloop()''\'.format(objects['name'],objects['name'],objects['title'],objects['name'],objects['geometry'],option,wiget,sose,objects['name']))
실행''')
        return '''try:
    from Tkinter import *
except:
    from tkinter import *
{} = Tk()
{}.title({})
{}.geometry({})
{}
{}
{}
{}.mainloop()'''.format(objects['name'],objects['name'],objects['title'],objects['name'],objects['geometry'],option,wiget,sose,objects['name'])
    prints('클래스 메소드 sose 정의 성공')
prints('Tks 정의 성공')