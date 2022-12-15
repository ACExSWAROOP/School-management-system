#thanks to rdbende for the tkinter theme sv_ttk
#BY ACExSWAROOP aka MSG SWARUPA

#############################################importing all modules#############################################

import ssl
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector as sequal
import sv_ttk as sv
import csv
from csv import *
from tkinter import filedialog
import smtplib
from email.message import EmailMessage
import requests
import time
import os 
from datetime import date, timedelta
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits

##################################################mainprogram############################################

global count
count = 0
global allclasssection
allclasssection = []
global inaccounts
inaccounts = ["--select institution--"]

global braccounts
braccounts = ["--select branch--"]

batches = ["2022-2023", "2023-2024", "2024-2025", "2025-2026", "2026-2027", "2027-2028", "2028-2029", "2029-2030", "2030-2031", "2031-2032",
           "2032-2033", "2033-2034", "2034-2035", "2035-2036", "2036-2037", "2037-2038", "2038-2039", "2039-2040", "2040-2041", "2041-2042",
           "2042-2043", "2043-2044", "2044-2045", "2045-2046", "2046-2047", "2047-2048", "2048-2049", "2049-2050", "2050-2051", "2051-2052",
           "2052-2053", "2053-2054", "2054-2055", "2055-2056", "2056-2057", "2057-2058", "2058-2059", "2059-2060", "2060-2061", "2061-2062",
           "2062-2063", "2063-2064", "2064-2065", "2065-2066", "2066-2067", "2067-2068", "2068-2069", "2070-2071", "2071-2072", "2072-2073",
           "2073-2074", "2074-2075", "2075-2076", "2076-2077", "2077-2078", "2078-2079", "2079-2080", "2080-2081", "2081-2082"]
months = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
dates = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th",
         "16th", "17th", "18th", "19th", "20th",
         "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
attendancevalues = ["AB", "P"]


####encryption logic by VARUN ADITHYA GB#####

lcase, ucase, num, alpha, pun = (
    list(ascii_lowercase),
    list(ascii_uppercase),
    list(digits),
    list(ascii_letters),
    ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "/"],
)
charst = lcase + ucase + num

lcase_crypt = [
    'M','L','W','U','Z','C','H','A','N','J','O','P','I','S','T','D','G','K','X','E','B','Y','R','Q','V','F'
    ]
ucase_crypt = [
    'm','w','f','l','s','n','o','i','d','a','g','e','u','h','p','r','y','k','q','c','x','b','v','z','j','t'
    ]
num_crypt = [
    '6', '4', '7', '8', '5', '2', '0', '3', '1', '9'
    ]
charst_crypt = lcase_crypt + ucase_crypt + num_crypt

def encrypt(strg: str):
    # takes input a string and returns a encryted passwd
    str_ls = list(strg)
    for i in str_ls:

        if i in charst:
            i_pos = str_ls.index(i)
            c_pos = charst.index(i)
            str_ls[i_pos] = charst_crypt[c_pos]
        else:
            pass

    strg = "".join(str_ls)
    return strg


def decrypt(strg: str):
    ## takes input a string and returns a encryted passwd
    str_ls = list(strg)
    for i in str_ls:

        if i in charst:
            i_pos = str_ls.index(i)
            c_pos = charst_crypt.index(i)
            str_ls[i_pos] = charst[c_pos]
        else:
            pass

    strg = "".join(str_ls)
    return strg

#############################################read theme mode############################################

with open("mode.txt", "r") as x:
    y=x.readline()
    mode=y

############################################write theme mode############################################

with open("mode.txt",'w') as x:
        x.write(mode)

############################################settingswindow##############################################

def settings():
    global setting
    setting = Toplevel()
    setting.title("settings")
    setting.geometry("128x64+835+290")
    setting.resizable(0, 0)
    setting.overrideredirect(1)
    themebut = ttk.Button(setting, text="THEME",command=lambda: [themechose()])
    themebut.place(x=32, y=15)
    
    setting.after(3000,lambda:setting.destroy())
    setting.mainloop()
##############################################themewindow###############################################

def themechose():
    global theme
    theme = Toplevel()
    theme.tk.call('wm', 'iconphoto', theme._w, ImageTk.PhotoImage(file='images\SMS.ico'))
    theme.title("choose theme:-")
    theme.resizable(0, 0)
    app_width = 512
    app_height = 256
    screenwidth = theme.winfo_screenwidth()
    screenheight = theme.winfo_screenheight()

    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)

    theme.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    if mode == "light":
        bg_image = ImageTk.PhotoImage(Image.open(r"images\themechooselight.png"))
        label1 = Label(theme, image=bg_image)
        label1.pack()
    elif mode == "dark":
        bg_image = ImageTk.PhotoImage(Image.open(r"images\themechoosedark.png"))
        label1 = Label(theme, image=bg_image)
        label1.pack()

    light_button = ttk.Button(theme, text="LIGHT", command=lambda: [light()])
    light_button.place(x=267, y=112)
    dark_button = ttk.Button(theme, text="DARK",  command=lambda: [dark()])
    dark_button.place(x=380, y=112)
    close_button = ttk.Button(theme, text="close",  command=lambda: [theme.destroy()])
    close_button.place(x=228, y=176)
    
    theme.mainloop()
#######################################################darkmode#############################################

def dark():
    global mode
    x=messagebox.askokcancel("want to reopen the app?", "restart needed to apply changes.please save your data.")
    if x==1:
        mode = "dark"
        with open("mode.txt",'w') as x:
            x.write(mode)
        
        theme.destroy()
        setting.destroy()
        main.destroy()
        os.system('python main.py')
        
###################################################lightmode############################################

def light():
    global mode
    x=messagebox.askokcancel("want to reopen the app?", "restart needed to apply changes.please save your data.")
    if x==1:
        mode = "light"
        with open("mode.txt",'w') as x:
            x.write(mode)

        theme.destroy()
        setting.destroy()
        main.destroy()
        os.system('python main.py')
        
###################################################mainsplash###########################################

mainsplash = Tk()
sv.set_theme(mode)

mainsplash.resizable(0, 0)
mainsplash.overrideredirect(True)
app_width = 512
app_height = 256
screenwidth = mainsplash.winfo_screenwidth()
screenheight = mainsplash.winfo_screenheight()

x = (screenwidth / 2) - (app_width / 2)
y = (screenheight / 2) - (app_height / 2)

mainsplash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

if mode == "light":
    bg_image = ImageTk.PhotoImage(Image.open(r"images\s,c,t management splash light.png"))
    label1 = Label(mainsplash, image=bg_image)
    label1.pack()
elif mode == "dark":
    bg_image = ImageTk.PhotoImage(Image.open(r"images\s,c,t management splash dark.png"))
    label1 = Label(mainsplash, image=bg_image)
    label1.pack()

################################################closeprogram############################################

def close():
    x = messagebox.askyesno("do you want to close this program?", "do you want to close this program?")
    if x == 1:
        exit()
##############################################makebuttonnormal##########################################

def butnormal(buttonname):
    buttonname['state'] = NORMAL

##############################################mainwindow################################################

def mainwindow():
    mainsplash.withdraw()
    global main
    main = Toplevel()
    main.protocol("WM_DELETE_WINDOW",lambda:[close()])
    main.tk.call('wm', 'iconphoto', main._w, ImageTk.PhotoImage(file='images\SMS.ico'))
    app_width=512
    app_height=384
    screenwidth = mainsplash.winfo_screenwidth()
    screenheight = mainsplash.winfo_screenheight()

    x = (screenwidth / 2) - (app_width / 2)
    y = (screenheight / 2) - (app_height / 2)

    main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    main.title("School management system")
    main.resizable(0, 0)
    if mode == "light":
        bg_image = ImageTk.PhotoImage(Image.open(r"images\attwindow light.png"))
        label1 = Label(main, image=bg_image)
        label1.pack()
    elif mode == "dark":
        bg_image = ImageTk.PhotoImage(Image.open(r"images\attwindow dark.png"))
        label1 = Label(main, image=bg_image)
        label1.pack()

    ############################################mysqlpasswordcheck#####################################

    def passcheck():
        password=False
        while password==False:
            with open("dnd.txt","r+") as x:
                y = x.read()
                y = decrypt(y)
                if y == "":
                    mysqlpassget()
                elif y!="":
                    try:
                        db = sequal.connect(host="localhost", user="root", passwd=y)
                        password=True
                        sql.destroy()
                        main.destroy()
                        os.system('python main.py')

                    except sequal.Error:
                        z=messagebox.askretrycancel("mysqlpassword incorrect.", "Please enter correct mysql password to proceed.")
                        if z==True:
                            x.write("")
                            sql.destroy()
                            mysqlpassget()
                        if z==False:
                            password=True
                            sql.destroy()
                            main.destroy()

        while password==True:
            break
    
    ###############################################mysqlpasswindow#####################################

    def mysqlpassget():
        main.withdraw()
        global sql
        sql = Toplevel()
        sql.tk.call('wm', 'iconphoto', sql._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        sql.title("Enter mysql password :-")
        app_width = 512
        app_height = 256
        screenwidth = sql.winfo_screenwidth()
        screenheight = sql.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        sql.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\mysqlpass light.png"))
            label1 = Label(sql, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\mysqlpass dark.png"))
            label1 = Label(sql, image=bg_image)
            label1.pack()

        def savepass():
            y = sequalpass.get()
            with open("dnd.txt", "w") as x:
                x.write(encrypt(y))

        sequalpass = Entry(sql)
        sequalpass.config(show="•")
        sequalpass.place(x=300, y=118)

        def show(mypass, sequalpass):
            if (mypass.get()) == 1:
                sequalpass.config(show="")
            else:
                sequalpass.config(show="•")

        mypass = IntVar()

        checkshow = ttk.Checkbutton(sql, text="Show Password", variable=mypass, onvalue=1, offvalue=0,
                                    command=lambda: [show(mypass, sequalpass)])
        checkshow.place(x=310, y=150)

        sql_button = ttk.Button(sql, text="save", padding=10, command=lambda: [savepass(),passcheck(),sql.destroy(),main.deiconify()])
        sql_button.place(x=220, y=180)
        
        sql.mainloop()
    ##############################################connecttosql#########################################
    
    with open("dnd.txt","r+") as x:
        y = x.read()
        y = decrypt(y)
        if y == "":
            mysqlpassget()
        try:
            db = sequal.connect(host="localhost", user="root", passwd=y)
            cur = db.cursor()
        except sequal.Error:
            mysqlpassget()
    ################################################createnewaccount###################################
    def newacc():
        global acc
        acc = Toplevel()
        acc.protocol("WM_DELETE_WINDOW",lambda:[admin.deiconify(),acc.destroy()])
        acc.tk.call('wm', 'iconphoto', acc._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        acc.title("new account")

        app_height=512
        app_height=512
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        acc.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\accountlight.png"))
            label1 = Label(acc, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\accountdark.png"))
            label1 = Label(acc, image=bg_image)
            label1.pack()

        global institution_entry
        institution_entry = ttk.Entry(acc)

        global branch_entry
        branch_entry = ttk.Entry(acc)

        adminpassentry= ttk.Entry(acc)
        confirmadminpassentry= ttk.Entry(acc)

        teacherpassentry=ttk.Entry(acc)
        confirmteacherpassentry=ttk.Entry(acc)

        institution_entry.place(x=267, y=90)
        branch_entry.place(x=267, y=133)

        adminpassentry.place(x=267,y=176)
        confirmadminpassentry.place(x=267,y=219)
        adminpassentry.config(show="•")
        confirmadminpassentry.config(show="•")

        teacherpassentry.place(x=267,y=305)
        confirmteacherpassentry.place(x=267,y=348)
        teacherpassentry.config(show="•")
        confirmteacherpassentry.config(show="•")

        def show(adm, adminpassentry,confirmadminpassentry):
                if (adm.get()) == 1:
                    adminpassentry.config(show="")
                    confirmadminpassentry.config(show="")
                else:
                    adminpassentry.config(show="•")
                    confirmadminpassentry.config(show="•")

        adm = IntVar()

        checkshow = ttk.Checkbutton(acc, text="Show Password", variable=adm, onvalue=1, offvalue=0,
                                    command=lambda: [show(adm, adminpassentry, confirmadminpassentry)])
        checkshow.place(x=267, y=263)

        def show2(adm2, teacherpassentry, confirmteacherpassentry):
                if (adm2.get()) == 1:
                    teacherpassentry.config(show="")
                    confirmteacherpassentry.config(show="")
                else:
                    teacherpassentry.config(show="•")
                    confirmteacherpassentry.config(show="•")

        adm2 = IntVar()

        checkshow = ttk.Checkbutton(acc, text="Show Password", variable=adm2, onvalue=1, offvalue=0,
                                    command=lambda: [show2(adm2, teacherpassentry, confirmteacherpassentry)])
        checkshow.place(x=267, y=391)

        #############################################savenewaccount#####################################
        
        def saveacc():
            if adminpassentry.get() == confirmadminpassentry.get() == "":
                n=messagebox.showinfo("empty field.", "please enter an admin password.")
                if n==False:
                    acc.destroy()
            
            if teacherpassentry.get() == confirmteacherpassentry.get() == "":
                n=messagebox.showinfo("empty field.", "please enter a teacher password.")
                if n==False:
                    acc.destroy()

            if adminpassentry.get() != confirmadminpassentry.get():
                n=messagebox.showinfo("incorrect adminpassword.", "wrong  admin password match.try again.")
                if n==False:
                    acc.destroy()
            
            if teacherpassentry.get() != confirmteacherpassentry.get():
                o=messagebox.showinfo("incorrect teacherpassword.", "wrong teacher password match.try again.")
                if o==False:
                    acc.destroy()
            if len(institution_entry.get()) == 0 or len(branch_entry.get()) == 0:
                l=messagebox.showinfo("fill the details to proceed.", "institution or branch is empty.")
                if l==False:
                    acc.destroy()
            
            elif len(institution_entry.get()) != 0 and len(branch_entry.get()) != 0 and len(adminpassentry.get())!= 0 \
            and len(confirmadminpassentry.get())!= 0 and len(teacherpassentry.get())!= 0 and len(confirmteacherpassentry.get()) != 0 \
            and adminpassentry.get() == confirmadminpassentry.get() and  teacherpassentry.get() == confirmteacherpassentry.get():
                cur.execute("SHOW SCHEMAS;")
                databases = []
                for i in cur:
                    databases.extend(i)

                databasename = "sms"

                if databasename in databases:
                    cur.execute(" USE {} ;".format(databasename))
                else:
                    cur.execute("CREATE DATABASE {};".format(databasename))
                    cur.execute(" USE {} ;".format(databasename))

                cur.execute("SHOW TABLES;")
                tables = []
                for i in cur:
                    tables.extend(i)

                cur.execute("USE {};".format(databasename))
                cur.execute("CREATE TABLE if not exists accounts(institution varchar(20)\
                ,branch varchar(20),adminpass varchar(20),teacherpass varchar(20));")
                cur.execute("INSERT INTO accounts(institution,branch,adminpass,teacherpass)\
                VALUES('{}','{}','{}','{}');".format(str(institution_entry.get()),str(branch_entry.get())\
                ,encrypt(adminpassentry.get()),encrypt(teacherpassentry.get())))
                db.commit()
                
                messagebox.showinfo("account", "successfully created the account.")
                acc.destroy()
                admin.destroy()
                main.destroy()
                os.system('python main.py')

        save = ttk.Button(acc, text="Save", width=12,
                          command=lambda: [saveacc()])
        save.place(x=120, y=434)

        closebut = ttk.Button(acc, text="Close", width=12,
                          command=lambda: [acc.destroy(),admin.deiconify()])
        closebut.place(x=280, y=434)

        acc.mainloop()

    ##################################################getaccounts#######################################
    
    def getaccounts():
        try:
            cur.execute(" USE {} ;".format("sms"))
            cur.execute("select institution from accounts;")
            x = cur.fetchall()
            for i in x:
                inaccounts.append(i)
            cur.execute("select branch from accounts;")
            y = cur.fetchall()
            for i in y:
                braccounts.append(i)

        except sequal.ProgrammingError:
            x=messagebox.showinfo("account not created.","create account in order to proceed.")
            teacher.deiconify()

    #####################################attendanceregistersplashscreen#################################
    
    def rootsplash():
        root_splash = Toplevel()
        app_height=512
        app_height=256
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        root_splash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        root_splash.overrideredirect(True)
        if mode == "light":
            bg = ImageTk.PhotoImage(Image.open(r"images\attendence register splash light.png"))
            label = Label(root_splash, image=bg)
            label.place(x=0, y=0)
        if mode == "dark":
            bg = ImageTk.PhotoImage(Image.open(r"images\attendence register splash dark.png"))
            label = Label(root_splash, image=bg)
            label.place(x=0, y=0)
        
        ###########################################attendanceregisterwindow##############################
        
        def rootwindow():
            global root
            root_splash.destroy()
            root = Toplevel()
            root.protocol("WM_DELETE_WINDOW",lambda:[teacher.deiconify(),root.destroy()])
            root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='images\SMS.ico'))
            app_height=324
            app_width=384
            screenwidth = mainsplash.winfo_screenwidth()
            screenheight = mainsplash.winfo_screenheight()

            x = (screenwidth / 2) - (app_width / 2)
            y = (screenheight / 2) - (app_height / 2)

            root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
            root.title("Attendance Register")
            if mode == "light":
                bg = ImageTk.PhotoImage(Image.open(r"images\attmenu light.png"))
                label = Label(root, image=bg)
                label.place(x=0, y=0)
            if mode == "dark":
                bg = ImageTk.PhotoImage(Image.open(r"images\attmenu dark.png"))
                label = Label(root, image=bg)
                label.place(x=0, y=0)

            ####################################creatingtablesforattendance############################

            def createattendancetables():
                global allclasssection
                
                x = institutionsel.get()
                y = branchsel.get()
                batch=batchbox.get()
                monthvalue=monthbox.get()

                a = '-'
                for n in a:
                    batch = batch.replace(n, "")

                name = x + y + batch + "attendance" + monthvalue
                dbname = name.strip()

                global dbname2
                dbname2 = dbname

                cur.execute("SHOW SCHEMAS;")
                databases = []

                for i in cur:
                    databases.extend(i)

                if dbname in databases:
                    cur.execute(" USE {} ;".format(dbname))
                else:
                    cur.execute("CREATE DATABASE if not exists {};".format(dbname))
                    cur.execute(" USE {} ;".format(dbname))

                yrsel=monthvalue[0:4]
                leapcheck=False
                if((int(yrsel) % 400 == 0) or  (int(yrsel) % 100 != 0) and (int(yrsel) % 4 == 0)):
                    leapcheck=True
                    
                cur.execute("SHOW TABLES;")
                tables = []

                for i in cur:
                    tables.extend(i)

                if tables == []:
                    cur.execute("USE {};".format(dbname))
                    for i in allclasssection:
                        if monthvalue[4:20] =="Febraury":
                            if leapcheck==False:
                                cur.execute(
                                "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),1st varchar(2) "
                                "DEFAULT '',2nd varchar(2) DEFAULT '',3rd varchar(2) DEFAULT '',4th varchar(2) DEFAULT "
                                "'',5th varchar(2) DEFAULT '',6th varchar(2) DEFAULT '',7th varchar(2) DEFAULT '',"
                                "8th varchar(2) DEFAULT '',9th varchar(2) DEFAULT '',10th varchar(2) DEFAULT '',"
                                "11th varchar(2) DEFAULT '',12th varchar(2) DEFAULT '',13th varchar(2) DEFAULT '',"
                                "14th varchar(2) DEFAULT '',15th varchar(2) DEFAULT '',16th varchar(2) DEFAULT '',"
                                "17th varchar(2) DEFAULT '',18th varchar(2) DEFAULT '',19th varchar(2) DEFAULT '',"
                                "20th varchar(2) DEFAULT '',21st varchar(2) DEFAULT '',22nd varchar(2) DEFAULT '',"
                                "23rd varchar(2) DEFAULT '',24th varchar(2) DEFAULT '',25th varchar(2) DEFAULT '',"
                                "26th varchar(2) DEFAULT '',27th varchar(2) DEFAULT '',28th varchar(2) DEFAULT '',\
                                workingdays varchar(3),attended varchar(3),attendancepercentage varchar(10));".format(i))
                            if leapcheck==True:
                                cur.execute(
                                "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),1st varchar(2) "
                                "DEFAULT '',2nd varchar(2) DEFAULT '',3rd varchar(2) DEFAULT '',4th varchar(2) DEFAULT "
                                "'',5th varchar(2) DEFAULT '',6th varchar(2) DEFAULT '',7th varchar(2) DEFAULT '',"
                                "8th varchar(2) DEFAULT '',9th varchar(2) DEFAULT '',10th varchar(2) DEFAULT '',"
                                "11th varchar(2) DEFAULT '',12th varchar(2) DEFAULT '',13th varchar(2) DEFAULT '',"
                                "14th varchar(2) DEFAULT '',15th varchar(2) DEFAULT '',16th varchar(2) DEFAULT '',"
                                "17th varchar(2) DEFAULT '',18th varchar(2) DEFAULT '',19th varchar(2) DEFAULT '',"
                                "20th varchar(2) DEFAULT '',21st varchar(2) DEFAULT '',22nd varchar(2) DEFAULT '',"
                                "23rd varchar(2) DEFAULT '',24th varchar(2) DEFAULT '',25th varchar(2) DEFAULT '',"
                                "26th varchar(2) DEFAULT '',27th varchar(2) DEFAULT '',28th varchar(2) DEFAULT '',\
                                29th varchar(2) DEFAULT '',workingdays varchar(3),attended varchar(3) ,attendancepercentage varchar(10) );".format(i))

                        elif monthvalue[4:20] == "January" or monthvalue[4:20] == "March" or  monthvalue[4:20] == "May" or  \
                            monthvalue[4:20] == "July" or  monthvalue[4:20] == "August" or  monthvalue[4:20] == "October" or  monthvalue[4:20] == "December":
                            
                            cur.execute(
                                "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),1st varchar(2) "
                                "DEFAULT '',2nd varchar(2) DEFAULT '',3rd varchar(2) DEFAULT '',4th varchar(2) DEFAULT "
                                "'',5th varchar(2) DEFAULT '',6th varchar(2) DEFAULT '',7th varchar(2) DEFAULT '',"
                                "8th varchar(2) DEFAULT '',9th varchar(2) DEFAULT '',10th varchar(2) DEFAULT '',"
                                "11th varchar(2) DEFAULT '',12th varchar(2) DEFAULT '',13th varchar(2) DEFAULT '',"
                                "14th varchar(2) DEFAULT '',15th varchar(2) DEFAULT '',16th varchar(2) DEFAULT '',"
                                "17th varchar(2) DEFAULT '',18th varchar(2) DEFAULT '',19th varchar(2) DEFAULT '',"
                                "20th varchar(2) DEFAULT '',21st varchar(2) DEFAULT '',22nd varchar(2) DEFAULT '',"
                                "23rd varchar(2) DEFAULT '',24th varchar(2) DEFAULT '',25th varchar(2) DEFAULT '',"
                                "26th varchar(2) DEFAULT '',27th varchar(2) DEFAULT '',28th varchar(2) DEFAULT '',"
                                "29th varchar(2) DEFAULT '',30th varchar(2) DEFAULT '',31st varchar(2) DEFAULT '',\
                                workingdays varchar(3) ,attended varchar(3),attendancepercentage varchar(10));".format(i))
                        elif  monthvalue[4:20] == "April" or  monthvalue[4:20] == "June" or  monthvalue[4:20] == "September" or  monthvalue[4:20] == "November":
                            cur.execute(
                                "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),1st varchar(2) "
                                "DEFAULT '',2nd varchar(2) DEFAULT '',3rd varchar(2) DEFAULT '',4th varchar(2) DEFAULT "
                                "'',5th varchar(2) DEFAULT '',6th varchar(2) DEFAULT '',7th varchar(2) DEFAULT '',"
                                "8th varchar(2) DEFAULT '',9th varchar(2) DEFAULT '',10th varchar(2) DEFAULT '',"
                                "11th varchar(2) DEFAULT '',12th varchar(2) DEFAULT '',13th varchar(2) DEFAULT '',"
                                "14th varchar(2) DEFAULT '',15th varchar(2) DEFAULT '',16th varchar(2) DEFAULT '',"
                                "17th varchar(2) DEFAULT '',18th varchar(2) DEFAULT '',19th varchar(2) DEFAULT '',"
                                "20th varchar(2) DEFAULT '',21st varchar(2) DEFAULT '',22nd varchar(2) DEFAULT '',"
                                "23rd varchar(2) DEFAULT '',24th varchar(2) DEFAULT '',25th varchar(2) DEFAULT '',"
                                "26th varchar(2) DEFAULT '',27th varchar(2) DEFAULT '',28th varchar(2) DEFAULT '',"
                                "29th varchar(2) DEFAULT '',30th varchar(2) DEFAULT '',\
                                workingdays varchar(3),attended varchar(3),attendancepercentage varchar(10));".format(i))
            ############################getclassesandsectionfortablecreation###########################
            
            def getclass():
                global allclasssection
                x = institutionsel.get()
                y = branchsel.get()
                batchvalue = batchbox.get()
                a = '-'
                for n in a:
                    batchvalue = batchvalue.replace(n, "")

                tablename = str(x + y + batchvalue + "classes")
                filename = str(tablename + ".txt")
                filename = filename.replace(" ", "")

                try:
                    with open(filename, "r") as x:
                        data = x.readlines()
                        for i in data:
                            allclasssection.append(i)
                    createattendancetables()
                    root2()

                except FileNotFoundError:
                    messagebox.showinfo("invalid selection", "INVALID SELECTION.NO DATABASE FOUND IN THE SELECTED BATCH.please create a database and try again.")
                    root.deiconify()
                    
            global batchbox, monthbox
            
            def monthboxvals(event):
                batch=str(event.widget.get())
                value=[]
                yr1=batch[0:4]
                yr2=batch[5:10]
                for i in months:
                    val=yr1+i
                    value.append(val)
                for j in months:
                    val=yr2+j
                    value.append(val)
                global monthbox
                monthbox = ttk.Combobox(root, values=value, width=15)
                monthbox.place(x=200, y=100)

            batchbox = ttk.Combobox(root, values=batches, width=15)
            batchbox.place(x=200, y=52)
            batchbox.bind("<<ComboboxSelected>>",monthboxvals)

            emptybox = ttk.Combobox(root, width=15)
            emptybox.place(x=200, y=100)

            proceed_button = ttk.Button(root, text="CONTINUE", width=15,
                                        command=lambda: [root.withdraw(),getclass()])
            proceed_button.place(x=130, y=150)

            help_button = ttk.Button(root, text="MANUAL", width=15,
                                     command=lambda: [manual(), root.withdraw()])

            help_button.place(x=130, y=200)

            exit_button = ttk.Button(root, text="EXIT", width=15,
                                        command=lambda: [root.destroy(),teacher.deiconify()])
            exit_button.place(x=130,y=250)
            
            root.mainloop()

        root_splash.after(3000, rootwindow)
        root_splash.mainloop()
    #########################################defaultadminpasswindow######################################
    def adminpass():
        if len(inaccounts)==1:
            global adminp
            adminp = Toplevel()
            adminp.protocol("WM_DELETE_WINDOW",lambda:[main.deiconify(),adminp.destroy()])
            adminp.tk.call('wm', 'iconphoto', adminp._w, ImageTk.PhotoImage(file='images\SMS.ico'))
            adminp.title("Enter admin password :-")
            app_width = 512
            app_height = 256
            screenwidth = adminp.winfo_screenwidth()
            screenheight = adminp.winfo_screenheight()

            x = (screenwidth / 2) - (app_width / 2)
            y = (screenheight / 2) - (app_height / 2)

            adminp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            if mode == "light":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\adpasslight.png"))
                label1 = Label(adminp, image=bg_image)
                label1.pack()
            elif mode == "dark":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\adpass dark.png"))
                label1 = Label(adminp, image=bg_image)
                label1.pack()

            def checkpass():
                j="admin"
                if admpass.get()==j:
                    adminp.withdraw()
                    adminwindow()
                            
                else:
                    z=messagebox.askretrycancel("wrong admin password","wrong admin password.try again.")
                    if z!=1:
                        adminp.destroy()
                        main.deiconify()
                        
            global admpass    
            admpass = Entry(adminp)
            admpass.config(show="•")
            admpass.place(x=300, y=118)
            
            def show(mypass, admpass):
                if (mypass.get()) == 1:
                    admpass.config(show="")
                else:
                    admpass.config(show="•")

            mypass = IntVar()

            checkshow = ttk.Checkbutton(adminp, text="Show Password", variable=mypass, onvalue=1, offvalue=0,
                                        command=lambda: [show(mypass, admpass)])
            checkshow.place(x=310, y=150)

            save_button = ttk.Button(adminp, text="Proceed", padding=8, command=lambda: [checkpass()])
            save_button.place(x=220, y=180)
            
            adminp.mainloop()
        ################################actualadminpassentrywindow#########################################  
        if len(inaccounts)!=1:  
            adminp = Toplevel()
            adminp.protocol("WM_DELETE_WINDOW",lambda:[main.deiconify(),adminp.destroy()])
            adminp.tk.call('wm', 'iconphoto', adminp._w, ImageTk.PhotoImage(file='images\SMS.ico'))
            adminp.title("Enter admin password :-")
            app_width = 512
            app_height = 256
            screenwidth = adminp.winfo_screenwidth()
            screenheight = adminp.winfo_screenheight()

            x = (screenwidth / 2) - (app_width / 2)
            y = (screenheight / 2) - (app_height / 2)

            adminp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            if mode == "light":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\adpasslight.png"))
                label1 = Label(adminp, image=bg_image)
                label1.pack()
            elif mode == "dark":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\adpass dark.png"))
                label1 = Label(adminp, image=bg_image)
                label1.pack()

            def checkpass():
                cur.execute(" USE {} ;".format("sms"))
                cur.execute("select adminpass from accounts where institution='{}' and branch='{}';".format(institutionsel.get(),branchsel.get()))
                x=cur.fetchall()
                for i in x:
                    for j in i:
                        j=decrypt(j)
                        if admpass.get()==j:
                            adminp.withdraw()
                            adminwindow()
                            
                        else:
                            z=messagebox.askretrycancel("wrong admin password","wrong admin password.try again.")
                            if z!=1:
                                adminp.destroy()
                                main.deiconify()

            admpass = Entry(adminp)
            admpass.config(show="•")
            admpass.place(x=300, y=118)
            
            if institutionsel.get() == "--select institution--" or branchsel.get()=="--select branch--":
                adminp.withdraw()
                messageb=messagebox.askretrycancel("no institution or branch selected.","select the institution or branch to continue.")
                main.deiconify()

            def show(mypass, admpass):
                if (mypass.get()) == 1:
                    admpass.config(show="")
                else:
                    admpass.config(show="•")

            mypass = IntVar()

            checkshow = ttk.Checkbutton(adminp, text="Show Password", variable=mypass, onvalue=1, offvalue=0,
                                        command=lambda: [show(mypass, admpass)])
            checkshow.place(x=310, y=150)

            save_button = ttk.Button(adminp, text="Proceed", padding=8, command=lambda: [checkpass()])
            save_button.place(x=220, y=180)
            
            adminp.mainloop()
    ###################################################adminwindow######################################
    def adminwindow():
        global admin
        admin = Toplevel()
        admin.protocol("WM_DELETE_WINDOW",lambda:[main.deiconify(),admin.destroy()])
        admin.tk.call('wm', 'iconphoto', admin._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        admin.title("hello Admin")
        app_height=256
        app_width=512
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        admin.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\adminwindow light.png"))
            label1 = Label(admin, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\adminwindow dark.png"))
            label1 = Label(admin, image=bg_image)
            label1.pack()

        new_button = ttk.Button(admin, text="New account", width=16, padding=8, command=lambda: [admin.withdraw(),newacc()])
        new_button.place(x=179, y=49)

        manage_button = ttk.Button(admin, text="MANAGE", width=16, padding=8,
                               command=lambda: [admin.withdraw(),manage_data()])
        manage_button.place(x=179, y=105)

        exit_button = ttk.Button(admin, text="BACK", width=16, padding=8, command=lambda:[admin.destroy(),main.deiconify()])
        exit_button.place(x=179, y=162)

        admin.mainloop()
    #############################################teacherpasswordentrywindow##############################
    def teacherpass():
        if len(inaccounts)==1:
            messageb=messagebox.askretrycancel("create account to continue","no account detected.please create one to continue.")
            main.deiconify()
        elif institutionsel.get() == "--select institution--" or branchsel.get()=="--select branch--":
            messageb=messagebox.askretrycancel("no institution or branch selected.","select the institution or branch to continue.")
            main.deiconify()
        if len(inaccounts)!=1:  
            global teacherx
            teacherx = Toplevel()
            teacherx.protocol("WM_DELETE_WINDOW",lambda:[main.deiconify(),teacherx.destroy()])
            teacherx.tk.call('wm', 'iconphoto', teacherx._w, ImageTk.PhotoImage(file='images\SMS.ico'))
            teacherx.title("Enter teacher password :-")
            app_width = 512
            app_height = 256
            screenwidth = teacherx.winfo_screenwidth()
            screenheight = teacherx.winfo_screenheight()

            x = (screenwidth / 2) - (app_width / 2)
            y = (screenheight / 2) - (app_height / 2)

            teacherx.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

            if mode == "light":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\teacherpass light.png"))
                label1 = Label(teacherx, image=bg_image)
                label1.pack()
            elif mode == "dark":
                bg_image = ImageTk.PhotoImage(Image.open(r"images\teacherpass dark.png"))
                label1 = Label(teacherx, image=bg_image)
                label1.pack()

            def checkpass():
                cur.execute(" USE {} ;".format("sms"))
                cur.execute("select teacherpass from accounts where institution='{}' and branch='{}';".format(institutionsel.get(),branchsel.get()))
                x=cur.fetchall()
                for i in x:
                    for j in i:
                        j=decrypt(j)
                        if teacherpass.get()==j:
                            teacherx.withdraw()
                            teacherwindow()
                            
                        else:
                            z=messagebox.askretrycancel("wrong teacher password","wrong teacher password.try again.")
                            if z!=1:
                                teacherx.destroy()
                                main.deiconify()

            global teacherpass    
            teacherpass = Entry(teacherx)
            teacherpass.config(show="•")
            teacherpass.place(x=300, y=118)
            
            def show(mypass, teacherpass):
                if (mypass.get()) == 1:
                    teacherpass.config(show="")
                else:
                    teacherpass.config(show="•")

            mypass = IntVar()

            checkshow = ttk.Checkbutton(teacherx, text="Show Password", variable=mypass, onvalue=1, offvalue=0,
                                        command=lambda: [show(mypass, teacherpass)])
            checkshow.place(x=310, y=150)

            save_button = ttk.Button(teacherx, text="Proceed", padding=8, command=lambda: [checkpass()])
            save_button.place(x=220, y=180)
            
            teacherx.mainloop()
    ##############################################teacherwindow###########################################
    def teacherwindow():
        global teacher
        teacher = Toplevel()
        teacher.protocol("WM_DELETE_WINDOW",lambda:[main.deiconify(),teacher.destroy()])
        teacher.tk.call('wm', 'iconphoto', teacher._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        teacher.title("hello teacher")
        app_height=256
        app_width=512
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        teacher.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\teacherwindow light.png"))
            label1 = Label(teacher, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\teacherwindow dark.png"))
            label1 = Label(teacher, image=bg_image)
            label1.pack()

        attendanceregbutton = ttk.Button(teacher, text="Attendance Register", width=16, padding=8,
                                        command=lambda: [teacher.withdraw(),getaccounts(),rootsplash()])
        attendanceregbutton.place(x=179, y=77)

        exit_button = ttk.Button(teacher, text="BACK", width=16, padding=8, command=lambda:[teacher.destroy(),main.deiconify()])
        exit_button.place(x=179, y=135)

        teacher.mainloop()

    try:
        cur.execute(" USE {} ;".format("sms"))
        cur.execute("select institution from accounts;")
        x = cur.fetchall()
        for i in x:
            inaccounts.append(i)
        cur.execute("select branch from accounts;")
        y = cur.fetchall()
        for i in y:
            braccounts.append(i)

    except sequal.ProgrammingError:
        pass

    
    global institutionsel
    global branchsel

    institutionsel = ttk.Combobox(main, values=inaccounts,width=17)
    branchsel = ttk.Combobox(main, values=braccounts,width=17)
    institutionsel.place(x=180,y=62)
    branchsel.place(x=180,y=105)
    institutionsel.current(0)
    branchsel.current(0) 

    adminbutton=ttk.Button(main, text="ADMIN", width=16, padding=8, command=lambda: [main.withdraw(),adminpass(),adminwindow()])
    adminbutton.place(x=179, y=149)

    teacherbutton=ttk.Button(main, text="TEACHER", width=16, padding=8, command=lambda: [main.withdraw(),teacherpass()])
    teacherbutton.place(x=179, y=210)

    exit_button = ttk.Button(main, text="EXIT", width=16, padding=8, command=lambda: close())
    exit_button.place(x=179, y=272)

    if mode == "light":
            img = ImageTk.PhotoImage(Image.open(r"images\settings light.png"))
            label1 = Label(image=img)
            label1.pack()
    elif mode == "dark":
            img = ImageTk.PhotoImage(Image.open(r"images\settings dark.png"))
            label1 = Label(image=img)
            label1.pack()
    setting_button = Button(main, image=img, bg="white", borderwidth=0,command=lambda: settings())
    setting_button.place(x=445, y=30)

    ##############################################managewindow##########################################
    def manage_data():
        global manage
        manage = Toplevel()
        manage.protocol("WM_DELETE_WINDOW",lambda:[admin.deiconify(),manage.destroy()])
        manage.tk.call('wm', 'iconphoto', manage._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        manage.title("manage data")
        app_height=512
        app_width=768
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        manage.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\manage templatelight.png"))
            label1 = Label(manage, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\manage templatedark.png"))
            label1 = Label(manage, image=bg_image)
            label1.pack()

        def getclasses():
            global stud
            global allclasssection
            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")
            tablename = str(ins + br + ba + "classes")
            filename = str(tablename + ".txt")
            filename = filename.replace(" ", "")
            try:
                allclasssection=[]
                with open(filename, "r") as x:
                    data = x.readlines()
                    for i in data:
                        allclasssection.append(i)
                addstudents()
            except FileNotFoundError:
                v=messagebox.askokcancel("no class and section selected.","select class and section and save to create database.")
                manage.deiconify()
        ##########################################studdetailstorage#####################################
        def save():
            global allclasssection
            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")

            name = str(ins+br+ba)
            dbname = name.strip()
            dbname=dbname.lower()

            cur.execute("SHOW SCHEMAS;")
            databases = []
        
            for i in cur:
                databases.extend(i)

            if dbname in databases:
                cur.execute(" USE {} ;".format(dbname))
            else:
                cur.execute("CREATE DATABASE {};".format(dbname))
                cur.execute(" USE {} ;".format(dbname))

            cur.execute("SHOW TABLES;")
            tables = []
            for i in cur:
                tables.extend(i)
            if tables == []:
                cur.execute("USE {};".format(dbname))
                for i in allclasssection:
                    cur.execute(
                        "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),admno varchar(50),\
                        batch varchar(50),parentemail varchar(50),class varchar(50),classteacher varchar(50));"\
                        .format(i))
            else:
                cur.execute("USE {};".format(dbname))
                for i in allclasssection:
                    cur.execute(
                        "CREATE TABLE if not exists {}(rollno varchar(50),studentname varchar(50),admno varchar(50),\
                        batch varchar(50),parentemail varchar(50),class varchar(50),classteacher varchar(50));"\
                        .format(i))
        try:
            cur.execute(" USE {} ;".format("sms"))
            cur.execute("select institution from accounts;")
            ins = cur.fetchall()
            for row in ins:
                for i in row:
                    inaccounts.append(i)
                    
            cur.execute("select branch from accounts;")
            br = cur.fetchall()
            for row in br:
                for i in row:
                    braccounts.append(i)

        except sequal.ProgrammingError:
            x=messagebox.askokcancel("account not created.","create account in order to proceed.")
            manage.deicontify
        #################################nobatchselcheck#################################################
        def chkbatch():
            if batchsel.get()=="":
                x=messagebox.showinfo("no batch selected.","please select batch to proceed")
                manage.deiconify()
            else:
                sel_cl()    

        global batchsel
        batchsel = ttk.Combobox(manage,width=22, values=batches)

        select_class = ttk.Button(manage, text="Select", width=20, command=lambda:[manage.withdraw() ,chkbatch()])

        global select_sec
        select_sec = ttk.Button(manage, text="Select", width=20,state=DISABLED,command=lambda:[manage.withdraw(), sel_sec()])

        global studentinfo
        studentinfo = ttk.Button(manage, text="Select", width=20, command=lambda: [manage.withdraw(),getclasses()])

        batchsel.place(x=440, y=130)

        select_class.place(x=442, y=200)

        select_sec.place(x=442, y=270)

        studentinfo.place(x=442, y=380)

        save_button = ttk.Button(manage, text="Save", width=13, command=lambda: [save()])
        save_button.place(x=320, y=323)

        back = ttk.Button(manage, text="Close", width=13, command=lambda: [manage.destroy(),admin.deiconify()])
        back.place(x=320, y=425)

        manage.mainloop()
    ############################################selectclasseswindow#####################################
    def sel_cl():
        def clicking_check():
            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")
            tablename = str(ins + br + ba + "classes")
            filename = str(tablename + ".txt")
            filename = filename.replace(" ", "")

            try:
                with open(filename, "r") as x:
                    data = x.readlines()
                    for i in data:
                        if i.startswith("mont1"):
                            mont1.set(1)
                        if i.startswith("mont2"):
                            mont2.set(1)
                        if i.startswith("mont3"):
                            mont3.set(1)
                        if i.startswith("std1") and len(i)==6:
                            std1.set(1)
                        if i.startswith("std2"):
                            std2.set(1)
                        if i.startswith("std3"):
                            std3.set(1)
                        if i.startswith("std4"):
                            std4.set(1)
                        if i.startswith("std5"):
                            std5.set(1)
                        if i.startswith("std6"):
                            std6.set(1)
                        if i.startswith("std7"):
                            std7.set(1)
                        if i.startswith("std8"):
                            std8.set(1)
                        if i.startswith("std9"):
                            std9.set(1)
                        if i.startswith("std10"):
                            std10.set(1)
                        if i.startswith("std11"):
                            std11.set(1)
                        if i.startswith("std12"):
                            std12.set(1)
                        if i.startswith("1styr"):
                            first_yr.set(1)
                        if i.startswith("2ndyr"):
                            second_yr.set(1)
                        if i.startswith("3rdyr"):
                            third_yr.set(1)
                        if i.startswith("4thyr"):
                            fourth_yr.set(1)
            except FileNotFoundError:
                pass

        cl = Toplevel()
        cl.protocol("WM_DELETE_WINDOW",lambda:[manage.deiconify(),cl.destroy()])
        cl.tk.call('wm', 'iconphoto', cl._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        cl.title("Select")
        cl.geometry("1024x512")
        app_height=512
        app_width=1024
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        cl.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            
        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\sel_cl light.png"))
            label1 = Label(cl, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\sel_cl dark.png"))
            label1 = Label(cl, image=bg_image)
            label1.pack()

        institution = institutionsel.get()
        branch = branchsel.get()

        info = ttk.Label(cl, text=str(institution+" "+branch))

        global mont1
        mont1 = IntVar()
        global mont2
        mont2 = IntVar()
        global mont3
        mont3 = IntVar()
        global std1
        std1 = IntVar()
        global std2
        std2 = IntVar()
        global std3
        std3 = IntVar()
        global std4
        std4 = IntVar()
        global std5
        std5 = IntVar()
        global std6
        std6 = IntVar()
        global std7
        std7 = IntVar()
        global std8
        std8 = IntVar()
        global std9
        std9 = IntVar()
        global std10
        std10 = IntVar()
        global std11
        std11 = IntVar()
        global std12
        std12 = IntVar()
        global first_yr
        first_yr = IntVar()
        global second_yr
        second_yr = IntVar()
        global third_yr
        third_yr = IntVar()
        global fourth_yr
        fourth_yr = IntVar()

        mont1check = ttk.Checkbutton(cl, variable=mont1)
        mont2check = ttk.Checkbutton(cl, variable=mont2)
        mont3check = ttk.Checkbutton(cl, variable=mont3)

        std1check = ttk.Checkbutton(cl, variable=std1)
        std2check = ttk.Checkbutton(cl, variable=std2)
        std3check = ttk.Checkbutton(cl, variable=std3)
        std4check = ttk.Checkbutton(cl, variable=std4)
        std5check = ttk.Checkbutton(cl, variable=std5)

        std6check = ttk.Checkbutton(cl, variable=std6)
        std7check = ttk.Checkbutton(cl, variable=std7)
        std8check = ttk.Checkbutton(cl, variable=std8)

        std9check = ttk.Checkbutton(cl, variable=std9)
        std10check = ttk.Checkbutton(cl, variable=std10)
        std11check = ttk.Checkbutton(cl, variable=std11)
        std12check = ttk.Checkbutton(cl, variable=std12)

        first_yr_check = ttk.Checkbutton(cl, variable=first_yr)
        second_yr_check = ttk.Checkbutton(cl, variable=second_yr)
        third_yr_check = ttk.Checkbutton(cl, variable=third_yr)
        fourth_yr_check = ttk.Checkbutton(cl, variable=fourth_yr)
        
        save_button = ttk.Button(cl, text="Save", width=16, command=lambda: [butnormal(select_sec), cl.destroy(),manage.deiconify()])

        info.place(x=470, y=115)
        mont1check.place(x=220, y=182)
        mont2check.place(x=395, y=182)
        mont3check.place(x=570, y=182)

        std1check.place(x=220, y=240)
        std2check.place(x=395, y=240)
        std3check.place(x=570, y=240)
        std4check.place(x=745, y=240)
        std5check.place(x=220, y=298)

        std6check.place(x=220, y=350)
        std7check.place(x=395, y=350)
        std8check.place(x=570, y=350)

        std9check.place(x=220, y=400)
        std10check.place(x=395, y=400)
        std11check.place(x=570, y=400)
        std12check.place(x=745, y=400)

        first_yr_check.place(x=220, y=455)
        second_yr_check.place(x=395, y=455)
        third_yr_check.place(x=570, y=455)
        fourth_yr_check.place(x=745, y=455)

        save_button.place(x=825, y=37)

        clicking_check()


        cl.mainloop()
    ###############################################selectsectionswindow#################################
    def sel_sec():
        def clicking_check():
            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")

            tablename2 = str(ins+br+ba+"sections")
            filename2 = str(tablename2 + ".txt")
            filename2 = filename2.replace(" ", "")

            try:
                with open(filename2, "r") as x:
                    text = x.read()

                    sections = len(text)
                    x = sections / 2
                    cnt = 0
                    y = 0
                    z = 2
                    data = []
                    while cnt <= x:
                        data.append(text[y:z])
                        cnt += 1
                        y += 2
                        z += 2

                    m1 = data[0]
                    m2 = data[1]
                    m3 = data[2]
                    s1 = data[3]
                    s2 = data[4]
                    s3 = data[5]
                    s4 = data[6]
                    s5 = data[7]
                    s6 = data[8]
                    s7 = data[9]
                    s8 = data[10]
                    s9 = data[11]
                    s10 = data[12]
                    s11 = data[13]
                    s12 = data[14]
                    c1 = data[15]
                    c2 = data[16]
                    c3 = data[17]
                    c4 = data[18]

                    try:
                        mont1sections.current(m1)
                    except TclError:
                        pass
                    try:
                        mont2sections.current(m2)
                    except TclError:
                        pass
                    try:
                        mont3sections.current(m3)
                    except TclError:
                        pass
                    try:
                        std1sections.current(s1)
                    except TclError:
                        pass
                    try:
                        std2sections.current(s2)
                    except TclError:
                        pass
                    try:
                        std3sections.current(s3)
                    except TclError:
                        pass
                    try:
                        std4sections.current(s4)
                    except TclError:
                        pass
                    try:
                        std5sections.current(s5)
                    except TclError:
                        pass
                    try:
                        std6sections.current(s6)
                    except TclError:
                        pass
                    try:
                        std7sections.current(s7)
                    except TclError:
                        pass
                    try:
                        std8sections.current(s8)
                    except TclError:
                        pass
                    try:
                        std9sections.current(s9)
                    except TclError:
                        pass
                    try:
                        std10sections.current(s10)
                    except TclError:
                        pass
                    try:
                        std11sections.current(s11)
                    except TclError:
                        pass
                    try:
                        std12sections.current(s12)
                    except TclError:
                        pass
                    try:
                        first_yr_sections.current(c1)
                    except TclError:
                        pass
                    try:
                        second_yr_sections.current(c2)
                    except TclError:
                        pass
                    try:
                        third_yr_sections.current(c3)
                    except TclError:
                        pass
                    try:
                        fourth_yr_sections.current(c4)
                    except TclError:
                        pass

            except FileNotFoundError:
                pass

        sec = Toplevel()
        sec.protocol("WM_DELETE_WINDOW",lambda:[manage.deiconify(),sec.destroy()])
        sec.tk.call('wm', 'iconphoto', sec._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        sec.title("Select")
        sec.geometry("768x700")
        app_height=700
        app_width=768
        screenwidth = mainsplash.winfo_screenwidth()
        screenheight = mainsplash.winfo_screenheight()

        x = (screenwidth / 2) - (app_width / 2)
        y = (screenheight / 2) - (app_height / 2)

        sec.geometry(f'{app_width}x{app_height}+{int(x)}+0')
        
        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\sel_sec light.png"))
            label1 = Label(sec, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\sel_sec dark.png"))
            label1 = Label(sec, image=bg_image)
            label1.pack()

        options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16",
                   "17",
                   "18", "19",
                   "20", "21", "22", "23", "24", "25", "26"]

        global mont1sections                                                                                                       
        global mont2sections
        global mont3sections
        global std1sections
        global std2sections
        global std3sections
        global std4sections
        global std5sections
        global std6sections
        global std7sections
        global std8sections
        global std9sections
        global std10sections
        global std11sections
        global std12sections
        global first_yr_sections
        global second_yr_sections
        global third_yr_sections
        global fourth_yr_sections

        mont1sections = ttk.Combobox(sec, values=options)
        mont2sections = ttk.Combobox(sec, values=options)
        mont3sections = ttk.Combobox(sec, values=options)
        std1sections = ttk.Combobox(sec, values=options)
        std2sections = ttk.Combobox(sec, values=options)
        std3sections = ttk.Combobox(sec, values=options)
        std4sections = ttk.Combobox(sec, values=options)
        std5sections = ttk.Combobox(sec, values=options)
        std6sections = ttk.Combobox(sec, values=options)
        std7sections = ttk.Combobox(sec, values=options)
        std8sections = ttk.Combobox(sec, values=options)
        std9sections = ttk.Combobox(sec, values=options)
        std10sections = ttk.Combobox(sec, values=options)
        std11sections = ttk.Combobox(sec, values=options)
        std12sections = ttk.Combobox(sec, values=options)
        first_yr_sections = ttk.Combobox(sec, values=options)
        second_yr_sections = ttk.Combobox(sec, values=options)
        third_yr_sections = ttk.Combobox(sec, values=options)
        fourth_yr_sections = ttk.Combobox(sec, values=options)

        def save():
            mont1sec = []
            mont2sec = []
            mont3sec = []
            std1sec = []
            std2sec = []
            std3sec = []
            std4sec = []
            std5sec = []
            std6sec = []
            std7sec = []
            std8sec = []
            std9sec = []
            std10sec = []
            std11sec = []
            std12sec = []
            firstyrsec = []
            secondyrsec = []
            thirdyrsec = []
            fourthyrsec = []

            m1sec = str(mont1sections.current())
            m2sec = str(mont2sections.current())
            m3sec = str(mont3sections.current())
            s1sec = str(std1sections.current())
            s2sec = str(std2sections.current())
            s3sec = str(std3sections.current())
            s4sec = str(std4sections.current())
            s5sec = str(std5sections.current())
            s6sec = str(std6sections.current())
            s7sec = str(std7sections.current())
            s8sec = str(std8sections.current())
            s9sec = str(std9sections.current())
            s10sec = str(std10sections.current())
            s11sec = str(std11sections.current())
            s12sec = str(std12sections.current())
            c1sec = str(first_yr_sections.current())
            c2sec = str(second_yr_sections.current())
            c3sec = str(third_yr_sections.current())
            c4sec = str(fourth_yr_sections.current())

            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")

            tablename2 = str(ins+br+ba+"sections")
            filename2 = str(tablename2 + ".txt")
            filename2 = filename2.replace(" ", "")

            with open(filename2, "w") as x:

                if int(m1sec) > 10:
                    x.write(m1sec)
                elif -1 < int(m1sec) < 10:
                    x.write("0" + m1sec)
                elif int(m1sec) == -1:
                    x.write(m1sec)

                if int(m2sec) > 10:
                    x.write(m2sec)
                elif -1 < int(m2sec) < 10:
                    x.write("0" + m2sec)
                elif int(m2sec) == -1:
                    x.write(m2sec)

                if int(m3sec) > 10:
                    x.write(m3sec)                                                                                    
                elif -1 < int(m3sec) < 10:
                    x.write("0" + m3sec)
                elif int(m3sec) == -1:
                    x.write(m3sec)

                if int(s1sec) > 10:
                    x.write(s1sec)
                elif -1 < int(s1sec) < 10:
                    x.write("0" + s1sec)
                elif int(s1sec) == -1:
                    x.write(s1sec)

                if int(s2sec) > 10:
                    x.write(s2sec)
                elif -1 < int(s2sec) < 10:
                    x.write("0" + s2sec)
                elif int(s2sec) == -1:
                    x.write(s2sec)

                if int(s3sec) > 10:
                    x.write(s3sec)
                elif -1 < int(s3sec) < 10:
                    x.write("0" + s3sec)
                elif int(s3sec) == -1:
                    x.write(s3sec)

                if int(s4sec) > 10:
                    x.write(s4sec)
                elif -1 < int(s4sec) < 10:
                    x.write("0" + s4sec)
                elif int(s4sec) == -1:
                    x.write(s4sec)

                if int(s5sec) > 10:
                    x.write(s5sec)
                elif -1 < int(s5sec) < 10:
                    x.write("0" + s5sec)
                elif int(s5sec) == -1:
                    x.write(s5sec)

                if int(s6sec) > 10:
                    x.write(s6sec)
                elif -1 < int(s6sec) < 10:
                    x.write("0" + s6sec)
                elif int(s6sec) == -1:
                    x.write(s6sec)

                if int(s7sec) > 10:
                    x.write(s7sec)
                elif -1 < int(s7sec) < 10:
                    x.write("0" + s7sec)
                elif int(s7sec) == -1:
                    x.write(s7sec)

                if int(s8sec) > 10:
                    x.write(s8sec)
                elif -1 < int(s8sec) < 10:
                    x.write("0" + s8sec)
                elif int(s8sec) == -1:
                    x.write(s8sec)

                if int(s9sec) > 10:
                    x.write(s9sec)
                elif -1 < int(s9sec) < 10:
                    x.write("0" + s9sec)
                elif int(s9sec) == -1:
                    x.write(s9sec)

                if int(s10sec) > 10:
                    x.write(s10sec)
                elif -1 < int(s10sec) < 10:
                    x.write("0" + s10sec)
                elif int(s10sec) == -1:
                    x.write(s10sec)

                if int(s11sec) > 10:
                    x.write(s11sec)
                elif -1 < int(s11sec) < 10:
                    x.write("0" + s11sec)
                elif int(s11sec) == -1:
                    x.write(s11sec)

                if int(s12sec) > 10:
                    x.write(s12sec)
                elif -1 < int(s12sec) < 10:
                    x.write("0" + s12sec)
                elif int(s12sec) == -1:
                    x.write(s12sec)

                if int(c1sec) > 10:
                    x.write(c1sec)
                elif -1 < int(c1sec) < 10:
                    x.write("0" + c1sec)
                elif int(c1sec) == -1:
                    x.write(c1sec)

                if int(c2sec) > 10:
                    x.write(c2sec)
                elif -1 < int(c2sec) < 10:
                    x.write("0" + c2sec)                                                                  
                elif int(c2sec) == -1:
                    x.write(c2sec)

                if int(c3sec) > 10:
                    x.write(c3sec)
                elif -1 < int(c3sec) < 10:
                    x.write("0" + c3sec)
                elif int(c3sec) == -1:
                    x.write(c3sec)

                if int(c4sec) > 10:
                    x.write(c4sec)
                elif -1 < int(c4sec) < 10:
                    x.write("0" + c4sec)
                elif int(c4sec) == -1:
                    x.write(c4sec)

            def addsections(x, y):
                sections = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S",
                            "T", "U", "V", "W", "X", "Y", "Z"]
                if x == "0":
                    for i in sections[0:1]:
                        y.append(i)
                elif x == "1":
                    for i in sections[0:2]:
                        y.append(i)
                elif x == "2":
                    for i in sections[0:3]:
                        y.append(i)
                elif x == "3":
                    for i in sections[0:4]:
                        y.append(i)
                elif x == "4":
                    for i in sections[0:5]:
                        y.append(i)
                elif x == "5":
                    for i in sections[0:6]:
                        y.append(i)
                elif x == "6":
                    for i in sections[0:7]:
                        y.append(i)
                elif x == "7":
                    for i in sections[0:8]:
                        y.append(i)
                elif x == "8":
                    for i in sections[0:9]:
                        y.append(i)
                elif x == "9":
                    for i in sections[0:10]:
                        y.append(i)
                elif x == "10":
                    for i in sections[0:11]:
                        y.append(i)
                elif x == "11":
                    for i in sections[0:12]:
                        y.append(i)
                elif x == "12":
                    for i in sections[0:13]:
                        y.append(i)
                elif x == "13":
                    for i in sections[0:14]:
                        y.append(i)
                elif x == "14":
                    for i in sections[0:15]:
                        y.append(i)
                elif x == "15":
                    for i in sections[0:16]:
                        y.append(i)
                elif x == "16":
                    for i in sections[0:17]:
                        y.append(i)
                elif x == "17":
                    for i in sections[0:18]:
                        y.append(i)
                elif x == "18":
                    for i in sections[0:19]:
                        y.append(i)
                elif x == "19":
                    for i in sections[0:20]:
                        y.append(i)
                elif x == "20":
                    for i in sections[0:21]:
                        y.append(i)
                elif x == "21":
                    for i in sections[0:22]:
                        y.append(i)
                elif x == "22":
                    for i in sections[0:23]:
                        y.append(i)
                elif x == "23":
                    for i in sections[0:24]:
                        y.append(i)
                elif x == "24":
                    for i in sections[0:25]:
                        y.append(i)
                elif x == "25":
                    for i in sections[0:26]:
                        y.append(i)

            addsections(m1sec, mont1sec)                                                                       
            addsections(m2sec, mont2sec)
            addsections(m3sec, mont3sec)
            addsections(s1sec, std1sec)
            addsections(s2sec, std2sec)
            addsections(s3sec, std3sec)
            addsections(s4sec, std4sec)
            addsections(s5sec, std5sec)
            addsections(s6sec, std6sec)
            addsections(s7sec, std7sec)
            addsections(s8sec, std8sec)
            addsections(s9sec, std9sec)
            addsections(s10sec, std10sec)
            addsections(s11sec, std11sec)
            addsections(s12sec, std12sec)
            addsections(c1sec, firstyrsec)
            addsections(c2sec, secondyrsec)
            addsections(c3sec, thirdyrsec)
            addsections(c4sec, fourthyrsec)

            for i in mont1sec:
                allclasssection.append("mont1" + i)
            for i in mont2sec:
                allclasssection.append("mont2" + i)
            for i in mont3sec:
                allclasssection.append("mont3" + i)
            for i in std1sec:
                allclasssection.append("std1" + i)
            for i in std2sec:
                allclasssection.append("std2" + i)
            for i in std3sec:
                allclasssection.append("std3" + i)
            for i in std4sec:
                allclasssection.append("std4" + i)
            for i in std5sec:
                allclasssection.append("std5" + i)
            for i in std6sec:
                allclasssection.append("std6" + i)
            for i in std7sec:
                allclasssection.append("std7" + i)
            for i in std8sec:
                allclasssection.append("std8" + i)
            for i in std9sec:
                allclasssection.append("std9" + i)
            for i in std10sec:
                allclasssection.append("std10" + i)
            for i in std11sec:
                allclasssection.append("std11" + i)
            for i in std12sec:
                allclasssection.append("std12" + i)
            for i in firstyrsec:
                allclasssection.append("1styr" + i)
            for i in secondyrsec:
                allclasssection.append("2ndyr" + i)
            for i in thirdyrsec:
                allclasssection.append("3rdyr" + i)
            for i in fourthyrsec:
                allclasssection.append("4thyr" + i)

            ins = institutionsel.get()
            br = branchsel.get()
            ba = batchsel.get()
            y = '-'
            for z in y:
                ba = ba.replace(z, "")

            tablename = str(ins+br+ba+"classes")
            filename = str(tablename + ".txt")
            filename = filename.replace(" ", "")

            with open(filename, "w") as x:
                for i in mont1sec:
                    x.write("mont1" + i + "\n")
                for i in mont2sec:
                    x.write("mont2" + i + "\n")
                for i in mont3sec:
                    x.write("mont3" + i + "\n")
                for i in std1sec:
                    x.write("std1" + i + "\n")
                for i in std2sec:
                    x.write("std2" + i + "\n")
                for i in std3sec:
                    x.write("std3" + i + "\n")
                for i in std4sec:
                    x.write("std4" + i + "\n")
                for i in std5sec:
                    x.write("std5" + i + "\n")
                for i in std6sec:
                    x.write("std6" + i + "\n")
                for i in std7sec:
                    x.write("std7" + i + "\n")
                for i in std8sec:
                    x.write("std8" + i + "\n")
                for i in std9sec:
                    x.write("std9" + i + "\n")
                for i in std10sec:
                    x.write("std10" + i + "\n")
                for i in std11sec:
                    x.write("std11" + i + "\n")
                for i in std12sec:
                    x.write("std12" + i + "\n")
                for i in firstyrsec:
                    x.write("1styr" + i + "\n")
                for i in secondyrsec:
                    x.write("2ndyr" + i + "\n")
                for i in thirdyrsec:
                    x.write("3rdyr" + i + "\n")
                for i in fourthyrsec:
                    x.write("4thyr" + i + "\n")

        mont1label = ttk.Label(sec, text="Mont1")
        mont2label = ttk.Label(sec, text="Mont2")
        mont3label = ttk.Label(sec, text="Mont3")
        std1label = ttk.Label(sec, text="std1")
        std2label = ttk.Label(sec, text="std2")
        std3label = ttk.Label(sec, text="std3")
        std4label = ttk.Label(sec, text="std4")
        std5label = ttk.Label(sec, text="std5")
        std6label = ttk.Label(sec, text="std6")
        std7label = ttk.Label(sec, text="std7")
        std8label = ttk.Label(sec, text="std8")
        std9label = ttk.Label(sec, text="std9")
        std10label = ttk.Label(sec, text="std10")
        std11label = ttk.Label(sec, text="std11")
        std12label = ttk.Label(sec, text="std12")
        first_yr_label = ttk.Label(sec, text="1styr")
        second_yr_label = ttk.Label(sec, text="2ndyr")
        third_yr_label = ttk.Label(sec, text="3rdyr")
        fourth_yr_label = ttk.Label(sec, text="4thyr")

        save_button = ttk.Button(sec, text="Save", width=16,
                                 command=lambda: [butnormal(studentinfo), save(), sec.destroy() ,manage.deiconify()])

        a = 40
        b = 110
        c = 100
        d = 100

        if mont1.get() == 1:
            mont1label.place(x=a, y=b)
            mont1sections.place(x=c, y=d)
        if mont2.get() == 1:
            b += 50
            d += 50
            mont2label.place(x=a, y=b)
            mont2sections.place(x=c, y=d)
        if mont3.get() == 1:
            b += 50
            d += 50
            mont3label.place(x=a, y=b)
            mont3sections.place(x=c, y=d)
        if std1.get() == 1:
            b += 50
            d += 50
            std1label.place(x=a, y=b)
            std1sections.place(x=c, y=d)
        if std2.get() == 1:
            b += 50
            d += 50
            std2label.place(x=a, y=b)
            std2sections.place(x=c, y=d)
        if std3.get() == 1:
            b += 50
            d += 50
            std3label.place(x=a, y=b)
            std3sections.place(x=c, y=d)
        if std4.get() == 1:
            b += 50
            d += 50
            std4label.place(x=a, y=b)
            std4sections.place(x=c, y=d)
        if std5.get() == 1:
            b += 50
            d += 50
            std5label.place(x=a, y=b)
            std5sections.place(x=c, y=d)
        if std6.get() == 1:
            b += 50
            d += 50
            std6label.place(x=a, y=b)
            std6sections.place(x=c, y=d)
        if std7.get() == 1:
            b += 50
            d += 50
            std7label.place(x=a, y=b)
            std7sections.place(x=c, y=d)
        if std8.get() == 1:
            b += 50
            d += 50
            std8label.place(x=a, y=b)
            std8sections.place(x=c, y=d)
        a = 300
        b = 110
        c = 360
        d = 100
        if std9.get() == 1:
            b += 50
            d += 50
            std9label.place(x=a, y=b)
            std9sections.place(x=c, y=d)
        if std10.get() == 1:
            b += 50
            d += 50
            std10label.place(x=a, y=b)
            std10sections.place(x=c, y=d)
        if std11.get() == 1:
            b += 50
            d += 50
            std11label.place(x=a, y=b)
            std11sections.place(x=c, y=d)
        if std12.get() == 1:
            b += 50
            d += 50
            std12label.place(x=a, y=b)
            std12sections.place(x=c, y=d)
        if first_yr.get() == 1:
            b += 50
            d += 50
            first_yr_label.place(x=a, y=b)
            first_yr_sections.place(x=c, y=d)
        if second_yr.get() == 1:
            b += 50
            d += 50
            second_yr_label.place(x=a, y=b)
            second_yr_sections.place(x=c, y=d)
        if third_yr.get() == 1:
            b += 50
            d += 50
            third_yr_label.place(x=a, y=b)
            third_yr_sections.place(x=c, y=d)
        if fourth_yr.get() == 1:
            b += 50
            d += 50
            fourth_yr_label.place(x=a, y=b)
            fourth_yr_sections.place(x=c, y=d)

        save_button.place(x=300, y=600)

        clicking_check()

        sec.mainloop()
    #######################################addstudentdetailswindow######################################
    def addstudents():
        global stud
        stud = Toplevel()
        stud.protocol("WM_DELETE_WINDOW",lambda:[manage.deiconify(),stud.destroy()])
        stud.tk.call('wm', 'iconphoto', stud._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        stud.title("Attendance Register")
        stud.geometry("1366x720+-8+0")
        stud.resizable(0, 0)
        stud.state('zoomed')

        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\add stud details light.png"))
            label1 = Label(stud, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\add stud details dark.png"))
            label1 = Label(stud, image=bg_image)
            label1.pack()
        #####################################fetcholdstuddetail########################################
        def fetchdata():
            global count
            ins = institutionsel.get()
            br = branchsel.get()
            batchvalue = batchsel.get()
            y = '-'
            for z in y:
                batchvalue = batchvalue.replace(z, "")

            name = str(ins+br+batchvalue)
            dbname = name.strip()
            try:
                cur.execute(" USE {} ;".format(dbname))

                classv = classsec.get()
                cur.execute("select * from {} order by rollno;".format(classv))
                data = cur.fetchall()
                lst = []

                for rows in data:
                    lst.append(rows)
                
                for i in lst:
                    tree.insert(parent='', index="end", iid=count, text="",
                                values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
                    counter = count + 1
                    count = counter

                if lst!=[]:
                    cur.execute("select classteacher from {};".format(classv))
                    y=cur.fetchall()
                    x=y[0]    
                    classteacher.delete(0 ,END)
                    classteacher.insert(0,x)
                if lst==[]:
                    classteacher.delete(0 ,END)
            except sequal.ProgrammingError:
                messagebox.showinfo("no database created.","please create a batch to add students.")
                stud.destroy()
        #####################################difftableforeachclass######################################
        def difftree():
            classx = classsec.get()
            treeframe = classx + "frame"
            treescroll = classx + "scroll"
            global tree
            tree = classx + "tree"

            treeframe = Frame(stud)
            treeframe.place(x=70, y=170)

            treescroll = ttk.Scrollbar(treeframe)
            treescroll.pack(side=RIGHT, fill=Y)

            tree = ttk.Treeview(treeframe, yscrollcommand=treescroll.set)
            treescroll.config(command=tree.yview)

            ###########################################savedetails######################################
            def savefn():
                def clear_all():
                    for item in tree.get_children():
                        tree.delete(item)

                batchvalue = batchsel.get()
                rollnovalue = rl.current() + 1
                studentnamevalue = studentname.get()
                admnovalue = admno.get()
                # batch
                pemailvalue = pemail.get()
                classv = int(classsec.current())
                classvalue = allclasssection[classv]
                classteachervalue = classteacher.get()

                ins = institutionsel.get()
                br = branchsel.get()

                y = '-'
                for z in y:
                    batchvalue = batchvalue.replace(z, "")

                name = str(ins+br+batchvalue)
                dbname = name.strip()
                cur.execute(" USE {} ;".format(dbname))
                cur.execute("insert into {} values('{}','{}','{}','{}','{}','{}','{}');".format(classvalue, rollnovalue,
                                                                                                studentnamevalue,
                                                                                                admnovalue, batchvalue,
                                                                                                pemailvalue, classvalue,
                                                                                                classteachervalue))
                db.commit()
                clear_all()
                fetchdata()

                rl.set(rollnovalue + 1)
                studentname.delete(0, END)
                admno.delete(0, END)
                pemail.delete(0, END)
                
            ################################################deletedetails################################
            def deletefn():
                def clear_all():
                    for item in tree.get_children():
                        tree.delete(item)

                selected = tree.focus()
                values = tree.item(selected, "values")
                rollno = values[0]

                ins = institutionsel.get()
                br = branchsel.get()
                batchvalue = batchsel.get()
                classv = int(classsec.current())
                classvalue = allclasssection[classv]

                y = '-'
                for z in y:
                    batchvalue = batchvalue.replace(z, "")

                name = str(ins+br+batchvalue)
                dbname = name.strip()
                cur.execute("use {};".format(dbname))
                cur.execute("delete from {} where rollno='{}';".format(classvalue, rollno))
                db.commit()

                x = tree.selection()
                for i in x:
                    tree.delete(i)
                clear_all()
                fetchdata()

            ############################################clearwidgets####################################
            def clearfn():
                rl.set('')
                studentname.delete(0, END)
                admno.delete(0, END)
                pemail.delete(0, END)
            ############################################selectrecords#######################################
            def select_record():
                rl.set('')
                classteacher.delete(0, END)
                studentname.delete(0, END)
                admno.delete(0, END)
                pemail.delete(0, END)

                selected = tree.focus()
                values = tree.item(selected, "values")

                rl.set(values[0])
                classteacher.insert(0, values[6])
                studentname.insert(0, values[1])
                admno.insert(0, values[2])
                pemail.insert(0, values[4])
            ############################################updateexistingdata################################
            def update_record():
                def clear_all():
                    for item in tree.get_children():
                        tree.delete(item)

                selected = tree.focus()
                classv = int(classsec.current())
                classvalue = allclasssection[classv]
                value = tree.item(selected, text="", values=(
                    int(rl.current() + 1), studentname.get(), admno.get(), batchsel.current(), pemail.get(),
                    allclasssection[classv], classteacher.get()))
                ins = institutionsel.get()
                br = branchsel.get()
                batchvalue = batchsel.get()
                roll = int(rl.current() + 1)
                stude = studentname.get()
                adm = admno.get()
                pmail = pemail.get()
                clteacher = classteacher.get()

                y = '-'
                for z in y:
                    batchvalue = batchvalue.replace(z, "")

                name = str(ins+br+batchvalue)
                dbname = name.strip()
                cur.execute(" USE {} ;".format(dbname))
                cur.execute(
                    "update {} set rollno={},studentname='{}',admno='{}',parentemail='{}',classteacher='{}' where rollno={}".format(
                        classvalue, roll, stude, adm, pmail, clteacher, roll))
                db.commit()
                clear_all()
                fetchdata()

                classteacher.delete(0, END)
                studentname.delete(0, END)
                admno.delete(0, END)
                pemail.delete(0, END)

            def clicker(e):
                select_record()

            tree['columns'] = ("ROLL NO", "STUDENT NAME", "ADM NO", "BATCH", "PARENT EMAIL", "CLASS", "CLASS TEACHER")
            tree.column("#0", width=0, stretch=NO)
            tree.column("#1", anchor=CENTER, width=120)
            tree.column("#2", anchor=CENTER, width=120)
            tree.column("#3", anchor=CENTER, width=120)
            tree.column("#4", anchor=CENTER, width=120)
            tree.column("#5", anchor=CENTER, width=180)
            tree.column("#6", anchor=CENTER, width=120)
            tree.column("#7", anchor=CENTER, width=120)

            tree.heading("#0")
            tree.heading("#1", text="ROLL NO", anchor=CENTER)
            tree.heading("#2", text="STUDENT NAME", anchor=CENTER)
            tree.heading("#3", text="ADM NO", anchor=CENTER)
            tree.heading("#4", text="BATCH", anchor=CENTER)
            tree.heading("#5", text="PARENT EMAIL", anchor=CENTER)
            tree.heading("#6", text="CLASS", anchor=CENTER)
            tree.heading("#7", text="CLASS TEACHER", anchor=CENTER)

            tree.pack()

            tree.bind('<Double-1>', clicker)

            save = ttk.Button(stud, text="SAVE", width=12, command=lambda: savefn())
            save.place(x=1133, y=80)

            clear = ttk.Button(stud, text="CLEAR", width=12, command=lambda: clearfn())
            clear.place(x=1130, y=149)

            update = ttk.Button(stud, text="UPDATE", width=12, command=lambda: update_record())
            update.place(x=1133, y=218)

            delete = ttk.Button(stud, text="DELETE", width=12, command=lambda: deletefn())
            delete.place(x=1130, y=287)

        classsec = ttk.Combobox(stud, values=allclasssection)
        classsec.place(x=349, y=85)

        global roll
        roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60]

        classteacher = ttk.Entry(stud, width=26)
        classteacher.place(x=781, y=85)

        global r1
        rl = ttk.Combobox(stud, values=roll, width=20)
        rl.place(x=508, y=548)

        studentname = ttk.Entry(stud, width=24)
        studentname.place(x=822, y=548)

        admno = ttk.Entry(stud, width=24)
        admno.place(x=508, y=600)

        pemail = ttk.Entry(stud, width=24)
        pemail.place(x=508, y=652)

        refresh = ttk.Button(stud, text="REFRESH TABLE", command=lambda: ([difftree(), fetchdata()]))
        refresh.place(x=570, y=85)

        exit = ttk.Button(stud, text="EXIT", width=12, command=lambda: [stud.destroy(),manage.deiconify()])
        exit.place(x=1133, y=356)

        stud.mainloop()
    #######################################manualforattendancereg#######################################
    def manual():
        man = Toplevel(main)
        man.tk.call('wm', 'iconphoto', man._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        man.title("Manual")
        man.geometry("512x512")
        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\manual template light.png"))
            label1 = Label(man, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\manual template dark.png"))
            label1 = Label(man, image=bg_image)
            label1.pack()
        close_button = ttk.Button(man, text="Close", padding=10, command=lambda: [man.destroy()])
        close_button.place(x=215, y=430)

        man.mainloop()
    ############################################attendanceentrywindow#######################################
    def root2():
        root_2 = Toplevel()
        root_2.protocol("WM_DELETE_WINDOW",lambda:[root.deiconify(),root_2.destroy()])
        root_2.tk.call('wm', 'iconphoto', root_2._w, ImageTk.PhotoImage(file='images\SMS.ico'))
        root_2.title("Attendance Register")
        app_width = 1366
        app_height = 768
        screenwidth = -8
        screenheight = 0
        root_2.geometry(f'{app_width}x{app_height}+{screenwidth}+{screenheight}')
        root_2.resizable(0, 0)
        root_2.state('zoomed')
        if mode == "light":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\template2 light.png"))
            label1 = Label(root_2, image=bg_image)
            label1.pack()
        elif mode == "dark":
            bg_image = ImageTk.PhotoImage(Image.open(r"images\template2 dark.png"))
            label1 = Label(root_2, image=bg_image)
            label1.pack()
        ##########################################refreshattendancedatabase###############################
        def attlistfn():
            def clear_all():
                    for item in tree2.get_children():
                        tree2.delete(item)
            clear_all()
            refreshfn()
            global lst4,lst5
            
            classx = int(class_box.current())
            classsel = allclasssection[classx]

            studframename = classsel+ "studframe"
            studframe2name = classsel+ "studframe2"
            studcanvasname = classsel+ "studcanvas"
            studscrollname = classsel+ "studscroll"

            studframename = Frame(root_2)
            studframename.place(x=1072, y=130)
            studframename.grid_rowconfigure(0, weight=1)
            studframename.grid_columnconfigure(0, weight=1)
            studframename.grid_propagate(0)

            studcanvasname=Canvas(studframename)
            studcanvasname.grid(row=0 ,column=0 ,sticky="news")

            studscrollname = ttk.Scrollbar(studframename,orient="vertical", command=studcanvasname.yview)
            studscrollname.grid(row=0 ,column=1, sticky='ns')
            studcanvasname.config(yscrollcommand=studscrollname.set)

            studframe2name=Frame(studcanvasname)
            studcanvasname.create_window((0, 0), window=studframe2name, anchor='nw')
            
            selstud = IntVar()  

            selectallstud = ttk.Checkbutton(studframe2name, text="Select all", variable=selstud, onvalue=1, offvalue=0,command=lambda:selall())
            selectallstud.grid(row=0,column=1, sticky='news')

            rolllabel=ttk.Label(studframe2name,text="  Roll no.  ")
            rolllabel.grid(row=1,column=0)

            studlabel=ttk.Label(studframe2name,text="  Student name  ")
            studlabel.grid(row=1,column=1)

            attlabel=ttk.Label(studframe2name,text="  Attendance  ")
            attlabel.grid(row=1,column=2)
            
            rollcnt=2
            for i in lst4:
                Label(studframe2name,text=i).grid(row=rollcnt,column=0)
                rollcnt+=1         

            global varnames

            varnames=[]
            studcnt=2
            for i in lst5:
                var=i+"var"
                var=IntVar()
                varnames.append(var)
                Label(studframe2name,text=i).grid(row=studcnt,column=1)
                checkbutname=str(i)+"check"
                checkbutname = ttk.Checkbutton(studframe2name, variable=var, onvalue=1, offvalue=0)
                checkbutname.grid(row=studcnt,column=2)   
                studcnt+=1

            def selall():
                choice=selstud.get()
                if choice==1:
                    for i in varnames:
                        i.set(1)
                if choice==0:
                    for i in varnames:
                        i.set(0)

            studframename.config(width=260,height=450)

            ##########################################saveattendance########################################
            def savefn():
                def clear_all():
                    for item in tree2.get_children():
                        tree2.delete(item)
                attlist=[]
                attendancelist=[]

                for i in varnames:
                    attendance=i.get()
                    if attendance==1:
                        attlist.append("P")
                    if attendance==0:
                        attlist.append("AB")

                for i in range(0, len(attlist)):
                    attendancelist.append([lst4[i], attlist[i]])

                tempdate = int(datebox.current())
                date = dates[tempdate]

                cur.execute("USE {};".format(dbname2))
                for i in attendancelist:
                    cur.execute("update {} set {}='{}' where rollno='{}';".format(classsel, date, i[1],i[0]))
                
                db.commit()
                clear_all()
                refreshfn()
                
    
            savebutton = ttk.Button(root_2, text="SAVE",width=15 , padding=5, command=lambda: savefn())
            savebutton.place(x=1130, y=590)


        def refreshfn():      
            classx = int(class_box.current())
            classsel = allclasssection[classx]
            month=monthbox.get()
            
            y = "attendance"+month
            for i in y:
                dbname = dbname2.replace(y, "")

            cur.execute("use {};".format(dbname2))
            try:
                cur.execute("select rollno from {};".format(classsel))
            except sequal.ProgrammingError:
                messagebox.askokcancel("empty data in table.", " admin must add students in order to add attendance.")
            data4 = cur.fetchall()
            global lst4
            lst4 = []

            for i in data4:
                for j in i:
                    lst4.append(j)

            cur.execute("use {};".format(dbname2))
            cur.execute("select studentname from {};".format(classsel))
            data5 = cur.fetchall()
            global lst5
            lst5 = []

            for i in data5:
                for j in i:
                    lst5.append(j)

            cur.execute("use {};".format(dbname))
            cur.execute("select rollno from {};".format(classsel))
            data2 = cur.fetchall()
            lst2 = []

            for i in data2:
                for j in i:
                    lst2.append(j)

            lstt = []
            for i in range(0, len(lst4)):
                lstt.append([lst4[i], lst5[i]])

            cur.execute("use {};".format(dbname))
            cur.execute("select studentname from {};".format(classsel))
            data3 = cur.fetchall()
            lst3 = []

            for i in data3:
                for j in i:
                    lst3.append(j)

            global lst
            lst = []
            for i in range(0, len(lst3)):
                lst.append([lst2[i], lst3[i]])

            for i in lst:
                if i not in lstt:
                    cur.execute("USE {};".format(dbname2))
                    cur.execute("insert into {}(rollno,studentname) values('{}','{}');".format(classsel, i[0], i[1]))
            
            db.commit()

            yrsundays=[]

            yrjanuarysundays=[]
            yrfebraurysundays=[]
            yrmarchsundays=[]
            yraprilsundays=[]
            yrmaysundays=[]
            yrjunesundays=[]
            yrjulysundays=[]
            yraugustsundays=[]
            yrseptembersundays=[]
            yroctobersundays=[]
            yrnovembersundays=[]
            yrdecembersundays=[]

            yr=month[0:4]
            
            #######################################getsundays###########################################
            def allsundays(year):
                d = date(int(year), 1, 1)     
                d += timedelta(days = 6 - d.weekday())
                while d.year == int(year):
                    yield d
                    d += timedelta(days = 7) 

            for d in allsundays(yr):
                yrsundays.append(str(d))

            for i in yrsundays:
                if i[5:7]=="01":
                    yrjanuarysundays.append(i)
                if i[5:7]=="02":
                    yrfebraurysundays.append(i)
                if i[5:7]=="03":
                    yrmarchsundays.append(i)
                if i[5:7]=="04":
                    yraprilsundays.append(i)
                if i[5:7]=="05":
                    yrmaysundays.append(i)
                if i[5:7]=="06":
                    yrjunesundays.append(i)
                if i[5:7]=="07":
                    yrjulysundays.append(i)
                if i[5:7]=="08":
                    yraugustsundays.append(i)
                if i[5:7]=="09":
                    yrseptembersundays.append(i)
                if i[5:7]=="10":
                    yroctobersundays.append(i)
                if i[5:7]=="11":
                    yrnovembersundays.append(i)
                if i[5:7]=="12":
                    yrdecembersundays.append(i)

            mon=month[4:20]
            dates=[]

            if mon=="January":
                for i in yrjanuarysundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="Febraury":
                for i in yrfebraurysundays:
                    if i[8:10]=="01":                                                                               
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":                                                                     
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="March":
                for i in yrmarchsundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")                                                                                                            
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="April":
                for i in yraprilsundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="May":
                for i in yrmaysundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")                                                                            
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="June":
                for i in yrjunesundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":                                                                         
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="July":
                for i in yrjulysundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")      

            elif mon=="August":
                for i in yraugustsundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="September":
                for i in yrseptembersundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":                                                                                             
                        dates.append("30th")                                                                                    
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="October":
                for i in yroctobersundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="November":
                for i in yrnovembersundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")                                                                        
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            elif mon=="December":
                for i in yrdecembersundays:
                    if i[8:10]=="01":
                        dates.append("1st")
                    elif i[8:10]=="02":
                        dates.append("2nd")
                    elif i[8:10]=="03":
                        dates.append("3rd")
                    elif i[8:10]=="04":
                        dates.append("4th")
                    elif i[8:10]=="05":
                        dates.append("5th")
                    elif i[8:10]=="06":
                        dates.append("6th")
                    elif i[8:10]=="07":
                        dates.append("7th")
                    elif i[8:10]=="08":
                        dates.append("8th")
                    elif i[8:10]=="09":
                        dates.append("9th")
                    elif i[8:10]=="10":
                        dates.append("10th")
                    elif i[8:10]=="11":
                        dates.append("11th")
                    elif i[8:10]=="12":
                        dates.append("12th")
                    elif i[8:10]=="13":
                        dates.append("13th")
                    elif i[8:10]=="14":
                        dates.append("14th")
                    elif i[8:10]=="15":
                        dates.append("15th")
                    elif i[8:10]=="16":
                        dates.append("16th")
                    elif i[8:10]=="17":
                        dates.append("17th")
                    elif i[8:10]=="18":
                        dates.append("18th")
                    elif i[8:10]=="19":
                        dates.append("19th")
                    elif i[8:10]=="20":
                        dates.append("20th")
                    elif i[8:10]=="21":
                        dates.append("21st")
                    elif i[8:10]=="22":
                        dates.append("22nd")
                    elif i[8:10]=="23":
                        dates.append("23rd")
                    elif i[8:10]=="24":
                        dates.append("24th")
                    elif i[8:10]=="25":
                        dates.append("25th")
                    elif i[8:10]=="26":
                        dates.append("26th")
                    elif i[8:10]=="27":
                        dates.append("27th")
                    elif i[8:10]=="28":
                        dates.append("28th")
                    elif i[8:10]=="29":
                        dates.append("29th")
                    elif i[8:10]=="30":
                        dates.append("30th")
                    elif i[8:10]=="31":
                        dates.append("31st")

            ##################################-onallsundays##############################################
            for i in dates:
                cur.execute("use {};".format(dbname2))
                cur.execute("update {} set {}='-';".format(classsel,i))
            db.commit()

            #################################getrollstudnamefromothertable###############################
            global count

            classx = int(class_box.current())
            classsel = allclasssection[classx]

            cur.execute(" USE {};".format(dbname2))
            cur.execute("select * from {};".format(classsel))
            data = cur.fetchall()

            lstt = []
            for rows in data:
                lstt.append(rows)
            ####################################leapcheck###############################################
            yrsel=month[0:4]
            leapcheck=False
            if((int(yrsel) % 400 == 0) or  (int(yrsel) % 100 != 0) and (int(yrsel) % 4 == 0)):
                leapcheck=True

            for i in lstt:
                if month[4:20]=="Febraury":

                    if leapcheck==False:
                        tree2.insert(parent='', index="end", iid=count, text="",
                                values=(
                                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                                i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26],
                                i[27], i[28], i[29]))
                        counter = count + 1
                        count = counter
                    if leapcheck==True:
                        tree2.insert(parent='', index="end", iid=count, text="",
                                values=(
                                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                                i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26],
                                i[27], i[28], i[29], i[30]))
                        counter = count + 1
                        count = counter

                elif month[4:20] == "January" or month[4:20] == "March" or  month[4:20] == "May" or  month[4:20] == "July" or  \
                month[4:20] == "August" or  month[4:20]== "October" or  month[4:20] == "December":
                    tree2.insert(parent='', index="end", iid=count, text="",
                                values=(
                                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                                i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26],
                                i[27], i[28], i[29], i[30], i[31], i[32]))
                    counter = count + 1
                    count = counter

                elif  month[4:20] == "April" or  month[4:20] == "June" or  month[4:20] == "September" or  month[4:20] == "November":
                    tree2.insert(parent='', index="end", iid=count, text="",
                                values=(
                                i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13],
                                i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25], i[26],
                                i[27], i[28], i[29], i[30], i[31]))
                    counter = count + 1
                    count = counter

        ####################################diffattendancetablefordiffclass##############################
        def difftree():

            classx = int(class_box.current())
            classsel = allclasssection[classx]

            treeframe = classsel + "frame"
            treescroll = classsel + "scroll"

            global tree2

            tree2 = classsel + "tree"
            treeframe = ttk.Frame(root_2)
            treeframe.place(x=24, y=150)

            treescroll = ttk.Scrollbar(treeframe)
            treescroll.pack(side=RIGHT, fill=Y)

            tree2 = ttk.Treeview(treeframe, yscrollcommand=treescroll.set)
            treescroll.config(command=tree2.yview)

            classx = int(class_box.current())
            classsel = allclasssection[classx]

            def clicker(e):
                pass

            month=monthbox.get()
            yrsel=month[0:4]
            leapcheck=False
            if((int(yrsel) % 400 == 0) or  (int(yrsel) % 100 != 0) and (int(yrsel) % 4 == 0)):
                leapcheck=True

            if month[4:20] == "Febraury":
                if leapcheck==False:
                    tree2['columns'] = (
                    "ROLL NO", "STUDENT NAME", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                    "15",
                    "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28")
                    
                    tree2.column("#0", width=0, stretch=NO)
                    tree2.column("#1", anchor=CENTER, width=120)
                    tree2.column("#2", anchor=CENTER, width=120)
                    tree2.column("#3", anchor=CENTER, width=24)
                    tree2.column("#4", anchor=CENTER, width=24)
                    tree2.column("#5", anchor=CENTER, width=24)
                    tree2.column("#6", anchor=CENTER, width=24)
                    tree2.column("#7", anchor=CENTER, width=24)
                    tree2.column("#8", anchor=CENTER, width=24)
                    tree2.column("#9", anchor=CENTER, width=24)
                    tree2.column("#10", anchor=CENTER, width=24)
                    tree2.column("#11", anchor=CENTER, width=24)
                    tree2.column("#12", anchor=CENTER, width=24)
                    tree2.column("#13", anchor=CENTER, width=24)
                    tree2.column("#14", anchor=CENTER, width=24)
                    tree2.column("#15", anchor=CENTER, width=24)
                    tree2.column("#16", anchor=CENTER, width=24)
                    tree2.column("#17", anchor=CENTER, width=24)
                    tree2.column("#18", anchor=CENTER, width=24)
                    tree2.column("#19", anchor=CENTER, width=24)
                    tree2.column("#20", anchor=CENTER, width=24)
                    tree2.column("#21", anchor=CENTER, width=24)
                    tree2.column("#22", anchor=CENTER, width=24)
                    tree2.column("#23", anchor=CENTER, width=24)
                    tree2.column("#24", anchor=CENTER, width=24)
                    tree2.column("#25", anchor=CENTER, width=24)
                    tree2.column("#26", anchor=CENTER, width=24)
                    tree2.column("#27", anchor=CENTER, width=24)
                    tree2.column("#28", anchor=CENTER, width=24)
                    tree2.column("#29", anchor=CENTER, width=24)
                    tree2.column("#30", anchor=CENTER, width=24)

                    tree2.heading("#0")
                    tree2.heading("#1", text="ROLL NO", anchor=CENTER)
                    tree2.heading("#2", text="STUDENT NAME", anchor=CENTER)
                    tree2.heading("#3", text="1", anchor=CENTER)
                    tree2.heading("#4", text="2", anchor=CENTER)
                    tree2.heading("#5", text="3", anchor=CENTER)
                    tree2.heading("#6", text="4", anchor=CENTER)
                    tree2.heading("#7", text="5", anchor=CENTER)
                    tree2.heading("#8", text="6", anchor=CENTER)
                    tree2.heading("#9", text="7", anchor=CENTER)
                    tree2.heading("#10", text="8", anchor=CENTER)
                    tree2.heading("#11", text="9", anchor=CENTER)
                    tree2.heading("#12", text="10", anchor=CENTER)
                    tree2.heading("#13", text="11", anchor=CENTER)
                    tree2.heading("#14", text="12", anchor=CENTER)
                    tree2.heading("#15", text="13", anchor=CENTER)
                    tree2.heading("#16", text="14", anchor=CENTER)
                    tree2.heading("#17", text="15", anchor=CENTER)
                    tree2.heading("#18", text="16", anchor=CENTER)
                    tree2.heading("#19", text="17", anchor=CENTER)
                    tree2.heading("#20", text="18", anchor=CENTER)
                    tree2.heading("#21", text="19", anchor=CENTER)
                    tree2.heading("#22", text="20", anchor=CENTER)
                    tree2.heading("#23", text="21", anchor=CENTER)
                    tree2.heading("#24", text="22", anchor=CENTER)
                    tree2.heading("#25", text="23", anchor=CENTER)
                    tree2.heading("#26", text="24", anchor=CENTER)
                    tree2.heading("#27", text="25", anchor=CENTER)
                    tree2.heading("#28", text="26", anchor=CENTER)
                    tree2.heading("#29", text="27", anchor=CENTER)
                    tree2.heading("#30", text="28", anchor=CENTER)
                    tree2.pack()
                    tree2.bind('<Double-1>', clicker)

                elif leapcheck==True:
                    tree2['columns'] = (
                    "ROLL NO", "STUDENT NAME", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                    "15",
                    "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29")
                    
                    tree2.column("#0", width=0, stretch=NO)
                    tree2.column("#1", anchor=CENTER, width=120)
                    tree2.column("#2", anchor=CENTER, width=120)
                    tree2.column("#3", anchor=CENTER, width=24)
                    tree2.column("#4", anchor=CENTER, width=24)
                    tree2.column("#5", anchor=CENTER, width=24)
                    tree2.column("#6", anchor=CENTER, width=24)
                    tree2.column("#7", anchor=CENTER, width=24)
                    tree2.column("#8", anchor=CENTER, width=24)
                    tree2.column("#9", anchor=CENTER, width=24)
                    tree2.column("#10", anchor=CENTER, width=24)
                    tree2.column("#11", anchor=CENTER, width=24)
                    tree2.column("#12", anchor=CENTER, width=24)
                    tree2.column("#13", anchor=CENTER, width=24)
                    tree2.column("#14", anchor=CENTER, width=24)
                    tree2.column("#15", anchor=CENTER, width=24)
                    tree2.column("#16", anchor=CENTER, width=24)
                    tree2.column("#17", anchor=CENTER, width=24)
                    tree2.column("#18", anchor=CENTER, width=24)
                    tree2.column("#19", anchor=CENTER, width=24)
                    tree2.column("#20", anchor=CENTER, width=24)
                    tree2.column("#21", anchor=CENTER, width=24)
                    tree2.column("#22", anchor=CENTER, width=24)
                    tree2.column("#23", anchor=CENTER, width=24)
                    tree2.column("#24", anchor=CENTER, width=24)
                    tree2.column("#25", anchor=CENTER, width=24)
                    tree2.column("#26", anchor=CENTER, width=24)
                    tree2.column("#27", anchor=CENTER, width=24)
                    tree2.column("#28", anchor=CENTER, width=24)
                    tree2.column("#29", anchor=CENTER, width=24)
                    tree2.column("#30", anchor=CENTER, width=24)
                    tree2.column("#31", anchor=CENTER, width=24)

                    tree2.heading("#0")
                    tree2.heading("#1", text="ROLL NO", anchor=CENTER)
                    tree2.heading("#2", text="STUDENT NAME", anchor=CENTER)
                    tree2.heading("#3", text="1", anchor=CENTER)
                    tree2.heading("#4", text="2", anchor=CENTER)
                    tree2.heading("#5", text="3", anchor=CENTER)
                    tree2.heading("#6", text="4", anchor=CENTER)
                    tree2.heading("#7", text="5", anchor=CENTER)
                    tree2.heading("#8", text="6", anchor=CENTER)
                    tree2.heading("#9", text="7", anchor=CENTER)
                    tree2.heading("#10", text="8", anchor=CENTER)
                    tree2.heading("#11", text="9", anchor=CENTER)
                    tree2.heading("#12", text="10", anchor=CENTER)
                    tree2.heading("#13", text="11", anchor=CENTER)
                    tree2.heading("#14", text="12", anchor=CENTER)
                    tree2.heading("#15", text="13", anchor=CENTER)
                    tree2.heading("#16", text="14", anchor=CENTER)
                    tree2.heading("#17", text="15", anchor=CENTER)
                    tree2.heading("#18", text="16", anchor=CENTER)
                    tree2.heading("#19", text="17", anchor=CENTER)
                    tree2.heading("#20", text="18", anchor=CENTER)
                    tree2.heading("#21", text="19", anchor=CENTER)
                    tree2.heading("#22", text="20", anchor=CENTER)
                    tree2.heading("#23", text="21", anchor=CENTER)
                    tree2.heading("#24", text="22", anchor=CENTER)
                    tree2.heading("#25", text="23", anchor=CENTER)
                    tree2.heading("#26", text="24", anchor=CENTER)
                    tree2.heading("#27", text="25", anchor=CENTER)
                    tree2.heading("#28", text="26", anchor=CENTER)
                    tree2.heading("#29", text="27", anchor=CENTER)
                    tree2.heading("#30", text="28", anchor=CENTER)
                    tree2.heading('#31',text="29",anchor=CENTER)
                    tree2.pack()
                    tree2.bind('<Double-1>', clicker)

            elif month[4:20] == "January" or month[4:20] == "March" or  month[4:20] == "May" or  month[4:20] == "July" or  \
            month[4:20] == "August" or  month[4:20] == "October" or  month[4:20] == "December":
                tree2['columns'] = (
                    "ROLL NO", "STUDENT NAME", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                    "15",
                    "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
                tree2.column("#0", width=0, stretch=NO)
                tree2.column("#1", anchor=CENTER, width=120)
                tree2.column("#2", anchor=CENTER, width=120)
                tree2.column("#3", anchor=CENTER, width=24)
                tree2.column("#4", anchor=CENTER, width=24)
                tree2.column("#5", anchor=CENTER, width=24)
                tree2.column("#6", anchor=CENTER, width=24)
                tree2.column("#7", anchor=CENTER, width=24)
                tree2.column("#8", anchor=CENTER, width=24)
                tree2.column("#9", anchor=CENTER, width=24)
                tree2.column("#10", anchor=CENTER, width=24)
                tree2.column("#11", anchor=CENTER, width=24)
                tree2.column("#12", anchor=CENTER, width=24)
                tree2.column("#13", anchor=CENTER, width=24)
                tree2.column("#14", anchor=CENTER, width=24)
                tree2.column("#15", anchor=CENTER, width=24)
                tree2.column("#16", anchor=CENTER, width=24)
                tree2.column("#17", anchor=CENTER, width=24)
                tree2.column("#18", anchor=CENTER, width=24)
                tree2.column("#19", anchor=CENTER, width=24)
                tree2.column("#20", anchor=CENTER, width=24)
                tree2.column("#21", anchor=CENTER, width=24)
                tree2.column("#22", anchor=CENTER, width=24)
                tree2.column("#23", anchor=CENTER, width=24)
                tree2.column("#24", anchor=CENTER, width=24)
                tree2.column("#25", anchor=CENTER, width=24)
                tree2.column("#26", anchor=CENTER, width=24)
                tree2.column("#27", anchor=CENTER, width=24)
                tree2.column("#28", anchor=CENTER, width=24)
                tree2.column("#29", anchor=CENTER, width=24)
                tree2.column("#30", anchor=CENTER, width=24)
                tree2.column("#31", anchor=CENTER, width=24)
                tree2.column("#32", anchor=CENTER, width=24)
                tree2.column("#33", anchor=CENTER, width=24)

                tree2.heading("#0")
                tree2.heading("#1", text="ROLL NO", anchor=CENTER)
                tree2.heading("#2", text="STUDENT NAME", anchor=CENTER)
                tree2.heading("#3", text="1", anchor=CENTER)
                tree2.heading("#4", text="2", anchor=CENTER)
                tree2.heading("#5", text="3", anchor=CENTER)
                tree2.heading("#6", text="4", anchor=CENTER)
                tree2.heading("#7", text="5", anchor=CENTER)
                tree2.heading("#8", text="6", anchor=CENTER)
                tree2.heading("#9", text="7", anchor=CENTER)
                tree2.heading("#10", text="8", anchor=CENTER)
                tree2.heading("#11", text="9", anchor=CENTER)
                tree2.heading("#12", text="10", anchor=CENTER)
                tree2.heading("#13", text="11", anchor=CENTER)
                tree2.heading("#14", text="12", anchor=CENTER)
                tree2.heading("#15", text="13", anchor=CENTER)
                tree2.heading("#16", text="14", anchor=CENTER)
                tree2.heading("#17", text="15", anchor=CENTER)
                tree2.heading("#18", text="16", anchor=CENTER)
                tree2.heading("#19", text="17", anchor=CENTER)
                tree2.heading("#20", text="18", anchor=CENTER)
                tree2.heading("#21", text="19", anchor=CENTER)
                tree2.heading("#22", text="20", anchor=CENTER)
                tree2.heading("#23", text="21", anchor=CENTER)
                tree2.heading("#24", text="22", anchor=CENTER)
                tree2.heading("#25", text="23", anchor=CENTER)
                tree2.heading("#26", text="24", anchor=CENTER)
                tree2.heading("#27", text="25", anchor=CENTER)
                tree2.heading("#28", text="26", anchor=CENTER)
                tree2.heading("#29", text="27", anchor=CENTER)
                tree2.heading("#30", text="28", anchor=CENTER)
                tree2.heading("#31", text="29", anchor=CENTER)
                tree2.heading("#32", text="30", anchor=CENTER)
                tree2.heading("#33", text="31", anchor=CENTER)
                tree2.pack()
                tree2.bind('<Double-1>', clicker)

            elif  month[4:20] == "April" or  month[4:20] == "June" or  month[4:20] == "September" or  month[4:20] == "November":
                tree2['columns'] = (
                    "ROLL NO", "STUDENT NAME", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                    "15",
                    "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30")
                tree2.column("#0", width=0, stretch=NO)
                tree2.column("#1", anchor=CENTER, width=120)
                tree2.column("#2", anchor=CENTER, width=120)
                tree2.column("#3", anchor=CENTER, width=24)
                tree2.column("#4", anchor=CENTER, width=24)
                tree2.column("#5", anchor=CENTER, width=24)
                tree2.column("#6", anchor=CENTER, width=24)
                tree2.column("#7", anchor=CENTER, width=24)
                tree2.column("#8", anchor=CENTER, width=24)
                tree2.column("#9", anchor=CENTER, width=24)
                tree2.column("#10", anchor=CENTER, width=24)
                tree2.column("#11", anchor=CENTER, width=24)
                tree2.column("#12", anchor=CENTER, width=24)
                tree2.column("#13", anchor=CENTER, width=24)
                tree2.column("#14", anchor=CENTER, width=24)
                tree2.column("#15", anchor=CENTER, width=24)
                tree2.column("#16", anchor=CENTER, width=24)
                tree2.column("#17", anchor=CENTER, width=24)
                tree2.column("#18", anchor=CENTER, width=24)
                tree2.column("#19", anchor=CENTER, width=24)
                tree2.column("#20", anchor=CENTER, width=24)
                tree2.column("#21", anchor=CENTER, width=24)
                tree2.column("#22", anchor=CENTER, width=24)
                tree2.column("#23", anchor=CENTER, width=24)
                tree2.column("#24", anchor=CENTER, width=24)
                tree2.column("#25", anchor=CENTER, width=24)
                tree2.column("#26", anchor=CENTER, width=24)
                tree2.column("#27", anchor=CENTER, width=24)
                tree2.column("#28", anchor=CENTER, width=24)
                tree2.column("#29", anchor=CENTER, width=24)
                tree2.column("#30", anchor=CENTER, width=24)
                tree2.column("#31", anchor=CENTER, width=24)
                tree2.column("#32", anchor=CENTER, width=24)

                tree2.heading("#0")
                tree2.heading("#1", text="ROLL NO", anchor=CENTER)
                tree2.heading("#2", text="STUDENT NAME", anchor=CENTER)
                tree2.heading("#3", text="1", anchor=CENTER)
                tree2.heading("#4", text="2", anchor=CENTER)
                tree2.heading("#5", text="3", anchor=CENTER)
                tree2.heading("#6", text="4", anchor=CENTER)
                tree2.heading("#7", text="5", anchor=CENTER)
                tree2.heading("#8", text="6", anchor=CENTER)
                tree2.heading("#9", text="7", anchor=CENTER)
                tree2.heading("#10", text="8", anchor=CENTER)
                tree2.heading("#11", text="9", anchor=CENTER)
                tree2.heading("#12", text="10", anchor=CENTER)
                tree2.heading("#13", text="11", anchor=CENTER)
                tree2.heading("#14", text="12", anchor=CENTER)
                tree2.heading("#15", text="13", anchor=CENTER)
                tree2.heading("#16", text="14", anchor=CENTER)
                tree2.heading("#17", text="15", anchor=CENTER)
                tree2.heading("#18", text="16", anchor=CENTER)
                tree2.heading("#19", text="17", anchor=CENTER)
                tree2.heading("#20", text="18", anchor=CENTER)
                tree2.heading("#21", text="19", anchor=CENTER)
                tree2.heading("#22", text="20", anchor=CENTER)
                tree2.heading("#23", text="21", anchor=CENTER)
                tree2.heading("#24", text="22", anchor=CENTER)
                tree2.heading("#25", text="23", anchor=CENTER)
                tree2.heading("#26", text="24", anchor=CENTER)
                tree2.heading("#27", text="25", anchor=CENTER)
                tree2.heading("#28", text="26", anchor=CENTER)
                tree2.heading("#29", text="27", anchor=CENTER)
                tree2.heading("#30", text="28", anchor=CENTER)
                tree2.heading("#31", text="29", anchor=CENTER)
                tree2.heading("#32", text="30", anchor=CENTER)
                tree2.pack()

                tree2.bind('<Double-1>', clicker)

        ##############################################excelfilecreateadddata#####################################
        def writetocsv():
            classx = int(class_box.current())
            classsel = allclasssection[classx]
            #######################################################attendance working days,present,percentage###############################################
            month=monthbox.get()
            yrsel=month[0:4]
            
            wdays=[]
            pdays=[]
            perc=[]

            wcount=0
            pcount=0

            leapcheck=False
            if((int(yrsel) % 400 == 0) or  (int(yrsel) % 100 != 0) and (int(yrsel) % 4 == 0)):
                leapcheck=True

            if month[4:20] == "Febraury":
                if leapcheck==False:
                    cur.execute("use {};".format(dbname2))
                    cur.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th,9th,10th,11th,12th,13th,14th,15th,16th,17th,18th,\
                    19th,20th,21st,22nd,23rd,24th,25th,26th,27th,28th from {};".format(classsel))
                    vals=cur.fetchall()
                    for i in vals:
                        for j in i:
                            if j!="-":
                                wcount+=1
                        wdays.append(wcount)
                        wcount=0

                    for i in vals:
                        for j in i:
                            if j=="P":
                                pcount+=1
                        pdays.append(pcount)
                        pcount=0

                    percalc = []

                    for i in range(0, len(wdays)):
                        percalc.append([pdays[i], wdays[i]])
                    
                    for i in percalc:
                        percentage=int(i[0])/int(i[1])*100
                        per=round(percentage, 2)
                        perc.append(per)

                    cur.execute("select rollno from {};".format(classsel))
                    rollstemp=cur.fetchall()
                    roll=[]
                    for i in rollstemp:
                        roll.append(i[0])

                    rollworking = []
                    
                    for i in range(0, len(roll)):
                        rollworking.append([roll[i], wdays[i]])

                    rollpresent= []
                    
                    for i in range(0, len(roll)):
                        rollpresent.append([roll[i], pdays[i]])

                    rollperc= []
                    
                    for i in range(0, len(roll)):
                        rollperc.append([roll[i], perc[i]])

                    for i in rollworking:
                        cur.execute("update {} set workingdays={} where rollno='{}';".format(classsel,i[1],i[0]))
                    wdays=[]
                    rollworking=[]
                    for i in rollpresent:
                        cur.execute("update {} set attended={} where rollno='{}';".format(classsel,i[1],i[0]))
                    pdays=[]
                    rollpresent=[]
                    for i in rollperc:
                        cur.execute("update {} set attendancepercentage={} where rollno='{}';".format(classsel,i[1],i[0]))

                    db.commit()    
                    perc=[]
                    rollperc=[]

                elif leapcheck==True:
                    cur.execute("use {};".format(dbname2))
                    cur.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th,9th,10th,11th,12th,13th,14th,15th,16th,17th,18th,19th,20th,\
                    21st,22nd,23rd,24th,25th,26th,27th,28th,29th from {};".format(classsel))
                    vals=cur.fetchall()
                    for i in vals:
                        for j in i:
                            if j!="-":
                                wcount+=1
                        wdays.append(wcount)
                        wcount=0

                    for i in vals:
                        for j in i:
                            if j=="P":
                                pcount+=1
                        pdays.append(pcount)
                        pcount=0

                    percalc = []
                    for i in range(0, len(wdays)):
                        percalc.append([pdays[i], wdays[i]])
                    
                    for i in percalc:
                        percentage=int(i[0])/int(i[1])*100
                        per=round(percentage, 2)
                        perc.append(per)

                    cur.execute("select rollno from {};".format(classsel))
                    rollstemp=cur.fetchall()
                    roll=[]
                    for i in rollstemp:
                        roll.append(i[0])

                    rollworking = []
                    
                    for i in range(0, len(roll)):
                        rollworking.append([roll[i], wdays[i]])

                    rollpresent= []
                    
                    for i in range(0, len(roll)):
                        rollpresent.append([roll[i], pdays[i]])

                    rollperc= []
                    
                    for i in range(0, len(roll)):
                        rollperc.append([roll[i], perc[i]])

                    for i in rollworking:
                        cur.execute("update {} set workingdays={} where rollno='{}';".format(classsel,i[1],i[0]))
                    wdays=[]
                    rollworking=[]
                    for i in rollpresent:
                        cur.execute("update {} set attended={} where rollno='{}';".format(classsel,i[1],i[0]))
                    pdays=[]
                    rollpresent=[]
                    for i in rollperc:
                        cur.execute("update {} set attendancepercentage={} where rollno='{}';".format(classsel,i[1],i[0]))

                    db.commit()    
                    perc=[]
                    rollperc=[]

            elif month[4:20] == "January" or month[4:20] == "March" or  month[4:20] == "May" or  month[4:20] == "July" or  month[4:20] == "August" \
                or  month[4:20] == "October" or  month[4:20] == "December":
                cur.execute("use {};".format(dbname2))
                cur.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th,9th,10th,11th,12th,13th,14th,15th,16th,17th,18th,19th,20th,21st,22nd,23rd,24th,25th,\
                26th,27th,28th,29th,30th,31st from {};".format(classsel))
                vals=cur.fetchall()
                for i in vals:
                    for j in i:
                        if j!="-":
                            wcount+=1
                    wdays.append(wcount)
                    wcount=0

                for i in vals:
                    for j in i:
                        if j=="P":
                            pcount+=1
                    pdays.append(pcount)
                    pcount=0

                percalc = []
                for i in range(0, len(wdays)):
                    percalc.append([pdays[i], wdays[i]])
                
                for i in percalc:
                    percentage=int(i[0])/int(i[1])*100
                    per=round(percentage, 2)
                    perc.append(per)

                cur.execute("select rollno from {};".format(classsel))
                rollstemp=cur.fetchall()
                roll=[]
                for i in rollstemp:
                    roll.append(i[0])

                rollworking = []
                
                for i in range(0, len(roll)):
                    rollworking.append([roll[i], wdays[i]])

                rollpresent= []
                
                for i in range(0, len(roll)):
                    rollpresent.append([roll[i], pdays[i]])

                rollperc= []
                
                for i in range(0, len(roll)):
                    rollperc.append([roll[i], perc[i]])

                for i in rollworking:
                    cur.execute("update {} set workingdays={} where rollno='{}';".format(classsel,i[1],i[0]))
                wdays=[]
                rollworking=[]
                for i in rollpresent:
                    cur.execute("update {} set attended={} where rollno='{}';".format(classsel,i[1],i[0]))
                pdays=[]
                rollpresent=[]
                for i in rollperc:
                    cur.execute("update {} set attendancepercentage={} where rollno='{}';".format(classsel,i[1],i[0]))

                db.commit()    
                perc=[]
                rollperc=[]

            elif  month[4:20] == "April" or  month[4:20] == "June" or  month[4:20] == "September" or  month[4:20] == "November":
                cur.execute("use {};".format(dbname2))
                cur.execute("select 1st,2nd,3rd,4th,5th,6th,7th,8th,9th,10th,11th,12th,13th,14th,15th,16th,17th,18th,19th,20th,21st,22nd,\
                23rd,24th,25th,26th,27th,28th,29th,30th from {};".format(classsel))
                vals=cur.fetchall()
                for i in vals:
                    for j in i:
                        if j!="-":
                            wcount+=1
                    wdays.append(wcount)
                    wcount=0

                for i in vals:
                    for j in i:
                        if j=="P":
                            pcount+=1
                    pdays.append(pcount)
                    pcount=0

                percalc = []
                for i in range(0, len(wdays)):
                    percalc.append([pdays[i], wdays[i]])
                
                for i in percalc:
                    percentage=int(i[0])/int(i[1])*100
                    per=round(percentage, 2)
                    perc.append(per)

                cur.execute("select rollno from {};".format(classsel))
                rollstemp=cur.fetchall()
                roll=[]
                for i in rollstemp:
                    roll.append(i[0])

                rollworking = []
                
                for i in range(0, len(roll)):
                    rollworking.append([roll[i], wdays[i]])

                rollpresent= []
                
                for i in range(0, len(roll)):
                    rollpresent.append([roll[i], pdays[i]])

                rollperc= []
                
                for i in range(0, len(roll)):
                    rollperc.append([roll[i], perc[i]])

                for i in rollworking:
                    cur.execute("update {} set workingdays={} where rollno='{}';".format(classsel,i[1],i[0]))
                wdays=[]
                rollworking=[]
                for i in rollpresent:
                    cur.execute("update {} set attended={} where rollno='{}';".format(classsel,i[1],i[0]))
                pdays=[]
                rollpresent=[]
                for i in rollperc:
                    cur.execute("update {} set attendancepercentage={} where rollno='{}';".format(classsel,i[1],i[0]))

                db.commit()    
                perc=[]
                rollperc=[]

            cur.execute(" USE {} ;".format(dbname2))
            cur.execute("select * from {};".format(classsel))
            data=cur.fetchall()

            y = "\n"
            for i in y:
                classn = classsel.replace(y, "")
            file=dbname2+classn
            y=filedialog.asksaveasfilename(initialdir = 'HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'\
            ,initialfile = file
            ,defaultextension=".csv",title="Save as",filetypes=[("All Files","*.*"),("Excel file","*.csv")])
            
            if month[4:20] == "Febraury":
                if leapcheck==False:
                    try:
                        with open(y,"w",newline='') as x:
                            y=csv.writer(x,dialect='excel')
                            y.writerow(["Roll no", "Student name", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th",\
                            "12th", "13th", "14th", "15th","16th", "17th", "18th", "19th", "20th","21st", "22nd", "23rd", "24th", "25th", "26th",\
                            "27th", "28th", "workingdays", "attended", "attpercentage"])
                            for i in data:
                                y.writerow(i)
                    
                    except FileNotFoundError:
                        pass
                elif leapcheck==True:
                    try:
                        with open(y,"w",newline='') as x:
                            y=csv.writer(x,dialect='excel')
                            y.writerow(["Roll no", "Student name", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th",\
                            "13th", "14th", "15th","16th", "17th", "18th", "19th", "20th","21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th",\
                            "29th", "workingdays", "attended", "attpercentage"])
                            for i in data:
                                y.writerow(i)
                    
                    except FileNotFoundError:
                        pass
            
            elif month[4:20] == "January" or month[4:20] == "March" or  month[4:20] == "May" or  month[4:20] == "July" or  month[4:20] == "August" or  \
                month[4:20] == "October" or  month[4:20] == "December":
                try:
                    with open(y,"w",newline='') as x:
                        y=csv.writer(x,dialect='excel')
                        y.writerow(["Roll no", "Student name", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th",\
                         "14th", "15th","16th", "17th", "18th", "19th", "20th","21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th",\
                        "31st", "workingdays", "attended", "attpercentage"])
                        for i in data:
                            y.writerow(i)
                
                except FileNotFoundError:
                    pass
            
            elif  month[4:20] == "April" or  month[4:20] == "June" or  month[4:20] == "September" or  month[4:20] == "November":
                try:
                    with open(y,"w",newline='') as x:
                        y=csv.writer(x,dialect='excel')
                        y.writerow(["Roll no", "Student name", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th",\
                         "14th", "15th","16th", "17th", "18th", "19th", "20th","21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", \
                        "workingdays", "attended", "attpercentage"])
                        for i in data:
                            y.writerow(i)
                
                except FileNotFoundError:
                    pass
        
        #############################################addholidayinattendance#############################
        def holiday():
            def clear_all():
                for item in tree2.get_children():
                    tree2.delete(item)
            classx = int(class_box.current())
            classsel = allclasssection[classx]
            tempdate = int(datebox.current())
            date = dates[tempdate]
            cur.execute(" USE {} ;".format(dbname2))
            cur.execute("update {} set {}='-';".format(classsel,date))
            db.commit()
            clear_all()
            refreshfn()
        ######################################sendemailtoparent#########################################
        def alertparents():
            ################################internetcheck#########################################
            def internet_stat(url="https://www.google.com/", timeout=3):
                try:
                    r = requests.head(url=url, timeout=timeout)
                    return True
                except requests.exceptions.ConnectionError as e:
                    return False
            
            net_stat = internet_stat()

            while net_stat==False:
                x=messagebox.askretrycancel("no internet connection.","no internet connection please try later.")
                if x==1:
                    net_stat=internet_stat()
                    if net_stat==True:
                        break
                elif x==0:
                    break

            if net_stat==True:
                classx = int(class_box.current())
                classsel = allclasssection[classx]
                ins = institutionsel.get()
                br = branchsel.get()
                date=alertdatebox.get()

                month=monthbox.get()
                y = "attendance"+month
                for i in y:
                    dbname = dbname2.replace(y, "")

                attendance="AB"

                cur.execute("use {};".format(dbname2))
                cur.execute("select studentname from {} where {}='{}';".format(classsel,date,attendance))
                studlist=[]
                tempstudlist=cur.fetchall()
                for i in tempstudlist:
                    for j in i:
                        studlist.append(j)

                parent_emails=[]    

                for i in studlist:
                    cur.execute("use {};".format(dbname))
                    cur.execute("select parentemail from {} where studentname='{}';".format(classsel,i))
                    tempparentemails=cur.fetchall()
                    for i in tempparentemails:
                        for j in i:
                            parent_emails.append(j)

                students=[]
                for i in range(0, len(studlist)):
                    students.append([studlist[i], parent_emails[i]])

                senderemail="attendancereg9@gmail.com"
                senderpassword="mhsizjmniognyggf"            
                for i in students:
                    name=i[0]
                    address=i[1]
                    with open("alert.txt",'w') as x:
                        l1 = "Dear Parent,\n\n"
                        l2 = "This is to inform you that your ward {} is absent on {} {}.\n\n".format(name,date,month)
                        l3 = "regards,\n\n"
                        l4 = "{} {}\n".format(ins,br)
                        l5 = "Admin"
                        x.writelines([l1, l2, l3, l4 ,l5])
                    
                    inst=str(ins).strip()
                    bran=str(br).strip()
                    classselected=str(classsel).strip()

                    msg=EmailMessage()
                    msg["Subject"] = "Notice from {}{} {}".format(inst,bran,classselected)
                    msg["From"] = senderemail
                    msg["To"] = address
                    with open("alert.txt") as x:
                        data=x.read()
                        msg.set_content(data)
                    context = ssl.create_default_context()
                    server=smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)
                    server.login(senderemail,senderpassword)
                    server.send_message(msg,senderemail,address)
                    server.quit()
                    time.sleep(3)
        
        global count
        count = 0
        
        class_box = ttk.Combobox(root_2, values=allclasssection, width=15)
        class_box.place(x=515, y=518)
        
        datebox = ttk.Combobox(root_2, values=dates, width=15)
        datebox.place(x=845, y=518)

        alertdatebox = ttk.Combobox(root_2, values=dates, width=15)
        alertdatebox.place(x=170, y=518)

        refresh = ttk.Button(root_2, text="REFRESH", width=15, padding=5, command=lambda: [difftree(), refreshfn() ,attlistfn()])
        refresh.place(x=460, y=568)

        exit2_button = ttk.Button(root_2, text="EXIT" ,width=15, padding=5,
                                  command=lambda: [root_2.destroy(),root.deiconify()])
        exit2_button.place(x=1130, y=640)

        csvbutton=ttk.Button(root_2, text="SAVE TO EXCEL" ,width=15, padding=5,
                                  command=lambda: [writetocsv()])
        csvbutton.place(x=460, y=645)

        alert=ttk.Button(root_2, text="ALERT PARENTS" ,width=15, padding=5,
                                  command=lambda: [alertparents()])
        alert.place(x=120, y=568)

        holidaybutton=ttk.Button(root_2, text="HOLIDAY" ,width=15, padding=5,
                                  command=lambda: [holiday()])
        holidaybutton.place(x=780, y=568)

        root_2.mainloop()

    main.mainloop()
    db.close()
            
mainsplash.after(3000, mainwindow)
mainsplash.mainloop()