# 给钉钉发送通知

from dingtalkchatbot.chatbot import DingtalkChatbot
import time


def send_message(message):
    # WebHook地址
    webhook = '{Webhook 地址}'  # 在{Webhook 地址}填入钉钉的Webhook 地址
    # 初始化机器人
    xiaoding = DingtalkChatbot(webhook)
    # 当前时间
    now_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())# time.localtime()：计算机当地时间
    now_time = f"\n当前时间：{now_time}"
    # Test消息@所有人
    xiaoding.send_text(msg = '滴滴滴：' + message + now_time, is_at_all = False)

send_message('打卡！！！想被扣钱吗!!')
