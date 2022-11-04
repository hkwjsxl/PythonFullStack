import requests


def write_file(**kwargs):
    """将天气信息拼接起来，并写入到文件
    格式要求：
    	1. 每个城市的天气占一行
    	2. 每行的格式为：city-北京,cityid-101010100,temp-18...
    """
    # 补充代码
    with open(r'files/weather.txt', 'a', encoding='utf-8') as f:
        for k, v in kwargs.items():
            item = f'{k}-{v},'
            f.write(item)
        f.write('\n')


def get_weather(code):
    """ 获取天气信息 """
    url = "http://www.weather.com.cn/data/ks/{}.html".format(code)
    res = requests.get(url=url)
    res.encoding = "utf-8"
    weather_dict = res.json()
    return weather_dict


city_list = [
    {'code': "101020100", 'title': "上海"},
    {'code': "101010100", 'title': "北京"},
]

# 补充代码
for item in city_list:
    code = item.get('code')
    weather_dict = get_weather(code)
    write_file(**weather_dict.get('weatherinfo'))
