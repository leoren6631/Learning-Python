import hashlib, cProfile
f = file('dictionary.txt', 'r')
words = [word.strip() for word in f]
f.close()
#print words[:-1]
'''
pl = 'andy rocks your face off'
cipher = hashlib.sha512(pl).hexdigest()
print cipher
'''
def checkDictionary(secret):
    for word in words:
        if hashlib.sha512(secret) == secret:
            print word 
for i in words:
    checkDictionary(i)
    if i == words[-1]:
        print 'end'

#cipher = hashlib.sha512("banana").hexdigest()

#cProfile.run('checkDictionary(cipher)')

