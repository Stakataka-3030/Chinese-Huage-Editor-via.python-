from tkinter import *
from turtle import *
from time import *
from random import *
from math import *
from tkinter import messagebox
from tkinter import filedialog
from io import *
i=0
configlist=[]
lent=50
x=7
y=7
width=1
olt=0
drawon=0
ux=[]
uy=[]
uq=[]
ue=[]
hecwrite="已绘制：(按设置顺序)"+'\n'
def asksave():
    global filename
    filename = filedialog.asksaveasfilename(filetypes=[("花格输出器config文件","*.cfg")])
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何位置')
def askexp():
    global filename
    filename = filedialog.asksaveasfilename(filetypes=[("Eps矢量图文件","*.eps")])
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何位置')
def askfile():
    global filename
    filename = filedialog.askopenfilename()
    if filename != '':
         lb.config(text= filename)
    else:
         lb.config(text='您没有选择任何文件')
def openat(event=None):
    global root,lb
    root = Toplevel()
    btn=Button(root,text='选择文件',relief=RAISED,command=askfile)
    btn.grid(row=0,column=0)
    lb = Label(root,text='')
    lb.grid(row=0,column=1,padx=5)
    root_insure = Button(root,text="确定",command=openconfig)
    root_insure.grid(row=2,column=0)  
    root.mainloop()
def saveat(event=None):
    global root,lb
    root = Toplevel()
    btn=Button(root,text='选择文件位置并输入文件名和保存格式',relief=RAISED,command=asksave)
    btn.grid(row=0,column=0)
    lb = Label(root,text='')
    lb.grid(row=0,column=1,padx=5)
    root_insure = Button(root,text="确定",command=saveatrun)
    root_insure.grid(row=2,column=0)  
    root.mainloop()
def exportat(event=None):
    global root,lb
    root = Toplevel()
    btn=Button(root,text='选择文件位置并输入文件名和保存格式',relief=RAISED,command=askexp)
    btn.grid(row=0,column=0)
    lb = Label(root,text='')
    lb.grid(row=0,column=1,padx=5)
    root_insure = Button(root,text="确定",command=exportatrun)
    root_insure.grid(row=2,column=0)  
    root.mainloop()
def exportatrun(event=None):
    global olt,x,y,lent,width
    outtur()
    title("输出预览")
    ts = getscreen()
    try:
        exportfile=open('%s.eps'%(filename),mode='x+')
    except:
        exportfile=open('%s.eps'%(filename),mode='a+')
    ts.getcanvas().postscript(file=exportfile)
def saveatrun():
    global olt,x,y,lent,width
    try:
        savefile=open('%s'%(filename),mode='x+')
    except:
        savefile=open('%s'%(filename),mode='a+')
    savefile.truncate(0)
    xwei=numwi(x)
    ywei=numwi(y)
    lwei=numwi(lent)
    wwei=numwi(width)
    savefile.write(str(olt))
    savefile.write(str(xwei))
    savefile.write(str(ywei))
    savefile.write(str(lwei))
    savefile.write(str(wwei))
    savefile.write(str(x))
    savefile.write(str(y))
    savefile.write(str(lent))
    savefile.write(str(width))
    savefile.write("\n")
    for n in range(x*y):
        savefile.write(str(configlist[n]))
    savefile.write(hecwrite)
def numwi(num):
    num_str = str(abs(num))  # 去掉负号
    num_digits = len(num_str)
    return num_digits
for i in range(1000):
    configlist.append(1)
def generate_buttons(rows, cols):
    global chemov,output,hecprint
    global pic_list
    pic_list=[]
    try:
        for i in range(rows * cols):
            pic.destroy()
        hecprint.destory()
    except:
        pass
    try:
        hecprint.destory()
    except:
        pass
    for i in range(rows * cols):
        row = i // cols
        col = i % cols
        row = ceil(row)
        col = ceil(col)
        pic = Button(mainwindows, image=photo[0], command=lambda i=i+1: replace(pic_list[i-1], i))
        pic.grid(row=row, column=col,sticky='E')
        pic_list.append(pic)
    hecprint = Label(mainwindows,text=hecwrite)
    hecprint.grid(row=0,column=cols+1,rowspan=999,sticky="n")
    chemov = Checkbutton(mainwindows,text="动画",variable=ifmo,onvalue=1,offvalue=0)
    chemov.grid(row=rows+2,column=0)
    output=Button(mainwindows,text="预览",command=outtur)
    output.grid(row=rows+2,column=1)
def applyfr(event=None):
    for i in range(1000):
        configlist[i]=1
    global pic_list,x,y,lent,width,olt
    y=lenthx.get()
    x=lenthy.get()
    if x<3 or y<3:
        messagebox.showwarning(title='警告',message='边长至少为3')
    else:
        chemov.destroy()
        output.destroy()
        for pic in pic_list:
            pic.destroy()
        pic_list = []
        generate_buttons(x, y)
def applyot(event=None):
    global pic_list,x,y,lent,width,olt
    lent=lar.get()
    width=wid.get()
    olt=lin.get()
def outps(event=None):
    global lenthx,lenthy,lar,wid,lin
    otp=Toplevel()
    otp.title("输出设置")
    lar = IntVar()
    wid = IntVar()
    lin = IntVar()
    lar.set(lent)
    wid.set(width)
    lin.set(olt)
    frt_l = Label(otp, text="单图格边长(以像素记):")
    frt_l.grid(row=0,column=0,sticky=W)
    frt_l_input = Entry(otp, bd =5,textvariable=lar)
    frt_l_input.grid(row=0,column=1,sticky=E)
    frt_w = Label(otp, text="线宽度(以像素记):")
    frt_w.grid(row=1,column=0,sticky=W)
    frt_w_input = Entry(otp, bd =5,textvariable=wid)
    frt_w_input.grid(row=1,column=1,sticky=E)
    frt_a9 = Checkbutton(otp,text="输出包含参照线",variable=lin,onvalue=1,offvalue=0)
    frt_a9.grid(row=2,column=0)
    frt_c1=Button(otp,text="应用！",command=applyot)
    frt_c1.grid(row=2,column=1)
def frame(event=None):
    global lenthx,lenthy,lar,wid,lin
    frt=Toplevel()
    frt.title("框架设置")
    lenthx = IntVar()
    lenthy = IntVar()
    lenthx.set(x)
    lenthy.set(y)
    frt_x = Label(frt, text="X方向格数:")
    frt_x.grid(row=0,column=0,sticky=W)
    frt_x_input = Entry(frt, bd =5,textvariable=lenthx)
    frt_x_input.grid(row=0,column=1,sticky=E)
    frt_y = Label(frt, text="Y方向格数:")
    frt_y.grid(row=1,column=0,sticky=W)
    frt_y_input = Entry(frt, bd =5,textvariable=lenthy)
    frt_y_input.grid(row=1,column=1,sticky=E)
    frt_c=Button(frt,text="应用！",command=applyfr)
    frt_c.grid(row=2,column=0)
def draw(n,x,y):
    if configlist[n-1]==1:
        liujiao(x,y,lent)
    if configlist[n-1]==2:
        yazi(x,y,lent)
    else:
        pass
def yazi(x,y,l):
    lista=[90,90,90]
    listl=[l,l*0.2,l]
    lista_4_1=[90,90,90]
    listl_4_1=[l/2,l/2,l/2]
    lista_4_2=[90,90,90]
    listl_4_2=[l/2,l/2,l/2]
    n_angle(4,90,lista,listl,x-l*0.4,y-l)
    n_angle(4,180,lista,listl,x,y-l*0.4)
    up()
    goto(x-l,y)
    down()
    left(270)
    forward(l)
    up()
    left(270)
    forward(l)
    down()
    left(270)
    forward(l)
def liujiao(x,y,l):
    lista=[90,90,45,45]
    listl=[l*0.4,l*0.4,l*0.2,l*0.2*1.414]
    lista_4_1=[90,90,90]
    listl_4_1=[l*0.2,l*0.2,l*0.2]
    lista_4_2=[90,90,90]
    listl_4_2=[l*0.2,l*0.2,l*0.2]
    n_angle(5,90,lista,listl,x,y-l*0.4)
    n_angle(4,90,lista_4_1,listl_4_1,x,y-l*0.6)
    n_angle(5,0,lista,listl,x-l*0.4,y-l)
    n_angle(4,90,lista_4_2,listl_4_2,x-l*0.4,y-l*0.2)
    n_angle(4,90,lista_4_2,listl_4_2,x-l*0.4,y-l)
    n_angle(5,270,lista,listl,x-l,y-l*0.6)
    n_angle(4,90,lista_4_1,listl_4_1,x-l*0.8,y-l*0.6)
    n_angle(5,180,lista,listl,x-l*0.6,y)
    n_angle(4,90,lista_4_2,listl_4_2,x-l*0.4,y-l*0.2)
    n_angle(4,90,lista_4_2,listl_4_2,x-l*0.4,y-l)
    n_angle(5,270,lista,listl,x-l,y-l*0.6)
    n_angle(4,90,lista_4_1,listl_4_1,x-l*0.8,y-l*0.6)
    n_angle(5,180,lista,listl,x-l*0.6,y)
def n_angle(n,anglefirst,lista,listl,x,y):
    penup()
    goto(x,y)
    seth(anglefirst)
    pendown()
    i=0
    while i<n-1:
      forward(listl[i])
      left(lista[i])
      i=i+1
    goto(x,y)
def exp(event=None):
    exporteps()
    try:
        from pil import Image
    except:
        messagebox.showwarning(title="警告",message="PIL库未正确安装，无法正确输出")
    else:
        im = Image.open('Export/output.eps')
        # 转换格式保存
        im.save("output.eps",site[v.get()-1][0])
def select(event=None):
    dict = {1:'Eps',2:'Webp',3:'Png',4:'Jpeg'}
    strings = '您选择了' + dict.get(v.get()) + '，点击下方按钮导出'
    lable.config(text = strings)
def selectangle(event=None):
    dict = {1:'左上',2:'左下',3:'右上',4:'右下'}
    angledict = {1:'不旋转',2:'对角线翻转',3:'逆对角线翻转',4:'上下翻转',5:'左右翻转'}
    strings = '从' + dict.get(u.get()) + '到' + dict.get(f.get()) + '\n' + angledict.get(l.get()) + '\n' + '点击下方按钮' + '\n' + '复制/旋转'
    showr.config(text = strings)
def exporteps(event=None):
    outtur()
    title("输出预览")
    ts = getscreen()
    ts.getcanvas().postscript(file="Export/output.eps")
def exportot(event=None):
    global Chos,lable,v
    Chos = Toplevel()
    site = [('Eps',1),
        ('Webp',2),
        ('Png',3),
        ('Jpeg',4)]
    v = IntVar()
    lable = Label(Chos)
    lable.pack(side ='top')
    for name, num in site:
        radio_button = Radiobutton(Chos,text = name, variable = v,value =num,command=select)
        radio_button.pack(anchor ='w')
    output = Button(Chos,text="输出",command=exp)
    output.pack(side='bottom')
    Chos.mainloop()
def helpoutput(event=None):
    result=messagebox.askquestion(title="提示",message="请阅读README.txt,要为您打印到Shell吗？")
    if result=="yes" :
        file=open("README.txt",mode='r')
        red=file.readlines()
        for i in range(len(red)):
            if i != len(red)-1:
                red[i]=red[i][0:-1]
            print(red[i])
def aboutoutput(event=None):
    result=messagebox.askquestion(title="提示",message="请参阅License.txt,要为您打印到Shell吗？")
    if result=="yes" :
        file=open("License.txt",mode='r')
        red=file.readlines()
        for i in range(len(red)):
            if i != len(red)-1:
                red[i]=red[i][0:-1]
            print(red[i])
def hisoutput(event=None):
    result=messagebox.askquestion(title="提示",message="请参阅Update_History.txt,要为您打印到Shell吗？")
    if result=="yes" :
        file=open("Update_History.txt",mode='r')
        red=file.readlines()
        for i in range(len(red)):
            if i != len(red)-1:
                red[i]=red[i][0:-1]
            print(red[i])
def saveconfig(event=None):
    savefile=open('SaveFile/test.txt',mode='a+')
    savefile.truncate(0)
    xwei=numwi(x)
    ywei=numwi(y)
    lwei=numwi(lent)
    wwei=numwi(width)
    savefile.write(str(olt))
    savefile.write(str(xwei))
    savefile.write(str(ywei))
    savefile.write(str(lwei))
    savefile.write(str(wwei))
    savefile.write(str(x))
    savefile.write(str(y))
    savefile.write(str(lent))
    savefile.write(str(width))
    savefile.write("\n")
    for n in range(x*y):
        savefile.write(str(configlist[n]))
    savefile.write(hecwrite)
def openconfig(event=None):
    global olt,x,y,lent,width,configlist,pic_list,heclist,hecwrite,ue,uq,ux,uy,drawon
    openfile=open('SaveFile/test.txt',mode='a+')
    openfile.seek(0)
    olt=openfile.read(1)
    openfile.seek(1)
    xwei=openfile.read(1)
    openfile.seek(2)
    ywei=openfile.read(1)
    openfile.seek(3)
    lwei=openfile.read(1)
    openfile.seek(4)
    wwei=openfile.read(1)
    openfile.seek(5)
    xwei=int(xwei)
    ywei=int(ywei)
    lwei=int(lwei)
    wwei=int(wwei)
    x=int(openfile.read(xwei))
    openfile.seek(5+xwei)
    y=int(openfile.read(ywei))
    openfile.seek(5+xwei+ywei)
    lent=int(openfile.read(lwei))
    openfile.seek(5+xwei+ywei+lwei)
    width=int(openfile.read(wwei))
    for i in range(1000):
        configlist[i]=1
    for n in range(int(x*y)+3):
        openfile.seek(n+4+xwei+ywei+lwei+wwei)
        try:
            configlist[n-2]=int(openfile.read(1))
        except:
            pass
    oread=openfile.readlines()
    print(oread)
    ue=[]
    uq=[]
    ux=[]
    uy=[]
    hecwrite="已绘制：(按设置顺序)"+'\n'
    for n in range(len(oread)-1):
        ooread=oread[n+1]
        ooread=ooread[1:-4]
        result = ooread.split(',',4)
        ue.append(float(result[0]))
        uq.append(int(result[1]))
        ux.append(float(result[2]))
        uy.append(float(result[3]))
    chemov.destroy()
    output.destroy()
    for i in range(len(ux)):
        heclist=[ue[i],uq[i],ux[i],uy[i]]
        hecwrite=hecwrite+str(heclist)+"\n"
    drawon=1
    hecprint.config(text=hecwrite)
    for pic in pic_list:
            pic.destroy()
    generate_buttons(x,y)
    for n in range(int(x*y)):
        pic_list[n].configure(image=photo[configlist[n]-1])
def outtur(event=None):
    global o,ux,uy,ue,uq
    try:
        reset()
    finally:
        try:
            width=wid.get()
        except:
            width=1
        speed(0)
        if ifmo.get() != 1:
            tracer(False)
        clear()
        title("输出中")
        ht()
        hideturtle()
        pensize(width)
        setup(width=lent*y+100, height=lent*x+100)
        num=0
        w = lent
        h = lent
        left_x = -w / 2
        top_y = h / 2
        xr = [(j - y / 2 + 1.5) * lent for j in range(y)]
        xr = xr * x
        yr = [(i - x / 2 + 0.5) * lent for i in range(x)]
        yr = sorted(yr * y, reverse=True)
        penup()
        goto(x*lent/2,y*lent/2)
        pendown()
        goto(x*lent/2,-y*lent/2)
        while num<x*y:
            num += 1
            draw(num, xr[num-1] + left_x, yr[num-1] + top_y)
        if olt==1:
            pensize(1)
            num=0
            while num<x-1:
                num+=1
                penup()
                goto(xr[num-1]+left_x,y*lent/2)
                pendown()
                goto(xr[num-1]+left_x,-y*lent/2)
            num=1
            while num<y-1:
                num+=1
                penup()
                goto(x*lent/2,yr[(num)*x-1]+top_y)
                pendown()
                goto(-x*lent/2,yr[(num)*x-1]+top_y)
        if drawon == 1:
            for i in range(len(ux)):
                if uq[i]!=0:
                    ur=float(ue[i]/(2*sin((pi/2)/uq[i])))
                    penup()
                    goto(ux[i]+ur,uy[i])
                    pendown()
                    fillcolor('white')
                    begin_fill()
                    circle(ur,steps=uq[i])
                    end_fill()
                if uq[i]==0:
                    ur=ue[i]
                    penup()
                    goto(ux[i]+ur,uy[i])
                    pendown()
                    fillcolor('white')
                    begin_fill()
                    circle(ur)
                    end_fill()
        penup()
        goto(x*lent/2,yr[0]+top_y)
        pendown()
        goto(-x*lent/2,yr[0]+top_y)
        penup()
        goto(-x*lent/2,y*lent/2)
        pendown()
        goto(-x*lent/2,-y*lent/2)
        penup()
        goto(x*lent/2,-y*lent/2)
        pendown()
        goto(-x*lent/2,-y*lent/2)
        penup()
        goto(x*lent/2,y*lent/2)
        pendown()
        goto(x*lent/2,-y*lent/2)
        goto(x*lent/2,y*lent/2)
        title("输出完成")
        mainloop()
def replace(buttonname, buttonnum):
    if configlist[buttonnum-1] > len(photo) - 1:
        configlist[buttonnum-1] = 0
    buttonname.configure(image=photo[configlist[buttonnum-1]])
    configlist[buttonnum-1] += 1
def test(event=None):
    print("输出成功！")
def r_c(event=None):
    global rwindows,showr,u,f,l
    rwindows=Toplevel()
    site = [('左上',1),
        ('左下',2),
        ('右上',3),
        ('右下',4)]
    angle = [('不旋转',1),('对角线翻转',2),('逆对角线翻转',3),
        ('上下翻转',4),('左右翻转',5)]
    u = IntVar()
    f = IntVar()
    l = IntVar()
    u.set(1)
    f.set(1)
    l.set(1)
    showr = Label(rwindows,text="未选择")
    showr.grid(row=0,column=0,sticky='E')
    for name, num in site:
        radio_button = Radiobutton(rwindows,text = name, variable = u,value =num,command=selectangle)
        radio_button.grid(row=num,column=0,sticky='w')
    for name, num in site:
        radio_button = Radiobutton(rwindows,text = name, variable = f,value =num,command=selectangle)
        radio_button.grid(row=num,column=1,sticky='E')
    for name, num in angle:
        radio_button = Radiobutton(rwindows,text = name, variable = l,value =num,command=selectangle)
        radio_button.grid(row=num+4,column=0,sticky='E')
    output = Button(rwindows,text="应用",command=r_rc)
    output.grid(row=10,column=0)
    rwindows.mainloop()
def r_rc():
    configpaste=[]
    aqx=int(x/2)
    aqy=int(y/2)
    print(aqx,aqy)
    if u.get()==1:
        for p in range(aqy):
            for i in range(aqx):
                configpaste.append(configlist[p*x+i])
    elif u.get()==3:
        for p in range(aqy):
            for i in range(aqx):
                configpaste.append(configlist[p*x+ceil(x/2)+i])
    elif u.get()==2:
        for p in range(aqy):
            for i in range(aqx):
                configpaste.append(configlist[ceil(y/2)*x+p*x+i])
    elif u.get()==4:
        for p in range(aqy):
            for i in range(aqx):
                configpaste.append(configlist[ceil(y/2)*x+p*x+ceil(x/2)+i])
    configturn=[]
    for p in range(aqy):
        for i in range(aqx):
            configturn.append([p,i,configpaste[p*aqx+i]])
    if l.get()==1:
        pass
    elif l.get()==2:
        configturn=[[y,x, a] for x, y, a in configturn]
    elif l.get()==3:
        configturn=[[aqx-y-1, aqy-x-1, a] for x, y, a in configturn]
    elif l.get()==4:    
        configturn=[[aqy-x-1, y, a] for x, y, a in configturn]
    elif l.get()==5:
        configturn=[[x, aqx-y-1, a] for x, y, a in configturn]
    configturn = sorted(configturn, key=lambda x: (x[0], x[1]))
    for i in range(len(configturn)):
            configpaste[i]=configturn[i][2]
    if f.get()==1:
        for p in range(aqy):
            for i in range(aqx):
                configlist[p*x+i]=configpaste[p*aqx+i]
    elif f.get()==3:
        for p in range(aqy):
            for i in range(aqx):
                configlist[p*x+ceil(x/2)+i]=configpaste[p*aqx+i]
    elif f.get()==2:
        for p in range(aqy):
            for i in range(aqx):
                configlist[ceil(y/2)*x+p*x+i]=configpaste[p*aqx+i]
    elif f.get()==4:
        for p in range(aqy):
            for i in range(aqx):
                configlist[ceil(y/2)*x+p*x+ceil(x/2)+i]=configpaste[p*aqx+i]
    for n in range(int(x*y)):
        pic_list[n].configure(image=photo[configlist[n]-1])
def r_t(event=None):
    global rwindows,showt,q
    twindows=Toplevel()
    site = [('左90',1),
        ('右90',2),
        ('上下翻转',3),
        ('左右翻转',4)]
    q = IntVar()
    q.set(1)
    showt = Label(twindows,text="未选择")
    showt.grid(row=0,column=0,sticky='W')
    for name, num in site:
        radio_button = Radiobutton(twindows,text = name, variable = q,value =num,command=selectturn)
        radio_button.grid(row=num,column=0,sticky='w')
    output = Button(twindows,text="应用",command=r_tc)
    output.grid(row=5,column=0)
    twindows.mainloop()
def selectturn():
    dict = {1:'左90',2:'右90',3:'上下翻转',4:'左右翻转'}
    strings = '您选择了' + dict.get(q.get()) + '，点击下方按钮应用'
    showt.config(text = strings)
def r_tc():
    global x,y,configlist
    configpaste=[]
    for p in range(y):
            for i in range(x):
                configpaste.append(configlist[p*x+i])
    configturn=[]
    for p in range(y):
        for i in range(x):
            configturn.append([p,i,configpaste[p*x+i]])
    if q.get() == 2:
        configturn=[[w,y+1-z,a]for z,w,a in configturn]
    if q.get() == 1:
        configturn=[[y+1-w,z,a]for z,w,a in configturn]
    if q.get() == 3:
         configturn=[[y-z-1, w, a] for z, w, a in configturn]
    if q.get() == 4:
         configturn=[[z, x-w-1, a] for z, w, a in configturn]
    configturn = sorted(configturn, key=lambda x: (x[0], x[1]))

    for i in range(len(configturn)):
            configpaste[i]=configturn[i][2]
    for p in range(y):
            for i in range(x):
                configlist[p*x+i]=configpaste[p*x+i]
    for n in range(int(x*y)):
        pic_list[n].configure(image=photo[configlist[n]-1])
def drawwhat():
    global drawpoint,lp,lx,ly,lt,le
    drawpoint=Toplevel()
    lp=IntVar()
    le=IntVar()
    lx=IntVar()
    ly=IntVar()
    lt=IntVar()
    drawpoint.title("图形标记框")
    drt_1 = Label(drawpoint, text="图形边数(若为圆则保持0):")
    drt_1.grid(row=0,column=0,sticky=W)
    drt_1_input = Entry(drawpoint, bd =5,textvariable=lp)
    drt_1_input.grid(row=0,column=1,sticky=E)
    drt_1 = Label(drawpoint, text="图形边长(若为圆则填半径):")
    drt_1.grid(row=1,column=0,sticky=W)
    drt_1_input = Entry(drawpoint, bd =5,textvariable=le)
    drt_1_input.grid(row=1,column=1,sticky=E)
    drt_2 = Label(drawpoint, text="X方向偏移量（从中央计）")
    drt_2.grid(row=2,column=0,sticky=W)
    drt_2_input = Entry(drawpoint, bd =5,textvariable=lx)
    drt_2_input.grid(row=2,column=1,sticky=E)
    drt_3 = Label(drawpoint, text="Y方向偏移量（从中央计）")
    drt_3.grid(row=3,column=0,sticky=W)
    drt_3_input = Entry(drawpoint, bd =5,textvariable=ly)
    drt_3_input.grid(row=3,column=1,sticky=W)
    outputd = Button(drawpoint,text="应用",command=drawpo)
    outputd.grid(row=4,column=0)
def drawpo():
    global drawon,ux,uy,ue,uq,hecwrite,hecprint
    ux.append(float(lx.get()))
    uy.append(float(ly.get()))
    ue.append(float(le.get()))
    uq.append(lp.get())
    hecwrite="已绘制：(按设置顺序)\n"
    for i in range(len(ux)):
        heclist=[ue[i],uq[i],ux[i],uy[i]]
        hecwrite=hecwrite+str(heclist)+"\n"
    drawon=1
    hecprint.config(text=hecwrite)
mainwindows = Tk()
mainwindows.title("花格输出器")
mainwindows.resizable(False,False)
mainmenu = Menu(mainwindows)
file = Menu(mainmenu,tearoff=0)
file.add_command(label="打开(Open)", command=openconfig,accelerator="Ctrl+O")
file.add_command(label="打开外置文件(Open at...)", command=openat,accelerator="Alt+O")
file.add_separator()
file.add_command(label="保存(Save)", command=saveconfig,accelerator="Ctrl+S")
file.add_command(label="另存到(Save at...)", command=saveat,accelerator="Alt+S")
file.add_separator()
file.add_command(label="退出(Quit)", command=mainwindows.destroy,accelerator="Ctrl+Q")
mainmenu.add_cascade(label="文件(File)",menu=file)
export = Menu(mainmenu,tearoff=0)
export.add_command(label="导出为Eps(Export as Eps)",command=exporteps,accelerator="Ctrl+E")
export.add_command(label="导出为Eps到...(Export as Eps at...)",command=exportat,accelerator="Command+E")
export.add_command(label="导出为...(Export as...)",command=exportot,accelerator="Alt+E")
mainmenu.add_cascade(label="导出(Export)",menu=export)
setmenu = Menu(mainmenu,tearoff=0)
setmenu.add_command(label="框架设置(Frame...)",command=frame,accelerator="Command+F")
setmenu.add_command(label="输出设置(Output...)",command=outps,accelerator="Command+O")
mainmenu.add_cascade(label="设置(Setting)",menu=setmenu)
drawmenu = Menu(mainmenu,tearoff=0)
drawmenu.add_command(label="形状(Draw...)",command=drawwhat,accelerator="Command+D")
drawmenu.add_separator()
drawmenu.add_command(label="复制(Copy...)",command=r_c,accelerator="Ctrl+R")
drawmenu.add_command(label="旋转(Turn...)",command=r_t,accelerator="Ctrl+T")
mainmenu.add_cascade(label="绘图(Paint)",menu=drawmenu)
helpmenu = Menu(mainmenu,tearoff=0)
helpmenu.add_command(label="帮助(Help Index)",command=helpoutput,accelerator="Ctrl+H")
helpmenu.add_command(label="关于(About...)",command=aboutoutput,accelerator="Ctrl+A")
helpmenu.add_command(label="更新历史(Update History...)",command=hisoutput,accelerator="Ctrl+U")
mainmenu.add_cascade(label="帮助(Help)",menu=helpmenu)
mainwindows.config(menu=mainmenu)
mainwindows.bind ("<Command-f>",frame)
mainwindows.bind ("<Command-o>",outps)
mainwindows.bind ("<Command-e>",exportat)
mainwindows.bind ("<Command-i>",test)
mainwindows.bind ("<Command-d>",test)
mainwindows.bind ("<Control-r>",r_c)
mainwindows.bind ("<Control-o>",openconfig)
mainwindows.bind ("<Control-s>",saveconfig)
mainwindows.bind ("<Control-u>",hisoutput)
mainwindows.bind ("<Control-t>",r_t)
mainwindows.bind ("<Alt-o>",openat)
mainwindows.bind ("<Alt-s>",saveat)
mainwindows.bind ("<Control-e>",exporteps)
mainwindows.bind ("<Alt-e>",exportot)
mainwindows.bind ("<Control-h>",helpoutput)
mainwindows.bind ("<Control-a>",aboutoutput)
ifmo = IntVar()
photo = [PhotoImage(file = 'SaveFile/test1.jpg'),PhotoImage(file = 'SaveFile/test2.jpg'),PhotoImage(file = 'SaveFile/test3.jpg')]
generate_buttons(x,y)
mainwindows.mainloop()
