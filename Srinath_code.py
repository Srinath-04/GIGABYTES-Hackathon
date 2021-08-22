import tkinter as tk 
import csv 

win = tk.Tk()
win.geometry("400x400")

tk.Label(win, text = "Select querry to reslove").place(x=140, y=10)

i = 40
List = ["alpha","beta","gamma","delta","epsilon"]

''' Model file -

Users.csv :

[ "RndmPswd1" , "User1" , [ "text1" , "sender1" ] , [ "text2" , "sender2" ] , [ "text3" , "sender1" ] ]
[ "RndmPswd2" , "User2" , [ "text1" , "sender1" ] , [ "text2" , "sender1" ] , [ "text3" , "sender2" ] ]
[ "RndmPswd3" , "User3" , [ "text1" , "sender1" ] , [ "text2" , "sender2" ] , [ "text3" , "sender2" ] ]

'''
'''

UsersList = []
fh = open('Users.csv',r)
re = csv.reader(fh)

try:
   for i in re:
      j=i[-1]
      if j[1] == i[1]:
         UsersList += i[1]
except:
   pass
'''

bDict = {}

#for k in UsersList:
for k in List:

   def move(x = k):

      print(x)

      win.destroy()

   bDict[k] = tk.Button(win, text = k , width = 30, command = move, wraplength = 300)
   bDict[k].place(x = 10, y = 20 + i)
   i += 30

win.mainloop