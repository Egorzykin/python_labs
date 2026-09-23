import re
m=str(input("ФИО: "))
n=m.replace(" ","")
x=re.sub('[а-яё]+',"",n)
print("Инициалы: ", x,".",sep="")
print("Длина (символов): ", len(n)+2)