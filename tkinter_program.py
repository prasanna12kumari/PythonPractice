# my first program in Tkinter

from tkinter import *

# Login form 
def user_login():
    frame.grid_forget()
    
    global login_frame
    login_frame = Frame(tk, bg = 'lightsteelblue')
    login_frame.grid(padx = 100, pady = 20)

    label = Label(login_frame, text = "Login", font = 'bold',bg='lavender',fg='dodgerblue')
    label.grid(row = 0,padx = 20, pady=20)

    label1 = Label(login_frame, text = "User Name:" ,bg='lavender',fg='dodgerblue')
    label1.grid(row = 1,padx=20, pady=10)

    label2 = Label(login_frame, text = "Password:" ,bg='lavender',fg='dodgerblue')
    label2.grid(row = 3,padx=20, pady = 10)
    global entry1
    global entry2
    entry1 = Entry(login_frame)
    entry1.grid(row = 2,padx=20, pady = 10)

    entry2 = Entry(login_frame,show = '*')
    entry2.grid(row = 4, pady=10)

    button = Button(login_frame, text = "Submit" ,bg='lavender',fg='dodgerblue',command=greet_user)
    button.grid(row = 5, pady = 20)
    mainloop()
	
def greet_user():
	frame.grid_forget()
	
	entry1.delete(0, END)
	entry2.delete(0, END)
	
	global greet_frame
	greet_frame = Frame(tk,bg = 'turquoise',width = 100,height = 10)
	greet_frame.grid(padx =10,pady = 5)
	label = Label(greet_frame,text="User Register Successfully!",font ='bold',bg='lavender',fg='dodgerblue')
	label.grid(row=0,padx = 10,pady = 10)
	mainloop()

global tk
	
tk = Tk()

tk.config(bg = 'white')
tk.title('My Window')
tk.minsize(400,400) # first argument width;second argument height
# tk.minsize(300,300)


global frame

frame = Frame(tk,bg = 'white',width=100,height=500)
frame.grid(padx=100,pady=100)

button = Button(frame,text="Login",bg='steelblue',command=user_login)
button.grid(row=0,pady=20)


tk.mainloop()




