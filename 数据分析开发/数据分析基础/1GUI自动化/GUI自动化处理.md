# 总结---GUI自动化处理

- 安装

~~~python
pip install pyautogui
~~~

- 获取电脑屏幕的宽和高的像素数

~~~python
import pyautogui
width, height = pyautogui.size()
print(width,height)
~~~

## 鼠标

- 移动鼠标

~~~python
# pyautogui.moveTo() 函数将鼠标立即移动到屏幕的指定位置

import pyautogui
for i in range(5):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
~~~

- 移动鼠标

~~~python
# pyautogui.moveRel() 函数相对于当前的位置移动鼠标

import pyautogui
for i in range(5):
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)
~~~

- 获取鼠标位置

~~~python
import pyautogui
pyautogui.position()
~~~

- 鼠标点击

~~~python
import pyautogui
pyautogui.click(10, 5)

# 指定鼠标按键
如果想指定鼠标按键，就加入 button 关键字参数，值分别为 'left'、'middle'或 'right'。
例如，pyautogui.click（100，150，button='left'）将在坐标（100，150）处点击鼠标左键。
而 pyautogui.click（200，250，button='right'）将在坐标（200，250）处点击右键。

# 实现点击的其他方法
- pyautogui. mouseDown()
    - 只是按下鼠标按键
- pyautogui.mouseUp()
    - 只是释放鼠标按键
- pyautogui.doubleClick()
    - 执行双击鼠标左键
- pyautogui.rightClick()，pyautogui.middleClick()
    - 分别执行双击右键和双击中键
~~~

- 拖动鼠标

~~~python
# pyautogui.dragTo() 和 pyautogui.dragRel() 函数
# 打开画图软件
import pyautogui, time
time.sleep(2)
pyautogui.click()
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2,button='left') # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2,button='left') # move down
    pyautogui.dragRel(-distance, 0, duration=0.2,button='left') # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2,button='left') # move up
# - 注意：如果出现如下报错信息
#     - AssertionError: button argument not in ('left', 'middle', 'right')
#     - 则在函数中添加button参数指定鼠标按键即可
~~~

- 滚动鼠标

~~~python
import pyautogui, time
time.sleep(2)
pyautogui.scroll(-500)  # 负数向下
~~~

## 处理屏幕

- 获取屏幕快照

~~~python
import pyautogui
img = pyautogui.screenshot()
img.save('./current_screen.png')
# 返回目标像素点颜色，Image对象getpixel() 
img.getpixel((23,560))
~~~

- 匹配颜色

~~~python
import pyautogui
img = pyautogui.screenshot()
print(img.getpixel((500, 200)))
result = pyautogui.pixelMatchesColor(500, 200, (248, 248, 248))
print(result)
~~~

## 图像识别

- 安装/测试

~~~python
pip install opencv-python

import cv2
~~~

- 打开腾讯会议，识别【加入会议】按钮，对其进行点击操作

~~~python
import cv2
import pyautogui
import time

time.sleep(2)
# 获取带有腾讯会议的屏幕快照且保存到本地
im = pyautogui.screenshot()
im.save('screen.png')

# 基于cv2读取照片
screen = cv2.imread('screen.png')
joinMeeting = cv2.imread('./joinMeeting.png')
# 在屏幕快照中对比加入会议按钮照片，定位其准确位置
result = cv2.matchTemplate(joinMeeting, screen, cv2.TM_CCOEFF_NORMED)
# result是一个二维列表，列表中最大值元素的位置就是我们对比后相似度最高的图片【最上角】位置
print(result)

# minMaxLoc返回一个元组，其中三个元素，以此为最不相似点分数，最相似点分数，最不相似点位置坐标，最相似点位置坐标
pos_start = cv2.minMaxLoc(result)[3]  # 获取最相似点相似坐标
print(pos_start)
# x = pos_start[0]
# y = pos_start[1]

# 定位到点击图片的中间位置
x = int(pos_start[0]) + int(joinMeeting.shape[1] / 2)
y = int(pos_start[1]) + int(joinMeeting.shape[0] / 2)

time.sleep(1)
pyautogui.click(x,y)

~~~

## 控制键盘

![下载](https://img2023.cnblogs.com/blog/2570053/202212/2570053-20221221115321385-541809069.png)

![下载 (1)](https://img2023.cnblogs.com/blog/2570053/202212/2570053-20221221115336600-1211459400.png)

- 通过键盘发送一个字符串

~~~python
import pyautogui
import time
time.sleep(2)
pyautogui.click(300, 300)
pyautogui.typewrite('Hello',interval=0.25)
pyautogui.press('space',interval=0.25)
pyautogui.typewrite('world!',interval=0.25)
~~~

- 按下按键

~~~python
pyautogui.press('enter')
~~~

- 按下和释放键盘

~~~python
import pyautogui
import time
time.sleep(2)
pyautogui.keyDown('shift')
pyautogui.press('4')
pyautogui.keyUp('shift')
~~~

- 热键组合

~~~python
import pyautogui
import time
time.sleep(2)
pyautogui.hotkey('ctrl', 'v')
~~~

- 微信自动化

~~~python
import cv2
import pyperclip  # 用于复制粘贴的模块
import pyautogui
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


# 主要程序
x, y = findImg()
send_name_to_search(x, y, '阿房宫')
time.sleep(1)
send_msg('Python Gui Test!!!')
send_msg('Python Gui Test!!!') 
~~~

- 监视程序

~~~python
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

~~~

