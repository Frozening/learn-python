f = file('score.txt','r')
while True:
	line = f.readline()
 	if len(line) == 0:
  		break
	print line,
f.close()
