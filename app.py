from tkinter import *
from mydb import Database
from tkinter import messagebox                           #jaruri hai likhna
from myapi import API


class NLPApp:

    def __init__(self):

        self.dbo=Database()                               #obj of Database class & self lagaya for using in diff func
        self.apio=API()

        self.root=Tk()                                    #main class of tkinter
        self.root.title("NLPApp")                         #root is not a keyword, can use anything
        self.root.iconbitmap("resources/favicon.ico")     #to set icon,ico format required strictly
        self.root.geometry("350x600")                     #width=350 ; height= 600
        self.root.configure(bg="#605E5D")                 #set bg color using colour code

        self.login_gui()

        self.root.mainloop()                              #gui hold karke rakhta hai screen

    def login_gui(self):
        self.clear()

        #self.root k thr UI mai place karenge
        heading=Label(self.root,text="NLPApp",bg="#605E5D",fg="white")             #in tkinter for displaying text, we have label class
        heading.pack(pady=(30,30))                                     #geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading.configure(font=("verdana",24,"bold"))

        label1=Label(self.root,text="Enter Email")         #Label class se text display hota
        label1.pack(pady=(10,10))

        self.email_input=Entry(self.root,width=50)         #height nhi koi parameter & Entry to take i/p
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root, text="Enter Password")  # Label class se text display hota
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50,show="*")  # height nhi koi parameter
        self.password_input.pack(pady=(5, 10), ipady=4)

        login_btn=Button(self.root,text="Login",width=30,height=2,command=self.perform_login)          #why not self?, since not an instance var
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text="Not a Member?")  # Label class se text display hota
        label3.pack(pady=(40, 10))

        redirect_btn = Button(self.root, text="Register Now", width=30, height=2,command=self.register_gui)  # why not self?, since not an instance var
        redirect_btn.pack(pady=(5, 10))                  #upar se 20 , neeche se 10


    def register_gui(self):
        self.clear()

        # self.root k thr UI mai place karenge
        heading = Label(self.root, text="NLPApp", bg="#605E5D",fg="white")  # in tkinter for displaying text, we have label class
        heading.pack(pady=(30, 30))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading.configure(font=("verdana", 24, "bold"))

        label0 = Label(self.root, text="Enter Name")  # Label class se text display hota
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)  # height nhi koi parameter & Entry to take i/p
        self.name_input.pack(pady=(5, 10), ipady=4)

        label1 = Label(self.root, text="Enter Email")  # Label class se text display hota
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)  # height nhi koi parameter & Entry to take i/p
        self.email_input.pack(pady=(5, 10), ipady=4)

        label2 = Label(self.root, text="Enter Password")  # Label class se text display hota
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show="*")  # height nhi koi parameter
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text="Register", width=30, height=2,command=self.perform_registration)  # why not self?, since not an instance var
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text="Already a Member?")  # Label class se text display hota
        label3.pack(pady=(40, 10))

        redirect_btn = Button(self.root, text="Login Now", width=30, height=2,command=self.login_gui)  # why not self?, since not an instance var
        redirect_btn.pack(pady=(5, 10))

    def clear(self):
        #clear existing GUI
            for i in self.root.slaves():
                i.destroy()

    def perform_registration(self):
        name=self.name_input.get()                 #get() fetch kardeta hai GUI ka data
        email=self.email_input.get()
        password=self.password_input.get()

        response = self.dbo.add_data(name,email,password)
        self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success","Registration Successfull")
        else:
            messagebox.showerror("Error","Email already exists")

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo("success","Login Successfull")
            self.home_gui()
        else:
            messagebox.showerror("error","Incorrect Email/Password")


    def home_gui(self):

        self.clear()

        # self.root k thr UI mai place karenge
        heading = Label(self.root, text="NLPApp", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading.pack(pady=(30, 30))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading.configure(font=("verdana", 24, "bold"))


        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=4,
                              command=self.sentiment_gui)  # why not self?, since not an instance var
        sentiment_btn.pack(pady=(10, 10))

        ner_btn = Button(self.root, text="Named Entity Recognition", width=30, height=4,
                              command=self.ner_gui)  # why not self?, since not an instance var
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root,text="Emotion Detection", width=30, height=4,
                              command=self.emotion_gui)  # why not self?, since not an instance var
        emotion_btn.pack(pady=(10, 10))

        logout_btn = Button(self.root, text="Wanna Logout?", width=20, height=2,
                              command=self.login_gui)  # why not self?, since not an instance var
        logout_btn.pack(pady=(50, 10))


    def sentiment_gui(self):

        self.clear()

        # self.root k thr UI mai place karenge
        heading1 = Label(self.root, text="NLPApp", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading1.pack(pady=(30, 30))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading1.configure(font=("verdana", 24, "bold"))

        # self.root k thr UI mai place karenge
        heading2= Label(self.root, text="Sentiment Analysis", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading2.pack(pady=(10, 20))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text to be analyzed")  # Label class se text display hota
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)  # height nhi koi parameter & Entry to take i/p
        self.sentiment_input.pack(pady=(5, 10), ipady=4)

        sentiment_btn = Button(self.root, text="Analyze Sentiment",command=self.do_sentiment_analysis)  # why not self?, since not an instance var
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text="",bg="#605E5D",fg="white")  # Label class se text display hota
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=("verdana", 16, "bold"))   #font size increased, result aache se dikhe

        goback_btn = Button(self.root, text="Back",command=self.home_gui)  # why not self?, since not an instance var
        goback_btn.pack(pady=(30, 10))


    def do_sentiment_analysis(self):

        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        txt=""
        for i in result["sentiment"]:
            txt+=i+"--->"+str(result["sentiment"][i])+"\n"

        self.sentiment_result["text"]=txt                         #wow aaisa lag araha dict hai



    def ner_gui(self):

        self.clear()

        # self.root k thr UI mai place karenge
        heading1 = Label(self.root, text="NLPApp", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading1.pack(pady=(30, 30))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading1.configure(font=("verdana", 24, "bold"))

        # self.root k thr UI mai place karenge
        heading2= Label(self.root, text="Named Entity Recognition", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading2.pack(pady=(10, 20))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text to be analyzed")  # Label class se text display hota
        label1.pack(pady=(10, 10))

        self.ner_input = Entry(self.root, width=50)  # height nhi koi parameter & Entry to take i/p
        self.ner_input.pack(pady=(5, 10), ipady=4)

        ner_btn = Button(self.root, text="Analyze NER",command=self.do_ner_analysis)  # why not self?, since not an instance var
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text="",bg="#605E5D",fg="white")  # Label class se text display hota
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=("verdana", 10, "bold"))   #font size increased, result aache se dikhe

        goback_btn = Button(self.root, text="Back",command=self.home_gui)  # why not self?, since not an instance var
        goback_btn.pack(pady=(30, 10))


    def do_ner_analysis(self):

        text=self.ner_input.get()
        result=self.apio.ner_analysis(text)

        self.ner_result["text"]=result["entities"]                        #wow aaisa lag araha dict hai



    def emotion_gui(self):

        self.clear()

        # self.root k thr UI mai place karenge
        heading1 = Label(self.root, text="NLPApp", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading1.pack(pady=(30, 30))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading1.configure(font=("verdana", 24, "bold"))

        # self.root k thr UI mai place karenge
        heading2= Label(self.root, text="Emotion Analysis", bg="#605E5D",
                        fg="white")  # in tkinter for displaying text, we have label class
        heading2.pack(pady=(10, 20))  # geometry manager(kind interior designer)-->pack/grid--> to place obj
        heading2.configure(font=("verdana", 20))

        label1 = Label(self.root, text="Enter the text to be analyzed")  # Label class se text display hota
        label1.pack(pady=(10, 10))

        self.emotion_input = Entry(self.root, width=50)  # height nhi koi parameter & Entry to take i/p
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        emotion_btn = Button(self.root, text="Analyze Emotion",command=self.do_emotion_analysis)  # why not self?, since not an instance var
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text="",bg="#605E5D",fg="white")  # Label class se text display hota
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=("verdana", 16, "bold"))              #font size increased, result aache se dikhe

        goback_btn = Button(self.root, text="Back",command=self.home_gui)        # why not self?, since not an instance var
        goback_btn.pack(pady=(30, 10))


    def do_emotion_analysis(self):

        text=self.emotion_input.get()
        result=self.apio.emotion_analysis(text)
        out=max(result["emotion"].values())

        #self.ner_result["text"]=result["emotion"][out]                                 #wow aaisa lag araha dict hai


nlp=NLPApp()
