from functools import reduce
'''
def prod(L):
    return reduce(reduce_prod, L)
def reduce_prod(x, y):
    return x*y
    '''
def prod(L):
    return reduce(lambda x, y:x*y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
