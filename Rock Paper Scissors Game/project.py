import tkinter
from tkinter import *
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
import pygame
from tkinter import messagebox



#create App root
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("700x400")
root.resizable(width=0, height=0)

global name
global c_score,y_score
c_score=0
y_score=0

frame1=Frame(root,width=700,height=400,bg="#97A2FF")
frame1.pack()
frame2=Frame(root)
frame2.pack()
pygame.mixer.init()

def rock():
	pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/Click.mpeg")
	pygame.mixer.music.play(loops=0)
	
	if hand1var.get()==0 and hand2var.get()==0:
		
		hand3var.set(1)
	elif hand2var.get()==0 and hand3var.get()==0:
		
		hand1var.set(1)
	elif hand1var.get()==0 and hand3var.get()==0:
		hand2var.set(1)
	

	if hand1var.get()==1:
		
		redrock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/redrock.png')
		redrock_label= Label(frame4,image=redrock_img,bg='red')
		redrock_label.place(x=370,y=10)
		redrock_label.image=redrock_img
		
		
	elif hand3var.get()==1:
		
		hulkrock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/green rock.png')
		hulkrock_label= Label(frame4,image=hulkrock_img,bg='red')
		hulkrock_label.place(x=370,y=10)
		hulkrock_label.image=hulkrock_img
		

	elif hand2var.get()==1:
		
		bluerock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/blue rock.png')
		bluerock_label= Label(frame4,image=bluerock_img,bg='red')
		bluerock_label.place(x=370,y=10)
		bluerock_label.image=bluerock_img

	user_choice="rock"
	ls=["rock","paper","scissors"]
	ran=randint(0,2)
	computer_choice=ls[ran]
	compselected.set(ls[ran])
	userselected.set(user_choice)
	global c_score , y_score

	if ls[ran]=="rock":
		comprock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp rock.png')
		comprock_label= Label(frame3,image=comprock_img,bg='blue')
		comprock_label.place(x=370,y=-40)
		comprock_label.image=comprock_img
		

	if ls[ran]=="paper":
		comppaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp paper.png')
		comppaper_label= Label(frame3,image=comppaper_img,bg='blue')
		comppaper_label.place(x=370,y=-40)
		comppaper_label.image=comppaper_img
		c_score=c_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)
		

	if ls[ran]=="scissors":
		compscissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp scissors.png')
		compscissors_label= Label(frame3,image=compscissors_img,bg='blue')
		compscissors_label.place(x=370,y=-40)
		compscissors_label.image=compscissors_img
		y_score=y_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)

	if c_score==5 or y_score==5:
		frame3.destroy()
		frame4.destroy()
		root.geometry("600x400")
		root.resizable(width=0, height=0)
		global frame5
		frame5=Frame(root,height=700,width=700,bg="Yellow")
		frame5.pack()
		myFont2 = font.Font(size=70,weight='bold',family="Copperplate")
		if c_score==5:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/lose.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Blue"
			labelsample=Label(frame5,text="You lost!",font=myFont2,bg="Blue",fg="White")
			labelsample.place(x=120,y=150)
		else:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/winning.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Red"
			labelsample2=Label(frame5,text="You Won!",font=myFont2,bg="Red",fg="White")
			labelsample2.place(x=120,y=150)
	

'''
	print("Hello")
	redrock=tk.PhotoImage(file="/Users/soumyyaa_jain/Downloads/red rock.png")
	print(redrock)
	label1 = tk.Label(frame4,image=redrock)
	label1.place(x=290,y=10)
'''


def paper():
	pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/Click.mpeg")
	pygame.mixer.music.play(loops=0)
	if hand1var.get()==0 and hand2var.get()==0:
		
		hand3var.set(1)
	elif hand2var.get()==0 and hand3var.get()==0:
		
		hand1var.set(1)
	elif hand1var.get()==0 and hand3var.get()==0:
		hand2var.set(1)
	

	if hand1var.get()==1:
		
		redpaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/red paper.png')
		redpaper_label= Label(frame4,image=redpaper_img,bg='red')
		redpaper_label.place(x=370,y=10)
		redpaper_label.image=redpaper_img
		
		
	elif hand3var.get()==1:
		
		hulkpaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/green paper.png')
		hulkpaper_label= Label(frame4,image=hulkpaper_img,bg='red')
		hulkpaper_label.place(x=370,y=10)
		hulkpaper_label.image=hulkpaper_img
		

	elif hand2var.get()==1:
		
		bluepaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/blue paper.png')
		bluepaper_label= Label(frame4,image=bluepaper_img,bg='red')
		bluepaper_label.place(x=370,y=10)
		bluepaper_label.image=bluepaper_img


	user_choice="paper"
	ls=["rock","paper","scissors"]
	ran=randint(0,2)
	computer_choice=ls[ran]
	compselected.set(ls[ran])
	userselected.set(user_choice)
	global c_score,y_score

	if ls[ran]=="rock":
		comprock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp rock.png')
		comprock_label= Label(frame3,image=comprock_img,bg='blue')
		comprock_label.place(x=370,y=-40)
		comprock_label.image=comprock_img
		y_score=y_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)
		

	if ls[ran]=="paper":
		comppaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp paper.png')
		comppaper_label= Label(frame3,image=comppaper_img,bg='blue')
		comppaper_label.place(x=370,y=-40)
		comppaper_label.image=comppaper_img
		

	if ls[ran]=="scissors":
		compscissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp scissors.png')
		compscissors_label= Label(frame3,image=compscissors_img,bg='blue')
		compscissors_label.place(x=370,y=-40)
		compscissors_label.image=compscissors_img
		c_score=c_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)

	if c_score==5 or y_score==5:
		frame3.destroy()
		frame4.destroy()
		root.geometry("600x400")
		root.resizable(width=0, height=0)
		global frame5
		frame5=Frame(root,height=700,width=700,bg="Yellow")
		frame5.pack()
		myFont2 = font.Font(size=70,weight='bold',family="Copperplate")
		if c_score==5:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/lose.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Blue"
			labelsample=Label(frame5,text="You lost!",font=myFont2,bg="Blue",fg="White")
			labelsample.place(x=120,y=150)
		else:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/winning.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Red"
			labelsample2=Label(frame5,text="You Won!",font=myFont2,bg="Red",fg="White")
			labelsample2.place(x=120,y=150)
		



def scissors():
	pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/Click.mpeg")
	pygame.mixer.music.play(loops=0)
	global c_score , y_score
	if hand1var.get()==0 and hand2var.get()==0:
		
		hand3var.set(1)
	elif hand2var.get()==0 and hand3var.get()==0:
		
		hand1var.set(1)
	elif hand1var.get()==0 and hand3var.get()==0:
		hand2var.set(1)
	

	if hand1var.get()==1:
		
		redscissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/red scissors.png')
		redscissors_label= Label(frame4,image=redscissors_img,bg='red')
		redscissors_label.place(x=370,y=10)
		redscissors_label.image=redscissors_img
		
		
	elif hand3var.get()==1:
		
		hulkscissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/green scissors.png')
		hulkscissors_label= Label(frame4,image=hulkscissors_img,bg='red')
		hulkscissors_label.place(x=370,y=10)
		hulkscissors_label.image=hulkscissors_img
		

	elif hand2var.get()==1:
		
		bluescissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/blue scissors.png')
		bluescissors_label= Label(frame4,image=bluescissors_img,bg='red')
		bluescissors_label.place(x=370,y=10)
		bluescissors_label.image=bluescissors_img

	user_choice="scissors"
	ls=["rock","paper","scissors"]
	ran=randint(0,2)
	computer_choice=ls[ran]
	compselected.set(ls[ran])
	userselected.set(user_choice)

	if ls[ran]=="rock":
		comprock_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp rock.png')
		comprock_label= Label(frame3,image=comprock_img,bg='blue')
		comprock_label.place(x=370,y=-40)
		comprock_label.image=comprock_img
		c_score=c_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)
		

	if ls[ran]=="paper":
		comppaper_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp paper.png')
		comppaper_label= Label(frame3,image=comppaper_img,bg='blue')
		comppaper_label.place(x=370,y=-40)
		comppaper_label.image=comppaper_img
		y_score=y_score+1
		comppoints.set(c_score)
		userpoints.set(y_score)
		

	if ls[ran]=="scissors":
		compscissors_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/PP Project/comp scissors.png')
		compscissors_label= Label(frame3,image=compscissors_img,bg='blue')
		compscissors_label.place(x=370,y=-40)
		compscissors_label.image=compscissors_img

	if c_score==5 or y_score==5:
		frame3.destroy()
		frame4.destroy()
		root.geometry("600x400")
		root.resizable(width=0, height=0)
		global frame5
		frame5=Frame(root,height=700,width=700,bg="Yellow")
		frame5.pack()
		myFont2 = font.Font(size=70,weight='bold',family="Copperplate")
		if c_score==5:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/lose.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Blue"
			labelsample=Label(frame5,text="You lost!",font=myFont2,bg="Blue",fg="White")
			labelsample.place(x=120,y=150)
		else:
			pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/winning.mpeg")
			pygame.mixer.music.play(loops=0)
			frame5["bg"]="Red"
			labelsample2=Label(frame5,text="You Won!",font=myFont2,bg="Red",fg="White")
			labelsample2.place(x=120,y=150)

		

def my_command(num):
	pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/Click.mpeg")
	pygame.mixer.music.play(loops=0)
	name=str(name_entrytext.get())
	if num==1:
		hand1var.set(1)
	elif num==2:
		hand2var.set(1)
	elif num==3:
		hand3var.set(1)

	next_button= Button(frame1, text= "",command=frame1destroy,fg="Black",bg="#E69A8D",font=myFontframe1)
	next_button["highlightbackground"]="Black"
	#next_button["highlightbackground"]="#8FE381"
	#next_button["highlightthickness"]=5
	next_button.place(x=340,y=350)
	next_button.config(text= "Next")
	


def frame1destroy():
	if name_entrytext.get()=="":
		messagebox.showwarning("Empty Fields","Name cannot be left blank")
	else:
		pygame.mixer.music.load("/Users/soumyyaa_jain/Desktop/PP Project/Click.mpeg")
		pygame.mixer.music.play(loops=0)
		name=str(name_entrytext.get())
		#frame 1 is destroyed 
		frame1.destroy()

		root.geometry("1000x700")
		root.resizable(width=0, height=0)

		global frame3,frame4

		frame3=Frame(root,height=350,width=1000,bg='Blue')
		frame3.pack()

		frame4=Frame(root,height=350,width=1000,bg='Red')
		frame4.pack()

		myFontlabel = font.Font(size=23,weight='bold',family="Krungthep")

		name_label=Label(frame4,text=name,font=myFontlabel,fg="white",bg="red")
		name_label.place(x=0,y=0)

		
		comp_label=Label(frame3,text="Computer",bg="blue",font=myFontlabel,fg="white")
		comp_label.place(x=0,y=0)

		myFont = font.Font(size=20,weight='bold',family="Helvetica")

		rock_button=Button(frame4,text="Rock",command=rock,height=1,fg="Red")
		rock_button["highlightbackground"]="Black"
		rock_button["highlightthickness"]=5
		rock_button.place(x=800,y=300)
		rock_button['font']=myFont

		paper_button=Button(frame4,text="Paper",command=paper,height=1,width=5,fg="Red")
		paper_button["highlightbackground"]="Black"
		paper_button["highlightthickness"]=5
		paper_button.place(x=700,y=300)
		paper_button['font']=myFont

		scissors_button=Button(frame4,text="Scissors",command=scissors,height=1,width=7,fg="Red")
		scissors_button["highlightbackground"]="Black"
		scissors_button["highlightthickness"]=5
		scissors_button.place(x=890,y=300)
		scissors_button['font']=myFont

		scoreboard_label=Label(frame3,text="Scoreboard",font=myFont,width=16,bg="Yellow",relief="raised",borderwidth=2)
		scoreboard_label['highlightbackground']="Grey"
		scoreboard_label.place(x=700,y=70)

		selected_label=Label(frame3,text="Selected:",width=11,relief="raised",borderwidth=2,font=("Helvica",13,'bold'))
		selected_label.place(x=700,y=100.5)

		global compselected,comppoints

		compselected=StringVar()
		compselected_label=Label(frame3,width=10,textvariable=compselected,relief="raised",borderwidth=2,fg="Blue",font=("Helvica",13,'bold'))
		compselected_label.place(x=802,y=100.5)

		points_label=Label(frame3,text="Points:",height=3,width=11,relief="raised",borderwidth=2,font=("Helvica",13,'bold'))
		points_label.place(x=700,y=125)

		comppoints=IntVar()
		comppoint_label=Label(frame3,height=3,width=10,textvariable=comppoints,font=("Helvica",13,'bold'),relief="raised",borderwidth=2,fg="Blue")
		comppoint_label.place(x=802,y=125)

		scoreboard_label_user=Label(frame4,text="Scoreboard",font=myFont,width=16,bg="Yellow",relief="raised",borderwidth=2)
		scoreboard_label_user['highlightbackground']="Grey"
		scoreboard_label_user.place(x=80,y=100)

		selected_label_user=Label(frame4,text="Selected:",width=11,relief="raised",borderwidth=2,font=("Helvica",13,'bold'))
		selected_label_user.place(x=80,y=130)

		global userselected,userpoints

		userselected=StringVar()
		userselected_label=Label(frame4,width=10,textvariable=userselected,relief="raised",borderwidth=2,fg="Red",font=("Helvica",13,'bold'))
		userselected_label.place(x=181,y=130)

		points_label_user=Label(frame4,text="Points:",height=3,width=11,relief="raised",borderwidth=2,font=("Helvica",13,'bold'))
		points_label_user.place(x=80,y=153)

		userpoints=IntVar()
		userpoint_label=Label(frame4,height=3,width=10,textvariable=userpoints,font=("Helvica",13,'bold'),relief="raised",borderwidth=2,fg="Red")
		userpoint_label.place(x=181,y=153)


myFontframe1 = font.Font(size=16,family="DIN Alternate",weight='bold')

name_label=Label(frame1,text="Enter your name: ",bg="#97A2FF",font=myFontframe1)
name_label.place(x=180,y=80)

myFontname = font.Font(size=16,family="Ayuthaya")


name_entrytext=Entry(frame1,bg="#97A2FF",font=myFontname)
name_entrytext.place(x=330,y=77)



hand1_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/Picture 1.png')


hand1_label= Label(image=hand1_img)


hand1var=IntVar()
hand1_button= Button(frame1, image=hand1_img,command= lambda:my_command(1),borderwidth=0,textvariable=hand1var)
hand1_button["highlightbackground"]="#97A2FF"
hand1_button.place(x=200,y=160)


hand2_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/Picture 5 copy.png')


hand2_label= Label(image=hand2_img)


hand2var=IntVar()
hand2_button= Button(frame1, image=hand2_img,command= lambda:my_command(2),borderwidth=0,textvariable=hand2var)
hand2_button["highlightbackground"]="#97A2FF"
hand2_button.place(x=330,y=160)

hand3_img= PhotoImage(file='/Users/soumyyaa_jain/Desktop/Picture 6.png')


hand3_label= Label(image=hand3_img)


hand3var=IntVar()
hand3_button= Button(frame1, image=hand3_img,command= lambda:my_command(3),borderwidth=0,textvariable=hand3var)
hand3_button["highlightbackground"]="#97A2FF"
hand3_button["highlightthickness"]=2
hand3_button.place(x=460,y=160)

heading_label=Label(frame1,text="~~~~Select your hand~~~~",bg="#97A2FF",font=myFontframe1,fg="white")
heading_label.place(x=260,y=123)

myFontmain = font.Font(size=40,family="Luminari",weight='bold')
main_label=Label(frame1,text='Rock Paper Scissors',bg="#97A2FF",font=myFontmain,fg='#362951')
main_label.place(x=155,y=5)


root.mainloop()





 
