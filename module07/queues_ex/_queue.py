from collections import deque

l = list(range(1, 10))
l_deque = deque(l)
print(l_deque)

l_deque = deque(l, 5)
print(l_deque)

l_deque.appendleft(10)
print(l_deque)
l_deque.append(11)
print(l_deque)
print(l_deque.count(5))
print(l_deque.index(6))

l_deque.rotate(2)
print(l_deque)

l_deque.reverse()
print(l_deque)
