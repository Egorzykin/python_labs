m=int(input("Минуты: "))
if (m%60)>0:
    print(m//60,":",m%60,sep="")
else: print(m//60,":",m%60,"0",sep="")