while True:
    num = input('>>>').strip()
    if not num.isdecimal():
        print('again')
        continue
    break
num = int(num)
if num != 0 and (num % 4 == 0 and num % 100 != 0 or num % 100 == 0 and num % 400 == 0):
    print(f'{num}是闰年')
else:
    print(f'{num}是平年')
