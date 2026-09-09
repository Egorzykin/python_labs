import re
m=str(input("ФИО: "))
n=m.replace(" ","")
x=re.sub('[а-яё]+',"",n)
print("Инициалы: ", x)
print("Длина (символов): ", len(n)+2)