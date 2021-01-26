# 给钉钉发送通知

from dingtalkchatbot.chatbot import DingtalkChatbot
import time


def send_message(message):
    # WebHook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=c832267a88fc358ad068e256e6b66e34eb21e0131eb89ce0a0ea781ef5838238'
    # 初始化机器人
    xiaoding = DingtalkChatbot(webhook)
    # 当前时间
    now_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())# time.localtime()：计算机当地时间
    now_time = f"\n当前时间：{now_time}"
    # Test消息@所有人
    xiaoding.send_text(msg = '滴滴滴：' + message + now_time, is_at_all = False)

send_message('打卡！！！想被扣钱吗!!')