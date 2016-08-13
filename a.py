a = {'abc':('male',110),'bbc':('male',120),'nyt':('female',100)}
max_key = 0
max_score = 0
for (k,v) in a.items():
        if v[1] > max_score:
                max_score = v[1]
                max_key = k
print "the Highest : %s,%d" %(max_key,a[max_key][1])
