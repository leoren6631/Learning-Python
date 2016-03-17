def _odd_iter():#generate odd number
    n = 1
    while True:
        n = n + 2
        yield n 
def _not_divisible(n):#check if it is a divisible
    return lambda x:x % n > 0
def primes():#generate prime numbers
    yield 2
    it = _odd_iter() #initial 
    while True:
        n = next(it)
        yield n 
        it = filter(_not_divisible(n), it)
for n in primes():#test prime
    if n < 3:
        print n
    else:
        break

def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome,range(1,1000))#test palindrome
print (list(output))
    