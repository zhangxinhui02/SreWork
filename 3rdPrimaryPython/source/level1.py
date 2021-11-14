"""三局两胜的猜拳游戏"""
import random

xuejie_list = ["学姐正在思考新的战术", "学姐在思考人生", "学姐已经准备好了", "学姐的拳术秀了你一脸", "学姐说：“正面上我啊”",
               "学姐说：“我等得花都谢了”", "学姐在把玩你的学习资料", "学姐朝你大胯捏了一把"
               ]


def convert_result(turn):
    """转换结果表示的数值为对应的文字"""
    if turn == 1:
        return "石头"
    elif turn == 2:
        return "剪刀"
    elif turn == 3:
        return "布"
    else:
        return


def check_result(player_turn, xuejie_turn):
    """返回玩家是否获胜，如果平局则返回空值"""
    if player_turn == xuejie_turn:
        return None

    if player_turn == 1:
        if xuejie_turn == 2:
            return True
        else:
            return False
    if player_turn == 2:
        if xuejie_turn == 3:
            return True
        else:
            return False
    if player_turn == 3:
        if xuejie_turn == 1:
            return True
        else:
            return False


def game():
    """运行游戏"""
    player_score = 0
    xuejie_score = 0
    print("游戏开始，输入 1出石头， 2出剪刀， 3出布")
    while True:
        print("\n" + xuejie_list[random.randint(0, len(xuejie_list) - 1)])
        player_turn = input("你决定要出：")
        try:
            player_turn = int(player_turn)
        except ValueError:
            print("\t输入错误")
            continue
        xuejie_turn = random.randint(1, 3)
        player_result = convert_result(player_turn)
        xuejie_result = convert_result(xuejie_turn)

        if not player_result:
            print("\t输入错误")
            continue
        print("你出了 " + player_result)
        print("学姐出了 " + xuejie_result)

        if check_result(player_turn, xuejie_turn) is None:
            print("哇，平局！再来一局吧")
        elif check_result(player_turn, xuejie_turn) is True:
            print("你赢下一局！")
            player_score += 1
        else:
            print("学姐赢下一局！")
            xuejie_score += 1

        if player_score >= 2 or xuejie_score >= 2:
            break

    print("\n你赢了" + str(player_score) + "局")
    print("学姐赢了" + str(xuejie_score) + "局")
    if player_score > xuejie_score:
        print("你碾压了学姐！拿回了宝贵的学习资料！（顺便摸到了学姐的手）")
    else:
        print("学姐碾压了你！她决定对你的学习资料下手！")


if __name__ == "__main__":
    while True:
        print("""
\t由于你的贪心，你的电脑上出现了一段字符：hacked by yyz。
\t你感到十分的惊恐与无措，因为这台计算机上有着你大量的学习资料。
\t还好yyz发现你是sre的学弟（学妹），
\t于是yyz决定和你来三局两胜制的猜拳决定这台电脑的命运
""")
        input("按下回车键来与学姐对线\n")
        game()
        if input("\n要就此罢休(输入q)还是继续与学姐酣战一场(按下回车)？") == 'q':
            print("你丧失了摸学姐的手的大好机会……\n")
            input()
            break
        else:
            print("你选择继续与学姐对线！\n")
