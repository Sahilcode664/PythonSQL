n=input()
while n!="EXIT":
    if n=="CREATE DATABASE":
        print("Enter the file name:")
        a=input()
        f = open(a,"x")
        print("Your file succesfully created")
        f=open(a,"w")
        f.write("Sr No.".center(10," ")+"|")
        f.write("\n"+"".center(10," ")+"|\n")
        f.write("_"*10+"|\n")
        f.close()    
        n=input()
    if n=="OPEN DATABASE":
        print("Enter the file name:")
        a=input()
        f = open(a,"r")
        lin=f.readlines()
        lin0=str(lin[0][:-2])
        lin1=str(lin[1][:-2])
        lst0=lin0.split("|")
        lst1=lin1.split("|")
        for i in range(len(lst0)):
            dat1=(lst1[i].strip())
            lst1[i]=dat1
            dat2=str(lst0[i].strip())
            lst0[i]=dat2
        f.close()
        x=input()
        while x!="EXIT":
            if x=="ADD ROW":
               print("Enter the data list")
               y=eval(input())
               f=open(a,"r")
               length=len(f.readlines())
               f.close()
               data=str(length-2).center(10," ")+"|"
               for i in range(len(y)):
                   if len(y[i])>int(lst1[i+1]):
                       data=data+str(y[i][:int(lst1[i+1])]).center(int(lst1[i+1])," ")+"|"
                   else:
                       data=data+str(y[i]).center(int(lst1[i+1])," ")+"|"
               data=data+"\n"
               f=open(a,"a")
               f.write(data)
               f.close()
               x=input()
            if x=="UPDATE":
                r=int(input(print("Enter the row no.")))
                c=eval(input(print("Enter the data:")))
                f=open(a,"r")
                lin=f.readlines()
                dat=lin[r+2]
                dat1=lin[r+2]
                for i in range(int(len(c)/2)):
                    cd=c[i*2]
                    cnd=c[(i*2)+1]
                    ind=lst0.index(cd)
                    sum=0
                    if ind!=0:
                        for j in range(ind):
                            sum=sum+int(lst1[j])+1
                        if int(lst1[ind])>=len(cnd):
                            dat=dat[:sum]+cnd.center(int(lst1[ind])," ")+dat[sum+int(lst1[ind]):]
                        else:
                            dat=dat[:sum]+cnd[:int(lst1[ind])].center(int(lst1[ind])," ")+dat[sum+int(lst1[ind]):]
                    else:
                        dat=cnd.center(int(lst1[ind])," ")+dat[sum+int(lst1[ind]):]
                lin[r+2]=dat
                f.close()
                f=open(a,"w")
                for line in lin:
                    f.write(line)
                f.close()
                x=input()
            if x=="ADD COLUMN": 
               print("Enter the column name:")
               y=input()
               lst0.append(y)
               print("Enter the column length")
               l=int(input())
               lst1.append(l)
               f=open(a,"r")
               lin=f.readlines()
               lin0=str(lin[0][:-1])
               lin1=str(lin[1][:-1])
               lin2=str(lin[2][:-1])
               lin[0]=lin0+ y.center(l," ") + "|\n"
               lin[1]=lin1+ str(l).center(l," ") + "|\n"
               lin[2]=lin2+"_"*l+"|\n"
               f.close()
               f = open(a,"w")
               for line in lin:
                   f.write(line)
               f.close()
               x=input()
            if x=="CREATE COLUMN":
                print("Enter the columns name and thier size :--")
                y=eval(input())
                lin0=""
                lin1=""
                lin2=""
                for i in range(int(len(y)/2)):
                    lst0.append(y[i*2])
                    lst1.append(y[(i*2)+1])
                    lin0=lin0+y[i*2].center(y[(i*2)+1]," ")+"|"
                    lin1=lin1+str(y[(i*2)+1]).center(y[(i*2)+1]," ")+"|"
                    lin2=lin2+"_"*y[(i*2)+1]+"|"
                f=open(a,"r")
                lin=f.readlines()
                lin[0]=str(lin[0][:-1])+lin0+"\n"
                lin[1]=str(lin[1][:-1])+lin1+"\n"
                lin[2]=str(lin[2][:-1])+lin2+"\n"
                f.close()
                f=open(a,"w")
                for line in lin:
                    f.write(line)
                f.close()
                x=input()
            if x=="INSERT ROW":
               pos=int(input(print("Enter the position at you want to change")))
               y=eval(input(print("Enter the data list")))
               dat=str(pos).center(int(lst1[0])," ")+"|"
               for i in range(len(y)):
                   if len(y[i])<=int(lst1[i+1]):
                       dat=dat+y[i].center(int(lst1[i+1])," ")+"|"
                   else:
                       dat=dat+y[i][:int(lst1[i+1])].center(int(lst1[i+1])," ")+"|"
               dat=dat+"\n"
               f=open(a,"r")
               lin=f.readlines()
               c=-3
               i=-1
               for line in lin:
                   c=c+1
                   i=i+1
                   if c==pos:
                       new=str(lin[i])
                       new=str(c+1).center(int(lst1[0])," ")+new[int(lst1[0]):]
                       lin[i]=dat
                       dat=new
                   elif c>pos:
                       new=str(lin[i])
                       new=str(c+1).center(int(lst1[0])," ")+new[int(lst1[0]):]
                       lin[i]=dat
                       dat=new
               f.close()
               f=open(a,"w")
               for line in lin:
                   f.write(line)
               f.close()
               f=open(a,"a")
               f.write(dat)
               f.close()
               x=input() 
            if x=="SELECT":
                y=eval(input(print("Enter the columns want to get data:")))
                f=open(a,"r")
                lin=f.readlines()
                l=len(lin)
                for k in range(l):
                    val=str(lin[k])
                    dat=val[:int(lst1[0])+1]
                    for i in range(len(y)):
                        c=y[i]
                        sum=0
                        ind=lst0.index(c)
                        for j in range(ind):
                            sum=sum+int(lst1[j])+1
                        if ind!=len(lst1)-1:
                            dat=dat+val[sum:sum+int(lst1[ind+1])+1]
                        else:
                            dat=dat+val[sum:-1]
                    print(dat)
                f.close()
                x=input()       
        break
print(0)
