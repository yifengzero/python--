import cards_tools
# 无限循环，由用户主动决定什么时候退出循环

while True:

    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作： ")
    print("您选择的操作是【%s】" % action_str)

    #  1，2，3 针对名片操作
    if action_str in ["1", "2", "3"]:
        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

        pass

    # 0 退出系统
    elif action_str == "0":
        # 如果再开发时，不希望立刻编写分支可以用pass，表示一个占位符，保证程序代码结构正确
        print("欢迎再次使用【名片管理系统】")
        break
        # pass
    # 其它情况表示输入错误
    else:
        print("您输入的不正确，请重新选择")
