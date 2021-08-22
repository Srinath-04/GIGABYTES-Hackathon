import tkinter as tk 
import csv 

win = tk.Tk()
win.geometry("960x540")
win.configure(bg="light blue")

tk.Label(win, text = "Select querry to reslove",font=("Consolas", 20) , background = "light blue", foreground = "magenta").place(x=300, y=10)
i = 40

UsersList = []
fh = open('Users.csv','r+')
re = csv.reader(fh)

try:
   
   for a in re:
      
      print(a)
      b=eval(a[-1])
      #print(b)
      #print(b[1],a[1])
      if b[1] == a[1]:
         UsersList.append([b[1],b[0],a[0]])
      else:
         pass
         
except:
   pass

print(UsersList)
bDict = {}

for k in UsersList:
#for k in List:

   def move(x = k):
      
      print(x[0],x[2])
      
      win.destroy()

   #print(UsersList)
   ntext = str(k[0]) + " : " + str(k[1])
   #print(ntext)
   
   bDict[k[0]] = tk.Button(win, text = ntext , width = 30, command = move)
   bDict[k[0]].place(x = 10, y = 20 + i)
   i += 30

win.mainloop
