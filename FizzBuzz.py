def fizzbuzz(n):
    l = ['Fizz','Buzz','FizzBuzz']
    while 0 < n <= 10**7:
        for i in range(1,n+1):
            if i % 3 == 0 and i % 15 !=0:
                print l[0]
            elif i % 5 == 0 and i % 15 !=0:
                print l[1]
            elif i % 15 == 0:
                print l[2]
            else:
                print i
        break
    return None
fizzbuzz(100)
