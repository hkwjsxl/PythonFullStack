def down_img(user ,url):
    print(user, url)
    pass


with open(r'file/csv_file.csv', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        info = line.split(',')
        user = info[1]
        url = info[2]
        if not url.startswith('https'):
            continue
        down_img(user, url)


