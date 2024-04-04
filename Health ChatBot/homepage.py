
from tkinter import *
from PIL import Image,ImageTk
from chatbot import ChatBot

class hospital:
    def __init__(self,root):
       self.root=root;
       self.root.title("LIFESAVER")
       self.root.geometry("1550x800+0+0")
        
    
    # ist image
       img1=Image.open("aims2.jpg")
       img1=img1.resize((1550,140),Image.ANTIALIAS)
       self.photo=ImageTk.PhotoImage(img1)
       lbimg=Label(self.root,image=self.photo,bd=4,relief=RIDGE)
       lbimg.place(x=0,y=0,width=1550,height=140)
    # 2nd image
       img2=Image.open("AIIMS.jpg")
       img2=img2.resize((230,140),Image.ANTIALIAS)
       self.photo2=ImageTk.PhotoImage(img2)
       lbimg=Label(self.root,image=self.photo2,bd=4,relief=RIDGE)
       lbimg.place(x=0,y=0,width=230,height=140)
    #    ###############
       lbl_title=Label(self.root,text="AIMS NAGPUR",font=("times new roman",40,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
       lbl_title.place(x=0,y=140,width=1550,height=50)

    ##frame
       main_frame=Frame(self.root,bd=4,relief=RIDGE)
       main_frame.place(x=0,y=190,width=1550,height=620)

      ###menu

       lbl_menu=Label(main_frame,text="MENU",font=("times new roman",40,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
       lbl_menu.place(x=0,y=0,width=230)

      ##frame
       btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
       btn_frame.place(x=0,y=70,width=228,height=300)

       cust_btn=Button(btn_frame,text="CUSTOMER",width=15,font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE,cursor="hand1")
       cust_btn.grid(row=0,column=0)

       
       room_btn=Button(btn_frame,text="ROOM",width=15,font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE,cursor="hand1")
       room_btn.grid(row=1,column=0)

       details_btn=Button(btn_frame,text="DETAILS",width=15,font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE,cursor="hand1")
       details_btn.grid(row=2,column=0)

       report_btn=Button(btn_frame,text="REPORT",width=15,font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE,cursor="hand1")
       report_btn.grid(row=3,column=0)

       chat_btn=Button(btn_frame,text="chat to me",command=self.ahatbot,width=15,font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,cursor="hand1")
       chat_btn.grid(row=5,column=0)
      
       logout_btn=Button(btn_frame,text="LOGOUT",width=15,font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,cursor="hand1")
       logout_btn.grid(row=4,column=0)
    #   ######RIGHT IMAGE

       img3=Image.open("aims3.jpg")
       img3=img3.resize((1310,590),Image.ANTIALIAS)
       self.photo3=ImageTk.PhotoImage(img3)
       lbimg3=Label(main_frame,image=self.photo3,bd=4,relief=RIDGE)
       lbimg3.place(x=225,y=0,width=1310,height=590)

    def ahatbot(self):
           self.new_window=Toplevel(self.root)
           self.app=ChatBot(self.new_window)  



    





if __name__=="__main__":
    root=Tk()
    obj=hospital(root)
    root.mainloop()