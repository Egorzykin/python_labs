## ЛР1 — Ввод/вывод и форматирование

### Задание 1
x=str(input("Имя: "))
y=int(input("Возраст: "))
print("Привет, ",x,"! Через год тебе будет ",y+1,".",sep="")

![](../../images/lab01/ex01.png) 
### Задание 2
x=float(input("a: "))
y=float(input("b: "))
print("sum=",x+y,"; avg=",f"{(x+y)/2:.2f}")

![](../../images/lab01/ex02.png) 
### Задание 3
price=float(input())
discount=float(input())
vat=float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print("База после скидки: ", f"{base:.2f}","₽")
print("НДС:               ", f"{vat_amount:.2f}","₽")
print("Итого к оплате:    ", f"{total:.2f}","₽")

![](../../images/lab01/ex03.png) 
### Задание 4
m=int(input("Минуты: "))
if (m%60)>0:
    print(m//60,":",m%60,sep="")
else: print(m//60,":",m%60,"0",sep="")

![](../../images/lab01/ex04.png) 
### Задание 5
import re
m=str(input("ФИО: "))
n=m.replace(" ","")
x=re.sub('[а-яё]+',"",n)
print("Инициалы: ", x)
print("Длина (символов): ", len(n)+2)

![](../../images/lab01/ex05.png) 