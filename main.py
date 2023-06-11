from tkinter import OptionMenu,StringVar, Button,Radiobutton,Tk,Label,IntVar,DISABLED,Text,INSERT,END,Frame,Entry
from PIL import ImageTk,Image
import webbrowser
import matplotlib.pyplot as plt
import numpy as np
import csv
plot_list=['2019-2020.csv','2018-2019.csv','2017-2018.csv','2016-2017.csv','2015-2016.csv','2014-2015.csv','2013-2014.csv']
def plots(i):
	global plot_list
	x = []
	y = []
	with open(plot_list[i],'r') as csvfile:
		plots = csv.reader(csvfile, delimiter = ',')
		for row in plots:
			x.append(row[0])
			y.append(int(row[1]))
	plt.bar(x, y, color = 'r', width = 0.72, label = "number of students placed")
	plt.xlabel('Branch')
	plt.ylabel('Number of students placed')
	plt.title('placement statistics'+plot_list[i][:-4])
	plt.legend()
	plt.xticks(rotation = 90)
	plt.show()


def plot():
	root2=Tk()
	Label(root2,text="SELECT THE ACADEMIC YEAR",padx=10,pady=10,fg='blue',bg='yellow').pack()
	Button(root2,text='2020-2021',command=lambda : plots(0)).pack()
	Button(root2,text='2019-2020',command=lambda : plots(1)).pack()
	Button(root2,text='2017-2018',command=lambda : plots(2)).pack()
	Button(root2,text='2016-2017',command=lambda : plots(3)).pack()
	Button(root2,text='2015-2016',command=lambda : plots(4)).pack()
	Button(root2,text='2014-2015',command=lambda : plots(5)).pack()
	Button(root2,text='2018-2019',command=lambda : plots(6)).pack()
	root2.mainloop()
def CDC_EVENTS():
	win = Tk()
	win.geometry("500x500")
	win.title('CDC_EVENTS')
	def show():
		x=clicked.get()
		if "2010-2011"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2010-11.pdf'
            
			webbrowser.open_new(path)
		elif "2011-2012"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2011-12.pdf'
			webbrowser.open_new(path)
		elif "2012-2013"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2012-13.pdf' 
			webbrowser.open_new(path)
		elif "2013-2014"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2013-14.pdf'
			webbrowser.open_new(path)
		elif "2014-2015"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2014-15.pdf'
			webbrowser.open_new(path)
       
		elif "2015-2016"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2015-16.pdf'
			webbrowser.open_new(path)
       
		elif "2016-2017"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2016-17.pdf'
			webbrowser.open_new(path)
		elif "2017-2018"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2017-18.pdf'
			webbrowser.open_new(path)
		elif "2018-2019"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2018-19.pdf'
			webbrowser.open_new(path)
		elif "2019-2020"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2019-20.pdf'
			webbrowser.open_new(path)
		elif "2020-2021"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/PC-List-2020-21.pdf'
			webbrowser.open_new(path)
		elif "2021-2022"==x:
			path ='https://cbit.ac.in/wp-content/uploads/2019/12/PC-List-2021-22.pdf'
			webbrowser.open_new(path)
		elif "2022-2023"==x:
			path ='https://cbit.ac.in/wp-content/uploads/2019/12/PLacement-Coordinators-list-2022-23.pdf'
			webbrowser.open_new(path) 
	options = ["2010-2011","2011-2012","2012-2013","2013-2014","2014-2015","2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021","2021-2022","2022-2023"]
	clicked = StringVar()
	clicked.set("Select the academic year")
	drop = OptionMenu(win, clicked, *options)
	drop.pack()
	button = Button(win, text="Get Details", command=show).pack()
	win.mainloop()
def CDC_STAFF():
	win = Tk()
	win.geometry("500x500")
	win.title('CDC_STAFF')
	def show():
		x=clicked.get()
		if "2013"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2013.pdf'
			webbrowser.open_new(path)
		elif "2014"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2014.pdf'
			webbrowser.open_new(path)
		elif "2015"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2015.pdf'
			webbrowser.open_new(path)
		elif "2016"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2016.pdf'
			webbrowser.open_new(path)
		elif "2017"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2017.pdf'
			webbrowser.open_new(path)
		elif "2018"==x:
			path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2018.pdf'
			webbrowser.open_new(path)
		elif "2019"==x:
			path ='https://www.cbit.ac.in/wp-content/uploads/2019/12/Events-2019.pdf'
			webbrowser.open_new(path)
		elif "2020"==x:
			path ='https://cbit.ac.in/wp-content/uploads/2019/12/Events-2020.pdf'
			webbrowser.open_new(path)
		elif "2021"==x:
			path ='https://cbit.ac.in/wp-content/uploads/2019/12/Events-2021.pdf'
			webbrowser.open_new(path)
        
	options = ["2013","2014","2015","2016", "2017", "2018", "2019", "2020", "2021"]
	clicked = StringVar()
	clicked.set("Select the academic year")
	drop = OptionMenu(win, clicked, *options)
	drop.pack()
	button = Button(win, text="Get Details", command=show).pack()
	win.mainloop()


def NoticeBoard():
    noticeboard=Tk()
    noticeboard.title('NoticeBoard')
    noticeboard.geometry("500x500")
    def links(i):
        webbrowser.open_new(list_paths[i])
    
    Label(noticeboard,text='Industry Linkage Placement Information',font=('consolas','14'),padx=3).place(x=0,y=0)

    list_buttons=['> Placement Circulars Barclays PPT, online Exam & Interviews Placement Circular on 16 & 18.08.2022',
        '> Gain Sight Software Pvt Ltd Placement Circular on 11.08.2022',
        '> Micron Interviews Placement Circular on 09.08.2022',
        '> Infosys (S.E. Role) Online Exam  Placement Circular on 07.08.2022',
        '> Micron PPT, online Exam & Interview Placement Circular on 03, 04 & 09.08.2022',
        '> Oracle PPT & Interviews Placement Circular on 29.07.2022',
        '> Furures First Personal Interviews (Round1)  Placement Circular on 28.07.2022',
        '> Servicenow PPT Placement Circular on 14.07.2022',
        '> Bureau Veritas India Pvt. Ltd.s Online Exam Placement Circular on 09.07.2022',
        '> Electronics Arts Online Test Placement Circular on 08.07.2022',
        '> Cognizant GenC Next Technical Interview Placement Circular on 02.07.2022',
        '> Berkadia – Interview Placement Circular on 01.07.2022','> Neuland Labs PPT, Written Test & Interviews Placement Circular on 29.06.2022',
    '> Infosys Student Interaction Session Placement Circular on 04.07.2022',
    ]
    Label(noticeboard,text='Placement Circulars',font=('consolas',14)).place(x=0,y=25)
    Button(noticeboard,text=list_buttons[0],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(0)).place(x=0,y=60)
    Button(noticeboard,text=list_buttons[1],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(1)).place(x=0,y=85)
    Button(noticeboard,text=list_buttons[2],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(2)).place(x=0,y=110)
    Button(noticeboard,text=list_buttons[3],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(3)).place(x=0,y=135)
    Button(noticeboard,text=list_buttons[4],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(4)).place(x=0,y=160)
    Button(noticeboard,text=list_buttons[5],font=('arial',10),cursor="hand2",pady=0,padx=0,borderwidth=0,command=lambda :links(5)).place(x=0,y=185)
    Button(noticeboard,text=list_buttons[6],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(6)).place(x=0,y=210)
    Button(noticeboard,text=list_buttons[7],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(7)).place(x=0,y=235)
    Button(noticeboard,text=list_buttons[8],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(8)).place(x=0,y=260)
    Button(noticeboard,text=list_buttons[9],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(9)).place(x=0,y=285)
    Button(noticeboard,text=list_buttons[10],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(10)).place(x=0,y=310)
    Button(noticeboard,text=list_buttons[11],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(11)).place(x=0,y=335)
    Button(noticeboard,text=list_buttons[12],font=('arial',10),cursor='hand2',pady=0,padx=0,borderwidth=0,command=lambda :links(12)).place(x=0,y=360)
    Button(noticeboard,text=list_buttons[13],font=('arial',10),cursor='hand2',padx=0,pady=0,borderwidth=0,command=lambda :links(12)).place(x=0,y=385)
    list_paths=['https://www.cbit.ac.in/wp-content/uploads/2019/12/Barclays-PPT-online-Exam-Interviews-Placement-Circular-on-16-18.08.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Gainsight-Software-Pvt-Ltd-Placement-Circular-on-11.08.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Micron-Interviews-Placement-Circular-on-09.08.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Infosys-S.E.-Role-Online-Exam-Placement-Circular-on-07.08.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Micron-PPT-online-Exam-Interview-Placement-Circular-on-03-04-09.08.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Oracle-PPT-Interviews-Placement-Circular-on-29.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Furures-First-Personal-Interviews-Round1-Placement-Circular-on-28.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Servicenow-PPT-Placement-Circular-on-14.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Bureau-Veritas-India-Pvt.-Ltd.s-Online-Exam-Placement-Circular-on-09.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Electronics-Arts-Online-Test-Placement-Circular-on-08.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Cognizant-GenC-Next-Technical-Interview-Placement-Circular-on-02.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Berkadia-Interview-Placement-Circular-on-01.07.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Neuland-Labs-PPT-Written-Test-Interviews-Placement-Circular-on-29.06.2022.pdf',
                'https://www.cbit.ac.in/wp-content/uploads/2019/12/Infosys-Student-Interaction-Session-Placement-Circular-on-04.07.2022.pdf']

    noticeboard.mainloop()  
       
def Objectives():
    objective=Tk()
    objective.geometry("500x500")
    Label(objective,text="CAREER CENTRE OBJECTIVES",font=('consolas',20),bg='blue',padx=5,pady=5).place(x=470,y=0)
    frame=Frame(objective,height=550,width=600+600,bg='yellow').place(x=100,y=50)
    text1='> To make CBIT the favorite destination for all multinational companies\n> To establish state of the art in house training facility for honing the skills of the students.\n> To build CBIT brand value in the corporate world.\n> Plan more industry-institution interactions to benefit students and faculty.\n> Establishing exclusive Life Skill Lab for soft skills & technical skills.\n> Strive towards 100% placements.\n> To improve on our Previous Rankings (9th Rank – 2019 Ranking Source: Chronicle Survey, August 2019 edition, 29th Rank – 2019 Ranking Source: Times Engineering, Magazine July 2019 edition, 36th Rank – 2019 Ranking Source: OUTLOOK Magazine June 2019 Edition, & 50th Rank – 2019 ranking Source: THE WEEK Magazine 16th June 2019 edition) in placements among the top 100 engineering colleges in the country.\n> Introducing video conferencing with industry experts & successful alumni to create\n> Awareness for Campus to Corporate Transformation.\n> Introducing biometric attendance for monitoring attendance for each placement.\n> Broad basing the existing list of companies.\n> Scheduling training programs from 1st year to prepare students to cater corporate needs & requirements.\n> Adopting into Digital Technologies. '
    text2=Text(objective)
    text2.place(x=330,y=60)
    text2.insert(INSERT,text1)
    text2.configure(state='disabled')
    objective.mainloop()
def intership_guidelines():
    intership=Tk()
    intership.geometry("500x500")
    Label(intership,text="INTERSHIP GUIDELINES",font=('consolas',20),bg='blue',padx=0,pady=0).place(x=470,y=0)
    Label(intership,text='intership guidelines',font=('consolas',16)).place(x=300+100,y=55)
    Button(intership,padx=0,pady=0,text='veiw document',font=('consolas',16),command=lambda :webbrowser.open_new('https://www.cbit.ac.in/placement_post/internship-guidelines/')).place(x=650,y=50)
    frame=Frame(intership,height=550,width=600+550,bg='yellow').place(x=100,y=110)
    text1='> Official Mail from the Company Offering Internship.\n> Affidavit on Rs. 100 Stamp Paper duly signed by the Students & Parent.\n> The affidavit should carry Parent & Student, Mobile No. & E-mail id along with the signature.\n> Original Affidavit copy to the submitted to the HOD along with official mail copy from the company carrying signatures of Director – CDC & Director – AEC.\n> Photocopy of Affidavit along with Company mail to be submitted at Director – CDC & Director – AEC Office.\n> Acknowledgment to be taken from concerned HOD, Director – CDC & Director – AEC.\n> Retain one photocopy carrying signatures of HOD, Director – CDC & Director – AEC.\n'
    text2=Text(intership)
    text2.place(x=330,y=150)
    text2.insert(INSERT,text1)
    text2.configure(state='disabled')
    Label(intership,text="INTERSHIP PROCEDURE",font=('consolas',16),bg='blue',padx=0,pady=0).place(x=495,y=110)

    intership.mainloop()
def company_eligibilty():
    
    win = Tk()
    win.title('Company Eligibility')
    win.geometry("500x500")
    def show():
        if (clicked.get())=="2015-2016":
            path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-2015-2016.pdf'
            webbrowser.open_new(path)
        elif (clicked.get())=="2016-2017":
            path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-2016-2017.pdf'
            webbrowser.open_new(path)
        elif (clicked.get())=="2017-2018":
            path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-2017-2018.pdf'
            webbrowser.open_new(path)
        elif (clicked.get())== "2018-2019":
            path = 'https://www.cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-2018-2019.pdf'
            webbrowser.open_new(path)
        elif  (clicked.get())=="2019-2020":
            path = 'https://cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-Criteria-2019-2020.pdf'
            webbrowser.open_new(path)
        elif (clicked.get())=="2020-2021":
            path = 'https://cbit.ac.in/wp-content/uploads/2019/12/Company-Wise-Eligibility-Criteria-2020-2021In-Progress.pdf'
            webbrowser.open_new(path)

    options = ["2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021"]
    clicked = StringVar()
    text="Select the academic year"
    clicked.set(text)
    drop = OptionMenu(win, clicked, *options)
    drop.pack()
    button = Button(win, text="Get Details", command=show).pack()
    win.mainloop()      


root=Tk()
root['bg']='#addaec'
root.iconbitmap(r"imageicon.jpg")# title image of cbit
root.title('BATCH-4,CSE-2,Nithya,Hindu,Meghana,Sreemuki,Swathi')
image1 = Image.open(r"image.jpg")
test = ImageTk.PhotoImage(image1)

label1 = Label(image=test)
label1.image = test

# Position image
label1.place(x=0, y=0)
Label(text='CHAITANYA BHARATHI INSTITUTE OF TECHNOLOGY\n PLACEMENT MANAGEMENT SYSTEM',padx=420,pady=2,fg='blue',font=('courier','14'),highlightthickness='2',bg="#63C5DA").place(x=50,y=0)
image1=Image.open(r"placement1.png")
test = ImageTk.PhotoImage(image1)
cbit_images = Label(image=test,padx=0,pady=0)
cbit_images.image= test
cbit_images.place(x=1,y=85)
image1=Image.open(r"placement2.png")
test = ImageTk.PhotoImage(image1)
cbit_images = Label(image=test,padx=0,pady=0)
cbit_images.image= test
cbit_images.place(x=10+450,y=85)
image1=Image.open(r"placement3.png")
test = ImageTk.PhotoImage(image1)
cbit_images = Label(image=test,padx=0,pady=0)
cbit_images.image= test
cbit_images.place(x=10+450+459,y=85)
cdc_staff=Button(text='CDC STAFF',font=('consolas','10'),command=CDC_STAFF)
cdc_staff.place(x=50,y=57)
cdc_co_ordinators=Button(text='CDC CO-ORDINATES',font=('consolas','10'),highlightthickness='2')
cdc_co_ordinators.place(x=200+100,y=57)
cdc_events=Button(text='CDC EVENTS',font=('consolas','10'),command=CDC_EVENTS)
cdc_events.place(x=450+150+50,y=57)
objectives=Button(text='OBJECTIVES',font=('consolas','10'),command=Objectives)
objectives.place(x=650+100+100+50+20,y=57)
login=Button(text='LOGIN',font=('consolas','10'))
login.place(x=850+100+100+70+100,y=57)
Quicklinks=Label(height=2,width=24,bg='blue',text='QuickLinks',font=('consolas','12'))
Quicklinks.place(x=0,y=210+30+15+22)
# image size of 2*2 if we upload here
b1=Button(height=2,width=30,fg='blue',text='Notice Board',bg="#63C5DA",command=NoticeBoard)
b1.place(x=0,y=250+30+15+22)
b2=Button(height=2,width=30,fg='blue',bg="#63C5DA",text='Intership\nGuidelines',command=intership_guidelines)
b2.place(x=0,y=290+30+15+22)
b3=Button(height=2,width=30,fg='blue',bg="#63C5DA",text='Hiring guidelines\nfor students',command=lambda :webbrowser.open_new('https://www.cbit.ac.in/wp-content/uploads/2019/03/Guidelines-06.12.2019.pdf'))
b3.place(x=0,y=330+30+15+22)
b4=Button(height=2,width=30,fg='blue',bg="#63C5DA",text='Year wise\nplacements',command=plot)
b4.place(x=0,y=370+30+15+22)
b5=Button(height=2,width=30,fg='blue',bg="#63C5DA",text='Company wise\neligibilty criteria',command=company_eligibilty)
b5.place(x=0,y=410+30+15+22)
b6=Button(height=2,width=30,fg='blue',bg='#63C5DA',text='Our recuiters',command=lambda : webbrowser.open_new('https://www.cbit.ac.in/wp-content/uploads/2019/03/Companies-visited-to-CBIT-06.12.2019.pdf'))
b6.place(x=0,y=450+30+15+22)
about_us=Text(height=18,width=140)# about us
about_us.insert(INSERT,'                    CAREER DEVELOPMENT CENTRE\n')
about_us.insert(INSERT,'VISSION\n')
about_us.insert(INSERT,'   > To be centre of excellence in technical education and research\n')
about_us.insert(INSERT,'MISSION')
about_us.insert(INSERT,'''
   > To address the emerging needs through quality technical education and advanced research
   > To improve the industry institute interaction
   > To organize Conferences/Workshops/Seminars
   > To promote R&D activity
   > To strive for students’ placement
   > To organize co-curricular and extra curricular activities
   > To develop and maintain the linkage with alumni associations of CBIT
   > To improve internal communication
''')
about_us.insert(INSERT,'''Total No of Students Placed from 2000 onwards 15284 in leading MNCs, Microsoft, Google, JPMC, Oracle, Amazon, Deloitte, ITC, HUL, HIL, MRF, Dr.Reddy’s, Aurobindo, Hetero, CTS, Infosys, Accenture, TCS, Wipro, Capgemini, Sirpur Paper Mills & Orient Cement.
CBIT(A) signed MOU’S With Automation Anywhere University, Hexagon, Task, Gradvine, Atlas, Auburn University Cognizant, Infosys, Wipro, Capgemini, Ericssion, Mahindra & Mahindra, Unisys, ICICI Bank, IUCEE, Inpods etc. For Students & Faculty development programmes.
CBIT(A) established Automation Anywhere University Robotic Process Automation (COE) with 40 licenses worth Rs. 50 Lakhs, Hexagon 3D Innovation Lab with softwares worth Rs. 7 Crores &  Cognizant innovation lab worth Rs 6 Lakhs.''')
about_us.insert(END,'')
about_us.configure(state='disabled')
about_us.place(x=225,y=230+30+11+5)
image1=Image.open("Company.png")
test = ImageTk.PhotoImage(image1)
company_pics = Label(image=test,padx=0,pady=0)
company_pics.image= test
company_pics.place(x=15,y=575)
image1=Image.open("Company2.png")
test = ImageTk.PhotoImage(image1)
company_pics2 = Label(image=test,padx=0,pady=0)
company_pics2.image= test
company_pics2.place(x=50+140+130-35,y=575)
image1=Image.open("Company3.png")
test = ImageTk.PhotoImage(image1)
company_pics3 = Label(image=test,padx=0,pady=0)
company_pics3.image= test
company_pics3.place(x=50+280+260-35,y=575) 
image1=Image.open('Company4.png')
test = ImageTk.PhotoImage(image1)
company_pics4 = Label(image=test,padx=0,pady=0)
company_pics4.image= test
company_pics4.place(x=50+420+390-35,y=575)
image1=Image.open('Company5.png')
test = ImageTk.PhotoImage(image1)
company_pics5 = Label(image=test,padx=0,pady=0)
company_pics5.image= test
company_pics5.place(x=50+560+520-35,y=575)
# creating labels of images,first i will place an image of size 30*30 (means image label),then i will write text
image1=Image.open(r"1logo(1).jpg")
test = ImageTk.PhotoImage(image1)
logo1 = Label(image=test,padx=0,pady=0)
logo1.image= test
#logo1=Label(image=ImageTk.PhotoImage(Image.open(r"C:\Users\HP\Downloads\1logo(1).jpg")),bg='yellow')
logo1.place(x=3,y=250+30+15+4.5+22)
image1=Image.open(r"2logo.jpg")
test = ImageTk.PhotoImage(image1)
logo2 = Label(image=test,padx=0,pady=0)
logo2.image= test
logo2.place(x=3,y=250+30+15+4.5+40+22)
image1=Image.open(r"3logo.jpg")
test = ImageTk.PhotoImage(image1)
logo3 = Label(image=test,padx=0,pady=0)
logo3.image= test
logo3.place(x=3,y=250+30+15+4.5+80+22)
image1=Image.open(r"4logo.jpg")
test = ImageTk.PhotoImage(image1)
logo4 = Label(image=test,padx=0,pady=0)
logo4.image= test
logo4.place(x=3,y=250+30+15+4.5+120-3+22)
image1=Image.open(r"6logo.jpg")
test = ImageTk.PhotoImage(image1)
logo6 = Label(image=test,padx=0,pady=0)
logo6.image= test
logo6.place(x=3,y=250+30+15+4.5+160+22)
image1=Image.open(r"7logo.jpg")
test = ImageTk.PhotoImage(image1)
logo7 = Label(image=test,padx=0,pady=0)
logo7.image= test
logo7.place(x=3,y=250+30+15+4.5+200+22)
image1=Image.open(r"facebook.png")
test = ImageTk.PhotoImage(image1)
Social_logo1=Button(image=test,command=lambda : webbrowser.open_new('https://www.facebook.com/CBIThyderabad/'))
Social_logo1.place(x=1200,y=680)
Social_logo1.image= test
image1=Image.open(r"youtube.png")
test = ImageTk.PhotoImage(image1)
Social_logo2=Button(image=test,command=lambda : webbrowser.open_new('https://www.youtube.com/channel/UCUW8oQB8Fl6j-pg2g_sf1tw'))
Social_logo2.place(x=1233,y=680)
Social_logo2.image= test
image1=Image.open(r"twitter.png")
test = ImageTk.PhotoImage(image1)
Social_logo3=Button(image=test,command=lambda: webbrowser.open_new('https://twitter.com/CBIThyd'))
Social_logo3.place(x=1266,y=680)
Social_logo3.image= test
image1=Image.open(r"instagram.png")
test = ImageTk.PhotoImage(image1)
Social_logo4=Button(image=test,command=lambda: webbrowser.open_new('https://www.instagram.com/cbithyderabad/'))
Social_logo4.place(x=1299,y=680)
Social_logo4.image= test
Label(text="Let's talk social #CBIT").place(x=1060,y=680)
root.mainloop()