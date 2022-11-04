import importlib
from settings import NOTIFY_LIST


def sendall(content):
    for path_str in NOTIFY_LIST:
        model_path, class_name = path_str.rsplit('.', maxsplit=1)  # 'notify.qq.QQ',
        # 'notify.qq'      'QQ'
        model = importlib.import_module(model_path)  # from notify import qq
        cls = getattr(model, class_name)  # 反射获取类名
        obj = cls()  # 实例化
        obj.send(content)  # 鸭子类型调用send方法
