from constant import *

from tkinter import*
from tkinter import ttk
home=Tk()
home.title("Arithmós")
home.geometry("800x500")


from unitconv import *
import solver
import Stats
import quad


#stat calculations
def stat_calc():
    'Takes input from the entry box and stores it in userData'
    userData=str(entry.get())
    
    'Puts userData in Stats.calc. Then the result of Stats.calc is given to Stats.output as input. Stats.output displays'
    'the result of the calculations'
    return Stats.output(Stats.calc(userData))
    

#Quadratic equation
def quad_eq():
    userData=str(entry.get())
    return quad.output(quad.calc(userData))
    
#math expression calculation
def math_exp():
    userData=str(entry.get())
    entry.delete(0,'end')
    
    #if entry box is empty, don't do anything
    if userData=='':
        return None
    else:
        pinp=solver.parse(userData)
    
        if type(pinp)==str:
            math_exp.ans=solver.sol_func(pinp)
        else:
            math_exp.ans= solver.sol(pinp)
        
        
        if math_exp.ans=='Syntax Error':
            #math_exp.ans=0       
            return entry.insert(END, 'Syntax Error')
        else:
            return entry.insert(END, math_exp.ans)

#Unit conversions:
    
def F_C():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bF_C['text']=='F|C':           
            bF_C.config(text='C|F')
            math_exp.ans=Conv['F_C'](userData)
            
        else:
            bF_C.config(text='F|C')
            math_exp.ans=Conv['C_F'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')


def kmh_ms():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bkmh_ms['text']=='km/h|m/s':           
            bkmh_ms.config(text='m/s|km/h')
            math_exp.ans=Conv['ms_kmh'](userData)
            
        else:
            bkmh_ms.config(text='km/h|m/s')
            math_exp.ans=Conv['kmh_ms'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')
    
def J_C():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bJ_C['text']=='J|Cal':           
            bJ_C.config(text='Cal|J')
            math_exp.ans=Conv['Cal_J'](userData)
            
        else:
            bJ_C.config(text='J|Cal')
            math_exp.ans=Conv['J_Cal'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')


def inch_cm():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bin_cm['text']=='inch|cm':           
            bin_cm.config(text='cm|inch')
            math_exp.ans=Conv['cm_inch'](userData)
            
        else:
            bin_cm.config(text='inch|cm')
            math_exp.ans=Conv['inch_cm'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')
    
def ft_m():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bft_m['text']=='ft|m':           
            bft_m.config(text='m|ft')
            math_exp.ans=Conv['m_ft'](userData)
            
        else:
            bft_m.config(text='ft|m')
            math_exp.ans=Conv['ft_m'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')



def km_m():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if bkm_m['text']=='km|m':           
            bkm_m.config(text='m|km')
            math_exp.ans=Conv['m_km'](userData)
            
        else:
            bkm_m.config(text='km|m')
            math_exp.ans=Conv['km_m'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')


def atm_Pa():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if batm_Pa['text']=='atm|Pa':           
            batm_Pa.config(text='Pa|atm')
            math_exp.ans=Conv['Pa_atm'](userData)
            
        else:
            batm_Pa.config(text='atm|Pa')
            math_exp.ans=Conv['atm_Pa'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')

def oz_g():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if boz_g['text']=='oz|g':           
            boz_g.config(text='g|oz')
            math_exp.ans=Conv['g_oz'](userData)
            
        else:
            boz_g.config(text='oz|g')
            math_exp.ans=Conv['oz_g'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')

def lb_kg():
    userData=str(entry.get())
    entry.delete(0,'end')
    try:
        userData=float(userData)
        if blb_kg['text']=='lb|kg':           
            blb_kg.config(text='kg|lb')
            math_exp.ans=Conv['kg_lb'](userData)
            
        else:
            blb_kg.config(text='lb|kg')
            math_exp.ans=Conv['lb_kg'](userData)
            
        return entry.insert(END, math_exp.ans)
        
    except:
        return entry.insert(END,'Syntax Error')

#Entry_box
entry=ttk.Entry(home, width=73)
entry.grid(columnspan=8,row=0,column=0, ipady=4, pady=12)

    

#Numbers
one=ttk.Button(text='1',width=6, command=lambda: entry.insert(END, "1") )
one.grid(column=3,row=3)

two=ttk.Button(text='2',width=6, command=lambda: entry.insert (END, "2") )
two.grid(column=2,row=3)

three=ttk.Button(text='3',width=6, command=lambda: entry.insert (END, "3") )
three.grid(column=1,row=3)

four=ttk.Button(text='4',width=6,command=lambda: entry.insert (END, "4") )
four.grid(column=3,row=2)

five=ttk.Button(text='5',width=6, command=lambda: entry.insert (END, "5") )
five.grid(column=2,row=2)

six=ttk.Button(text='6',width=6, command=lambda: entry.insert (END, "6") )
six.grid(column=1,row=2)

seven=ttk.Button(text='7',width=6, command=lambda: entry.insert (END, "7") )
seven.grid(column=1,row=1)

eight=ttk.Button(text='8',width=6, command=lambda: entry.insert (END, "8") )
eight.grid(column=2,row=1)

nine=ttk.Button(text='9',width=6, command=lambda: entry.insert (END, "9") )
nine.grid(column=3,row=1)

zero=ttk.Button(text='0',width=6, command=lambda: entry.insert (END, "0") )
zero.grid(column=1,row=4)

double_zero=ttk.Button(text='00',width=6, command=lambda: entry.insert (END, "00") ) 
double_zero.grid(column=3,row=4)


#-------Functions-------
point=ttk.Button(text='.',width=6, command=lambda: entry.insert (END, ".") )
point.grid(column=2,row=4)

brk=ttk.Button(text='(',width=6, command=lambda: entry.insert(END, '('))
brk.grid(column=0,row=1)

brk2=ttk.Button(text=')',width=6, command=lambda: entry.insert(END, ')'))
brk2.grid(column=0,row=4)

AC=ttk.Button(text='AC',width=6, command=lambda: entry.delete(0,'end'))
AC.grid(column=0,row=2)

plus=ttk.Button(text='+',width=6, command=lambda: entry.insert (END, "+") )
plus.grid(column=4,row=1)

minus=ttk.Button(text='-',width=6, command=lambda: entry.insert (END, "-") )
minus.grid(column=4,row=2)

divide=ttk.Button(text='/',width=6, command=lambda: entry.insert (END, "/")  )
divide.grid(column=4,row=3)

multiply=ttk.Button(text='x',width=6, command=lambda: entry.insert (END, "x") )
multiply.grid(column=4,row=4)

Ans=ttk.Button(text='Ans',width=6,command=lambda: entry.insert(END, math_exp.ans) )
Ans.grid(column=0,row=3)


one_divide_x=ttk.Button(text='1/x',width=6, command=lambda: entry.insert (END, "1/") )
one_divide_x.grid(column=0,row=5)

square_root_x=ttk.Button(text=u"\u221A",width=6, command=lambda: entry.insert (END, 'sqrt(') )
square_root_x.grid(column=1,row=5)

root_x=ttk.Button(text=u"y\u221A",width=6, command=lambda: entry.insert (END, 'nthroot(') )
root_x.grid(column=2,row=5)

x_power_o=ttk.Button(text='x^',width=6, command=lambda: entry.insert (END, "pwr(") )
x_power_o.grid(column=3,row=5)

x_square=ttk.Button(text='x^2',width=6,  command=lambda: entry.insert (END, "sqr("))
x_square.grid(column=4,row=5)

ln=ttk.Button(text='ln',width=6, command=lambda: entry.insert (END, "ln(") )
ln.grid(column=0,row=6)

Natural_log=ttk.Button(text='log10x',width=6, command=lambda: entry.insert (END, "log10("))
Natural_log.grid(column=1,row=6)

sin=ttk.Button(text='sin',width=6, command=lambda: entry.insert (END, "sin(") )
sin.grid(column=2,row=6)

cos=ttk.Button(text='cos',width=6, command=lambda: entry.insert (END, "cos(") )
cos.grid(column=3,row=6)

factorial=ttk.Button(text='!',width=6, command=lambda: entry.insert (END, "fact(") )
factorial.grid(column=4,row=6)

sinh=ttk.Button(text='sinh',width=6, command=lambda: entry.insert (END, "sinh(") )
sinh.grid(column=3,row=7)

cosh=ttk.Button(text='cosh',width=6, command=lambda: entry.insert (END, "cosh(") )
cosh.grid(column=2,row=7)

absolute=ttk.Button(text='abs',width=6, command=lambda: entry.insert (END, "abs(")  )
absolute.grid(column=0,row=7)

HCF=ttk.Button(text='HCF',width=6, command=lambda: entry.insert (END, "HCF(") )
HCF.grid(column=1,row=7)

expontial=ttk.Button(text='e^x',width=6, command=lambda: entry.insert (END, "e^("))
expontial.grid(column=4,row=7)


#-----Constants---------
pi=ttk.Button(text=u"\u03C0",width=10, command=lambda: entry.insert (END, constant["pi"]))
pi.grid(column=5,row=1)

G=ttk.Button(text='G',width=10, command=lambda: entry.insert (END, constant["G"]) )
G.grid(column=6,row=1)

e=ttk.Button(text='e',width=10, command=lambda: entry.insert (END, constant["e"]) )
e.grid(column=7,row=1)

F=ttk.Button(text='F',width=10, command=lambda: entry.insert (END, constant["F"]) )
F.grid(column=5,row=2)

NA=ttk.Button(text='NA',width=10, command=lambda: entry.insert (END, constant["NA"]) )
NA.grid(column=6,row=2)

k=ttk.Button(text='k',width=10, command=lambda: entry.insert (END, constant["k"]))
k.grid(column=7,row=2)

R=ttk.Button(text='R',width=10, command=lambda: entry.insert (END, constant["R"]) )
R.grid(column=5,row=3)

g=ttk.Button(text='g',width=10, command=lambda: entry.insert (END, constant["g"]) )
g.grid(column=6,row=3)

μo=ttk.Button(text='μo',width=10, command=lambda: entry.insert (END, constant["μo"]) )
μo.grid(column=7,row=3)

#-----Unit conversions------
bF_C=ttk.Button(text='F|C',width=10, command=F_C)
bF_C.grid(column=5,row=4)

bkmh_ms=ttk.Button(text='km/h|m/s',width=10, command=kmh_ms)
bkmh_ms.grid(column=6,row=4)

bJ_C=ttk.Button(text='J|C',width=10, command=J_C)
bJ_C.grid(column=7,row=4)

bin_cm=ttk.Button(text='in|cm',width=10, command=inch_cm)
bin_cm.grid(column=7,row=5)

bft_m=ttk.Button(text='ft|m',width=10, command=ft_m)
bft_m.grid(column=6,row=5)

bkm_m=ttk.Button(text='km|m',width=10, command=km_m)
bkm_m.grid(column=5,row=5)

batm_Pa=ttk.Button(text='atm|Pa',width=10, command=atm_Pa)
batm_Pa.grid(column=7,row=6)

boz_g=ttk.Button(text='oz|g',width=10, command=oz_g)
boz_g.grid(column=6,row=6)

blb_kg=ttk.Button(text='lb|Kg',width=10, command=lb_kg)
blb_kg.grid(column=5,row=6)

Equals_to=ttk.Button(text='=',width=20, command=math_exp)
Equals_to.grid(column=3,row=10, columnspan=3)

B1=ttk.Button(text='Quadratic Eqn',width=14, command=quad_eq)
B1.grid(column=4,row=7,columnspan=3)

B2=ttk.Button(text='stats',width=14, command=stat_calc)
B2.grid(column=6,row=7,columnspan=3)


#Calls function math_exp when enter key is pressed
def enter(event):
    math_exp()   
home.bind('<Return>', enter)

home.maxsize(450,270)
home.mainloop()

