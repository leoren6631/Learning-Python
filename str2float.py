from functools import reduce
char2num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':-1}
def str2float(s):
    nums = map(lambda ch: char2num[ch], s)
    point = 0
    def to_float(x, y):
        nonlocal point
        if y ==-1:
            point = 1
            return x
        if point == 0:
            return x*10+y
        else:
            point = point*10
            return x+y/point
    return reduce(to_float, nums, 0.0)
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
