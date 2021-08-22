import csv
'''fh = open('Users.csv','r')
x = csv.reader(fh)

try:
   for u in x:
      print(u)
except:
   pass

fh.close()
'''
fh = open('Users.csv','a+')
wr = csv.writer(fh)
wr.writerow(['password222','testuser223',['i am feeling bored','testuser222'],['Hobbies may help you!','couns'],['thanks','testuser223']])
fh.close()
'''
'''
