import cv2
import pyperclip  # 用于复制粘贴的模块
import pyautogui
import schedule
import time

time.sleep(2)


# 从屏幕screen中找到source的位置坐标(找到微信搜索框的位置)
def findImg():
    im = pyautogui.screenshot()
    im.save('screen.png')
    screen = cv2.imread('screen.png')
    joinMeeting = cv2.imread('wechat.png')
    result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
    pos_start = cv2.minMaxLoc(result)[3]  # 获取最相似点相似坐标
    x = int(pos_start[0]) + int(joinMeeting.shape[1] / 2)
    y = int(pos_start[1]) + int(joinMeeting.shape[0] / 2)
    return x, y


# 向搜索框中录入要查找的好友名称:name好友名称，x，y搜索框位置
def send_name_to_search(x, y, name):
    pyautogui.click(x, y)
    time.sleep(1)
    # 赋值好友名称
    pyperclip.copy(name)
    # 粘贴复制内容
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('enter')
    # 向下移动100个像素定位到搜索到第一个好友位置点击


#     pyautogui.moveTo(x, y+80)
#     pyautogui.click(x, y+80)

# 向好友发送消息
def send_msg(msg):
    pyperclip.copy(msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')


def run():
    # 主要程序
    x, y = findImg()
    send_name_to_search(x, y, '阿房宫')
    time.sleep(1)
    send_msg('Python Gui Test!!!')
    send_msg('当前时间: %s' % time.strftime('%Y-%m-%d %X', time.localtime()))
    print('发送成功!')


schedule.every().day.at('16:30').do(run)
while True:
    schedule.run_pending()
