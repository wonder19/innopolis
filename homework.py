def monster():
    """Функция создания массива чудовищ
        monster_tuple=(view, force, health)
    """
    monsters = []
    i = 5
    for i in range(5, 30):
        if i % 2 == 0:
            monster_tuple = ('o(:/:)o', i, i)
            monsters.append(monster_tuple)
        elif i % 2 == 1 and i % 5 != 0:
            monster_tuple = ('@(/__*)@', i * 2, i*2)
            monsters.append(monster_tuple)
        elif i % 5 == 0:
            monster_tuple = ('C(*__*)o', i, i*5)
            monsters.append(monster_tuple)
        else:
            monster_tuple = ('\(8 + 8)/', i * 4, i*4)
            monsters.append(monster_tuple)
    i = +1
    return monsters


def apple():
    """Функция возвращает массив яблок
        apples=[view, health]
    """
    apples = []
    i = 5
    for i in range(5, 30):
        if i % 2 == 0:
            apple_tuple = ('(`)', i)
            apples.append(apple_tuple)
        elif i % 2 == 1 and i % 5 != 0:
            apple_tuple = ('( `)', i * 2)
            apples.append(apple_tuple)
        elif i % 5 == 0:
            apple_tuple = ('(  `)', i * 3)
            apples.append(apple_tuple)
        else:
            apple_tuple = ('(   )', i*4 )
            apples.append(apple_tuple)
    i = +1
    return apples


def sword():
    """Функция возвращает массив мечей"""
    swords = []
    i = 5
    for i in range(5, 30):
        if i % 2 == 0:
            sword_tuple = ('<-/-', i)
            swords.append(sword_tuple)
        elif i % 2 == 1 and i % 5 != 0:
            sword_tuple = ('--->-', i * 2)
            swords.append(sword_tuple)
        elif i % 5 == 0:
            sword_tuple = ('<---X-', i * 5)
            swords.append(sword_tuple)
        else:
            sword_tuple = ('___/_', i * 4)
            swords.append(sword_tuple)
    i = +1
    return swords


def output_print( monster, apple, sword, step_count):
    """Функция выводит уведомления о том, что выпало игроку"""
    monster_list = monster
    apple_list = apple
    sword_list = sword
    step_count=step_count
    step_for_out = 0
    if step_count % 2 == 0:
        print('You meet monster   ', monster_list[step_count][0], '  force  ', monster_list[step_count][1], "health  ", monster_list[step_count][2])
        step_for_out = 'monster'
        #return step_for_out

    elif step_count % 2 == 1 and step_count % 3 != 0 :
        print('You get apple for force! look at it  ', apple_list[step_count][0], "   you get ", apple_list[step_count][1],
              "health")
        step_for_out = 'apple'
        #return step_for_out

    elif step_count % 3 == 0 :
        print('You get a new sword  ', sword_list[step_count][0], "   its force is", sword_list[step_count][1])
        step_for_out ='sword'

    return step_for_out


def submit_knight_health_with_apple(knight, apple, step_count):
    """Функция подсчета здоровья"""
    knight_for_health = knight
    apple_for_health = apple
    knight_health = knight_for_health[2] + apple_for_health[step_count][1]
    knight[2] = knight_health
    return knight


def chooose_next_step(who):
    """Функция выбора следующего шага"""
    valid_input = False
    while valid_input is not True:
        chose_for_return=None
        if who=="monster":
            chooos_input = list(input('Input 1 for FIGTHT or 2 for MOVE FORWARD '))
        else:
            chooos_input = list(input('Input 1 TAKE it or 2 for MOVE FORWARD '))
        if len(chooos_input)!=0:
            if len(chooos_input)>1:
                print("easy easy, not so many letters")
                continue
            else:
                chooos = chooos_input[0]
                try:
                    int(chooos)
                except:
                    print("not a number, dear friend")
                    continue
            valid_input = input_validation(int(chooos))
        else:
            print('print something for better result')
            continue
    chose_for_return=int(chooos)
    return chose_for_return


def monster_fight(knight, monster, step_count):
    """Функция сражения с монстром"""
    knight_for_fight = knight[2]
    monster_for_fight = monster[step_count][2]
    if monster_for_fight > knight_for_fight:
        return False
    else:
        knight[2] = knight_for_fight - monster_for_fight
        return True


# def chooose_for_sword():
#     """Функция выбора шага для выбора меча"""
#     valid_input = False
#     valid_input = False
#     while valid_input is not True:
#         chose_for_return=None
#         input = input('Input 1 TAKE it or 2 for MOVE FORWARD ')
#         if input:
#             chooos_input=list(input)
#             if len(chooos_input)>1:
#                 print("easy easy, not so many letters")
#                 continue
#             else:
#                 chooos = chooos_input[0]
#                 try:
#                     int(chooos)
#                 except:
#                     print("not a number, dear friend")
#                     continue
#             valid_input = input_validation(int(chooos))
#         else:
#             print('print something for best resul')
#             continue
#     chose_for_return=int(chooos)
#     return chose_for_return


def take_the_sword(knight, sword, step_count):
    """Функция смены меча"""
    knight_sword_for_change = knight
    sword_for_change = sword
    knight_sword_for_change[1] = sword_for_change[step_count][1]
    return knight


def check_the_win(monster_death):
    """Функция проверки выигрыша"""
    if monster_death == 10:
        return True


def input_validation(chooos):
    """Функция проверки того, что ввел игрок"""
    chooos=chooos
    choice_list = [1, 2]
    if chooos in choice_list:
        return True
    else:
        print('1 or 2 pleaseee')
        return False


def play():
    """Функция игры"""
    knight = ["(';')", 10, 10]
    monster_death = 0
    mon = monster()
    ap = apple()
    sw = sword()
    step_count = 0
    list_for_print=['monster','sword']
    print("welcome, ", knight[0], "! lets start.. you are knight, you should kill 10 monsters, you have force ", knight[1], "and healht ", knight[1])
    while True:
        output_info = output_print(mon, ap, sw, step_count)
        if output_info == "monster":
            choose_step = chooose_next_step(list_for_print[0])
            if choose_step==1:
                fight = monster_fight(knight, mon, step_count)
                if fight:
                    monster_death = monster_death +1
                    check_wining = check_the_win(monster_death)
                    if check_wining:
                        print("Congr! you WIIIIN")
                        return False
                    else:
                        print("CONGRATULATION! you kill", monster_death, "monsters")
                else:
                    print("you looose, game over")
                    return False
        elif output_info == "apple":
            knight= submit_knight_health_with_apple(knight, ap, step_count)
            print("Now knight healht", knight[2])

        elif output_info == "sword":
            choose_step = chooose_next_step(list_for_print[1])
            if choose_step==1:
                knight=take_the_sword(knight, sw, step_count)
                print("Now your force is", knight[1])

        step_count = step_count +1
        if step_count>24:
            step_count=0


if __name__ == '__main__':
    play()
