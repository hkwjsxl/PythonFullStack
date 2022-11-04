import requests

# 可供用户下载的图片如下
image_dict = {
    "1": ("吉他男神", "https://hbimg.huabanimg.com/51d46dc32abe7ac7f83b94c67bb88cacc46869954f478-aP4Q3V"),
    "2": ("漫画美女", "https://hbimg.huabanimg.com/703fdb063bdc37b11033ef794f9b3a7adfa01fd21a6d1-wTFbnO"),
    "3": ("游戏地图", "https://hbimg.huabanimg.com/b438d8c61ed2abf50ca94e00f257ca7a223e3b364b471-xrzoQd"),
    "4": ("alex媳妇", "https://hbimg.huabanimg.com/4edba1ed6a71797f52355aa1de5af961b85bf824cb71-px1nZz"),
}

# 可供用户下载的短视频如下
video_dict = {
    "1": {"title": "东北F4模仿秀",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"},
    "2": {"title": "卡特扣篮",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"},
    "3": {"title": "罗斯mvp",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg"},
}

# 可供用户下载的NBA视频如下
nba_dict = {
    "1": {"title": "威少奇才首秀三双",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
    "2": {"title": "塔图姆三分准绝杀",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"}
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}


def down_img(title, url):
    # 下载图片示例
    res = requests.get(
        url=url,
        headers=headers
    )

    with open(f"{title}.png", mode="wb") as f:
        f.write(res.content)
    ...


def down_video(title, url):
    # 下载视频示例
    res = requests.get(
        url=url,
        headers=headers
    )
    with open(f'{title}.mp4', mode='wb') as f:
        f.write(res.content)
    ...


def down_NBA(title, url):
    # 下载示例
    res = requests.get(
        url=url,
        headers=headers
    )
    with open(f'{title}.mp4', mode='wb') as f:
        f.write(res.content)
    ...


def main():
    while True:
        info_lst = {
            '1': ['下载图片', down_img, image_dict],
            '2': ['下载视频', down_video, video_dict],
            '3': ['下载NBA集锦', down_NBA, nba_dict],
        }
        for k, lst in info_lst.items():
            print(k, lst[0])
        code = input('请输入要选择的专区编号（Q退出）>>>').strip()
        if code.upper() == 'Q':
            break
        if code not in info_lst.keys():
            print('编号输入不合法！')
            continue
        while True:
            if len(info_lst.get(code)[2]) == 0:
                print('空了...')
                break
            param_dict = info_lst.get(code)[2]
            for k, v in param_dict.items():
                print(k, v)
            down_code = input('请输入要选择的下载编号（Q退出）>>>').strip()
            if down_code.upper() == 'Q':
                break
            if down_code not in param_dict.keys():
                print('编号不合法!')
                continue
            params = param_dict.get(down_code)
            print(info_lst[code][1])
            print(params)
            if isinstance(params, dict):
                info_lst[code][1](**params)
            else:
                info_lst[code][1](*params)
            param_dict.pop(down_code)


if __name__ == '__main__':
    main()
