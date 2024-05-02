import collections

temperatures = [0.5, 0.0, -3.5, 0.0, 2.5, 3.5, 4.0, 0.5, 3.5, 5.5, 6.0, 10.0, 12.5]

t_count = collections.Counter(temperatures)
print(t_count)
print(t_count.most_common())
print(t_count.most_common())
