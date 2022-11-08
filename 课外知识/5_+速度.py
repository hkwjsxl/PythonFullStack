import taichi as tc
import time

tc.init()


@tc.kernel
def main():
    n = 0
    for i in range(100000000):
        n += i


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time() - start_time)
