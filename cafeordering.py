from tkinter import*
import random
import time

#functions
def receipt():
    x=random.randint(100,1000)
    billnumber='BILL'+str(x)
    date=time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
    textReceipt.insert(END,'***************************************************************\n')
    textReceipt.insert(END,'Items:\t\tCost of Items(Rs)\n')
    textReceipt.insert(END,'***************************************************************\n')
    if e_vegetablesalad.get()!='0':
        textReceipt.insert(END,f'Vegetable Salad\t\t\t{int(e_vegetablesalad.get())*10}\n\n')

    if e_roastchicken.get()!='0':
        textReceipt.insert(END,f'Vegetable Salad\t\t\t{int(e_roastchicken.get())*60}\n\n')
    if e_frenchfries.get()!='0':
        textReceipt.insert(END,f'Roaster Chicken\t\t\t{int(e_frenchfries.get())*100}\n\n')
    if e_udonnoodles.get()!='0':
        textReceipt.insert(END,f'Udon Noodles\t\t\t{int(e_udonnoodles.get())*50}\n\n')
    if e_lamannoodles.get()!='0':
        textReceipt.insert(END,f'Laman Noodles\t\t\t{int(e_lamannoodles.get())*40}\n\n')
    if e_garlicbread.get()!='0':
        textReceipt.insert(END,f'Garlic Noodles\t\t\t{int(e_garlicbread.get())*30}\n\n')
    if e_pizza.get()!='0':
        textReceipt.insert(END,f'Pizza\t\t\t{int(e_pizza.get())*120}\n\n')
    if e_spaghetti.get()!='0':
        textReceipt.insert(END,f'Sphaghetti\t\t\t{int(e_spaghetti.get())*100}\n\n')
    if e_hakkanoodles.get()!='0':
        textReceipt.insert(END,f'Hakka Noodles\t\t\t{int(e_hakkanoodles.get())*120}\n\n')  

def totalcost():
    item1=int(e_vegetablesalad.get())
    item2=int(e_roastchicken.get())
    item3 = int(e_frenchfries.get())
    item4 = int(e_udonnoodles.get())
    item5 = int(e_lamannoodles.get())
    item6 = int(e_garlicbread.get())
    item7 = int(e_pizza.get())
    item8 = int(e_spaghetti.get())
    item9=int(e_hakkanoodles.get())
    
    item10 = int(e_americano.get())
    item11 = int(e_latte.get())
    item12 = int(e_cappuccino.get())
    item13 = int(e_lemonicedtea.get())
    item14 = int(e_greentea.get())
    item15 = int(e_masalatea.get())
    item16 = int(e_virginmojito.get())
    item17 = int(e_mintmojito.get())
    item18 = int(e_blueberrymojito.get())
    item19 = int(e_strawberrycake.get())
    item20 = int(e_macaroonscake.get())
    item21 = int(e_koreanpancake.get())
    item22 = int(e_chocopie.get())
    item23 = int(e_chocolatetruffle.get())
    item24 = int(e_banoffeetiramisu.get())
    item25 = int(e_chocolatefudge.get())
    item26 = int(e_blueberrycheesecake.get())
    item27 = int(e_applepie.get())
    
    priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+ (item5*40) + (item6*30) + (item7*120) + (item8*100) + (item9 * 120)
    priceofDrinks=(item10*50)+(item11*40)+ (item12*80) + (item13*30) + (item14*40) + (item15 * 60)  + (item16*20) + (item17*50) + (item18 * 80)
    priceofDesert=(item19*400)+(item20*300)+ (item21 * 500) + (item22*550) + (item23*450) + (item24*800)  + (item25*620)+(item26*700) + (item27 * 550)

    costoffoodvar.set(str(priceofFood)+ 'Rs')
    costofdrinksvar.set(str(priceofDrinks)+'Rs')
    costofdesertvar.set(str(priceofDesert)+'Rs')

    subtotalofItems=priceofFood+priceofDrinks+priceofDesert
    subtotalvar.set(str(subtotalofItems)+' Rs')
    servicetaxvar.set('50 Rs')

    tottalcost=subtotalofItems+50
    totalcostvar.set(str(tottalcost)+' Rs')

def vegetablesalad():
    if var1.get()==1:
        textvegetablesalad.config(state=NORMAL)
        textvegetablesalad.delete(0,END)
        textvegetablesalad.focus()
    else:
        textvegetablesalad.config(state=DISABLED)
        e_vegetablesalad.set('0')

def roastchicken():
    if var2.get()==1:
        textroastchicken.config(state=NORMAL)
        textroastchicken.delete(0,END)
        textroastchicken.focus()
    else:
        textroastchicken.config(state=DISABLED)
        e_roastchicken.set('0')   

def frenchfries():
    if var3.get()==1:
        textfrenchfries.config(state=NORMAL)
        textfrenchfries.delete(0,END)
        textfrenchfries.focus()
    else:
        textfrenchfries.config(state=DISABLED)
        e_frenchfries.set('0') 

def udonnoodles():
    if var4.get()==1:
        textudonoodles.config(state=NORMAL)
        textudonoodles.delete(0,END)
        textudonoodles.focus()
    else:
        textudonoodles.config(state=DISABLED)
        e_udonnoodles.set('0')

def lamannoodles():
    if var5.get()==1:
        textlamannoodles.config(state=NORMAL)
        textlamannoodles.delete(0,END)
        textlamannoodles.focus()
    else:
        textlamannoodles.config(state=DISABLED)
        e_lamannoodles.set('0')

def garlicbread():
    if var6.get()==1:
        textgarlicbread.config(state=NORMAL)
        textgarlicbread.delete(0,END)
        textgarlicbread.focus()
    else:
        textgarlicbread.config(state=DISABLED)
        e_garlicbread.set('0') 

def pizza():
    if var7.get()==1:
        textpizza.config(state=NORMAL)
        textpizza.delete(0,END)
        textpizza.focus()
    else:
        textpizza.config(state=DISABLED)
        e_pizza.set('0') 

def spaghetti():
    if var8.get()==1:
        textspaghetti.config(state=NORMAL)
        textspaghetti.delete(0,END)
        textspaghetti.focus()
    else:
        textspaghetti.config(state=DISABLED)
        e_spaghetti.set('0')

def hakkanoodles():
    if var9.get()==1:
        texthakkanoodles.config(state=NORMAL)
        texthakkanoodles.delete(0,END)
        texthakkanoodles.focus()
    else:
        texthakkanoodles.config(state=DISABLED)
        e_hakkanoodles.set('0')


def americano():
    if var10.get()==1:
        textamericano.config(state=NORMAL)
        textamericano.delete(0,END)
        textamericano.focus()
    else:
        textamericano.config(state=DISABLED)
        e_americano.set('0')

def latte():
    if var11.get()==1:
        textlatte.config(state=NORMAL)
        textlatte.delete(0,END)
        textlatte.focus()
    else:
        textlatte.config(state=DISABLED)
        e_latte.set('0')

def cappuccino():
    if var12.get()==1:
        textcappuccino.config(state=NORMAL)
        textcappuccino.delete(0,END)
        textcappuccino.focus()
    else:
        textcappuccino.config(state=DISABLED)
        e_cappuccino.set('0')

def lemonicedtea():
    if var13.get()==1:
        textlemonicedtea.config(state=NORMAL)
        textlemonicedtea.delete(0,END)
        textlemonicedtea.focus()
    else:
        textlemonicedtea.config(state=DISABLED)
        e_lemonicedtea.set('0')

def greentea():
    if var14.get()==1:
        textgreentea.config(state=NORMAL)
        textgreentea.delete(0,END)
        textgreentea.focus()
    else:
        textgreentea.config(state=DISABLED)
        e_greentea.set('0')

def masalatea():
    if var15.get()==1:
        textmasalatea.config(state=NORMAL)
        textmasalatea.delete(0,END)
        textmasalatea.focus()
    else:
        textmasalatea.config(state=DISABLED)
        e_masalatea.set('0')

def virginmojito():
    if var16.get()==1:
        textvirginmojito.config(state=NORMAL)
        textvirginmojito.delete(0,END)
        textvirginmojito.focus()
    else:
        textvirginmojito.config(state=DISABLED)
        e_virginmojito.set('0')

def mintmojito():
    if var17.get()==1:
        textmintmojito.config(state=NORMAL)
        textmintmojito.delete(0,END)
        textmintmojito.focus()
    else:
        textmintmojito.config(state=DISABLED)
        e_mintmojito.set('0')

def blueberrymojito():
    if var18.get()==1:
        textblueberrymojito.config(state=NORMAL)
        textblueberrymojito.delete(0,END)
        textblueberrymojito.focus()
    else:
        textblueberrymojito.config(state=DISABLED)
        e_blueberrymojito.set('0')

def strawberrycake():
    if var19.get()==1:
        textstrawberrycake.config(state=NORMAL)
        textstrawberrycake.delete(0,END)
        textstrawberrycake.focus()
    else:
        textstrawberrycake.config(state=DISABLED)
        e_strawberrycake.set('0')

def macaroonscake():
    if var20.get()==1:
        textmacaroonscake.config(state=NORMAL)
        textmacaroonscake.delete(0,END)
        textmacaroonscake.focus()
    else:
        textmacaroonscake.config(state=DISABLED)
        e_macaroonscake.set('0')

def koreanpancake():
    if var21.get()==1:
        textkoreanpancake.config(state=NORMAL)
        textkoreanpancake.delete(0,END)
        textkoreanpancake.focus()
    else:
        textkoreanpancake.config(state=DISABLED)
        e_koreanpancake.set('0')

def chocopie():
    if var22.get()==1:
        textchocopie.config(state=NORMAL)
        textchocopie.delete(0,END)
        textchocopie.focus()
    else:
        textchocopie.config(state=DISABLED)
        e_chocopie.set('0')

def chocolatetruffle():
    if var23.get()==1:
        textchocolatetruffle.config(state=NORMAL)
        textchocolatetruffle.delete(0,END)
        textchocolatetruffle.focus()
    else:
        textchocolatetruffle.config(state=DISABLED)
        e_chocolatetruffle.set('0')

def banoffeetiramisu():
    if var24.get()==1:
        textbanoffeetiramisu.config(state=NORMAL)
        textbanoffeetiramisu.delete(0,END)
        textbanoffeetiramisu.focus()
    else:
        textbanoffeetiramisu.config(state=DISABLED)
        e_banoffeetiramisu.set('0')

def chocolatefudge():
    if var25.get()==1:
        textchocolatefudge.config(state=NORMAL)
        textchocolatefudge.delete(0,END)
        textchocolatefudge.focus()
    else:
        textchocolatefudge.config(state=DISABLED)
        e_chocolatefudge.set('0')

def blueberrycheesecake():
    if var26.get()==1:
        textblueberrycheesecake.config(state=NORMAL)
        textblueberrycheesecake.delete(0,END)
        textblueberrycheesecake.focus()
    else:
        textblueberrycheesecake.config(state=DISABLED)
        e_blueberrycheesecake.set('0')

def applepie():
    if var27.get()==1:
        textapplepie.config(state=NORMAL)
        textapplepie.delete(0,END)
        textapplepie.focus()
    else:
        textapplepie.config(state=DISABLED)
        e_applepie.set('0')


root=Tk()
root.geometry('1560x780+0+0')
root.resizable(0,0)
root.title('cafe ordering system')
root.config(bg='#000000')
topFrame=Frame(root,bd=10,relief=RIDGE,bg='#000000')
topFrame.pack(side=TOP)
labelTitle=Label(topFrame,text='WHISK AND SIP CAFE',font=('arial',30,'bold'),fg='blue',bd=7,bg='#FFFFFF',width=68)
labelTitle.grid(row=0,column=0)   
menuFrame=Frame(root,bd=15,relief=RIDGE,bg='#FFFFFF')   
menuFrame.pack(side=LEFT)
costFrame=Frame(menuFrame,bd=10,relief=RIDGE,bg='#FFFFFF',pady=10)   
costFrame.pack(side=BOTTOM) 

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FFFFFF')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FFFFFF')
drinksFrame.pack(side=LEFT)

desertFrame=LabelFrame(menuFrame,text='Desert',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FFFFFF')
desertFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='#FFFFFF')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='#FFFFFF')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#FFFFFF')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#FFFFFF')
buttonFrame.pack()
#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_vegetablesalad=StringVar()
e_roastchicken=StringVar()
e_frenchfries=StringVar()
e_udonnoodles=StringVar()
e_lamannoodles=StringVar()
e_garlicbread=StringVar()
e_pizza=StringVar()
e_spaghetti=StringVar()
e_hakkanoodles=StringVar()
e_americano=StringVar()
e_latte=StringVar()
e_cappuccino=StringVar()
e_lemonicedtea=StringVar()
e_greentea=StringVar()
e_masalatea=StringVar()
e_virginmojito=StringVar()
e_mintmojito=StringVar()
e_blueberrymojito=StringVar()
e_strawberrycake=StringVar()
e_macaroonscake=StringVar()
e_koreanpancake=StringVar()
e_chocopie=StringVar()
e_chocolatetruffle=StringVar()
e_banoffeetiramisu=StringVar()
e_chocolatefudge=StringVar()
e_blueberrycheesecake=StringVar()
e_applepie=StringVar()


costoffoodvar=StringVar()
costofdrinksvar= StringVar()
costofdesertvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()


e_vegetablesalad.set('0')
e_roastchicken.set('0')
e_frenchfries.set('0')
e_udonnoodles.set('0')
e_lamannoodles.set('0')
e_pizza.set('0')
e_garlicbread.set('0')
e_spaghetti.set('0')
e_hakkanoodles.set('0')


e_americano.set('0')
e_latte.set('0')
e_cappuccino.set('0')
e_lemonicedtea.set('0')
e_greentea.set('0')
e_masalatea.set('0')
e_virginmojito.set('0')
e_mintmojito.set('0')
e_blueberrymojito.set('0')


e_strawberrycake.set('0')
e_macaroonscake.set('0')
e_koreanpancake.set('0')
e_chocopie.set('0')
e_chocolatetruffle.set('0')
e_banoffeetiramisu.set('0')
e_chocolatefudge.set('0')
e_blueberrycheesecake.set('0')
e_applepie.set('0')


##food

vegetablesalad=Checkbutton(foodFrame,text='Vegetable Salad',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=vegetablesalad)
vegetablesalad.grid(row=0,column=0,sticky=W)
roastchicken=Checkbutton(foodFrame,text='Roast Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=roastchicken)
roastchicken.grid(row=1,column=0,sticky=W)
frenchfries=Checkbutton(foodFrame,text='French Fries',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=frenchfries)
frenchfries.grid(row=2,column=0,sticky=W)
udonnoodles=Checkbutton(foodFrame,text='Udon Noodles',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=udonnoodles)
udonnoodles.grid(row=3,column=0,sticky=W)
lamannoodles=Checkbutton(foodFrame,text='Lamian Noodles',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=lamannoodles)
lamannoodles.grid(row=4,column=0,sticky=W)
garlicbread=Checkbutton(foodFrame,text='Garlic Bread',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=garlicbread)
garlicbread.grid(row=5,column=0,sticky=W)
pizza=Checkbutton(foodFrame,text='Pizza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=pizza)
pizza.grid(row=6,column=0,sticky=W)
spaghetti=Checkbutton(foodFrame,text='Spaghetti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=spaghetti)
spaghetti.grid(row=7,column=0,sticky=W)
hakkanoodles=Checkbutton(foodFrame,text='Hakka Noddles',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=hakkanoodles)
hakkanoodles.grid(row=8,column=0,sticky=W)

##entry fields for food items 
textvegetablesalad=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vegetablesalad)
textvegetablesalad.grid(row=0,column=1)

textroastchicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roastchicken)
textroastchicken.grid(row=1,column=1)

textfrenchfries=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_frenchfries)
textfrenchfries.grid(row=2,column=1)

textudonoodles=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_udonnoodles)
textudonoodles.grid(row=3,column=1)

textlamannoodles=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lamannoodles)
textlamannoodles.grid(row=4,column=1)

textgarlicbread=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_garlicbread)
textgarlicbread.grid(row=5,column=1)

textpizza=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizza)
textpizza.grid(row=6,column=1)

textspaghetti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_spaghetti)
textspaghetti.grid(row=7,column=1)

texthakkanoodles=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_hakkanoodles)
texthakkanoodles.grid(row=8,column=1)

##Drinks

americano=Checkbutton(drinksFrame,text='Americano',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=americano)
americano.grid(row=0,column=0,sticky=W)

latte=Checkbutton(drinksFrame,text='Latte',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=latte)
latte.grid(row=1,column=0,sticky=W)

cappuccino=Checkbutton(drinksFrame,text='Cappuccino',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=cappuccino)
cappuccino.grid(row=2,column=0,sticky=W)

lemonicedtea=Checkbutton(drinksFrame,text='Lemon Iced Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=lemonicedtea)
lemonicedtea.grid(row=3,column=0,sticky=W)

greentea=Checkbutton(drinksFrame,text='Green Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=greentea)
greentea.grid(row=4,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masala Tea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=masalatea)
masalatea.grid(row=5,column=0,sticky=W)

virginmojito=Checkbutton(drinksFrame,text='Virgin Mojito',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=virginmojito)
virginmojito.grid(row=6,column=0,sticky=W)

mintmojito=Checkbutton(drinksFrame,text='Mint Mojito',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=mintmojito)
mintmojito.grid(row=7,column=0,sticky=W)

blueberrymojito=Checkbutton(drinksFrame,text='Blue Berry Mojito',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=blueberrymojito)
blueberrymojito.grid(row=8,column=0,sticky=W)


##entry fields for drinks items 
textamericano=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_americano)
textamericano.grid(row=0,column=1)

textlatte=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_latte)
textlatte.grid(row=1,column=1)

textcappuccino=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cappuccino)
textcappuccino.grid(row=2,column=1)

textlemonicedtea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lemonicedtea)
textlemonicedtea.grid(row=3,column=1)

textgreentea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_greentea)
textgreentea.grid(row=4,column=1)

textmasalatea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=5,column=1)

textvirginmojito=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_virginmojito)
textvirginmojito.grid(row=6,column=1)

textmintmojito=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mintmojito)
textmintmojito.grid(row=7,column=1)

textblueberrymojito=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blueberrymojito)
textblueberrymojito.grid(row=8,column=1)

##Deserts
strawberrycake=Checkbutton(desertFrame,text='Strawberry Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=strawberrycake)
strawberrycake.grid(row=0,column=0,sticky=W)

macaroonscake=Checkbutton(desertFrame,text='Macaroons Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=macaroonscake)
macaroonscake.grid(row=1,column=0,sticky=W)

koreanpancake=Checkbutton(desertFrame,text='Korean Pancake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=koreanpancake)
koreanpancake.grid(row=2,column=0,sticky=W)

chocopie=Checkbutton(desertFrame,text='Choco Pie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=chocopie)
chocopie.grid(row=3,column=0,sticky=W)

chocolatetruffle=Checkbutton(desertFrame,text='Chocolate Truffle',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=chocolatetruffle)
chocolatetruffle.grid(row=4,column=0,sticky=W)

banoffeetiramisu=Checkbutton(desertFrame,text='Banoffet Tiramisu',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=banoffeetiramisu)
banoffeetiramisu.grid(row=5,column=0,sticky=W)

chocolatefudge=Checkbutton(desertFrame,text='Chocolate Fudge',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=chocolatefudge)
chocolatefudge.grid(row=6,column=0,sticky=W)

blueberrycheesecake=Checkbutton(desertFrame,text='Blueberry Cheese Cake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=blueberrycheesecake)
blueberrycheesecake.grid(row=7,column=0,sticky=W)

applepie=Checkbutton(desertFrame,text='Apple Pie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=applepie)
applepie.grid(row=8,column=0,sticky=W)

##entry field for deserts   
textstrawberrycake=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_strawberrycake)
textstrawberrycake.grid(row=0,column=1)

textmacaroonscake=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_macaroonscake)
textmacaroonscake.grid(row=1,column=1)

textkoreanpancake=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_koreanpancake)
textkoreanpancake.grid(row=2,column=1)

textchocopie=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocopie)
textchocopie.grid(row=3,column=1)

textchocolatetruffle=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolatetruffle)
textchocolatetruffle.grid(row=4,column=1)

textbanoffeetiramisu=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banoffeetiramisu)
textbanoffeetiramisu.grid(row=5,column=1)

textchocolatefudge=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolatefudge)
textchocolatefudge.grid(row=6,column=1)

textblueberrycheesecake=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blueberrycheesecake)
textblueberrycheesecake.grid(row=7,column=1)

textapplepie=Entry(desertFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_applepie)
textapplepie.grid(row=8,column=1)


#costlabels & entry fields

labelCostofFood=Label(costFrame, text='Cost of Food', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)


labelCostofDrinks=Label(costFrame, text='Cost of Drinks', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)


labelCostofDesert=Label(costFrame, text='Cost of Deserts', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labelCostofDesert.grid(row=2,column=0)

textCostofDesert=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdesertvar)
textCostofDesert.grid(row=2,column=1,padx=41)

labelSubtotal=Label(costFrame, text='Sub Total', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labelSubtotal.grid(row=0,column=2)

textSubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubtotal.grid(row=0,column=3,padx=41) 


labelServicetax=Label(costFrame, text='Service Tax', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labelServicetax.grid(row=1,column=2)

textServicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServicetax.grid(row=1,column=3,padx=41) 


labeltotalcost=Label(costFrame, text='Total Cost', font=('arial', 16, 'bold'),bg='#FFFFFF',fg='black')
labeltotalcost.grid(row=2,column=2)

texttotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=41)

#Button
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='black',bg='#FFFFFF',bd=3,padx=5,command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='black',bg='#FFFFFF',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='black',bg='#FFFFFF',bd=3,padx=5)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='black',bg='#FFFFFF',bd=3,padx=5)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='black',bg='#FFFFFF',bd=3,padx=5)
buttonReset.grid(row=0,column=4)


#textarea for receipt
textReceipt=Text(recieptFrame, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
textReceipt.grid(row=0,column=8)


#Calculator
operator=''
def buttonClick(numbers):
    global operator
    operator=operator+numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''


calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame, text='7', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6, width=6,command=lambda:buttonClick('7'))
button7.grid ( row = 1 ,column=0)

button8=Button(calculatorFrame, text='8', font=('arial', 16, 'bold'), fg='black',bg='white', bd = 6, width=6,command=lambda:buttonClick('8'))
button8.grid ( row = 1 ,column=1)

button9=Button(calculatorFrame, text='9', font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width=6,command=lambda:buttonClick('9'))
button9.grid ( row = 1, column=2)

buttonPlus=Button(calculatorFrame, text='+', font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame, text='4', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6,width=6,command=lambda:buttonClick('4')) 
button4.grid(row=2,column=0)

button5=Button(calculatorFrame, text='5', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6,width=6,command=lambda:buttonClick('5') )
button5.grid(row=2,column=1)

button6=Button(calculatorFrame, text='6', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6,width=6,command=lambda:buttonClick('6') )
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame, text='-', font=('arial', 16, 'bold'), fg='black',bg='white', bd=6,width=6,command=lambda:buttonClick('-')) 
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame, text='1', font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame, text='2',font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width  = 6 ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame, text='3', font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3, column=2)

buttonMult=Button(calculatorFrame, text='*', font=('arial', 16, 'bold'), fg='black', bg='white', bd = 6 ,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame, text='Ans', font=('arial', 16, 'bold'), fg='black', bg='white',bd=6, width=6,command=answer) 
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame, text='Clear', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6, width=6,command=clear)
buttonClear.grid(row=4,column=1)

buttone=Button(calculatorFrame, text='0', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6,width=6,command=lambda:buttonClick('0'))
buttone.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame, text='/', font=('arial', 16, 'bold'), fg='black', bg='white', bd=6, width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()