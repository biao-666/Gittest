# 给钉钉发送通知

from dingtalkchatbot.chatbot import DingtalkChatbot
import time


def send_message(message):
    # WebHook地址
    webhook = '{Webhook 地址}'  # 在{Webhook 地址}填入钉钉的Webhook 地址
    # 初始化机器人
    xiaoding = DingtalkChatbot(webhook)
    # 当前时间
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # time.localtime()：计算机当地时间
    # Test消息@所有人
    xiaoding.send_text(msg=f"滴滴滴：{message} \n当前时间：{now_time}", is_at_all=False)  # "滴滴滴："是钉钉的安全设置的自定义关键词

    # xiaoding.send_text(msg = '滴滴滴：test' + message + now_time, is_at_all = False)


send_message('打卡啊！！！迟到一分钟一块钱啊!!!')