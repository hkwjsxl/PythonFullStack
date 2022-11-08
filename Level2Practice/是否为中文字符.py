s = '中文hello字符world'
for line in s:
    if '\u4e00' <= line <= '\u9fff':
        print(line)

