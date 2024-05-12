import time
import keyboard
import sys
import random, getpass
sleep = time.sleep

def hp_bar(max_hp, hp):
    a = int(hp/max_hp *10)
    b = 10-a
    print('HP: ', end='')
    if ((hp/max_hp *100) % 10) >=5:
        a += 1
        b -= 1
    for i in range(a):
        print('■', end='')
    for i in range(b):
        print('□', end='')
    print()
    print(f'    {hp} / {max_hp}')
def text(n):
    a = 0
    for i in n:
        print(i, end = '', flush=1)
        time.sleep(0.03)
        a += 1
        if a == 59:
            print('\n')
            a = 0
    print()
    while 1:
        if keyboard.is_pressed('enter'):
            input()
            return
def cl(n): #clear_line
    for _ in range(n):
        sys.stdout.write("\033[F")  # 현재 행의 첫 번째 위치로 이동
        sys.stdout.write("\033[K")  # 현재 위치부터 행의 끝까지 지움
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
        text_skip(n[a][1])
                
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
name = input('당신의 이름은?')
def enemy_die():
    text(f'{name}의 승리!')
    sys.exit()


#공격형 스킬
def damage_skill(entity, to, level, skill):
    entity['자세'] = ''
    text(f'{entity}')
    damage = entity['공격력'] * level
    if to['보호막'] > damage:
        to['보호막'] > damage
    elif to['보호막'] < damage:
        to['체력'] -= damage - to['보호막']
        to['보호막'] = 0
    if to['자세'] == 'counter':
        damage_skill(to, entity)


#방어형 스킬
def guard_skill(entity, level, skill):
    entity['보호막'] += entity['최대체력']*(0.1*level)
    
#반격 스킬
def declar_counter(entity, name, level, skill):
    entity['자세'] += level

def act_counter(on, to, skill):
    damage_skill

#버프형 스킬
def buff_skill(entity, type, turn, level):
    if type == 'speed':
        entity['속도'] += level * 5
    elif type == 'attack':
        entity['공격력'] *= 1 + (level*0.1)
        entity['공격력'] = int(entity['공격력'])




#리스트 자료들
act_list = [['공격','상대방을 공격합니다',2, 5],['방어','방어 자세를 2회 취합니다',3],['스킬','스킬을 사용합니다',5]]
act_list_enemy = [['1번 행동',1, 2],['2번 행동',3,3],['3번 행동',5,5]]
player_guard = 0
skill = [['화염구', '지끼미 상대방을 그냥 조져뿐따이', 3, 10], ['GAY','게이는 문화다', 1],['취소', '스킬취소', 0]]
dummy_1 = {'이름': '무명', '체력':20,'공격력':5, '원공격력': 5, '방어력':5,'속도':15, '최대체력':20, '보호막': 0, '자세': '', }
dummy_2 = {'이름': '이름 없는자', '체력':20,'공격력':10, '원공격력':10, '방어력':5,'속도':10, '최대체력':20, '보호막': 0}
turn_count = [dummy_1['속도'], dummy_2['속도']]
ft_me = [['선수입니다! 싸움에 있어 이만한것이 없지요!','재빠른 발놀림으로 갑시다!','선빵필승 아니겠습니까!'],['상대방이 선수를 가져갑니다!','침착하게 준비합시다! 상대방이 들어옵니다','느긋하게 가봅시다']]


#text delete의 줄임말, 그냥 줄넘김 30번
def td():
    print('\n'*30)

#플레이어의 차례
def player_turn():
    global dummy_1, player_guard
    turn_count[0] -= 100
    td()
    text_skip(f'{name}의 턴')
    print()
    hp_bar(dummy_1['최대체력'],dummy_1['체력'])
    print()
    c = ac_description(act_list)
    if c[0] == '스킬':
        td()
        text_skip(f'{name}의턴')
        print()
        c = ac_description(skill)
    elif c[0] == '방어':
        player_guard = 2
    if len(c) == 4:
        damage_skill(c)
    turn_check()

#플레이어의 죽음
def die():
    td()
    text('당신은 죽었습니다')
    text('게임오버')
    sys.exit()

#상대방의 차례
def enemy_turn():  
    global dummy_2, player_guard, turn
    turn_count[1] -= 100
    td()
    text_skip('상대방의 턴')
    print()
    a = random.choice(act_list_enemy)
    text(f'상대방의 {a[0]}')
    dam = a[2]
    if player_guard > 0:
        text('당신은 방어 자세를 취하고 있다')
        dam = int(dam*0.7)
        text_skip(f'당신에게 {dam}만큼 피해')
        dummy_1['체력'] -= dam
        hp_bar(dummy_1['최대체력'],dummy_1['체력'])
        input()
        player_guard -= 1
        if player_guard == 0:
            text('당신의 방어가 깨졌다')
    else:        
        text_skip(f'당신에게 {dam}만큼 피해')
        dummy_1['체력'] -= dam
        hp_bar(dummy_1['최대체력'],dummy_1['체력'])
        input()
    if dummy_1['체력'] < 1:
        die()
    turn_check()
turn = 0

#턴 체크
def turn_check(b = dummy_1, c = dummy_2):
    global turn_count, turn
    turn += 1
    while (turn_count[0] or turn_count[1]) < 99:
        turn_count[0], turn_count[1] = turn_count[0] + b['속도'], turn_count[1] + c['속도']
    if (turn_count[0] and turn_count[1]) > 99:
        n,m = turn_count[0] % 100, turn_count[1] % 100
        if turn == 1:
            if dummy_1['속도'] > dummy_2['속도']:
                player_turn()
            else:
                enemy_turn()
        if n == 0: n += 100
        if m == 0: m += 100 
        check = random.randrange(1,n+m)
        if check <= n:
            player_turn()
        else:
            enemy_turn()
    elif turn_count[0] > 99:
        player_turn()
    elif turn_count[1] > 99:
        enemy_turn()

#싸움 선언    
def fight_turn(a,b):
    global turn
    turn = 0
    turn_check(a,b)

fight_turn(dummy_1, dummy_2)