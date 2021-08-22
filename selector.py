import tkinter as tk 
import csv 

win = tk.Tk()
win.geometry("400x400")

tk.Label(win, text = "Select querry to reslove").place(x=140, y=10)

i = 40
List = ["alpha","beta","gamma","delta","epsilon"]

'''
Model file -
Users.csv :

[ "RndmPswd1" , "User1" , [ "text1" , "sender1" ] , [ "text2" , "sender2" ] , [ "text3" , "sender1" ] ]
[ "RndmPswd2" , "User2" , [ "text1" , "sender1" ] , [ "text2" , "sender1" ] , [ "text3" , "sender2" ] ]
[ "RndmPswd3" , "User3" , [ "text1" , "sender1" ] , [ "text2" , "sender2" ] , [ "text3" , "sender2" ] ]

'''

UsersList = []
fh = open('Users.csv','r+')
re = csv.reader(fh)

try:
   
   for a in re:
      
      #print(a)
      b=eval(a[-1])
      #print(b)
      
      if b[1] == a[1]:
         UsersList.append([b[1],b[0]])
         
except:
   pass

print(UsersList)
bDict = {}

for k in UsersList:
#for k in List:

   def move(x=k):
      
      print(k[0],k[1])
      
      win.destroy()

   #print(UsersList)
   ntext = str(k[0]) + " : " + str(k[1])
   #print(ntext)
   
   bDict[str(k[0])] = tk.Button(win, text = ntext , width = 30, command = move, wraplength = 300)
   bDict[str(k[0])].place(x = 10, y = 20 + i)
   i += 30

win.mainloop
