stinformation = {}
compare = {}
scores = []
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
	compare[score] = (name,sex,age)
	scores.append(score)
max_key = 0
min_key = 150
for (key,value) in compare.items():
	if key > max_key:
		max_key = key
	elif key < min_key:
		min_key = key
print "the Highest score : %d,%s,%s,%d" %(max_key,compare[max_key][0],compare[max_key][1],compare[max_key][2])
print "the Lowest score : %d,%s,%s,%d" %(min_key,compare[min_key][0],compare[min_key][1],compare[min_key][2])
#Another way: Highest = scores[scores.index(max(scores))]
#Another way: Lowest = scores[scores.index(min(scores))]
#Another way: print "The Highest score is",Highest,"and the student's name,sex,age are %s,%s,%d" %(compare[Highest][0],compare[Highest][1],compare[Highest][2])
#print "The Lowsest score is",Lowest,"and the student's name,sex,age are %s,%s,%d" %(compare[Lowest][0],compare[Lowest][1],compare[Lowest][2])
name = raw_input('Please enter a name:')
if stinformation.has_key(name):
	ziliao = stinformation[name]
	print "the student's sex,age and score are %s,%d and %d" %(ziliao[0],int(ziliao[1]),int(ziliao[2]))
