stinformation = {}
f = file('score.txt','r')
while True:
        line = f.readline()
        if len(line) == 0:
                break
        print line,

	stin = line
	i = stin.split(':')
	print i
	stinformation[i[0]] = i[1][:-1]
print stinformation
