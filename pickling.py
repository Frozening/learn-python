#!/usr/bin/python
# Filename : pickling.py

import cPickle as p

shoplistfile = 'shoplist.data' #the name of the file where we will store the object
shoplist = ['apple','mango','carrot']
f = file(shoplistfile,'w') #Write to the file
p.dump(shoplist,f) #dump the object to a file
f.close()

del shoplist
f = file(shoplistfile)
storedlist = p.load(f) #Read back from the storage
print storedlist
