#아 ㅅㅂ 파일 다 날라갔네 어카지 그래도 주요 기능은 다 남아있긴 한데 개빡치네
import sys,time,getpass, keyboard
sleep =time.sleep

def text_skip(n):
    a = 0
    for i in n:
        print(i, end = '', flush=1)
        time.sleep(0.03)
        a += 1
        if a == 59:
            print('\n')
            a = 0
    print()
def ac_description(n):                     #arrow and choice
    a = 0
    b = 0
    while 1:
        if len(n) == 3:
            if a == -1: a+=3
            a %= 3
            if a == 0:
                print(f'   ▶{n[0][0]}◀       {n[1][0]}        {n[2][0]}')
            elif a == 1:
                print(f'    {n[0][0]}       ▶{n[1][0]}◀       {n[2][0]}')
            else:
                print(f'    {n[0][0]}         {n[1][0]}       ▶{n[2][0]}◀')
        elif len(n) == 4:
            if a == -1: a+=4
            a %= 4
            if a == 0:
                print(f'''   ▶{n[0][0]}◀                    {n[1][0]}    
                               {n[2][0]}                     {n[3][0]}
                      ''')
            elif a == 1:
                print(f'''     {n[0][0]}                    ▶{n[1][0]}◀     
                               {n[2][0]}                     {n[3][0]}
                      ''')
            elif a == 2:
                print(f'''     {n[0][0]}                     {n[1][0]}     
                             ▶{n[2][0]}◀                    {n[3][0]}
                      ''')
            else:
                print(f'''     {n[0][0]}                     {n[1][0]}     
                               {n[2][0]}                   ▶{n[3][0]}◀
                      ''')
        elif len(n) == 2:
            if a == -1: a+=2
            a%= 2
            if a == 0:
                print(f'   ▶{n[0][0]}◀                     {n[1][0]}')
            else:
                print(f'    {n[0][0]}                      ▶{n[1][0]}◀')
        print()
        (n[a][1])
                
        while 1:
            if keyboard.is_pressed('left'):
                a -=1
                b = 1
                break
            elif keyboard.is_pressed('right'):
                a +=1
                b = 1
                break
            elif keyboard.is_pressed('up') or keyboard.is_pressed('down'):
                if len(n) == 4:
                    a+=2
                    b = 1
            elif keyboard.is_pressed('enter'):
                getpass.getpass('')
                return n[a]
        sleep(0.15)
        if b >0:
            if len(n) == 4:
                cl(4)
            else: cl(3)
def hp_bar(max_hp, hp): #체력바 
    a = int(hp/max_hp *10)
    b = 10-a
    if ((hp/max_hp *100) % 10) >=5:
        a += 1
        b -= 1
    return 'HP:'+'■'*a + '□'*b + '\n'+(f'    {hp} / {max_hp}')


def cl(n): #clear_line
    for _ in range(n):
        sys.stdout.write("\033[F")  # 현재 행의 첫 번째 위치로 이동
        sys.stdout.write("\033[K")  # 현재 위치부터 행의 끝까지 지움

enemy_name= 'enemy'
print(hp_bar(20,12))

def interface():
    #69칸
    print(f'''
╔═══════════════════════════════════════════════════════════════════╗
          ''')
    print(f'''
  ═════════════════════════════════════════════════════════════════
    
╚═══════════════════════════════════════════════════════════════════╝''')