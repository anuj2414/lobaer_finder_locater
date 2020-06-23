import mysql.connector
from getpass import getpass
import requests, json  
import requests
from geopy.distance import geodesic
import tkinter as tk
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
		val=(first_name1,last_name1,location1,email_id1,user_name1,password1,hieght1,streght1)
		sql="INSERT INTO customers(first_name,last_name,location ,email_id,user_name,password,height,strenght)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
		mycursor.execute(sql,val)
		mydb.commit()
		label_0 =tk.Label(master, text="successfully sotre the data",width=20,font=("bold", 20))
		label_0.place(x=300,y=400)
		print("SUCCRESS FULLY INSERTED")
	master=tk.Tk()
	master.geometry("500x500")
	frame=tk.Frame(master)
	root.title("registration")
	label_0 =tk.Label(master, text="laber_management",width=20,font=("bold", 20))
	label_0.pack()
	label_0 =tk.Label(master, text="Registration form",width=20,font=("bold", 20))
	label_0.place(x=90,y=60)
	label_1 = tk.Label(master, text="FullName",width=20,font=("bold", 10))
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
	label_8 = tk.Label(master, text="hieght",width=20,font=("bold", 10))
	label_8.place(x=70,y=350)
	entry_8 = tk.Entry(master,textvariable=ur_nm)
	entry_8.place(x=240,y=350)
	label_9 = tk.Label(master, text="strength/hourse",width=20,font=("bold", 10))
	label_9.place(x=70,y=400)
	entry_9 = tk.Entry(master,textvariable=ur_nm)
	entry_9.place(x=240,y=400)
	
	button1=tk.Button(master,text="sumbit",width=25,command=new_this)
	button1.place(x=240,y=450)
	frame.pack()
	
def retrive():	
	master1=tk.Tk()
	def thsi():
		y2=entry_2.get()
		y3=entry_3.get()
		y3=int(y3)
		T = tk.Text(master1, height=50, width=100)
		T.pack()
		print(y2)
		print(y3)
		a=[]
		a1=[]
		i=0
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
						print(x)
					a1.append(a[i])
	label_2 = tk.Label(master1, text="enter your location",width=20,font=("bold", 10))
	label_2.place(x=80,y=150)
	entry_2 = tk.Entry(master1)
	entry_2.place(x=240,y=150)
	label_3 = tk.Label(master1, text="enter your range",width=20,font=("bold", 10))
	label_3.place(x=100,y=200)
	entry_3 = tk.Entry(master1)
	entry_3.place(x=240,y=200)
	button4=tk.Button(master1,text="print",width=20,command=thsi)
	button4.place(x=150,y=350)
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
	master.geometry("500x500")
	label_0 =tk.Label(master, text="laber_management",width=20,font=("bold", 20))
	label_0.pack()
	button1=tk.Button(master,text="registration",width=25,command=registration)
	button1.place(x=80,y=200)
	button2=tk.Button(master,text="retrive",width=20,command=retrive)
	button2.place(x=200,y=200)
	k=master
	button4=tk.Button(master,text="quite",width=20,command=quite)
	button4.place(x=150,y=350)
	label_2 =tk.Label(master, text="created by ------ and her team",width=20,font=("bold", 20))
	label_2.place(x=400,y=400)

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