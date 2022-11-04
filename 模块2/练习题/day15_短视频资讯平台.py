import os
import re
import time
from datetime import datetime

import requests

# 拼接路径
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DIR_PATH = os.path.join(BASE_PATH, 'files')
FILE_PATH = os.path.join(DIR_PATH, 'video.csv')


# 分页看新闻
def look_news():
    while True:
        data_list = []
        temp_list = []
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            i, index = 0, 1
            for line in f:
                line = line.strip()
                temp_list.append((index, line))
                i += 1
                index += 1
                if i == 10:
                    data_list.append(temp_list)
                    i = 0
                    temp_list = []
        page_num = input('请输入要查看的页码：').strip()
        if page_num.upper() == 'Q':
            print('退出上一层！')
            break
        if not page_num.isdecimal():
            print('请输入数字页码')
            break
        page_num = int(page_num)
        page_num -= 1
        if page_num not in range(len(data_list)):
            print('页码输入错误，跳转到第一页')
            page_num = 0
        print(f'正在观看第{page_num + 1}页')
        datas = data_list[page_num]
        for index, data in datas:
            print(index, data)


# 搜索专区
def search():
    while True:
        # 直接输入ID或关键词
        keyword = input('请直接输入要筛选的ID或关键词：').strip()
        if keyword.upper() == 'Q':
            print('退出上一层！')
            break
        if not keyword:
            print('非空值！')
            continue
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 判断用户输入是否是ID
                if keyword.isdecimal():
                    video_id = line.split(',')[0]
                    if video_id != keyword:
                        continue
                    print(line)
                    break
                content = re.search(keyword, line, re.S)
                if not content:
                    continue
                print(line)


# 下载专区
def down_load():
    while True:
        # 存储视频ID和URL
        video_id_list = []
        video_url_list = []
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                video_id_list.append(line.split(',')[0])
                video_url_list.append(line.split(',')[-1])
        video_id = input('请输入视频ID：').strip()
        if video_id.upper() == 'Q':
            print('退出上一层！')
            break
        if video_id not in video_id_list:
            print('视频ID不存在！')
            continue
        for k, v in zip(video_id_list, video_url_list):
            if k != video_id:
                continue
            video_index = video_id_list.index(k)
            down_load_video(video_id, video_url_list[video_index])


# 下载视频
def down_load_video(video_id, video_url):
    video_file_name = video_id + '-' + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.mp4'
    print(f'正在下载---{video_file_name}---{video_url}')
    file_path = os.path.join(DIR_PATH, video_file_name)
    res = requests.get(video_url, headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    })
    with open(file_path, 'wb') as f:
        f.write(res.content)
    for i in range(101):
        text = "\r{}%".format(i)
        print(text, end="")
        time.sleep(0.01)
    print(f'下载完成---{video_file_name}---{video_url}')


def main():
    while True:
        core_dict = {
            '1': ['分页看新闻', look_news],
            '2': ['搜索专区', search],
            '3': ['下载专区', down_load],
        }
        for core_k, core_v in core_dict.items():
            print(core_k, core_v[0])
        code_area = input('请输入要进入的专区：').strip()
        if code_area.upper() == 'Q':
            print('退出！')
            break
        if code_area not in core_dict.keys():
            print('编号不正确！')
            continue
        core_dict[code_area][1]()


if __name__ == '__main__':
    main()



"""
优化建议：

1、专区1和专区2获取一下数据的总长度，比如新闻总条数news_total=1000，页码范围page_range: 1-100页，以后做web时这两个数据可以很好的提升用户体验

2、下载视频时要考虑下链接是否可用，下载过程中是否会出现异常，要有个兜底的逻辑（已经超纲了，但是学生具备这样的能力）

3、优化一些提示语，比如搜不到新闻有个提示等等

"""

