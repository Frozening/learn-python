stinformation = {}
scores = []
max_value = 0
max_key = 0
min_value = 150
min_key = 0
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
for (key,value) in stinformation.items():
        if value[2] > max_value:
		max_value = value[2]
                max_key = key
        if value[2] < min_value:
                min_value = value[2]
                min_key = key
print "the Highest score : %d,%s,%s,%d" %(max_value,max_key,stinformation[max_key][0],stinformation[max_key][1])
print "the Lowest score : %d,%s,%s,%d" %(min_value,min_key,stinformation[min_key][0],stinformation[min_key][1])
name = raw_input('Please enter a name:')
if stinformation.has_key(name):
        ziliao = stinformation[name]
        print "the student's sex,age and score are %s,%d and %d" %(ziliao[0],int(ziliao[1]),int(ziliao[2]))
