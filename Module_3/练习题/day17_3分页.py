class Pagination:
    def __init__(self, current_page, page_num=10):
        self.current_page = current_page
        self.page_num = page_num

        if not self.current_page.isdecimal():
            self.current_page = 1

        self.current_page = int(self.current_page)
        if self.current_page < 1:
            self.current_page = 1

    @property
    def start(self):
        return (self.current_page - 1) * 10

    @property
    def end(self):
        return self.current_page * self.page_num


def run():
    range_list = range(1, 100)
    page_obj = Pagination('1', 10)
    num_list = range_list[page_obj.start: page_obj.end]
    for num in num_list:
        print(num)


if __name__ == '__main__':
    run()
