import tkinter
import socket
import pygame
from Hackathon_Main_Page import Pass_on_message

#Pygame for bg music
pygame.init()
sound = pygame.mixer.music.load('Assets\\Sound.mp3')
pygame.mixer.music.play(-1)

#Socket Connections
Socket_con = socket.socket()
Device_info = socket.gethostname()	
Ip = socket.gethostbyname(Device_info)
Port = 5050
Socket_con.connect((Ip,Port))

#Tkinter Set up
root = tkinter.Tk()
root.title("Chatbox")
width, height =   960, 540
root.geometry(f"{width}x{height}")
user_chat = []

def type_of_issue():
	Socket_con.send(Pass_on_message.encode())
	List_box.insert(0,'[USER]: '+Pass_on_message)

def chat_history():
	global user_chat
	mesg = Chatbox.get()				#To get the data from the textbox
	Chatbox.delete(0,len(mesg))			#To clear text in textbox
	List_box.insert(0,'[USER]: '+mesg)	#To insert Data in the Chat history Box
	user_chat.append(mesg)
	Socket_con.send(mesg.encode())		#Send the message to the server
	received_message = Socket_con.recv(1024)
	received_message = repr(received_message)[2:-1]
	List_box.insert(0,'[EXPERT]: '+received_message)
        
def heading():
	global Heading
	Heading = tkinter.Label(root,
		font = ('Consolas',50),
		text = 'CLIENT SIDE')
	Heading.place(x = width//2, y = 0)

def LstBox():
	global List_box
	List_box = tkinter.Listbox(root,
		width = 200,
		height = 10,
		font = 'Consolas')
	List_box.place(x = 20, y = 100)

def Chat_box():
	global Chatbox
	Chatbox = tkinter.Entry(root,
		font = "Consolas",
		width = 70)
	Chatbox.place(x = 20, y = height - 100)

def Send_button():
	global Send
	Send = tkinter.Button(root,
		text = "SEND",
		font = "Consolas",
		fg = "Blue",
		command = chat_history)
	Send.place(x = width -50, y = height - 80)


heading()
LstBox()
Chat_box()
type_of_issue()
Send_button()
tkinter.mainloop()
Socket_con.close()
pygame.quit()
print(1,1,Pass_on_message)