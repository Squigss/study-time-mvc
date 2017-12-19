import tkinter
from tkinter import ttk



class StudyHelperView(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.grid()
        self.init_login(starting_row=0)
        self.init_detailed_summary_table(starting_row=6)
        self.init_subject_entry(starting_row=9)

    def init_login(self, starting_row):
        l1 = tkinter.Label(self, text='WELCOME TO YOUR STUDY HELPER!', font='avenir 24 bold', fg="#00C590")
        l1.grid(column=0, row=starting_row, columnspan=4, padx=20, pady=(20, 10))

        l1_two = tkinter.Label(self, text='The study helper will keep track of the number of pages and how much time it will take you to study each subject. It will then calculate how much time will be required to study all of your subjects!', font='avenir 12')
        l1_two.grid(column=0, row=starting_row +1, columnspan=4, padx=20, pady=(0, 20))
        l1_two.config(wraplength=350)


        l2 = tkinter.Label(self, text='Please enter your name', font='avenir 16 bold')
        l2.grid(column=0, row=starting_row + 2, columnspan=4)

        self.user_name_variable = tkinter.StringVar()
        self.e1 = tkinter.Entry(self, textvariable=self.user_name_variable, font='avenir 14')
        self.e1.grid(column=0, row=starting_row + 3, columnspan=4, padx=(0, 70))

        self.login_button = tkinter.Button(self, text=u"Login", font='avenir 12')
        self.login_button.grid(column=1, row=starting_row + 3, columnspan=4, sticky="W", padx=(20, 0))

        self.user_comment_variable = tkinter.StringVar()
        self.l3 = tkinter.Label(self, textvariable=self.user_comment_variable, font='avenir 14')
        self.l3.grid(column=0, row=starting_row + 5, columnspan=4, pady=(10, 10))

        self.time_to_study_comment_variable = tkinter.StringVar()
        self.l4 = tkinter.Label(self, textvariable=self.time_to_study_comment_variable, font='avenir 16', fg="#00C590")
        self.l4.grid(column=0, row=starting_row + 6, columnspan=4, pady=(0, 20))

        ttk.Separator(self, orient=tkinter.HORIZONTAL).grid(row=starting_row + 7, columnspan=4, sticky="ew")


    def init_detailed_summary_table(self, starting_row):
        l5 = tkinter.Label(self, text='Summary of your study programme:', font='avenir 16 bold')
        l5.grid(column=0, row=starting_row + 1, columnspan=4)

        self.listbox = tkinter.Listbox(self, font='avenir 14')
        self.listbox.grid(column=0, row=starting_row + 2, columnspan=4, sticky="ew", padx=40, pady=(10, 30))



    def init_subject_entry(self, starting_row):
        l6 = tkinter.Label(self, text='Subject information', font='avenir 16 bold')
        l6.grid(column=0, row=starting_row, columnspan=4)

        l6_two = tkinter.Label(self, text='Add information about each subject you will need to study here. You can update information at any time by entering the name of the subject.', font='avenir 12')
        l6_two.grid(column=0, row=starting_row + 1, columnspan=4, pady=(0, 20))
        l6_two.config(wrap=350)

        l7 = tkinter.Label(self, text='Subject name', font='avenir 14')
        l7.grid(column=0, row=starting_row + 3, columnspan=1, sticky="E")

        self.subject_name_variable = tkinter.StringVar()
        self.e2 = tkinter.Entry(self, textvariable=self.subject_name_variable, font='avenir 14')
        self.e2.grid(column=1, row=starting_row + 3, columnspan=1)

        l8 = tkinter.Label(self, text='Number of pages to read:', font='avenir 14')
        l8.grid(column=0, row=starting_row + 4, columnspan=1, sticky="E")

        self.pages_to_read_variable = tkinter.IntVar()
        self.e3 = tkinter.Entry(self, textvariable=self.pages_to_read_variable, font='avenir 14')
        self.e3.grid(column=1, row=starting_row + 4, columnspan=1)

        l9 = tkinter.Label(self, text='Time needed to study a page (in minutes):', font='avenir 14')
        l9.grid(column=0, row=starting_row + 5, columnspan=1, sticky="E")

        self.time_per_page_variable = tkinter.IntVar()
        self.e4 = tkinter.Entry(self, textvariable=self.time_per_page_variable, font='avenir 14')
        self.e4.grid(column=1, row=starting_row + 5, columnspan=1)

        self.save_button = tkinter.Button(self, text=u"Save subject", font='avenir 12')
        self.save_button.grid(column=0, row=starting_row + 6, columnspan=4, pady=(10, 40))




        #ttk.Separator(self, orient=tkinter.HORIZONTAL).grid(row=starting_row + 2, columnspan=4, sticky="ew", pady=5)
