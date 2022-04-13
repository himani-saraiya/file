list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("question3.txt","w")
i=0
while i<len(list):
    f.write(list[i])
    f.append("/n")
    i=i+1
    print(f)