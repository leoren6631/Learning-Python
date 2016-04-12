l1 = []
l2 = []
f1 = open('file.txt', 'r')
f2 = open('file1.txt', 'r')
scalar_product = 0
if f1 == '' or f2 == '':
	scalar_product = 0
for line1 in f1:
	line1 = line1.rstrip('\n')
	line1 = int(line1)
	l1.append(line1)
for line2 in f2:
	line2 = line2.rstrip('\n')
	line2 = int(line2)
	l2.append(line2)	
if len(l1) >= len(l2):
	for i in range(len(l2)):
		scalar_product += l1[i]*l2[i]
else:
	for i in range(len(l1)):
			scalar_product += l1[i]*l2[i]

	
print scalar_product