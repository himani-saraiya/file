f=open("question3.txt","r")
x=f.readlines()
for i in x:
    if "delhi" in i:
        f1=open("delhi.txt","a")
        f1.write(i)
        print(f1)
    elif "shimla" in i:
        f2=open("shimla.txt","a")
        f2.write(i)
        print(f2)
    else:
        f3=open("other.txt","a")
        f3.write(i)
        print(f3)
f.close()
    