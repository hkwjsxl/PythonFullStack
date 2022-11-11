from hashlib import md5


class TextMethod:
    def __init__(self, text, method):
        self.text = text
        self.method = method


class UserDict:
    def __init__(self, ):
        self.id = None
        self.username = None
        self.nickname = None
        self.phone = None
        self.email = None

    def set_info(self, user_dict):
        for k, v in user_dict.items():
            setattr(self, k, v)

    def clear(self):
        self.__init__()


def enc_passwrod(pwd):
    md5_obj = md5()
    md5_obj.update('除却君身三层雪，天下谁人配白衣。'.encode('utf-8'))
    md5_obj.update(pwd.encode('utf-8'))
    return md5_obj.hexdigest()
