import json

class Response:
    def __init__(self, code=200, message='success', data=None):
        self.code = code
        self.message = message
        self.data = data

    def get_info(self):
        return json.dumps(self.__dict__, ensure_ascii=True)
