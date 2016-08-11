stinformation = {}
f = file('score.txt','r')
while True:
        line = f.readline()
        if len(line) == 0:
                break	
	stin = line
	students = stin.split(':')
	name = students[0]
	details = students[1]
	detail = tuple(details[:-1].split(','))
	sex = detail[0]
	age = int(detail[1])
	score = int(detail[2])
	stinformation[name] = (sex,age,score)
print stinformation

name = raw_input('Please enter a name:')
if stinformation.has_key(name):
	ziliao = stinformation[name]
	print "the student's sex,age and score are %s,%d and %d" %(ziliao[0],int(ziliao[1]),int(ziliao[2]))
