import mysql.connector
from getpass import getpass
import requests, json  
import requests
from geopy.distance import geodesic
import tkinter as tk
import re
import tkinter.messagebox
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="")
mycursor = mydb.cursor()
mycursor.execute("use laber")
def registration():
	def new_this():
		first_name1=entry_1.get()
		last_name1=entry_2.get()
		email_id1=entry_4.get()
		gen=entry_5.get()
		location1=entry_6.get()
		user_name1=entry_7.get()
		hieght1=entry_8.get()
		streght1=entry_9.get()
		password1="1n23"
		category1=entry_10.get()
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		r=['plumber','electrecian','laber','cooker']
		s="@gmail.com"
		#if category1 not in r or type(first_name1)!=str or re.search(regex,email_id1) or type(last_name1)!=str or type(location1)!=str or type(hieght1)!=int or type(streght1)!=str:
		if first_name1=='' or last_name1=='' or email_id1=='' or gen=='' or location1=='' or user_name1=='' or streght1=='' or category1=='':
			tk.messagebox.showerror("input is not valid", "fill value")
		elif s not in email_id1:
			tk.messagebox.showerror("input is not valid", "Error email")
		elif category1 not in r:
			tk.messagebox.showerror("input is not valid", "fill right category")
		else:
			val=(first_name1,last_name1,location1,email_id1,user_name1,password1,hieght1,streght1)
			sql="INSERT INTO customers(first_name,last_name,location ,email_id,user_name,password,height,strenght,category)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			mycursor.execute(sql,val)
			mydb.commit()
			label_0 =tk.Label(master, text="successfully sotre the data",width=20,font=("bold", 20))
			label_0.place(x=300,y=400)
			print("SUCCRESS FULLY INSERTED")
	master=tk.Tk()
	master.geometry("600x600")
	master.resizable(width=False, height=False)
	frame=tk.Frame(master)
	root.title("registration")
	label_0 =tk.Label(master, text="ADVANCED LABOUR MANAGEMTN",fg='green', bg='black',width=25,font=("bold", 20))
	label_0.pack()
	label_0 =tk.Label(master, text="Registration form",width=20,fg='green', bg='black',font=("bold", 15))
	label_0.place(x=120,y=60)
	label_1 = tk.Label(master, text="FirstName",width=20,font=("bold", 10))
	label_1.place(x=80,y=130)
	entry_1 = tk.Entry(master,textvariable=flnm)
	entry_1.place(x=240,y=130)
	label_2 = tk.Label(master, text="last_name",width=20,font=("bold", 10))
	label_2.place(x=80,y=150)

	entry_2 = tk.Entry(master,textvariable=lnm)
	entry_2.place(x=240,y=150)

	label_3 = tk.Label(master, text="Email",width=20,font=("bold", 10))
	label_3.place(x=68,y=180)

	entry_4 = tk.Entry(master,textvariable=eml)
	entry_4.place(x=240,y=180)

	label_5 = tk.Label(master, text="Gender",width=20,font=("bold", 10))
	label_5.place(x=70,y=230)
	entry_5 = tk.Entry(master)
	entry_5.place(x=235,y=230)

	label_6 = tk.Label(master, text="locaiton",width=20,font=("bold", 10))
	label_6.place(x=70,y=280)
	entry_6 = tk.Entry(master,textvariable=loct)
	entry_6.place(x=240,y=280)
	label_7 = tk.Label(master, text="user_name",width=20,font=("bold", 10))
	label_7.place(x=70,y=300)
	entry_7 = tk.Entry(master,textvariable=ur_nm)
	entry_7.place(x=240,y=300)
	label_8 = tk.Label(master, text="contact_no",width=20,font=("bold", 10))
	label_8.place(x=70,y=350)
	entry_8 = tk.Entry(master,textvariable=ur_nm)
	entry_8.place(x=240,y=350)
	label_10 = tk.Label(master, text="category",width=20,font=("bold", 10))
	label_10.place(x=70,y=400)
	entry_10 = tk.Entry(master)
	entry_10.place(x=240,y=400)
	label_9 = tk.Label(master, text="strength/hours",width=20,font=("bold", 10))
	label_9.place(x=70,y=450)
	entry_9 = tk.Entry(master,textvariable=ur_nm)
	entry_9.place(x=240,y=450)
	r=1
	button1=tk.Button(master,text="sumbit",width=25,fg='green', bg='black',foreground='black',background='red', highlightbackground='#3E4149',command=new_this)
	button1.place(x=240,y=480)
	frame.pack()
	
def retrive():	
	master1=tk.Tk()
	master1.geometry("700x700")
	master1.resizable(width=False, height=False)
	def thsi():
		def thisoneone(A3):
			A3=A3
			print(A3)
			#a=open(s,'w')
			f = open("thisone1.txt", 'w')
			for t in A3:
				line = ' '.join(str(x) for x in t)
				f.write(line + '\n')
			f.close()
			label_3 = tk.Label(master1, text="txt file created",width=40,font=("bold", 10))
			label_3.place(x=300,y=400)
		y2=entry_2.get()
		y3=entry_3.get()
		y4=entry_5.get()
		r=['plumber','electrecian','laber','cooker']
		if y2=='' or y3=='' or y4=='':
			tk.messagebox.showerror("input is not valid", "Error text")
		elif y4 not in r:
			tk.messagebox.showerror("input is not valid", "Error category")
		else:
			y3=int(y3)
			T = tk.Text(master1, height=20, width=80)
			T.pack()
			print(y2)
			print(y3)
			a=[]
			a1=[]
			i=0
			A3=[]
			o=1
			#sql2="SELECT location FROM customers WHERE location=%s"
			mycursor.execute("SELECT location FROM customers")
			myresult=mycursor.fetchall()
			for x in myresult:
				i=i+1
				a.append(x)	
			for i in range(i):
				r2=a[i]
				r1=distance(r2,y2)
				if r1<=y3:
					if a[i] not in a1:
						q=a[i]
						sql12="SELECT * FROM customers WHERE location=%s"
						mycursor.execute(sql12,q)
						myresult=mycursor.fetchall()
						for x  in myresult:
							T.insert(tk.END,x)
							T.insert(tk.END,"\n")
							o=2
							print(x)
							A3.append(x)
						a1.append(a[i])
			if o==2:
				button4=tk.Button(master1,text="download",width=20,command=thisoneone(A3))
	label_0 =tk.Label(master1, text="ADVANCED LABOUR MANAGEMTN",fg='green', bg='black',width=25,font=("bold", 20))
	label_0.pack()
	label_2 = tk.Label(master1, text="enter your location",width=20,font=("bold", 10))
	label_2.place(x=80,y=150)
	entry_2 = tk.Entry(master1)
	entry_2.place(x=240,y=150)
	label_3 = tk.Label(master1, text="enter your range",width=20,font=("bold", 10))
	label_3.place(x=80,y=200)
	entry_3 = tk.Entry(master1)
	entry_3.place(x=240,y=200)
	label_6 = tk.Label(master1, text="builder,plumber,electrician",fg='green',width=35,font=("bold", 15))
	label_6.place(x=60,y=250)
	label_5 = tk.Label(master1, text="category",width=35,font=("bold", 10))
	label_5.place(x=40,y=300)
	entry_5= tk.Entry(master1)
	entry_5.place(x=240,y=300)
	button4=tk.Button(master1,text="result",width=20,fg='green', bg='black',foreground='black',background='red', highlightbackground='#3E4149',command=thsi)
	button4.place(x=150,y=360)
def quite():
	pass
def distance(y1,y2):

	url = "https://trueway-geocoding.p.rapidapi.com/Geocode"
	r=y1
	querystring = {"language":"en","country":"india","address":r}

	headers = {
		'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com",
		'x-rapidapi-key': "2f13ffd4f4mshf71e2009decaa49p1ff74djsn3e5cf5c67cb2"
		}

	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)
	r=response.json()
	r1=r['results']
	for r3 in r1:
		lat=r3['location']['lat']
		lng=r3['location']['lng']
	#print(lat)
	#print(lng)
	r2=y2
	querystring = {"language":"en","country":"india","address":r2}

	headers = {
		'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com",
		'x-rapidapi-key': "2f13ffd4f4mshf71e2009decaa49p1ff74djsn3e5cf5c67cb2"
		}

	response = requests.request("GET", url, headers=headers, params=querystring)

	#print(response.text)
	r=response.json()
	r1=r['results']
	for r3 in r1:
		lat1=r3['location']['lat']
		lng2=r3['location']['lng']
	d1=(lat,lng)
	d2=(lat1,lng2)
	s1=geodesic(d1,d2).km
	s1=int(s1)
	return s1
def main_screen(master):
	master=master
	master.geometry("600x600")
	master.resizable(width=False, height=False)
	label_0 =tk.Label(master, text="ADVANCED LABOUR MANAGEMTN",width=35,fg='green', bg='black',font=("bold", 20))
	label_0.pack()
	button1=tk.Button(master,text="registration",width=23,fg='green', bg='black',foreground='black', background='red',command=registration)
	button1.place(x=60,y=200)
	button2=tk.Button(master,text="retrive",width=20,fg='green', bg='black',foreground='black', highlightbackground='#3E4149',background='red',command=retrive)
	button2.place(x=360,y=200)
	k=master
	button4=tk.Button(master,text="quit",width=20,fg='green', bg='black',foreground='black', background='red',command=master.destroy)
	button4.place(x=200,y=350)
	label_2 =tk.Label(master, text="created by SRITIAN STUDENT",width=35,fg='green', bg='black',font=("bold", 15))
	label_2.place(x=250,y=550)

root=tk.Tk()
flnm=tk.StringVar()
lnm=tk.StringVar()
eml=tk.StringVar()
var= tk.IntVar()
loct=tk.StringVar()
ur_nm=tk.StringVar()
root.geometry("500x500")
r1=1
main_screen(root)
root.mainloop()