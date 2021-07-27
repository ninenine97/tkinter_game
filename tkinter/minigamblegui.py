
from tkinter import*
from tkinter.ttk import*
from random import*
from tkinter import messagebox
background_color = "LightCyan2"
window=Tk()
window.title("TWO DICE")
window.iconbitmap('C:/Users/nai nai/Documents/pythontest/Gaming-Dice-icon.png')
window.geometry("730x600")
window.configure(bg=background_color)
wallet=None

lbl=Label(window,text="Enter the amount you want to exchange with points!",font=("Arial",12),background="black",foreground="orange")
lbl.place(x=200,y=48)
input_money=Entry(window,width=14)
input_money.pack()
input_money.focus()
def clicked():
    global wallet
    wallet=int(input_money.get())*1.1
    lbl1=Label(window,text='with our 10% special promotion {} points have been added to your wallet! goodluck! '.format(int(wallet)),font=("Arial",9,"bold italic"),background="Light Cyan2",foreground="black")
    lbl1.place(x=120,y=70)
btn=Button(window,text='click',command=clicked)
btn.pack()


def game_option():
    if int(input_money.get()) > 0 :
        if combo.get()=="game_one":
            lbl3=Label(window,text="Please enter your bet amount",font=("Times",10),background="RosyBrown2",foreground="black")
            lbl3.place(x=10,y=250)
            inputbet=Entry(window,width=10)
            inputbet.place(x=14,y=270)
            inputbet.focus()
            def bet_gameone():
                global wallet
                bet_amount=int(inputbet.get())
                if bet_amount <= int(wallet):
                    lbl4=Label(window,text="choose a number from 1-6",font=("Times",10),background="RosyBrown2",foreground="black")
                    lbl4.place(x=10,y=295)
                    spin=Spinbox(window,from_=1,to=6,width=7)
                    spin.place(x=14,y=317)
                    def okay():
                        global wallet
                        if int(wallet)>0 or bet_amount<=int(wallet):
                            result1=randint(1,6)
                            lbl5=Label(window,text="dice has rolled.........result is: "+ str(result1) )
                            lbl5.place(x=10,y=350)
                
                            if int(spin.get()) == result1:
                                wallet= int(wallet)+(bet_amount*5)
                                lbl6=Label(window,text="congratulations!\nyour guess is correct \nand here is points you own now: {}".format(int(wallet)))
                                lbl6.place(x=10,y=400)
                            else:
                                wallet= int(wallet)-bet_amount
                                lbl7=Label(window,text="your guess was wrong!\nyou lost "+str(bet_amount)+"\nyour current points: {}".format(int(wallet)))
                                lbl7.place(x=10,y=400)
                        else:
                            messagebox.showwarning('cannot proceed','no money in wallet\npls fill the wallet')

                    btn_ok=Button(window,text="ok",command=okay)
                    btn_ok.place(x=80,y=315)
                else:
                    messagebox.showwarning('cannot play','bet cannot be more than wallet\npls fill the wallet!')
            btn_gameone=Button(window,text="enter",command=bet_gameone)
            btn_gameone.place(x=85,y=269)
        if combo.get() == 'game_two':
            lbl8=Label(window,text="Please enter your bet amount",font=("Times",10),background="RosyBrown2",foreground="black")
            lbl8.place(x=560,y=250)
            inputbet1=Entry(window,width=10)
            inputbet1.place(x=564,y=270)
            inputbet1.focus()
            def bet_gametwo():
                global wallet
                bet_amount1=int(inputbet1.get())
                if bet_amount1 <= int(wallet):
                    lbl9=Label(window,text="choose a number from 1-12",font=("Times",10),background="RosyBrown2",foreground="black")
                    lbl9.place(x=560,y=296)

                    spin1=Spinbox(window,from_=1,to=12,width=7)
                    spin1.place(x=564,y=318)
 
                    def okay1():
                        global wallet
                        if int(wallet)>0:
                            result2=randint(1,12)
                            lbl10 = Label(window, text="dice has rolled.........result is: " + str(result2))
                            lbl10.place(x=560,y=350)

                            if int(spin1.get()) == result2:
                                wallet=int(wallet)+ (bet_amount1*10)
                                lbl11=Label(window,text="congratulations!\nyour guess is correct \nand here is points you own now: {}".format(int(wallet)))
                                lbl11.place(x=560,y=400)
                            else:
                                wallet=int(wallet)- bet_amount1
                                lbl12=Label(window,text="your guess was wrong!\nyou lost "+str(bet_amount1)+"\nyour current points\n: {}".format(int(wallet)))
                                lbl12.place(x=560,y=400)
                        else:
                            messagebox.showwarning('cannot proceed','no money in wallet\npls fill the wallet')
                    btn_ok1=Button(window,text="ok",command=okay1)
                    btn_ok1.place(x=630,y=317)
                else:
                    messagebox.showwarning('cannot play', 'bet cannot be more than wallet\npls fill the wallet!')

            btn_gametwo=Button(window,text="enter",command=bet_gametwo)
            btn_gametwo.place(x=635,y=270)
    else:
        messagebox.showwarning('cannot play','Empty Wallet!\npls fill the wallet!')      
     
                
def exit_change():
    global wallet
    window_one=Tk()
    window_one.title("have a nice day")  
    label_one=Label(window_one,text="congratulations! you can now change {} points to cash and enjoy".format(wallet),font=("Times",24),background="LightCyan",foreground="orange")
    label_one.pack()
 
    window.destroy()
    window_one.mainloop()

            


combo=Combobox(window,font=("Helvetica",10))
lbl2=Label(window,text="g a m e o p t i o n",font=("Times",13),foreground="orange",background="black")
lbl2.place(x=295,y=150)
combo['values']=["choose","game_one","game_two"]
combo.current(0)
combo.place(x=270,y=180)
btn1=Button(window,text="play",command=game_option)
btn1.place(x=320,y=203)

btn2=Button(window,text="Quit the game",command=exit_change)
btn2.place(x=320,y=575)


window.mainloop()