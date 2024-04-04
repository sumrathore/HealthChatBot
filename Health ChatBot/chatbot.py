from tkinter import *
from tkinter import ttk
import sqlite3
import re
from PIL import Image,ImageTk

#import long_responses as long
import hellko as hell
con= sqlite3.connect('hospital.db')
cur= con.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS Recordbook
                        (Talker text,Reply text)''')
cur.execute(''' CREATE TABLE IF NOT EXISTS Feedback
                        (Feedback text)''')
class ChatBot:
    
    def __init__(self,root):
        self.root=root;
        self.root.title=("chatbot");
        self.root.geometry("730x620+0+0")
        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        self.root.bind('<Return>',self.enter_func)
        main_frame.pack()
       
        # logoPic=PhotoImage(file='pic.png')
        # logoPicLabel=Label(root,image=logoPic,bg='deep pink')
        # logoPicLabel.pack(pady=2)
        # img = PhotoImage(file='pic.png')
        # Label(root,image=img).pack()
        








        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,text='AIIMS NAGPUR',font=('aerial',30,'bold'),bg='white')
        Title_label.pack(side=TOP)
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=4,relief=RAISED,font=('aerial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()
        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()
        label_1=Label(btn_frame,text='TYPE SOMETHING',font=('aerial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)


        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)
        self.send=Button(btn_frame,text="send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        self.clear=Button(btn_frame,text="clear",command=self.clear_func,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)
        self.msg=''
        label2=Label(btn_frame,text=self.msg,font=('aerial',14,'bold'),fg='red',bg='white')
        label2.grid(row=1,column=1,padx=5,sticky=W)
        

        
        bot="hey i am JARVIS"
        self.text.insert(END,'\n\n bot: '+bot)
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')
    def clear_func(self):
        self.text.delete('1.0',END)
        self.entry.set('')
    


    def send(self):
        se=self.entry.get()
        send='\nyou: '+se
        self.text.insert(END,'\n\n'+send)
        self.text.yview(END)
        if(se=='bye'):
            bot="Do you want to give feedback about our chatbox?[y/n]"
            self.text.insert(END,'\n'+'Jarvis: '+bot)
            cur.execute("Insert INTO Recordbook VALUES ('user',?)",[se])
            cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
            con.commit()
        
        elif(se=='y'):
                bot="Please write the ratings from below:\n#Best\n#Good\n#Bad"
                self.text.insert(END,'\n'+bot)
                e=self.entry.get()
                cur.execute("Insert INTO Recordbook VALUES ('user',?)",[e])
                cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
                con.commit() 
        elif(se=='Best' or se=='best'):
                bot="Thankyou for your time.We appreciate your ratings!!!"
                self.text.insert(END,'\n'+bot)
                cur.execute("Insert INTO Feedback VALUES (?)",[se])
                cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
                con.commit()                  
        elif(se=='Good'or se=='good'):
                bot="Thankyou.We will work to make it best!!!"
                self.text.insert(END,'\n'+bot)
                cur.execute("Insert INTO Feedback VALUES (?)",[se])
                cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
                con.commit()                  
        elif(se=='Bad'or se=='bad'):
                bot="Thankyou. We are sorry to hear that , we will improve it!!!"
                self.text.insert(END,'\n'+bot)
                cur.execute("Insert INTO Feedback VALUES (?)",[se])
                cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
                con.commit()                  

        elif(se=='n'):
                bot="We appreciate for your time.Thank you!!"
                self.text.insert(END,'\n'+bot)
                e=self.entry.get()
                cur.execute("Insert INTO Recordbook VALUES ('user',?)",[e])
                cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[bot])
                cur.execute("Insert INTO Feedback VALUES ('No ratings')")
                con.commit()        
        else:
            respon= hell.get_response(se)
            cur.execute("Insert INTO Recordbook VALUES ('user',?)",[se])
            cur.execute("Insert INTO Recordbook VALUES ('Jarvis',?)",[respon])
            self.text.insert(END,'\n\n'+'Jarvis: '+respon)
            con.commit()
        
       


   
        
if __name__ == '__main__':
  root=Tk()
  obj=ChatBot(root)
  root.mainloop()






































































































































# from tkinter import *
# from tkinter import ttk
# from PIL import Image,ImageTk

# class ChatBot:
#     def __init__(self,root):
#         self.root=root;
#         self.root.title=("chatbot");
#         self.root.geometry("730x620+0+0")
#         main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
#         self.root.bind('<Return>',self.enter_func)
#         main_frame.pack()

        # logoPic=PhotoImage(file='pic.png')
        # logoPicLabel=Label(root,image=logoPic,bg='deep pink')
        # logoPicLabel.pack(pady=2)
        # img = PhotoImage(file='pic.png')
        # Label(root,image=img).pack()


#         Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,text='chat me',font=('aerial',30,'bold'),bg='white')
#         Title_label.pack(side=TOP)
#         self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
#         self.text=Text(main_frame,width=65,height=20,bd=4,relief=RAISED,font=('aerial',14),yscrollcommand=self.scroll_y.set)
#         self.scroll_y.pack(side=RIGHT,fill=Y)
#         self.text.pack()
#         btn_frame=Frame(self.root,bd=4,bg='white',width=730)
#         btn_frame.pack()
#         label_1=Label(btn_frame,text='TYPE SOMETHING',font=('aerial',14,'bold'),fg='green',bg='white')
#         label_1.grid(row=0,column=0,padx=5,sticky=W)


#         self.entry=StringVar()
#         self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
#         self.entry1.grid(row=0,column=1,padx=5,sticky=W)
#         self.send=Button(btn_frame,text="send>>",command=self.send,font=('arial',15,'bold'),width=8,bg='green')
#         self.send.grid(row=0,column=2,padx=5,sticky=W)
#         self.clear=Button(btn_frame,text="clear",command=self.clear_func,font=('arial',15,'bold'),width=8,bg='red',fg='white')
#         self.clear.grid(row=1,column=0,padx=5,sticky=W)
#         self.msg=''
#         label2=Label(btn_frame,text=self.msg,font=('aerial',14,'bold'),fg='red',bg='white')
#         label2.grid(row=1,column=1,padx=5,sticky=W)
    
#     def enter_func(self,event):
#         self.send.invoke()
#         self.entry.set('')
#     def clear_func(self):
#         self.text.delete('1.0',END)
#         self.entry.set('')

#     def send(self):
#         send='\t\t\t'+'you: '+self.entry.get()
#         self.text.insert(END,'\n'+send)
#         self.text.yview(END)
#         if(send==''):
#             self.msg="please enter some input"
#             self.label2.config(text=self.msg,fg='red')
#         elif(self.entry.get()=='hello'):
#             bot='hi'
#             self.text.insert(END,'\n\n'+bot)
#         elif(send=="hello"):
#            self.text.insert(END,"\n\n"+"Bot: Hi")
#         elif(send=='hello'):
#            self.text.insert(END,'\n\n'+'Bot: Hi')
#         elif(send=='hello'):
#            self.text.insert(END,'\n\n'+'Bot: Hi')
#         elif(send=='hello'):
#            self.text.insert(END,'\n\n'+'Bot: Hi')
#         elif(send=='hello'):
#            self.text.insert(END,'\n\n'+'Bot: Hi')
#         elif(send=='hello'):
#            self.text.insert(END,'\n\n'+'Bot: Hi')

    
        
# if __name__ == '__main__':
#     root=Tk()
#     obj=ChatBot(root)
#     root.mainloop()
  
