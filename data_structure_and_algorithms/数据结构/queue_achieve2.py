"""
使用python内部函数操作队列
"""

from collections import deque

q = deque(maxlen=5)
for i in range(4):
    q.append(i)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())  # IndexError: pop from an empty deque
