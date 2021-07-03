# !/usr/bin/env python
# -*- coding: utf-8 -*-

import random

dic = {"a": "グー", "b": "チョキ", "c": "パー"}

count = 1
while True:
    try:
        print("じゃーんけーん")
        print("a=グー　b=チョキ　c=パー　aかbかcを入力")
        user = input('>>>  ')
        user = user.lower()
        user_choice = dic[user]

        choice_list = ["a", "b", "c"]
        pc = dic[random.choice(choice_list)]

        draw = 'DRAW'
        win = 'You Win!!'
        lose = 'You lose!!'

        if user_choice == pc:
            judge = draw
        else:
            if user_choice == "グー":
                if pc == "チョキ":
                    judge = win
                else:
                    judge = lose

            elif user_choice == "チョキ":
                if pc == "パー":
                    judge = win
                else:
                    judge = lose

            else:
                if pc == "グー":
                    judge = win
                else:
                    judge = lose

        print("あなた選んだのは %s" % user_choice)
        print("コンピュータが選んだのは %s" % pc)
        print("結果は%s\n" % judge)

        
        if judge == lose:
            print("再度挑戦してね(^o^)/")
            break

        elif judge == win:
            print("%i勝目" % count)
            count += 1

        if count == 5:
            print("flag{fnets}")
            break

    except:
        print("aかbかcを入力してください。")