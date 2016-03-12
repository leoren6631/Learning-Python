import itertools
import math
cipher = 'msoodryewaivhohtepoholbtllsidotkitrncyhcemtowuetfenomntneiutirrktndloedegenhsnhrghcetceenaelfheceotglbsaiwncsaiuvonotnisoeesiuigmndttmfvneslpleblotroohttoewoeuwthbaelynttmrextrurheahutetntthnohftnntedinssdwerksreeodeweueqocttbuirotsriahkdtaodooinhnsertoenaorlecawhoiorcwedmmelidriwoiurehwunonisohounnotcthreaptcaiwedetmtmrjiaeyvraoawvteentrastenevntrteugnhhwotlreututussgoesytmheasdehtrtftiviosnsoseeaehrrytnshsusntauttsieabntoiieyhoatedbnemftbvthiierntyaavoevetwgipehgduaterelryooheeisltehorzesssratuithgrnlassenteuyosrchneitgeurihrclsrftmofgwawfonteahflniwhnqaoiteeflgkneetkneaunfoh'
keylenth = 10

'''
def fn(string):
    n = []
    if len(string)<=584:
        for i in range(10):
            n.append(string[i])
            yield n
        return 'done'
'''
t = 0
l = []
#for i in range(0,len(cipher),len(cipher)//keylenth):
    #l.append(cipher[i:i+49])
for i in range(0,len(cipher),keylenth):
    l.append(cipher[i:i+10])
a = [[]for i in range(0,10)]
while t<len(l):
    for i in range(10):
        try:
            x=l[t][i]
            a[i].append(x)
        except:
            break
    t+=1

for i in a:
    print ((''.join(i)).count('t'))
    print ((''.join(i)).count('h'))
    print ((''.join(i)).count('e'))
    print ()
    '''
l1 = cipher[0:49]
l2 = cipher[50:99]
l3 = cipher[100:149]
l4 = cipher[150:199]
l5 = cipher[200:249]
l6 = cipher[250:299]
l7 = cipher[300:349]
l8 = cipher[350:399]
l9 = cipher[400:449]
l10 = cipher[500:549]
l11 = cipher[550:-1]

c = list(map(fn, l))
for n in c[100]:
    print(n)
'''

'''
#l = itertools.permutations(cipher, 50)
for i in itertools.permutations(cipher, 50):
    for j in range(math.factorial(50)):
        for k in range(50)
        l = i[][0]
'''
