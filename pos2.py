

from tkinter import *
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


master1= Tk()
master1.title("AEJAY'S CLOTHING")
master1.geometry("1350x750+0+0")
master1.config(bg='lavender')


Change_Input=StringVar()
Cash_Input=StringVar()
Total_Input=StringVar()
Tax_Input = StringVar()
SubTotal_Input = StringVar()
Item = StringVar()
QTY = StringVar()
Amount= StringVar()
Choice = StringVar()

'''
Pic1=PhotoImage(file ="children top 1.jpg")
pic2=PhotoImage(file="children top 2.jpeg")
pic3=PhotoImage(file="children sneakers 1.jpeg")
pic4=PhotoImage(file="children sneakers 2.jpeg")
pic5=PhotoImage(file="children sneakers 3.jpeg")
pic6=PhotoImage(file="children sneakers 4.jpeg")

pic7=PhotoImage(file="children pant.jpeg")
pic8=PhotoImage(file="children pant 2.jpeg")
pic9=PhotoImage(file="lady sneakers 3.jpeg")
pic10=PhotoImage(file="lady sneakers 1.jpeg")
pic11=PhotoImage(file="lady top 1.jpeg")
pic12=PhotoImage(file="lady top 2.jpeg")

pic13=PhotoImage(file="lady pant.jpeg")
pic14=PhotoImage(file="men top .jpeg")
pic15=PhotoImage(file="men top 2 .jpeg")
pic16=PhotoImage(file="men top 3.jpeg")
pic17=PhotoImage(file="men top 4.jpeg")
pic17=PhotoImage(file="men sneakers.jpeg")

pic19=PhotoImage(file="men sneakers 2.jpeg")
pic20=PhotoImage(file="men pant.jpeg")
pic21=PhotoImage(file="men pant 2.jpeg")
pic22=PhotoImage(file="men's suit.jpeg")
pic23=PhotoImage(file="men's suit 2.jpeg")
pic24=PhotoImage(file="men's suit 3.jpeg")

pic25=PhotoImage(file="baby's gown.jpeg")
pic26=PhotoImage(file="baby's gown 2.jpeg")
pic27=PhotoImage(file="baby's gown 3 .jpeg")
pic28=PhotoImage(file="new born.jpeg")
pic29=PhotoImage(file="new born 2.jpeg")
pic30=PhotoImage(file="lady pant 2.jpeg")
pic31=PhotoImage(file="lady's gown 1.jpeg")
pic32=PhotoImage(file="lady's gown 3.jpeg")
'''

#-=============================================================function==================================================================================


def delete():
    ItemCost=0.0
    Tax=2.5
    for child in Pos_records.get_children():
        ItemCost+=float(Pos_records.item(child,"values")[2])
    SubTotal_Input.set(str(ItemCost))
    Tax_Input.set(str((ItemCost * Tax)/100))
    Total_Input.set(str((ItemCost)+((ItemCost*Tax)/100)))
    selected_item=(Pos_records.selection()[0])
    Pos_records.delete(selected_item)

def givechange():
    ItemCost=0.0
    Tax=2.5
    CashInput = float( Cash_Input.get())
    for child in Pos_records.get_children():
        ItemCost+=float(Pos_records.item(child,"values")[2])
    Change_Input.set(str(CashInput-((ItemCost)+(ItemCost*Tax)/100)))
    if(Cash_Input.get()=="0"):
        Change_Input.set("")
      
def Exit(): 
    Exit=tkinter.messagebox.askyesno("point of sale","do you want to quit?")
    if Exit >0:
        master1.destroy()
        return

'''   
def method_of_pay():
    if (Choice.get()=="Cash"):
        txtCost.focus()
        Cash_Input.set("")
    elif (Choice.get()==""):
        Cash_input.("0")
        Change_Input.set
'''






def reset():

    #Pos_records.set("")
    Change_Input.set("")
    Cash_Input.set("")
    Total_Input.set("")
    Tax_Input .set("")
    SubTotal_Input.set("")
    Choice.set("")

#===========================================================framees=======================================================================================
MainFrame=Frame(master1,bg='cadetblue')
MainFrame.grid(padx=8,pady=5)

ButtonFrame = Frame(MainFrame, bg='cadetblue',bd=5,width=1348,height=160,padx=4,pady=4,relief=RIDGE)
ButtonFrame.pack(side=BOTTOM)

DataFrame = Frame(MainFrame, bg='lightpink',bd=5,width=800,height=300,padx=2,pady=2,relief=RIDGE)
DataFrame.pack(side=LEFT)

DataFrameLEFTCOVER =LabelFrame(DataFrame, bg='lightpink',bd=5,width=800,height=300,padx=4,pady=4,font=('arial',12,'bold'),text="point of sales",relief=RIDGE)
DataFrameLEFTCOVER.pack(side=LEFT)

ChangeButtonFrame=Frame(DataFrameLEFTCOVER,bd=5,width=300,height=460,pady=4,relief=RIDGE)
ChangeButtonFrame.pack(side=LEFT,padx=4)

ReceiptFrame = Frame(DataFrameLEFTCOVER, bd=5, width=200, height=400, padx=1, pady=5, relief=RIDGE)
ReceiptFrame.pack(side=RIGHT, padx=4)

FoodItemFrame = LabelFrame(DataFrame, bg='lightpink', bd=5, width=600, height=300, padx=5, pady=7,   font=('arial', 12, 'bold'), text="items", relief=RIDGE)
FoodItemFrame.pack(side=RIGHT)


CalFrame=Frame(ButtonFrame,bd=5,width=432,height=140,padx=4,pady=4,relief=RIDGE)
CalFrame.grid(row=0,column=0,padx=5)


ChangeFrame = Frame(ButtonFrame, bd=5, width=500, height=140, padx=4, pady=4, relief=RIDGE)
ChangeFrame.grid(row=0, column=1, padx=5)

RemoveFrame = Frame(ButtonFrame, bd=5, width=400, height=140, padx=4, pady=4, relief=RIDGE)
RemoveFrame.grid(row=0, column=2, padx=5)

# ==============================================ENTRY$LABEL WIDGET===============================================
lblSubTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Subtotal", bd=5)
lblSubTotal.grid(row=0, column=0, sticky=W, padx=5)
txtSubTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=SubTotal_Input, bd=2,width=24)
txtSubTotal.grid(row=0, column=1, sticky=W, padx=5)


lblTax = Label(CalFrame, font=('arial', 14, 'bold'), text="Tax", bd=5)
lblTax.grid(row=1, column=0, sticky=W, padx=5)
lblTax = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Tax_Input, bd=2, width=24)
lblTax.grid(row=1, column=1, sticky=W, padx=5)

lblTotal = Label(CalFrame, font=('arial', 14, 'bold'), text="Total", bd=5)
lblTotal.grid(row=2, column=0, sticky=W, padx=5)
lblTotal = Entry(CalFrame, font=('arial', 14, 'bold'), textvariable=Total_Input, bd=2, width=24)
lblTotal.grid(row=2, column=1, sticky=W, padx=5)


# ==============================================ENTRY  $LABEL WIDGET===============================================
lblMOP = Label(ChangeFrame, font=('arial', 12, 'bold'), text="METHOD OF PAYMENT", bd=5)
lblMOP.grid(row=0, column=0, sticky=W, padx=5)
cobMOP = ttk.Combobox(ChangeFrame, font=('arial', 12, 'bold'), width=36,state='readonly',textvariable=Choice,justify=RIGHT)
cobMOP['values']=('','cash','visacard','mastercard')
cobMOP.current(0)
cobMOP.grid(row=0, column=1)

lblCost = Label(ChangeFrame, font=('arial', 12, 'bold'), text="CASH", bd=5)
lblCost .grid(row=1, column=0, sticky=W, padx=5)
txtCost  = Entry(ChangeFrame, font=('arial', 12, 'bold'), textvariable=Cash_Input, bd=2, width=38)
txtCost.grid(row=1, column=1, sticky=W, padx=5)
txtCost.insert(0,"0")
lblChange = Label(ChangeFrame, font=('arial', 12, 'bold'), text="CHANGE", bd=5)
lblChange.grid(row=2, column=0, sticky=W, padx=5)
txtChange = Entry(ChangeFrame, font=('arial', 12, 'bold'), textvariable=Change_Input, bd=2, width=38)
txtChange.grid(row=2, column=1, sticky=W, padx=5)



# ==============================================ENTRY  $LABEL WIDGET===============================================
btnpay = Button(RemoveFrame,padx=4, font=('arial', 15, 'bold'), text="Pay",width=10,height=1, bd=2,command=givechange)
btnpay.grid(row=0, column=0, pady=2, padx=4)

btnexit = Button(RemoveFrame,padx=4, font=('arial', 15, 'bold'), text="Exit",width=10,height=1, bd=2,command=Exit)
btnexit .grid(row=0, column=1, pady=2, padx=4)

btnreset = Button(RemoveFrame,padx=4, font=('arial', 15, 'bold'), text="Reset",width=10,height=1, bd=2,command=reset)
btnreset.grid(row=1, column=0, pady=2, padx=4)

btnremoveitem = Button(RemoveFrame,padx=4, font=('arial', 15, 'bold'), text="Remove item",width=10,height=1, bd=2,command=delete)
btnremoveitem.grid(row=1, column=1, pady=2, padx=4)

# ==============================================BUTTON WIDGET=====================================================
scroll_x=Scrollbar(ReceiptFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ReceiptFrame,orient=VERTICAL)
Pos_records=ttk.Treeview(ReceiptFrame,height=20,columns=("Items","Qty","Amount"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

Pos_records.heading("Items",text="ITEMS")
Pos_records.heading("Qty",text="QTY") 
Pos_records.heading("Amount",text="AMOUNT")

Pos_records['show']='headings'

Pos_records.column("Items",width=120)
Pos_records.column("Qty",width=100)
Pos_records.column("Amount",width=100)

Pos_records.pack(fill=BOTH,expand=2)
Pos_records.bind("Buttonrelease-4>")
# =============================================FUNCTION==============================================
def pic1():
    ItemCost= 5000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("vintage boy's top","1","5000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-5000))
        Tax_Input.set(str(((ItemCost-5000)*Tax)/100))
        Total_Input.set(str((ItemCost-5000)+((ItemCost-5000)*Tax)/100))
def pic2():
    ItemCost= 3000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("designerlongsleeve for boys","1","3000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-3000))
        Tax_Input.set(str(((ItemCost-3000)*Tax)/100))
        Total_Input.set(str((ItemCost-3000)+((ItemCost-3000)*Tax)/100))
def pic3():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("white design sneakers  for boys","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic4():
    ItemCost= 7000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("gucci sneaker for girls","1","7000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-7000))
        Tax_Input.set(str(((ItemCost-7000)*Tax)/100))
        Total_Input.set(str((ItemCost-7000)+((ItemCost-3000)*Tax)/100))
def pic5():
    ItemCost= 9000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi sneakerds for  boys","1","9000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-9000))
        Tax_Input.set(str(((ItemCost-9000)*Tax)/100))
        Total_Input.set(str((ItemCost-9000)+((ItemCost-9000)*Tax)/100))
def pic6():
    ItemCost= 4000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("glitter sneakers for girls","1","4000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-4000))
        Tax_Input.set(str(((ItemCost-4000)*Tax)/100))
        Total_Input.set(str((ItemCost-4000)+((ItemCost-4000)*Tax)/100))
def pic7():
    ItemCost= 4000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("kevin trousers for boys ","1","4000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-4000))
        Tax_Input.set(str(((ItemCost-4000)*Tax)/100))
        Total_Input.set(str((ItemCost-4000)+((ItemCost-4000)*Tax)/100))
def pic8():
    ItemCost= 4000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("haven trousers for girls","1","4000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-4000))
        Tax_Input.set(str(((ItemCost-4000)*Tax)/100))
        Total_Input.set(str((ItemCost-4000)+((ItemCost-4000)*Tax)/100))
def pic9():
    ItemCost= 4000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("pink designers sneakers for girls","1","7000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-7000))
        Tax_Input.set(str(((ItemCost-7000)*Tax)/100))
        Total_Input.set(str((ItemCost-7000)+((ItemCost-7000)*Tax)/100))          
def pic10():
    ItemCost= 9000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi sneakers for girls","1","9000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-9000))
        Tax_Input.set(str(((ItemCost-9000)*Tax)/100))
        Total_Input.set(str((ItemCost-9000)+((ItemCost-9000)*Tax)/100))
def pic11():
    ItemCost= 9000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("One corner top for ladies","1","9000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-9000))
        Tax_Input.set(str(((ItemCost-9000)*Tax)/100))
        Total_Input.set(str((ItemCost-9000)+((ItemCost-9000)*Tax)/100))              
def pic12():
    ItemCost= 4000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("bounded top for ladies","1","4000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-4000))
        Tax_Input.set(str(((ItemCost-4000)*Tax)/100))
        Total_Input.set(str((ItemCost-4000)+((ItemCost-4000)*Tax)/100))
def pic13():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi palazo trouser for ladies","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic14():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi palazo trouser for ladies","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic15():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi palazo trouser for ladies","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic16():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi palazo trouser for ladies","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))        
def pic17():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("svenchi palazo trouser for ladies","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic18():
    ItemCost= 5000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("Ash adidas sneakers for men","1","5000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-5000))
        Tax_Input.set(str(((ItemCost-5000)*Tax)/100))
        Total_Input.set(str((ItemCost-5000)+((ItemCost-5000)*Tax)/100))
def pic19():
    ItemCost= 3000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("highleg sneakers for men","1","3000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-3000))
        Tax_Input.set(str(((ItemCost-3000)*Tax)/100))
        Total_Input.set(str((ItemCost-3000)+((ItemCost-3000)*Tax)/100))
def pic20():
    ItemCost= 5000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("straightleg men's pant","1","5000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-5000))
        Tax_Input.set(str(((ItemCost-5000)*Tax)/100))
        Total_Input.set(str((ItemCost-5000)+((ItemCost-5000)*Tax)/100))
def pic21():
    ItemCost= 3000
    Tax=2.5
    Pos_records.insert("",tk.END,values=(" coporate men's pant","1","3000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-3000))
        Tax_Input.set(str(((ItemCost-3000)*Tax)/100))
        Total_Input.set(str((ItemCost-3000)+((ItemCost-3000)*Tax)/100))
def pic22():
    ItemCost= 20000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("dinner suit for men ","1","20000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-20000))
        Tax_Input.set(str(((ItemCost-20000)*Tax)/100))
        Total_Input.set(str((ItemCost-20000)+((ItemCost-20000)*Tax)/100))
def pic23():
    ItemCost= 20000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("wedding suit for men ","1","20000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-20000))
        Tax_Input.set(str(((ItemCost-20000)*Tax)/100))
        Total_Input.set(str((ItemCost-20000)+((ItemCost-20000)*Tax)/100))
def pic24():
    ItemCost= 20000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("geng suit for men ","1","20000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-20000))
        Tax_Input.set(str(((ItemCost-20000)*Tax)/100))
        Total_Input.set(str((ItemCost-20000)+((ItemCost-20000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic25():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("chidren dinner gown with Ankara","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic26():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("chidren plain  gown with Ankara","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic27():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("chidren peplon gown with Ankara","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic28():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("new born shirt and trouser set","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic29():
    ItemCost= 3000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("newborn overall","1","3000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-3000))
        Tax_Input.set(str(((ItemCost-3000)*Tax)/100))
        Total_Input.set(str((ItemCost-3000)+((ItemCost-3000)*Tax)/100))
def pic30():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("lady's ankara with lace","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic31():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("lady's office gown","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))
def pic32():
    ItemCost= 6000
    Tax=2.5
    Pos_records.insert("",tk.END,values=("lady's dinner gown","1","6000"))
    for child in Pos_records.get_children():
        ItemCost+=float( Pos_records.item(child,"values")[2])
        SubTotal_Input.set(str(ItemCost-6000))
        Tax_Input.set(str(((ItemCost-6000)*Tax)/100))
        Total_Input.set(str((ItemCost-6000)+((ItemCost-6000)*Tax)/100))        
        
# ==============================================ENTRY  $LABEL WIDGET===============================================
btnpic1 = Button(ChangeButtonFrame,padx=2,height=5,width=10,bd=2,command=pic1
                 )
btnpic1.grid(row=0, column=0, pady=2, padx=4)
btnpic2 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic2)
btnpic2.grid(row=0, column=1, pady=2, padx=4)
btnpic3 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic3)
btnpic3.grid(row=1, column=0, pady=2, padx=4)
btnpic4 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic4)
btnpic4.grid(row=1, column=1, pady=2, padx=4)
btnpic5 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic5)
btnpic5.grid(row=2, column=0, pady=2, padx=4)
btnpic6 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic6)
btnpic6.grid(row=2, column=1, pady=2, padx=4)
btnpic7 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic7)
btnpic7.grid(row=3, column=0, pady=2, padx=4)
btnpic8 = Button(ChangeButtonFrame,padx=2 ,height=5,width=10,bd=2,command=pic8)
btnpic8.grid(row=3, column=1, pady=2, padx=4)


# ==============================================ENTRY  $LABEL WIDGET===============================================
btnpic9 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic9)
btnpic9.grid(row=0, column=0, pady=2, padx=4)
btnpic10 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic10)
btnpic10.grid(row=0, column=1, pady=2, padx=4)
btnpic11 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic11)
btnpic11.grid(row=0, column=2, pady=2, padx=4)
btnpic12 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic12)
btnpic12.grid(row=0, column=3, pady=2, padx=4)
btnpic13 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic13)
btnpic13.grid(row=1, column=0, pady=2, padx=4)
btnpic14 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic14)
btnpic14.grid(row=1, column=1, pady=2, padx=4)
btnpic15 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic15)
btnpic15.grid(row=1, column=2, pady=2, padx=4)
btnpic16 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic16)
btnpic16.grid(row=1, column=3, pady=2, padx=4)
btnpic17 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic17)
btnpic17.grid(row=2, column=0, pady=2, padx=4)
btnpic18 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic18)
btnpic18.grid(row=2, column=1, pady=2, padx=4)
btnpic19 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic19)
btnpic19.grid(row=2, column=2, pady=2, padx=4)
btnpic20 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic20)
btnpic20.grid(row=2, column=3, pady=2, padx=4)
btnpic21 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic21)
btnpic21.grid(row=3, column=0, pady=2, padx=4)
btnpic22 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic22)
btnpic22.grid(row=3, column=1, pady=2, padx=4)
btnpic23 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic23)
btnpic23.grid(row=3, column=2, pady=2, padx=4)
btnpic24 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic24)
btnpic24.grid(row=3, column=3, pady=2, padx=4)
btnpic25 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic25)
btnpic25.grid(row=4, column=0, pady=2, padx=4)
btnpic26 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic26)
btnpic26.grid(row=4, column=1, pady=2, padx=4)
btnpic27 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic27)
btnpic27.grid(row=4, column=2, pady=2, padx=4)
btnpic28 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic28)
btnpic28.grid(row=4, column=3, pady=2, padx=4)
btnpic29 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic29)
btnpic29.grid(row=5, column=0, pady=2, padx=4)
btnpic30 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic30)
btnpic30.grid(row=5, column=1, pady=2, padx=4)
btnpic31 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic31)
btnpic31.grid(row=5, column=2, pady=2, padx=4)
btnpic32 = Button(FoodItemFrame,padx=2 ,height=5,width=10,bd=2,command=pic32)
btnpic32.grid(row=5, column=3, pady=2, padx=4)


mainloop()


