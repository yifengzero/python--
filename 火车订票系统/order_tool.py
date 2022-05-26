import datetime
import random

card_list = []

hangban_list = {'上海-北京': {'海南航空HU7604': ['虹桥T2', '首都T2', '08:20', '10:40', '2时20分',
                                         {'公务舱': [10, 2140], '经济舱': [100, 890]}],
                          '海南航空HU7606': ['虹桥T2', '首都T2', '11:15', '13:30', '2时15分',
                                         {'公务舱': [15, 2140], '经济舱': [100, 940]}],
                          '海南航空HU7608': ['虹桥T2', '首都T2', '18:55', '21:10', '2时15分',
                                         {'公务舱': [8, 2140], '经济舱': [100, 890]}],
                          '海南航空HU7614': ['浦东T2', '首都T2', '20:40', '23:15', '2时35分',
                                         {'公务舱': [10, 2140], '经济舱': [80, 860]}],
                          '海南航空HU7602': ['虹桥T2', '首都T2', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 2140], '经济舱': [14, 890]}],
                          '东方航空MU5109': ['虹桥T2', '首都T2', '12:00', '14:15', '2时15分',
                                         {'公务舱': [5, 7640], '经济舱': [40, 880]}],
                          '厦门航空MF4704': ['浦东T2', '大兴T2', '07:55', '10:10', '2时15分',
                                         {'公务舱': [15, 4170], '经济舱': [30, 1490]}],
                          '厦门航空MF4702': ['虹桥T2', '大兴T2', '07:55', '10:10', '2时0分',
                                         {'公务舱': [12, 4170], '经济舱': [23, 1490]}],
                          '南方航空CZ8888': ['虹桥T2', '大兴T2', '15:30', '17:40', '2时10分',
                                         {'公务舱': [9, 4170], '经济舱': [44, 1490]}],
                          '南方航空CZ8884': ['浦东T2', '大兴T2', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 4170], '经济舱': [44, 1490]}],
                          '厦门航空MF4708': ['浦东T2', '大兴T2', '19:45', '22:00', '2时15分',
                                         {'公务舱': [6, 4170], '经济舱': [55, 1490]}],
                          '中国国航CA3279': ['虹桥T2', '大兴T2', '11:20', '13:35', '2时15分',
                                         {'公务舱': [15, 2690], '经济舱': [66, 1790]}],
                          '东方航空MU5111': ['浦东T2', '大兴T2', '13:00', '15:10', '2时10分',
                                         {'公务舱': [5, 7640], '经济舱': [77, 1932]}]},
                '北京-上海': {'海南航空HU7604': ['首都T2', '虹桥T2', '08:20', '10:40', '2时20分',
                                         {'公务舱': [2, 2140], '经济舱': [11, 890]}],
                          '海南航空HU7606': ['首都T2', '虹桥T2', '11:15', '13:30', '2时15分',
                                         {'公务舱': [1, 2140], '经济舱': [3, 940]}],
                          '海南航空HU7608': ['首都T2', '虹桥T2', '18:55', '21:10', '2时15分',
                                         {'公务舱': [5, 2140], '经济舱': [4, 890]}],
                          '海南航空HU7614': ['首都T2', '浦东T2', '20:40', '23:15', '2时35分',
                                         {'公务舱': [7, 2140], '经济舱': [5, 860]}],
                          '海南航空HU7602': ['首都T2', '虹桥T2', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 2140], '经济舱': [10, 890]}],
                          '东方航空MU5109': ['首都T2', '虹桥T2', '12:00', '14:15', '2时15分',
                                         {'公务舱': [10, 7640], '经济舱': [5, 880]}],
                          '厦门航空MF4704': ['大兴T2', '浦东T2', '07:55', '10:10', '2时15分',
                                         {'公务舱': [13, 4170], '经济舱': [33, 1490]}],
                          '厦门航空MF4702': ['大兴T2', '虹桥T2', '07:55', '10:10', '2时0分',
                                         {'公务舱': [13, 4170], '经济舱': [31, 1490]}],
                          '南方航空CZ8888': ['大兴T2', '虹桥T2', '15:30', '17:40', '2时10分',
                                         {'公务舱': [14, 4170], '经济舱': [31, 1490]}],
                          '南方航空CZ8884': ['大兴T2', '浦东T2', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 4170], '经济舱': [32, 1490]}],
                          '厦门航空MF4708': ['大兴T2', '浦东T2', '19:45', '22:00', '2时15分',
                                         {'公务舱': [9, 2690], '经济舱': [23, 1490]}],
                          '中国国航CA3279': ['大兴T2', '虹桥T2', '11:20', '13:35', '2时15分',
                                         {'公务舱': [7, 1620], '经济舱': [44, 1790]}],
                          '东方航空MU5111': ['大兴T2', '浦东T2', '13:00', '15:10', '2时10分',
                                         {'公务舱': [7, 7640], '经济舱': [77, 1932]}]},
                '上海-深圳': {'海南航空HU7604': ['虹桥T2', '宝安T3', '08:20', '10:40', '2时20分',
                                         {'公务舱': [10, 1620], '经济舱': [3, 470]}],
                          '海南航空HU7606': ['虹桥T2', '宝安T3', '11:15', '13:30', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [2, 470]}],
                          '海南航空HU7608': ['虹桥T2', '宝安T3', '18:55', '21:10', '2时15分',
                                         {'公务舱': [8, 1620], '经济舱': [32, 470]}],
                          '海南航空HU7614': ['浦东T2', '宝安T3', '20:40', '23:15', '2时35分',
                                         {'公务舱': [10, 1620], '经济舱': [23, 470]}],
                          '海南航空HU7602': ['虹桥T2', '宝安T3', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 1620], '经济舱': [11, 470]}],
                          '东方航空MU5109': ['虹桥T2', '宝安T3', '12:00', '14:15', '2时15分',
                                         {'公务舱': [5, 1620], '经济舱': ['16', 470]}],
                          '厦门航空MF4704': ['浦东T2', '大兴', '07:55', '10:10', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [17, 610]}],
                          '厦门航空MF4702': ['虹桥T2', '宝安T3', '07:55', '10:10', '2时0分',
                                         {'公务舱': [12, 1620], '经济舱': [17, 610]}],
                          '南方航空CZ8888': ['虹桥T2', '宝安T3', '15:30', '17:40', '2时10分',
                                         {'公务舱': [9, 1620], '经济舱': [18, 610]}],
                          '南方航空CZ8884': ['浦东T2', '宝安T3', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 1620], '经济舱': [81, 610]}],
                          '厦门航空MF4708': ['浦东T2', '宝安T3', '19:45', '22:00', '2时15分',
                                         {'公务舱': [6, 1620], '经济舱': [61, 610]}],
                          '中国国航CA3279': ['虹桥T2', '宝安T3', '11:20', '13:35', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [51, 610]}],
                          '东方航空MU5111': ['浦东T2', '宝安T3', '13:00', '15:10', '2时10分',
                                         {'公务舱': [15, 1620], '经济舱': [52, 710]}]},
                '深圳-上海': {'海南航空HU7604': ['宝安T3', '虹桥T2', '08:20', '10:40', '2时20分',
                                         {'公务舱': [10, 1620], '经济舱': [8, 470]}],
                          '海南航空HU7606': ['宝安T3', '虹桥T2', '11:15', '13:30', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [9, 470]}],
                          '海南航空HU7608': ['宝安T3', '虹桥T2', '18:55', '21:10', '2时15分',
                                         {'公务舱': [8, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7614': ['宝安T3', '浦东T2', '20:40', '23:15', '2时35分',
                                         {'公务舱': [10, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7602': ['宝安T3', '虹桥T2', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 1620], '经济舱': [4, 470]}],
                          '东方航空MU5109': ['宝安T3', '虹桥T2', '12:00', '14:15', '2时15分',
                                         {'公务舱': [5, 1620], '经济舱': [33, 470]}],
                          '厦门航空MF4704': ['宝安T3', '浦东T2', '07:55', '10:10', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [22, 470]}],
                          '厦门航空MF4702': ['宝安T3', '虹桥T2', '07:55', '10:10', '2时0分',
                                         {'公务舱': [12, 1620], '经济舱': [22, 710]}],
                          '南方航空CZ8888': ['宝安T3', '虹桥T2', '15:30', '17:40', '2时10分',
                                         {'公务舱': [9, 1620], '经济舱': [33, 710]}],
                          '南方航空CZ8884': ['宝安T3', '浦东T2', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 1620], '经济舱': [51, 710]}],
                          '厦门航空MF4708': ['宝安T3', '浦东T2', '19:45', '22:00', '2时15分',
                                         {'公务舱': [6, 1620], '经济舱': [32, 710]}],
                          '中国国航CA3279': ['宝安T3', '虹桥T2', '11:20', '13:35', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [42, 710]}],
                          '东方航空MU5111': ['宝安T3', '浦东T2', '13:00', '15:10', '2时10分',
                                         {'公务舱': [15, 1620], '经济舱': [52, 710]}]},
                '广州-上海': {'海南航空HU7604': ['白云T3', '虹桥T2', '08:20', '10:40', '2时20分',
                                         {'公务舱': [10, 1620], '经济舱': [8, 470]}],
                          '海南航空HU7606': ['白云T3', '虹桥T2', '11:15', '13:30', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [9, 470]}],
                          '海南航空HU7608': ['白云T3', '虹桥T2', '18:55', '21:10', '2时15分',
                                         {'公务舱': [8, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7614': ['白云T3', '浦东T2', '20:40', '23:15', '2时35分',
                                         {'公务舱': [10, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7602': ['白云T3', '虹桥T2', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 1620], '经济舱': [4, 470]}],
                          '东方航空MU5109': ['白云T3', '虹桥T2', '12:00', '14:15', '2时15分',
                                         {'公务舱': [5, 1620], '经济舱': [33, 470]}],
                          '厦门航空MF4704': ['白云T3', '浦东T2', '07:55', '10:10', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [22, 470]}],
                          '厦门航空MF4702': ['白云T3', '虹桥T2', '07:55', '10:10', '2时0分',
                                         {'公务舱': [12, 1620], '经济舱': [22, 710]}],
                          '南方航空CZ8888': ['白云T3', '虹桥T2', '15:30', '17:40', '2时10分',
                                         {'公务舱': [9, 1620], '经济舱': [33, 710]}],
                          '南方航空CZ8884': ['白云T3', '浦东T2', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 1620], '经济舱': [51, 710]}],
                          '厦门航空MF4708': ['白云T3', '浦东T2', '19:45', '22:00', '2时15分',
                                         {'公务舱': [6, 1620], '经济舱': [32, 710]}],
                          '中国国航CA3279': ['白云T3', '虹桥T2', '11:20', '13:35', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [42, 710]}],
                          '东方航空MU5111': ['白云T3', '浦东T2', '13:00', '15:10', '2时10分',
                                         {'公务舱': [15, 1620], '经济舱': [52, 710]}]},
                '上海-广州': {'海南航空HU7604': ['虹桥T2', '白云T3', '08:20', '10:40', '2时20分',
                                         {'公务舱': [10, 1620], '经济舱': [8, 470]}],
                          '海南航空HU7606': ['虹桥T2', '白云T3', '11:15', '13:30', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [9, 470]}],
                          '海南航空HU7608': ['虹桥T2', '白云T3', '18:55', '21:10', '2时15分',
                                         {'公务舱': [8, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7614': ['浦东T2', '白云T3', '20:40', '23:15', '2时35分',
                                         {'公务舱': [10, 1620], '经济舱': [5, 470]}],
                          '海南航空HU7602': ['虹桥T2', '白云T3', '20:55', '23:20', '2时20分',
                                         {'公务舱': [7, 1620], '经济舱': [4, 470]}],
                          '东方航空MU5109': ['虹桥T2', '白云T3', '12:00', '14:15', '2时15分',
                                         {'公务舱': [5, 1620], '经济舱': [33, 470]}],
                          '厦门航空MF4704': ['浦东T2', '白云T3', '07:55', '10:10', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [22, 470]}],
                          '厦门航空MF4702': ['虹桥T2', '白云T3', '07:55', '10:10', '2时0分',
                                         {'公务舱': [12, 1620], '经济舱': [22, 710]}],
                          '南方航空CZ8888': ['虹桥T2', '白云T3', '15:30', '17:40', '2时10分',
                                         {'公务舱': [9, 1620], '经济舱': [33, 710]}],
                          '南方航空CZ8884': ['浦东T2', '白云T3', '16:00', '18:25', '2时25分',
                                         {'公务舱': [8, 1620], '经济舱': [51, 710]}],
                          '厦门航空MF4708': ['浦东T2', '白云T3', '19:45', '22:00', '2时15分',
                                         {'公务舱': [6, 1620], '经济舱': [32, 710]}],
                          '中国国航CA3279': ['虹桥T2', '白云T3', '11:20', '13:35', '2时15分',
                                         {'公务舱': [15, 1620], '经济舱': [42, 710]}],
                          '东方航空MU5111': ['浦东T2', '白云T3', '13:00', '15:10', '2时10分',
                                         {'公务舱': [15, 1620], '经济舱': [52, 710]}]}
                }


def show_menu():
    print("\t\t************【飞机订票系统菜单】*************\n")
    print("\t\t*****************************************\n")
    print("\t\t*         订   票----------1           *\n")
    print("\t\t*         退   票----------2           *\n")
    print("\t\t*         查询订单----------3           *\n")
    print("\t\t*         查询机票----------4           *\n")
    print("\t\t*         改   签----------5           *\n")
    print("\t\t*         退   出----------0           *\n")
    print("\t\t*****************************************\n")


def booking():
    """订票"""
    print("----------------------------欢迎来到飞机票订购系统------------------------------------")
    nt = datetime.datetime.now()
    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
    hangban_title = [k for k, v in hangban_list.items()]
    print('全部航班信息：' + str(hangban_title))
    while True:
        flying_city = input("请输入您的起飞城市：")
        destination = input("请输入抵达城市：")
        time = input("请以(5-9)形式输入你的出发日期(只能购买今日起十五日内的飞机票)：")
        mon, day = time.split('-')
        bt = input("请输入查询or重置信息:")
        cm = flying_city + '-' + destination
        if bt == '查询':
            if (cm in hangban_title) == True and (int(mon) >= nt.month and nt.day <= int(day) <= nt.day + 15):
                break
            else:
                print("查不到航班信息，请重新输入")
        elif bt == '重置信息':
            print("请重新输入你的购票信息:")

        else:
            print("输入有误，请重置信息:")

    info = hangban_list[cm]
    print("------------------------全部航班信息-------------------------")
    print("航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时")
    for k, v in info.items():
        print(k + "\t" + v[0] + '\t\t' + v[1] + '\t' + v[2] + '\t' + v[3] + '\t' + v[4])

    while True:
        hangban = input("请输入购买的航班：")
        if hangban in info:
            print(
                "-------------------------------------------------------------------该航班信息-----------------------------"
                "-------------------------------")
            print(
                "航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时\t\t--------------------------------------票的信息(余票,"
                "价格)---------------------------------")
            print(hangban + '\t' + info[hangban][0] + '\t\t' + info[hangban][1] + '\t' + info[hangban][2] + '\t' + \
                  info[hangban][3] + '\t' + info[hangban][4] + '\t' + str(
                [{k: v} for k, v in info[hangban][5].items()]))
            flying_type = input("输入您要买的机票票类型（如经济舱、公务舱）：")
            if info[hangban][5][flying_type][0] <= 0:
                print('已无票！请选择其它机票。')

            else:
                print("请录入您的身份信息：")
                name_str = input("姓名：")
                id_number_str = input("身份证号：")
                phone_number_str = input("请输入您的手机号码：")

                # 显示班机信息
                a = random.randint(1, 19)
                b = random.randint(1, 25)
                c = random.choice("ABCD")
                print('该票的票价为：' + str(info[hangban][5][flying_type][1]) + '元，请输入’确认‘确认支付：')
                zhifu = input()
                if zhifu == '确认':
                    # 票数-1
                    info[hangban][5][flying_type][0] -= 1
                    # 保存乘客信息
                    card_dict = {"name": name_str,
                                 "id_number": id_number_str,
                                 "phone": phone_number_str,
                                 "banji": hangban,
                                 "date": time,
                                 "航班": cm,
                                 "座位": flying_type}
                    card_list.append(card_dict)
                    # 显示乘客具体信息
                    print('[航空客服温馨提示您]' + '您已购' + hangban + '次班机\t' + str(a) + '区|' + str(b) + str(c) + '\t' + \
                          cm + '\t' + str(nt.year) + '-' + time + '-' + info[hangban][2] + '开，请凭借身份证核验提前进站,祝您旅途愉快！')
                    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
                    print("-------------------------------------------------------------------------[航空客服]")
                    break
                else:
                    print('支付失败，请重新选择购买')

        else:
            print("您选择的不正确，请重新输入")


def tuipiao():
    """退票"""
    print("----------------------------欢迎来到飞机票退票系统------------------------------------")
    nt = datetime.datetime.now()
    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
    hangban_title = [k for k, v in hangban_list.items()]

    print('全部航班信息：' + str(hangban_title))
    while True:
        print("请录入您的身份信息：")
        name_str1 = input("姓名：")
        id_number_str1 = input("身份号：")
        phone_number_str1 = input("请输入您的手机号码：")

        for card_dict in card_list:
            if card_dict["name"] == name_str1 and card_dict["id_number"] == id_number_str1:
                info = hangban_list[card_dict["航班"]]
                print("姓名\t\t身份证号\t\t\t\t\t手机号码\t\t\t乘坐班机\t\t\t订购日期\t\t\t出发地-目的地")
                print("-" * 100)
                print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                            card_dict["id_number"],
                                                            card_dict["phone"],
                                                            card_dict["banji"],
                                                            card_dict["date"],
                                                            card_dict["航班"]))
                get_ticket = input("退票的话将会扣除10%的手续费，如果确认退票的话请输入【1】退票否则请输入【0】返回则返回上级菜单：")
                if get_ticket == "1":
                    info[card_dict["banji"]][5][card_dict["座位"]][0] += 1
                    card_list.remove(card_dict)
                    print("退票成功，您将会在1-3个工作日内收到退款到您的账户，欢迎下次与您相遇")
                    return
                else:
                    return

        else:
            print("抱歉，航班信息中并没有找到%s的信息" % name_str1)


def search():
    """查询订单"""
    print("----------------------------欢迎来到飞机票搜索系统------------------------------------")
    nt = datetime.datetime.now()
    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
    hangban_title = [k for k, v in hangban_list.items()]

    print('全部航班信息：' + str(hangban_title))
    while True:
        print("请录入您的身份信息：")
        name_str1 = input("姓名：")
        id_number_str1 = input("身份号：")
        phone_number_str1 = input("请输入您的手机号码：")

        for card_dict in card_list:
            if card_dict["name"] == name_str1 and card_dict["id_number"] == id_number_str1:
                info = hangban_list[card_dict["航班"]]
                print("姓名\t\t身份证号\t\t\t\t\t手机号码\t\t\t乘坐班机\t\t\t订购日期\t\t\t出发地-目的地")
                print("-" * 100)
                print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                            card_dict["id_number"],
                                                            card_dict["phone"],
                                                            card_dict["banji"],
                                                            card_dict["date"],
                                                            card_dict["航班"]))
                return
            else:
                print("抱歉，航班信息中并没有找到%s的信息" % name_str1)
                k = input("输入【1】返回主菜单，输入【0】重新搜索")
                if k == "1":
                    return
                else:
                    break


def change():
    """改签"""
    print("----------------------------欢迎来到飞机票改签系统------------------------------------")
    nt = datetime.datetime.now()
    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
    hangban_title = [k for k, v in hangban_list.items()]

    print('全部航班信息：' + str(hangban_title))
    while True:
        print("请录入您的身份信息：")
        name_str1 = input("姓名：")
        id_number_str1 = input("身份号：")
        phone_number_str1 = input("请输入您的手机号码：")

        for card_dict in card_list:
            if card_dict["name"] == name_str1 and card_dict["id_number"] == id_number_str1:
                info = hangban_list[card_dict["航班"]]
                print("姓名\t\t身份证号\t\t\t\t\t手机号码\t\t\t乘坐班机\t\t\t订购日期\t\t\t出发地-目的地")
                print("-" * 100)
                print("%s\t\t%s\t\t%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                                            card_dict["id_number"],
                                                            card_dict["phone"],
                                                            card_dict["banji"],
                                                            card_dict["date"],
                                                            card_dict["航班"]))
                get_ticket = input("如果确认改签的话请输入【1】改签否则请输入【0】返回则返回上级菜单：")
                if get_ticket == "1":
                    info[card_dict["banji"]][5][card_dict["座位"]][0] += 1
                    card_list.remove(card_dict)
                    while True:
                        flying_city = input("请重新输入您的起飞城市：")
                        destination = input("请重新输入抵达城市：")
                        time = input("请以(5-9)形式输入你的出发日期(只能购买今日起十五日内的飞机票)：")
                        mon, day = time.split('-')
                        bt = input("请输入查询or重置信息:")
                        cm = flying_city + '-' + destination
                        if bt == '查询':
                            if (cm in hangban_title) == True and (
                                    int(mon) >= nt.month and nt.day <= int(day) <= nt.day + 15):
                                break
                            else:
                                print("查不到航班信息，请重新输入")
                        elif bt == '重置信息':
                            print("请重新输入你的购票信息:")

                        else:
                            print("输入有误，请重置信息:")

                    info = hangban_list[cm]
                    print("------------------------全部航班信息-------------------------")
                    print("航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时")
                    for k, v in info.items():
                        print(k + "\t" + v[0] + '\t\t' + v[1] + '\t' + v[2] + '\t' + v[3] + '\t' + v[4])

                    while True:
                        hangban = input("请输入购买的航班：")
                        if hangban in info:
                            print(
                                "-------------------------------------------------------------------该航班信息----------------------------- "
                                "-------------------------------")
                            print(
                                "航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时\t\t--------------------------------------票的信息(余票,"
                                "价格)---------------------------------")
                            # 输出所有航班信息
                            print(hangban + '\t' + info[hangban][0] + '\t\t' + info[hangban][1] + '\t' + info[hangban][
                                2] + '\t' + \
                                  info[hangban][3] + '\t' + info[hangban][4] + '\t' + str(
                                [{k: v} for k, v in info[hangban][5].items()]))
                            flying_type = input("输入您要买的机票票类型（如经济舱、公务舱）：")
                            if info[hangban][5][flying_type][0] <= 0:
                                print('已无票！请选择其它机票。')

                            else:
                                # 将用户信息自动输入
                                name_str = name_str1
                                id_number_str = id_number_str1
                                phone_number_str = phone_number_str1

                                # 显示班机信息
                                a = random.randint(1, 19)
                                b = random.randint(1, 25)
                                c = random.choice("ABCD")
                                print('该票的票价为：' + str(info[hangban][5][flying_type][1]) + '元，请输入’确认‘确认支付：')
                                zhifu = input()
                                if zhifu == '确认':
                                    # 票数-1
                                    info[hangban][5][flying_type][0] -= 1
                                    # 保存乘客信息
                                    card_dict = {"name": name_str,
                                                 "id_number": id_number_str,
                                                 "phone": phone_number_str,
                                                 "banji": hangban,
                                                 "date": time,
                                                 "航班": cm,
                                                 "座位": flying_type}
                                    card_list.append(card_dict)
                                    # 显示乘客具体信息
                                    print('[航空客服温馨提示您]' + '您已购' + hangban + '次班机\t' + str(a) + '区|' + str(b) + str(
                                        c) + '\t' + \
                                          cm + '\t' + str(nt.year) + '-' + time + '-' + info[hangban][
                                              2] + '开，请凭借身份证核验提前进站,祝您旅途愉快！')
                                    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
                                    print(
                                        "-------------------------------------------------------------------------[航空客服]")
                                    break
                                else:
                                    print('支付失败，请重新选择购买')

                        else:
                            print("您选择的不正确，请重新输入")
                    return
                else:
                    return


def search1():
    print("----------------------------欢迎来到飞机票查询系统------------------------------------")
    nt = datetime.datetime.now()
    print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
    hangban_title = [k for k, v in hangban_list.items()]
    print('全部航班信息：' + str(hangban_title))
    while True:
        flying_city = input("请输入您的起飞城市：")
        destination = input("请输入抵达城市：")
        time = input("请以(5-9)形式输入你的出发日期(只能购买今日起十五日内的飞机票)：")
        mon, day = time.split('-')
        bt = input("请输入查询or重置信息:")
        cm = flying_city + '-' + destination
        if bt == '查询':
            if (cm in hangban_title) == True and (int(mon) >= nt.month and nt.day <= int(day) <= nt.day + 15):
                break
            else:
                print("查不到航班信息，请重新输入")
        elif bt == '重置信息':
            print("请重新输入你的购票信息:")

        else:
            print("输入有误，请重置信息:")

    info = hangban_list[cm]
    print("------------------------全部航班信息-------------------------")
    print("航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时")
    for k, v in info.items():
        print(k + "\t" + v[0] + '\t\t' + v[1] + '\t' + v[2] + '\t' + v[3] + '\t' + v[4])

    get_char = input("如果需要订票请输入【1】，否则输入【0】返回主菜单：")
    if get_char == "1":
        while True:
            hangban = input("请输入购买的航班：")
            if hangban in info:
                print(
                    "-------------------------------------------------------------------该航班信息-----------------------------"
                    "-------------------------------")
                print(
                    "航班\t\t\t\t出发站-------到达站\t出发时间\t到达时间\t历时\t\t--------------------------------------票的信息(余票,"
                    "价格)---------------------------------")
                print(hangban + '\t' + info[hangban][0] + '\t\t' + info[hangban][1] + '\t' + info[hangban][2] + '\t' + \
                      info[hangban][3] + '\t' + info[hangban][4] + '\t' + str(
                    [{k: v} for k, v in info[hangban][5].items()]))
                flying_type = input("输入您要买的机票票类型（如经济舱、公务舱）：")
                if info[hangban][5][flying_type][0] <= 0:
                    print('已无票！请选择其它机票。')

                else:
                    print("请录入您的身份信息：")
                    name_str = input("姓名：")
                    id_number_str = input("身份证号：")
                    phone_number_str = input("请输入您的手机号码：")

                    # 显示班机信息
                    a = random.randint(1, 19)
                    b = random.randint(1, 25)
                    c = random.choice("ABCD")
                    print('该票的票价为：' + str(info[hangban][5][flying_type][1]) + '元，请输入’确认‘确认支付：')
                    zhifu = input()
                    if zhifu == '确认':
                        # 票数-1
                        info[hangban][5][flying_type][0] -= 1
                        # 保存乘客信息
                        card_dict = {"name": name_str,
                                     "id_number": id_number_str,
                                     "phone": phone_number_str,
                                     "banji": hangban,
                                     "date": time,
                                     "航班": cm,
                                     "座位": flying_type}
                        card_list.append(card_dict)
                        # 显示乘客具体信息
                        print('[航空客服温馨提示您]' + '您已购' + hangban + '次班机\t' + str(a) + '区|' + str(b) + str(c) + '\t' + \
                              cm + '\t' + str(nt.year) + '-' + time + '-' + info[hangban][2] + '开，请凭借身份证核验提前进站,祝您旅途愉快！')
                        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t' + str(nt))
                        print("-------------------------------------------------------------------------[航空客服]")
                        break
                    else:
                        print('支付失败，请重新选择购买')

            else:
                print("您选择的不正确，请重新输入")
    else:
        return