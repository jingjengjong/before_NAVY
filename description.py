import keyboard
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