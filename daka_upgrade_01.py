# 给钉钉发送通知

from dingtalkchatbot.chatbot import DingtalkChatbot
import time
from datetime import datetime, timedelta

# 当前时间
# now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # time.localtime()：计算机当地时间
now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def send_message(message):
    """和钉钉关联起来，给钉钉的群发消息"""

    # WebHook地址
    webhook = '{Webhook 地址}'  # 在{Webhook 地址}填入钉钉的Webhook 地址
    # 初始化机器人
    xiaoding = DingtalkChatbot(webhook)
    # 当前时间
    now_time_print = f"\n当前时间：{now_time}"
    # print(now_time)
    # Test消息@所有人
    xiaoding.send_text(msg='滴滴滴：' + message + now_time_print, is_at_all=True)

add_time_list = {
    'add_time_print1': datetime.now().strftime('%Y-%m-%d') + ' 09:05:00',
    'add_time_print2': datetime.now().strftime('%Y-%m-%d') + ' 12:35:00',
    'add_time_print3': datetime.now().strftime('%Y-%m-%d') + ' 14:05:00',
    'add_time_print4': datetime.now().strftime('%Y-%m-%d') + ' 18:15:00',
}

def adddate_time(what_hour):
    """从字典中取时间，返回一个值"""

    return add_time_list[what_hour]


if now_time <= adddate_time('add_time_print1'):
    send_message('老铁！您该上班打卡了！！！')
    time.sleep(5)  # 停止执行5秒，防止反复运行程序
elif now_time <= adddate_time('add_time_print2'):
    send_message('老铁！您该下班吃饭了。')
    time.sleep(5)  # 停止执行5秒，防止反复运行程序
elif now_time <= adddate_time('add_time_print3'):
    send_message('老铁！您该开始上班了')
elif now_time <= adddate_time('add_time_print4'):
    send_message('老铁！您该回家了！！！')
    time.sleep(5)  # 停止执行5秒，防止反复运行程序
else:
    print("无满足条件时，退出！！！")


# def adddate_time(what_hour):
#     """从字典中取时间，返回一个值"""
#     # if what_hour == "早上上班":
#     #     add_time_print = datetime.now().strftime('%Y-%m-%d') + ' 09:05:00'  # 拼接出要比较的时间
#     # elif what_hour == "中午下班":
#     #     add_time_print = datetime.now().strftime('%Y-%m-%d') + ' 12:35:00'  # 拼接出要比较的时间
#     # elif what_hour == "中午上班":
#     #     add_time_print = datetime.now().strftime('%Y-%m-%d') + ' 14:05:00'  # 拼接出要比较的时间
#     # elif what_hour == "晚上下班":
#     #     add_time_print = datetime.now().strftime('%Y-%m-%d') + ' 18:15:00'  # 拼接出要比较的时间
#
#     return add_time_list[what_hour]