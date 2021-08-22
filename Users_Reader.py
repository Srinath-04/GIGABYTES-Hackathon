import csv
fh = open('Users.csv','r')
x = csv.reader(fh)

try:
   for u in x:
      print(u)
except:
   pass

fh.close()
