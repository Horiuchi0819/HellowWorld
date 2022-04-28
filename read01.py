f = open('myfile.txt', 'r', encoding='UTF-8')

#data = f.readline()
#print(data)

#data = f.readline()
#print(data)

#data = f.readline()
#print(data)

#while True:
 #data = f.readline()
 #if data == '':
   #break
 #print (data.rstrip('\n'))

for data in f:
 print (data.rstrip('\n'))

f.close()

