score = ''' alex,male,28,110
 CDB,male,20,119
 Neo,male,20,120
'''

f = file('score.txt','w')
f.write(score)
f.close

f = file('score.txt','r')
while True:
 line = f.readline()
 if len(line) == 0:
  break
 print line,

f.close() 

def inquiry(): 
 clin = {name:(sex,age,score)}
 name = int(raw_input('Please enter name : ')) 
 if name = 'alex':
  (sex,age,score) = (male,28,110)
 elif name = 'CDB':
  (sex,age,score) = (male,20,119)
 elif name = 'Neo':
  (sex,age,score) = (male,20,120)
 else:
  print 'This person does not exist,please verify name'
