"""监视程序"""
import time

import cv2
import pyautogui
import yagmail
import schedule


def run():
    print('开始监视......')
    # 截取屏幕图片
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'screen.png')
    # 基于cv2打开电脑摄像头，捕获实施照片
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    time.sleep(3)
    cv2.imwrite('photo.jpg', frame)
    # 关闭摄像头
    cap.release()

    received = ['hankewei0224@126.com', 'hankewei0224@163.com']
    yag = yagmail.SMTP(user='562172420@qq.com', host='smtp.qq.com')
    contents = ['<b> <font color="#FF1493" size="10"> 您好，一切都在监视中，尽情放心！</font> </b>',
                "screen.png",
                'photo.jpg']

    yag.send(received, '来自小鬼侦探的报告', contents)


schedule.every().minute.at(":30").do(run)
while True:
    schedule.run_pending()
    time.sleep(5)
