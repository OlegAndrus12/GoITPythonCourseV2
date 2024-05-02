import cProfile

cProfile.run('sum([i * 2 for i in range(10000)])')

cProfile.run('sum((i * 2 for i in range(10000)))')
