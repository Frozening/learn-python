stinformation = {}
f = file('score.txt','r')
while True:
        line = f.readline()
        if len(line) == 0:
                break	
	stin = line
	i = stin.split(':')
	stinformation[i[0]] = tuple(i[1]i[:-1].split(','))
print stinformation

name = raw_input('Please enter a name:')
if stinformation.has_key(name):
	j = stinformation[name]
	k = int(j[1])
	l = int(j[2])
	print "the student's sex,age and score are %s,%d and %d" %(j[0],k,l)
