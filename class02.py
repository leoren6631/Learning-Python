import hashlib, bcrypt
import time
x = ''
iteration = 1000
pwd = 'password'
salt = bcrypt.gensalt()
#print pwd + salt
def hashfn(x, pwd, salt):
    cipher = hashlib.sha256(x+ pwd + salt).hexdigest()
    return cipher

#y=time.clock()
for r in range(iteration):
    if r < iteration:
        cipher = hashfn(x, pwd, salt)
        x = cipher
print x

        

    