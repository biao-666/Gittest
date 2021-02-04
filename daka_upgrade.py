# 给钉钉发送通知

from dingtalkchatbot.chatbot import DingtalkChatbot
import time

# 当前时间
now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # time.localtime()：计算机当地时间

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
    xiaoding.send_text(msg = '滴滴滴：' + message + now_time_print, is_at_all = True)  # "滴滴滴："是钉钉的安全设置的自定义关键词

if now_time >= "2021-02-04 09:00:00" and now_time <= "2021-02-04 09:05:00":
    send_message('雄哥雄哥！您该上班打卡了！！！')
    time.sleep(61)  # 停止执行5秒，防止反复运行程序
elif now_time >= "2021-02-04 12:30:00" and now_time <= "2021-02-04 12:35:00":
    send_message('雄哥雄哥！您该下班吃饭了。')
    time.sleep(5)  # 停止执行5秒，防止反复运行程序
elif now_time >= "2021-02-04 14:00:00" and now_time <= "2021-02-04 14:05:00":
    send_message('雄哥雄哥！您该开始上班了。')
elif now_time >= "2021-02-04 18:10:00" and now_time <= "2021-02-04 18:15:00":
    send_message('雄哥雄哥！您该回家了！！！')
    time.sleep(5)  # 停止执行5秒，防止反复运行程序
else:
    print("无满足条件时，退出！！！")
