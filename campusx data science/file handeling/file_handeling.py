f = open('sample.txt','w')
f.write('hello captain')
f.close()

f = open('sample.txt','a')
f.write('\n welcome to the captans kingdom')
f.write('\n please introduce yourself')

l = ['\n hi','\n hello','\nhow are you']
f.writelines(l)
f.close()

f = open('sample.txt','r')
s = f.read(10)
print(s)
f.close()

#----------------------------------------------------------------------------

with open('sample.txt','w') as f:     # automaticaly closes the file when full block is executed
    f.write('dhjhsdfjhabdvjh')


