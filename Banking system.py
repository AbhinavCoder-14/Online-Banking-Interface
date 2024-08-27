from tkinter import *
import time
import tkinter.messagebox as msg


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('590x400')
        self.resizable(0, 0)
        self.intro = 'Welcome to The Axis Bank'
        self.Creadit_Intro = 'Welcome To The Creadit Option'
        self.count = 0
        self.text = ''
        self.dictname = {}
        self.dictname1 = {}
        self.dictname3 = {}
        self.TootalAmmount = {}
        self.pin1 = {}
        self.updateAccount_Ammount = {}
        self.introL = Label(
            self, text='Welcome To The Axis Bank', font='arial 26 bold')

        self.text1 = ''
        self.time = 50
        self.Account_Ammount = {}
        self.count1 = 0
        self.In = Label(self, text='', font='arial 26 bold')
        self.In.place(x=70, y=20)

        self.In1 = Label(self, text='', font='arial 26 italic bold')

        self.MenuB2 = Button(self, font='courier 12')

    def introduction(self):
        if self.count >= len(self.intro):
            self.count = -1
            self.text = ''
            self.In.configure(text=self.text)

        else:
            self.text += self.intro[self.count]
            self.In.configure(text=self.text)

        self.count += 1

        self.In.after(self.time, main.introduction)

    def Dpin(self):
        with open('newAccountpin.txt', 'rt') as f:
            pinReader = f.readlines()
            for data in pinReader:
                splitdata = data.split(':')
                self.pin1[splitdata[0]] = splitdata[1]


# ----------------------------------------------------------------------------------------------

    def Submit_Creadit(self):

        name = (self.varl.get())
        number = (self.number.get())
        pin = (self.pin.get())
        ammount = (self.Ammount.get())

        try:
            (number) = int(number)
            try:
                (pin) = int(pin)
                try:
                    (ammount) = int(ammount)
                    number = str(number)
                    pin1 = str(pin)
                    if len(number) == 10:
                        if len(pin1) == 4:
                            print('ok...')
                            with open('accountname.txt', 'rt') as f:
                                read1 = f.readlines()
                                for datas in read1:
                                    splitdata = datas.split(':')
                                    self.dictname3[splitdata[0]] = splitdata[1]

                            if name in self.dictname3.keys():
                                if pin1 in self.pin1[name]:
                                    data = self.dictname3.get(name)
                                    print(data)
                                    Split_Data = data[:12].lstrip("['")
                                    print(Split_Data)
                                    if str(number) in Split_Data:
                                        with open('AccountAmount.txt', 'rt') as f:
                                            R_Data = f.readlines()
                                            for data in R_Data:
                                                Split_Data = data.split(':-')
                                                self.Account_Ammount[Split_Data[0]
                                                                     ] = Split_Data[1]

                                            Amount = int(
                                                self.Account_Ammount[name])
                                            if ammount < Amount:

                                                if Amount > 0:
                                                    self.Account_Ammount[name] = Amount - int(
                                                        ammount)
                                                    print(self.Account_Ammount)
                                                    self.updateAccount_Ammount.update(
                                                        self.Account_Ammount)
                                                    Ammount = []
                                                    for name, balance in self.updateAccount_Ammount.items():
                                                        print(
                                                            f'{name}:{balance}')
                                                        Ammount.append(
                                                            f'{name}:-{balance}')
                                                    with open('AccountAmount.txt', 'r+') as f:
                                                        f.truncate(0)

                                                    for data in Ammount:
                                                        data_Split = data.strip()
                                                        with open('AccountAmount.txt', 'a') as f:
                                                            f.write(
                                                                f'{data_Split}\n')
                                                            print(
                                                                'All function performing well')
                                                    msg.showinfo(
                                                        'Info..', 'Your details are correct so your amount is creadit from your account.\nPlease Take your Cash\nThank you for visiting in ower bank...')
                                                    msg.showinfo(
                                                        'info', f'Your current Ammount :- {Amount-int(ammount)}')

                                                else:
                                                    msg.showerror(
                                                        'Error', f'Your bank ammount is {Amount-int(ammount)}')
                                            else:
                                                msg.showerror(
                                                    'Error', 'your bank balance is too low')
                                    else:
                                        print('fuck number')
                                        msg.showerror(
                                            'Error', 'Number is Not match to Your Name in Data\nPlease Enter the Correct Number')

                                else:
                                    msg.showerror(
                                        'info', 'Enter the Correct pin')
                                    print('name pin')

                            else:
                                print('name fuck')
                                msg.showerror(
                                    'info', 'Your name is not found in Ower data')

                        else:
                            print('fuck')
                            msg.showerror('info', 'Enter 4 Digit Pin')

                    else:
                        print('something went wrong...11')
                        msg.showerror('info', 'Enter 10 digit Number')

                except ValueError as e:
                    print('please Enter the ammount in integer form')
                    msg.showerror('Error', 'Enter Amount in Integer Form')

            except ValueError as e:
                print('please enter the pin in integer form')
                msg.showerror('Error', 'Enter Your Pin in Tnteger Form')

        except ValueError as e:
            print('please enter the number in integer form')
            msg.showerror('Error', 'Enter Number in Integer form')

    def Creadit_F9(self):
        pass

    def Creadit_F1(self):
        global NameL1, NumberL2, PinL3, AmountL4, InfoL5
        global EntryE1, EntryE2, EntryE3, EntryE4, SubmitB1

        self.varl = StringVar()
        self.number = StringVar()
        self.number.set('')
        self.pin = StringVar()
        self.pin.set('')
        self.Dpin1 = {}
        self.Ammount = StringVar()
        self.Ammount.set('')

        self.In.place(x=324234, y=3424234)
        self.In1.place(x=20, y=30)
        self.introL.place(x=32442, y=23424)
        L1.place(x=324324, y=243243)
        L2.place(x=324324, y=243243)
        L3.place(x=324324, y=243243)
        L4.place(x=324324, y=243243)
        L5.place(x=324324, y=243243)
        InFo.place(x=34243432, y=3423423)
        B1.place(x=3213, y=3424324)
        B2.place(x=3213, y=3424324)
        B3.place(x=3213, y=3424324)
        B4.place(x=3213, y=3424324)
        B5.place(x=3213, y=3424324)

        self.In1.configure(text=self.Creadit_Intro, font='Arial 25 bold')
        self.In1.place(x=30, y=20)

        NameL1 = Label(self, text='Full Name :-', font='Courier 15')
        NameL1.place(x=20, y=100)

        NumberL2 = Label(self, text='Mobile Number :- ', font='Courier 15')
        NumberL2.place(x=20, y=150)

        PinL3 = Label(self, text='Account Pin :- ', font='Courier 15')
        PinL3.place(x=20, y=200)

        AmountL4 = Label(self, text='Amount :- ', font='Courier 15')
        AmountL4.place(x=20, y=250)

        InfoL5 = Label(self, text='Info :- ', font='courier 13')
        InfoL5.place(x=20, y=300)

        SubmitB1 = Button(self, text='Submit', font='Courier 14',
                          width=20, bg='yellow', command=self.Submit_Creadit)
        SubmitB1.place(x=200, y=350)

        self.MenuB2.configure(text='<<<Main Menu>>>', command=self.Main_Menu)
        self.MenuB2.place(x=10, y=350)

        EntryE1 = Entry(self, width=25, font='Courier 12',
                        textvariable=self.varl)
        EntryE1.place(x=260, y=102)

        EntryE2 = Entry(self, width=27, font='courirer 12',
                        textvariable=self.number)
        EntryE2.place(x=260, y=152)

        EntryE3 = Entry(self, width=6, font='courirer 12',
                        textvariable=self.pin)
        EntryE3.place(x=350, y=202)

        EntryE4 = Entry(self, width=15, font='courirer 12',
                        textvariable=self.Ammount)
        EntryE4.place(x=300, y=252)


# ----------------------------------------------------------------------------------------------

    def Main_Menu(self):
        self.introL.place(x=40, y=20)

        L1.place(x=20, y=120)
        L2.place(x=20, y=170)
        L3.place(x=20, y=220)
        L4.place(x=20, y=270)

        L5.place(x=20, y=320)
        InFo.place(x=15, y=80)
        B1.place(x=450, y=120)
        B2.place(x=450, y=170)
        B3.place(x=450, y=220)
        B4.place(x=450, y=270)
        B5.place(x=450, y=320)

        NameL1.place(x=234234, y=3242344)

        NumberL2.place(x=234234, y=3242344)
        PinL3.place(x=234234, y=3242344)
        AmountL4.place(x=234234, y=3242344)
        # InfoL5.place(x=234234, y=3242344)

        EntryE1.place(x=324234, y=3242434)
        EntryE2.place(x=324234, y=3242434)
        EntryE3.place(x=324234, y=3242434)
        EntryE4.place(x=324234, y=3242434)

        SubmitB1.place(x=23423, y=32434)
        self.MenuB2.place(x=243234, y=3422543)
        self.In1.place(x=34234, y=24332)


# dictname3 :- accountname() Function


    def accountname(self):
        with open('accountname.txt', 'rt') as f:
            read1 = f.readlines()
            for datas in read1:
                splitdata = datas.split(':')
                self.dictname3[splitdata[0]] = splitdata[1]

    def Add_F4(self):
        self.In.place(x=4535350, y=43534530)
        self.introL.place(x=32442, y=23424)
        self.name_A = StringVar()
        self.No_A = StringVar()
        self.Date_A = StringVar()
        self.Month_A = StringVar()
        self.Year_A = StringVar()
        self.Pin_A = StringVar()
        L1.place(x=324324, y=243243)
        L2.place(x=324324, y=243243)
        L3.place(x=324324, y=243243)
        L4.place(x=324324, y=243243)
        L5.place(x=324324, y=243243)
        InFo.place(x=34243432, y=3423423)
        B1.place(x=3213, y=3424324)
        B2.place(x=3213, y=3424324)
        B3.place(x=3213, y=3424324)
        B4.place(x=3213, y=3424324)
        B5.place(x=3213, y=3424324)

        Intro_A = Label(self, text='Welcome To The Axis Bank',
                        font='Arial 26 bold')
        Intro_A.place(x=40, y=15)
        Info_A = Label(
            self, text='Enter your Correct information :-', font='Courier 13')
        Info_A.place(x=30, y=70)
        Name_A = Label(self, text='Name :-', font='Courier 13')
        Name_A.place(x=25, y=110)
        Number_A = Label(self, text='Number :-', font='Courier 13')
        Number_A.place(x=25, y=150)
        BirthDate_A = Label(self, text='Birth Date :-', font='Courier 13')
        BirthDate_A.place(x=25, y=190)
        BirthMonth_A = Label(self, text='Birth Month :-', font='Courier 13')
        BirthMonth_A.place(x=340, y=190)
        BirthYear_A = Label(self, text='Birth Year :-', font='Courier 13')
        BirthYear_A.place(x=25, y=235)
        Pin_A = Label(self, text='Create Pin 4 digit :-', font='Courier 13')
        Pin_A.place(x=25, y=285)
        Info1_A = Label(self, text='Info :-', font='courier 14')
        Info1_A.place(x=25, y=325)
        Submit_A = Button(self, text='Submit', font='Courier 16',
                          activebackground='purple', command=self.submit_A_F, width=20, bg='yellow')
        Submit_A.place(x=150, y=360)
        Entry_N_A = Entry(
            self, width=30, textvariable=self.name_A, font='Courier 13')
        Entry_N_A.place(x=180, y=110)
        Entry_No_A = Entry(
            self, width=30, textvariable=self.No_A, font='Courier 13')
        Entry_No_A.place(x=180, y=150)
        Entry_D_A = Entry(
            self, width=4, textvariable=self.Date_A, font='Courier 13')
        Entry_D_A.place(x=220, y=191)
        Entry_M_A = Entry(self, width=4, font='courier 13',
                          textvariable=self.Month_A)
        Entry_M_A.place(x=500, y=191)
        Entry_Y_A = Entry(
            self, width=4, textvariable=self.Year_A, font='courier 13')
        Entry_Y_A.place(x=220, y=235)
        Entry_Pin_A = Entry(
            self, width=8, textvariable=self.Pin_A, font='Courier 13')
        Entry_Pin_A.place(x=270, y=285)

    def submit_A_F(self):
        print('add member')
        InfoL1 = Label(self, text='', font='Courier 13')
        # InfoL1.place(x=110,y=300)
        InfoL2 = Label(self, text='', font='Courier 13')
        InfoL2.place(x=125, y=300)
        InfoL3 = Label(self, text='', font='Courier 13')
        InfoL3.place(x=125, y=300)
        InfoL4 = Label(self, text='', font='Courier 13')
        InfoL4.place(x=125, y=300)
        InfoL5 = Label(self, text='', font='Courier 13')
        InfoL5.place(x=125, y=300)
        InfoL6 = Label(self, text='', font='Courier 13')
        InfoL6.place(x=125, y=300)

        name = self.name_A.get()
        year = self.Year_A.get()
        date = self.Date_A.get()
        number1 = self.No_A.get()
        pin = self.Pin_A.get()
        month = self.Month_A.get()

        try:
            (number2) = int(number1)
            try:
                (pin2) = int(pin)
                try:
                    (date2) = int(date)
                    try:
                        (year2) = int(year)
                        try:
                            (month2) = int(month)
                            if date2 <= 31:
                                if month2 <= 12:
                                    if year2 > 1900 and year2 <= 2020:
                                        strdate = str(date2)
                                        strmonth = str(month2)
                                        stryear = str(year2)
                                        CorrectbithDate = f"{strdate}-{strmonth}-{stryear}"
                                        if len(str(number1)) == 10:
                                            stringPin = str(pin)
                                            if len(stringPin) == 4:

                                                strNumber1 = str(number1)
                                                print(
                                                    'ok all function prfromance is very good')

                                                with open('accountname.txt', 'rt') as f:
                                                    read1 = f.readlines()
                                                    for datas in read1:
                                                        splitdata = datas.split(
                                                            ':')
                                                        self.dictname3[splitdata[0]
                                                                       ] = splitdata[1]

                                                with open('newAccountpin.txt', 'a') as f:
                                                    f.write(
                                                        f'{name}:{int(pin2)}\n')

                                                Main_list = []
                                                Main_list.append(strNumber1)
                                                Main_list.append(
                                                    CorrectbithDate)

                                                Check_Number_D = []

                                                for data in self.dictname3.values():
                                                    a = data.split(',')
                                                    MainData = a[0].lstrip(
                                                        "['")
                                                    MainData1 = MainData.rstrip(
                                                        "']")
                                                    MainData2 = int(MainData1)
                                                    Check_Number_D.append(
                                                        MainData2)
                                                print(Check_Number_D)
                                                if int(number1) not in Check_Number_D:
                                                    print(
                                                        'ok This number is unik')
                                                    with open('accountname.txt', 'rt') as f:
                                                        read1 = f.readlines()
                                                        for data in read1:
                                                            splitdata = data.split(
                                                                ':')
                                                            self.dictname[splitdata[0]
                                                                          ] = splitdata[1]

                                                    if name not in self.dictname.keys():
                                                        with open('accountname.txt', 'a') as f:
                                                            f.write(
                                                                f'{name}:{Main_list}\n')
                                                            msg.showinfo(
                                                                'Info', 'Your Account is opened in axis bank')
                                                            text = f'Name -> {name}\n'
                                                            msg.showinfo(
                                                                'Details', f'name -> {name}\nDate Of Birth -> {CorrectbithDate}\nMobile Number -> {strNumber1}\npin or password -> {stringPin}')

                                                else:

                                                    print(
                                                        'no, this number is Exist in Ower data base')
                                                    msg.showinfo(
                                                        'into', f'{number1} number is exist in ower dataBase')

                                            else:
                                                print(
                                                    "Please Enter the 4 digits integer pin or password")
                                                msg.showinfo(
                                                    'into', 'PLease Enter te 4 digit pin or password')

                                        else:
                                            print(
                                                "Please Enter the 10 digit number...")
                                            msg.showinfo(
                                                'into', 'please Enter the valid number')

                                    else:
                                        print("Please Enter the correct year...")
                                        msg.showinfo(
                                            'into', 'please Enter the valid year')

                                else:
                                    print('please enter the valid month')
                                    msg.showinfo(
                                        'into', 'please Enter the valid month')

                            else:
                                print('please Enter valid date')
                                msg.showinfo(
                                    'into', 'please Enter the valid date')

                        except ValueError:
                            print('int problem Month')

                    except ValueError:
                        print('int problem Year')

                except ValueError:
                    print('int problem date')

            except ValueError:
                print('int problem pin')

        except ValueError:
            print('int problem number')

# 1530

    def Debit_F2(self):
        pass

    def Check_F3(self):
        pass

    def Options_F5(self):
        pass

    def Details(self):
        global L1, L2, L3, L4, L5, InFo, B1, B2, B3, B4, B5
        L1 = Label(self, text='1. Credit Ammount from the bank -- ',
                   font='Courier 15')
        L1.place(x=20, y=120)
        L2 = Label(self, text='2. Debit Rupees in Axis bank -- ',
                   font='Courier 15')
        L2.place(x=20, y=170)
        L3 = Label(self, text='3. Check Ammount in Axis Bank  -- ',
                   font='Courier 15')
        L3.place(x=20, y=220)
        L4 = Label(self, text='4. Add Member in Axis Bank -- ',
                   font='Courier 15')
        L4.place(x=20, y=270)

        L5 = Label(self, text='5. Axis Bank Option -- ', font='Courier 15')
        L5.place(x=20, y=320)

        InFo = Label(self, text='There are the Options :---',
                     font='courier 15')
        InFo.place(x=15, y=80)

        B1 = Button(self, text='Click For -- 1', font='courier 10',
                    bg='yellow', activebackground='Purple', command=self.Creadit_F1)
        B1.place(x=450, y=120)
        B2 = Button(self, text='Click For -- 2', font='courier 10',
                    bg='yellow', activebackground='Purple', command=self.Debit_F2)
        B2.place(x=450, y=170)
        B3 = Button(self, text='Click For -- 3', font='courier 10',
                    bg='yellow', activebackground='Purple', command=self.Check_F3)
        B3.place(x=450, y=220)
        B4 = Button(self, text='Click For -- 4', font='courier 10',
                    bg='yellow', activebackground='Purple', command=self.Add_F4)
        B4.place(x=450, y=270)
        B5 = Button(self, text='Click For -- 5', font='courier 10',
                    bg='yellow', activebackground='Purple', command=self.Options_F5)
        B5.place(x=450, y=320)
        # self.In.place()

    def accountname1(self):
        with open('Error data.txt', 'a') as f:
            read1 = f.write(f'Error - 1\n')


if __name__ == "__main__":
    main = GUI()
    main.introduction()
    # main.update()
    # time.sleep(5)
    main.Details()
    main.accountname()
    main.accountname1()
    main.Dpin()
    # main.accountname()
    main.mainloop()


# calculation game in tkiknter...


# https://timetoprogram.com/tkinter-project-ideas

    # str = name = (name)
    # str = birthday = (correctbirthDate)
    # int = number1 = (strNumber1)
    # int = pin = (stringPin)


# b = '9582969641'
# a = {'abhinav':['9582969641', '21-2-2001'],'abhinav1':['8448167907', '21-2-2001']}
# value = a.get('abhinav')
# value1 = value[0]

# if b in value1:
#     print('yes')

# else:
#     print('no')
