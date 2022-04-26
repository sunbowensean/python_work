#这是一个猜数字的游戏。
import random , time , sys


def hello():
    print(f"Hi!你好！我是小冰，是和你玩游戏的机器人，\n你现在在玩的游戏是{game_name}。如果想知道\n怎么玩，试试输入“help”，知道怎么玩"+\
          "就输入“start”快速开始吧！\n")
    time.sleep(1)
    print("对啦，要是想知道是谁做的我，可以输入“about us”来了解哦！（可能不会太详细）")
    
    while True:
        hd = input()

        if hd == "start":
            print("那就开始吧！")
            time.sleep(1)
            break
        
        if hd == "help":
            print(how_to_play)
            time.sleep(1)
            print("现在可以开始了吗？")
            
        if hd == "about us":
            print("小学部，五年七班，2号的孙博文编制， 王悦嘉测试，王啸林2次测试，五年级！")
            time.sleep(0.7)
            print("现在可以开始了吗？")

        elif hd != "start" or hd != "help" or hd != "about me":
            print("做出我的人只是小学生，我还没有那么智能，说点简单点的吧！")
            time.sleep(1)


game_name = "猜数字"
how_to_play = "这个游戏的玩法是：\n\t我说一个范围，你要在这个范围内根据提示猜数字，\n只有10次机会，猜到就赢了，超出次数就输了。(我的水"+\
              "平可是很高的呢！)"

hello()
while True:


    n_r = random.randint(1,100)
    print("我想了一个数字，范围在1-100之间，猜到你就赢啦！请猜吧。")
    time.sleep(1)
    print("对了，你只有十次机会呦！")

    #猜十次

    for g_s in range (1,11):
        guess = int(input())

        if guess < n_r:
            print("太小啦，再猜一次吧！")

        elif guess > n_r:
            print("太大了，下次就可以猜对了!")

        else:
            break
            #猜对啦！

    if guess == n_r:
        print(f"恭喜你，猜对啦！这次是用了{ g_s }次猜对的哦。"+\
              "\n想再玩一次请输入“重来”，想退出请输入“退出”。")
        
        xz = input()
        
        while True:
            if xz == "重来":
                print("那就开始吧！")
                break
            
            elif xz == "退出":
                print("那就下次见，跟你玩真开心！")
                time.sleep(2)
                sys.exit()

            else:
                print("我听不懂你在说什么呢。")
    else:
        print("你已经用光了10次机会，我赢了!"+\
              "想再玩一次请输入“重来”，想退出请输入“退出”")

        xz = input()

        while True:
            if xz == "重来":
                print("那就开始吧！\n")
                time.sleep(1)
                break
            
            elif xz == "退出":
                print("那就下次见，跟你玩真开心！")
                time.sleep(2)
                sys.exit()

            else:
                print("我听不懂你在说什么呢。")
