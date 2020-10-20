from src.SimTool import Generator

g = Generator('Test', (0, 8), 'test', distribution='normal')

current_time = 0
for i in range(10):
    current_time = g.generate(current_time)
    print(current_time)