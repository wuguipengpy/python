from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showinfo, showwarning, showerror

WARN = 'warn'
CRIT = 'CRIT'
REGU = 'regu'

SIGNS = {
    'do not enter' : CRIT,
    'railroad corssing' : WARN,
    '55\nspeed limit' : REGU,
    'wrong way' : CRIT,
    'merging tarffic' : WARN,
    'one way' : REGU
}

critCB = lambda : showerror('Error', 'Error Button Pressed!')
warnCB = lambda : showwarning('waring', 'Warning Button Pressed!')
infoCB = lambda : showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
Button(top, text = 'QUIT', command = top.quit, bg = 'red', fg = 'white').pack()

MyButton = pto(Button, top)
CritButton = pto(MyButton, command = critCB, bg = 'white', fg = 'red')
WarnButton = pto(MyButton, command = warnCB, bg = 'white')
ReguButton = pto(MyButton, command = infoCB, bg = 'white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = ('%sButton(text = %r%s).pack(fill = X, expand = True)' % (
        signType.title(), eachSign,
        '.upper()' if signType == CRIT else '.title()'))
    eval(cmd)

top.mainloop()