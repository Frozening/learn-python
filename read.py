stinformation = {}
f = file('score.txt','r')
while True:
        line = f.readline()
        if len(line) == 0:
                break
	
	stin = line
	i = stin.split(':')
	stinformation[i[0]] = i[1][:-1]
print stinformation
