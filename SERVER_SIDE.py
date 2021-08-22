import tkinter
import socket


#Initial Socket Set up
Server = socket.socket()
Device_info = socket.gethostname()	
Ip = socket.gethostbyname(Device_info)
Port = 5050
Server.bind((Ip, Port))
Server.listen(1)
print('SEARCHING FOR DEVICES ...')
Client, Address = Server.accept()
print(f'CONNECTED TO {Address}')

#Tkinter set-up
root = tkinter.Tk()
root.title("Chatbox")
width, height = 960,540
root.geometry(f"{width}x{height}")
user_chat = []


def chat_history():
	global mesg
	global check
	check = True
	mesg = Chatbox.get()				#To get the data from the textbox
	Chatbox.delete(0,len(mesg))			#To clear text in textbox
	List_box.insert(0,'[ME]: '+mesg)	#To insert Data in the Chat history Box
	user_chat.append(mesg)
	print(user_chat)
	Client.sendall(mesg.encode())		#Relay info to client
	received_message = Client.recv(1024)	#Recieve messages
	received_message = repr(received_message)[2:-1]	#covert messages to readable form
	List_box.insert(0,'[PATIENT]'+received_message)	#Insert the message in the chatwindow


def heading():				#Basic Set up of the header
	global Heading
	Heading = tkinter.Label(root,
		font = ('Consolas',50),
		text = 'SERVER SIDE')
	Heading.place(x = width//2, y = 0)

def LstBox():				#Basic Set up of Lstbox
	global List_box
	List_box = tkinter.Listbox(root,
		width = 200,
		height = 10,
		font = 'Consolas')
	List_box.place(x = 20, y = 100)

def Chat_box():				#Basic Set up of the chatbox or inputbox
	global Chatbox
	Chatbox = tkinter.Entry(root,
		font = "Consolas",
		width = 70)
	Chatbox.place(x = 20, y = height - 100)

def Send_button():			#Basic Set up of Send button
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
Send_button()
tkinter.mainloop()
Client.close()
